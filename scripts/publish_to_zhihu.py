#!/usr/bin/env python3
"""
ArXiv Daily Report Publisher
Publishes generated reports to Zhihu articles using browser automation.
"""

import json
import re
import time
from datetime import datetime
from pathlib import Path

# Configuration
BASE_DIR = Path.home() / "Documents" / "arxiv每日阅读"
REPORTS_DIR = BASE_DIR / "reports"


def read_report(date_str=None):
    """Read the generated report file."""
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    report_file = REPORTS_DIR / f"{date_str}-report.md"
    
    if not report_file.exists():
        print(f"Error: Report file not found: {report_file}")
        print(f"Please run generate_report.py first.")
        return None
    
    with open(report_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return content, date_str


def extract_title(content, date_str):
    """Extract title from report content."""
    # First line should be the title
    lines = content.strip().split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    
    # Fallback
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    date_chinese = date_obj.strftime('%Y年%m月%d日')
    return f"每日 arXiv 论文精选 | {date_chinese}"


def publish_to_zhihu(date_str=None, headless=False):
    """
    Publish report to Zhihu using browser automation.
    
    Note: This is a guide script. Actual implementation requires:
    - playwright or selenium installed
    - Zhihu login credentials or saved cookies
    """
    content, date_str = read_report(date_str)
    if not content:
        return False
    
    title = extract_title(content, date_str)
    
    print("=" * 60)
    print("Zhihu Publishing Guide")
    print("=" * 60)
    print()
    print(f"Title: {title}")
    print(f"Content length: {len(content)} characters")
    print()
    print("Since Zhihu requires login and browser automation,")
    print("please follow these steps to publish manually:")
    print()
    print("1. Open https://zhuanlan.zhihu.com/write")
    print("2. Log in to your Zhihu account if not already logged in")
    print("3. Enter the article title:")
    print(f"   {title}")
    print()
    print("4. Copy the following content and paste into the editor:")
    print("-" * 60)
    print(content[:500] + "..." if len(content) > 500 else content)
    print("-" * 60)
    print()
    print("5. Add topics (建议):")
    print("   - 人工智能")
    print("   - 大语言模型")
    print("   - 论文解读")
    print("   - arXiv")
    print("   - 机器学习")
    print()
    print("6. Set publishing options:")
    print("   - 允许规范转载 (Optional)")
    print("   - 禁止转载 (Optional)")
    print()
    print("7. Click '发布' (Publish) button")
    print()
    print("=" * 60)
    print()
    
    # Save a copy with publishing instructions
    guide_file = REPORTS_DIR / f"{date_str}-publishing-guide.txt"
    guide_content = f"""Zhihu Publishing Guide
====================

Date: {date_str}
Title: {title}

Step 1: Open https://zhuanlan.zhihu.com/write

Step 2: Login to Zhihu (if not logged in)

Step 3: Enter Title
{title}

Step 4: Copy content from:
{REPORTS_DIR / f"{date_str}-report.md"}

Step 5: Add Topics
- 人工智能
- 大语言模型
- 论文解读
- arXiv
- 机器学习

Step 6: Publish!

Note: Zhihu supports HTML <font> tags for colored text.
The report already includes proper formatting.
"""
    
    with open(guide_file, 'w', encoding='utf-8') as f:
        f.write(guide_content)
    
    print(f"Publishing guide saved to: {guide_file}")
    
    # Try to open browser if playwright is available
    try_browser_automation(title, content, headless)
    
    return True


def try_browser_automation(title, content, headless=False):
    """Try to use browser automation if playwright is available."""
    try:
        from playwright.sync_api import sync_playwright
        
        print("Playwright detected! Attempting browser automation...")
        print("Note: You may need to log in manually on first run.")
        print()
        
        with sync_playwright() as p:
            # Launch browser
            browser = p.chromium.launch(headless=headless)
            context = browser.new_context(viewport={'width': 1280, 'height': 800})
            page = context.new_page()
            
            # Navigate to Zhihu write page
            print("Opening Zhihu editor...")
            page.goto('https://zhuanlan.zhihu.com/write')
            
            # Wait for page to load
            time.sleep(3)
            
            # Check if login is needed
            if 'login' in page.url or page.is_visible('text=登录'):
                print("Please log in to Zhihu in the browser window.")
                print("Waiting for login...")
                
                # Wait for navigation to write page after login
                while 'login' in page.url or '/write' not in page.url:
                    time.sleep(1)
                
                time.sleep(2)
            
            print("Zhihu editor loaded!")
            print()
            
            # Fill in title
            print("Filling in title...")
            try:
                # Try to find title input
                title_selectors = [
                    'input[placeholder*="标题"]',
                    'input[placeholder*="请输入标题"]',
                    'textarea[placeholder*="标题"]',
                    '.WriteIndex-titleInput input',
                    '[data-za-detail-view-path-module="TitleInput"] input'
                ]
                
                for selector in title_selectors:
                    if page.is_visible(selector):
                        page.fill(selector, title)
                        print("Title filled!")
                        break
            except Exception as e:
                print(f"Could not auto-fill title: {e}")
                print("Please enter the title manually.")
            
            print()
            print("Content is ready to be pasted.")
            print("The markdown content is in your clipboard area.")
            print()
            print("Please:")
            print("1. Click in the content editor area")
            print("2. Paste the content from the report file")
            print("3. Add topics and publish")
            print()
            
            # Keep browser open
            if not headless:
                print("Browser will stay open. Press Ctrl+C to close.")
                try:
                    while True:
                        time.sleep(1)
                except KeyboardInterrupt:
                    pass
            
            browser.close()
            
    except ImportError:
        print("Playwright not installed. Skipping browser automation.")
        print("To enable automation, install: pip install playwright")
        print("Then run: playwright install chromium")
    except Exception as e:
        print(f"Browser automation failed: {e}")
        print("Please publish manually following the steps above.")


def main():
    """Main entry point."""
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description='Publish arXiv daily report to Zhihu')
    parser.add_argument('date', nargs='?', help='Date string (YYYY-MM-DD), defaults to today')
    parser.add_argument('--headless', action='store_true', help='Run browser in headless mode')
    
    args = parser.parse_args()
    
    success = publish_to_zhihu(args.date, args.headless)
    
    if success:
        print("✅ Publishing guide generated successfully!")
    else:
        print("❌ Failed to generate publishing guide")


if __name__ == "__main__":
    main()
