#!/usr/bin/env python3
"""
ArXiv Daily Paper Fetcher
Fetches papers from configured arXiv categories and extracts metadata.
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

# Configuration
BASE_DIR = Path.home() / "Documents" / "arxiv每日阅读"
CONFIG_FILE = BASE_DIR / "config" / "sources.json"
OUTPUT_DIR = BASE_DIR / "daily"

# Ensure directories exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_sources():
    """Load arXiv source URLs from config file."""
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config.get('sources', [])


def extract_category_from_url(url):
    """Extract category code from arXiv URL."""
    # URL format: https://arxiv.org/list/cs.CV/new
    match = re.search(r'/list/([^/]+)/new', url)
    return match.group(1) if match else "unknown"


def fetch_html(url, max_retries=3):
    """Fetch HTML content with retry logic."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.0'
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1}/{max_retries} failed for {url}: {e}")
            if attempt == max_retries - 1:
                raise
    return None


def extract_subject_full(subject_text):
    """Extract full subject name without abbreviation."""
    # Input: "Computer Vision and Pattern Recognition (cs.CV)"
    # Output: "Computer Vision and Pattern Recognition"
    match = re.match(r'([^()]+)', subject_text)
    return match.group(1).strip() if match else subject_text.strip()


def extract_arxiv_id_from_link(link):
    """Extract arXiv ID from link URL."""
    # Link format: https://arxiv.org/abs/XXXX.XXXXX
    match = re.search(r'/abs/(\d+\.\d+)', link)
    return match.group(1) if match else None


def parse_papers_from_section(section_html, category, submission_type):
    """Parse papers from a submission section HTML."""
    papers = []
    soup = BeautifulSoup(section_html, 'html.parser')
    
    # Find all paper entries (dt/dd pairs)
    dts = soup.find_all('dt')
    
    for dt in dts:
        try:
            # Find corresponding dd
            dd = dt.find_next_sibling('dd')
            if not dd:
                continue
            
            # Extract arXiv ID and link
            link_elem = dt.find('a', href=re.compile(r'/abs/'))
            if not link_elem:
                continue
            
            arxiv_id = link_elem.get('id', '')
            link = f"https://arxiv.org/abs/{arxiv_id}"
            
            # Extract title
            title_elem = dd.find('div', class_='list-title')
            if not title_elem:
                continue
            title = title_elem.get_text().replace('Title:', '').strip()
            
            # Extract authors
            authors_elem = dd.find('div', class_='list-authors')
            authors = []
            if authors_elem:
                author_links = authors_elem.find_all('a')
                authors = [a.get_text().strip() for a in author_links]
            
            # Extract subject
            subject_elem = dd.find('span', class_='primary-subject')
            subject = ""
            if subject_elem:
                subject = extract_subject_full(subject_elem.get_text())
            
            # Extract abstract
            abstract_elem = dd.find('p', class_='mathjax')
            abstract = ""
            if abstract_elem:
                abstract = abstract_elem.get_text().strip()
            
            paper = {
                "title": title,
                "link": link,
                "authors": authors,
                "subject": subject,
                "abstract": abstract,
                "correlation": "",
                "source_category": category,
                "submission_type": submission_type,
                "arxiv_id": arxiv_id
            }
            papers.append(paper)
            
        except Exception as e:
            print(f"Error parsing paper: {e}")
            continue
    
    return papers


def extract_section_by_header(soup, header_patterns):
    """Extract HTML content between a header (matching patterns) and the next h3."""
    # Find the header that matches any of the patterns
    headers = soup.find_all('h3')
    target_header = None
    
    for h in headers:
        header_text = h.get_text().lower()
        for pattern in header_patterns:
            if pattern.lower() in header_text:
                target_header = h
                break
        if target_header:
            break
    
    if not target_header:
        return ""
    
    # Collect all siblings until next h3
    content = []
    for sibling in target_header.find_next_siblings():
        if sibling.name == 'h3':
            break
        content.append(str(sibling))
    
    return '\n'.join(content)


def fetch_papers_from_category(url):
    """Fetch and parse papers from a single category URL."""
    category = extract_category_from_url(url)
    print(f"Fetching: {category} ({url})")
    
    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    
    all_papers = []
    
    # Extract New Submissions (look for "New submissions" in h3)
    new_section = extract_section_by_header(soup, ["New submissions"])
    if new_section:
        papers = parse_papers_from_section(new_section, category, "new")
        print(f"  Found {len(papers)} new submissions")
        all_papers.extend(papers)
    else:
        print(f"  No new submissions section found")
    
    return all_papers


def deduplicate_papers(papers):
    """Remove duplicate papers based on arXiv ID."""
    seen_ids = set()
    unique_papers = []
    
    for paper in papers:
        arxiv_id = paper.get('arxiv_id')
        if arxiv_id and arxiv_id not in seen_ids:
            seen_ids.add(arxiv_id)
            # Remove internal arxiv_id field before saving
            paper_copy = {k: v for k, v in paper.items() if k != 'arxiv_id'}
            unique_papers.append(paper_copy)
        elif arxiv_id:
            print(f"  Skipping duplicate: {arxiv_id}")
    
    return unique_papers


def save_papers(papers, date_str=None):
    """Save papers to JSON file."""
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    output_file = OUTPUT_DIR / f"{date_str}.json"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)
    
    print(f"\nSaved {len(papers)} papers to: {output_file}")
    return output_file


def main():
    """Main entry point."""
    print("ArXiv Daily Paper Fetcher")
    print("=" * 50)
    
    # Load sources
    try:
        sources = load_sources()
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)
    
    if not sources:
        print("No sources configured!")
        sys.exit(1)
    
    print(f"Sources: {len(sources)}")
    for src in sources:
        print(f"  - {src}")
    print()
    
    # Fetch papers from all sources
    all_papers = []
    for url in sources:
        try:
            papers = fetch_papers_from_category(url)
            all_papers.extend(papers)
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            continue
    
    # Deduplicate
    unique_papers = deduplicate_papers(all_papers)
    print(f"\nTotal unique papers: {len(unique_papers)}")
    
    # Save
    if unique_papers:
        output_file = save_papers(unique_papers)
        print(f"\nDone! Output: {output_file}")
    else:
        print("\nNo papers found!")


if __name__ == "__main__":
    main()
