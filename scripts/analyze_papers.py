#!/usr/bin/env python3
"""
ArXiv Paper Correlation Analyzer
Analyzes papers and assigns correlation levels based on title only.
"""

import json
import re
from datetime import datetime
from pathlib import Path

# Configuration
BASE_DIR = Path.home() / "Documents" / "arxiv每日阅读"
RULES_FILE = BASE_DIR / "analysis" / "rules.json"
DAILY_DIR = BASE_DIR / "daily"


def load_rules():
    """Load analysis rules from config file."""
    with open(RULES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def normalize_text(text):
    """Normalize text for matching (lowercase, remove extra spaces)."""
    if not text:
        return ""
    # Convert to lowercase
    text = text.lower()
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    return text


def check_keywords_match(text, keywords, partial_match=True):
    """Check if any keyword matches in the text.
    
    Args:
        text: Text to search in
        keywords: List of keywords to search for
        partial_match: If True, allows partial word matches
    
    Returns:
        (matched, matched_keyword)
    """
    text = normalize_text(text)
    
    for keyword in keywords:
        keyword_lower = keyword.lower()
        
        if partial_match:
            # Partial match - keyword can be part of a word
            if keyword_lower in text:
                return True, keyword
        else:
            # Whole word match
            pattern = r'\b' + re.escape(keyword_lower) + r'\b'
            if re.search(pattern, text):
                return True, keyword
    
    return False, None


def is_large_model_related(title, rules_def):
    """Check if paper is related to large models (using title only)."""
    large_model_terms = rules_def.get('large_models', [])
    
    title_lower = normalize_text(title)
    
    for term in large_model_terms:
        term_lower = term.lower()
        if term_lower in title_lower:
            return True
    
    return False


def analyze_paper(paper, rules_config):
    """Analyze a single paper and return correlation level.
    
    Priority: 1 (safety) > 2 (capability) > 3 (related) > 4 (other)
    Analysis is based on title ONLY.
    """
    title = paper.get('title', '')
    rules = rules_config.get('rules', [])
    rules_def = rules_config.get('definition', {})
    
    # Check if paper is large-model related first (for levels 1-3)
    is_llm_related = is_large_model_related(title, rules_def)
    
    # Get rules sorted by priority
    sorted_rules = sorted(rules, key=lambda x: x.get('priority', 999))
    
    # Level 1: Safety research (highest priority for LLM papers)
    safety_rule = next((r for r in sorted_rules if r['level'] == 1), None)
    if safety_rule and is_llm_related:
        title_keywords = safety_rule.get('keywords', {}).get('title', [])
        
        title_match, _ = check_keywords_match(title, title_keywords)
        
        if title_match:
            return 1
    
    # Level 2: Capability research
    capability_rule = next((r for r in sorted_rules if r['level'] == 2), None)
    if capability_rule and is_llm_related:
        title_keywords = capability_rule.get('keywords', {}).get('title', [])
        
        title_match, _ = check_keywords_match(title, title_keywords)
        
        if title_match:
            return 2
    
    # Level 3: General LLM related research
    if is_llm_related:
        return 3
    
    # Level 4: Other research
    return 4


def analyze_daily_file(date_str=None):
    """Analyze papers for a specific date."""
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    input_file = DAILY_DIR / f"{date_str}.json"
    
    if not input_file.exists():
        print(f"Error: File not found: {input_file}")
        return None
    
    # Load rules
    rules_config = load_rules()
    
    # Load papers
    with open(input_file, 'r', encoding='utf-8') as f:
        papers = json.load(f)
    
    print(f"Analyzing {len(papers)} papers from {date_str}...")
    print(f"Method: Title-only analysis")
    print("=" * 60)
    
    # Analyze each paper
    stats = {1: 0, 2: 0, 3: 0, 4: 0}
    
    for i, paper in enumerate(papers):
        level = analyze_paper(paper, rules_config)
        paper['correlation'] = level
        stats[level] += 1
        
        # Progress indicator every 20 papers
        if (i + 1) % 20 == 0:
            print(f"  Processed {i + 1}/{len(papers)} papers...")
    
    # Save updated papers
    with open(input_file, 'w', encoding='utf-8') as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)
    
    print("=" * 60)
    print(f"Analysis complete!")
    print(f"")
    print(f"Correlation distribution:")
    print(f"  Level 1 (大模型安全相关研究): {stats[1]} papers")
    print(f"  Level 2 (大模型内生能力研究): {stats[2]} papers")
    print(f"  Level 3 (大模型相关研究):     {stats[3]} papers")
    print(f"  Level 4 (其他研究):           {stats[4]} papers")
    print(f"")
    print(f"Updated file: {input_file}")
    
    return stats


def main():
    """Main entry point."""
    import sys
    
    # Check for date argument
    date_str = None
    if len(sys.argv) > 1:
        date_str = sys.argv[1]
    
    # Analyze
    stats = analyze_daily_file(date_str)
    
    if stats:
        print("\nDone!")
    else:
        print("\nFailed to analyze papers.")


if __name__ == "__main__":
    main()
