#!/usr/bin/env python3
"""
Notion Publisher - Send arXiv daily report to Notion page
Uses Notion API to append content blocks.
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# Try to import requests

try:
    import requests
except ImportError:
    print("❌ requests not installed. Install with: pip install requests")
    sys.exit(1)

BASE_DIR = Path.home() / "Documents" / "arxiv每日阅读"
REPORTS_DIR = BASE_DIR / "reports"
DAILY_DIR = BASE_DIR / "daily"

NOTION_API_BASE = "https://api.notion.com/v1"


def markdown_to_notion_blocks(markdown_text):
    """Convert markdown text to Notion blocks."""
    blocks = []
    lines = markdown_text.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Headers
        if line.startswith('# '):
            blocks.append({
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [{"type": "text", "text": {"content": line[2:]}}]
                }
            })
        elif line.startswith('## '):
            blocks.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": line[3:]}}]
                }
            })
        elif line.startswith('### '):
            blocks.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{"type": "text", "text": {"content": line[4:]}}]
                }
            })
        # Divider
        elif line == '---':
            blocks.append({
                "object": "block",
                "type": "divider",
                "divider": {}
            })
        # Quote
        elif line.startswith('>'):
            content = line[1:].strip()
            blocks.append({
                "object": "block",
                "type": "quote",
                "quote": {
                    "rich_text": [{"type": "text", "text": {"content": content}}]
                }
            })
        # Regular paragraph
        else:
            # Parse bold text
            rich_text = []
            parts = line.split('**')
            for i, part in enumerate(parts):
                if i % 2 == 1:  # Bold parts (odd indices after split)
                    rich_text.append({
                        "type": "text",
                        "text": {"content": part},
                        "annotations": {"bold": True}
                    })
                else:
                    rich_text.append({
                        "type": "text",
                        "text": {"content": part}
                    })
            
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": rich_text if rich_text else [{"type": "text", "text": {"content": line}}]
                }
            })
    
    return blocks


def append_to_notion_page(token, page_id, blocks):
    """Append blocks to Notion page."""
    url = f"{NOTION_API_BASE}/blocks/{page_id}/children"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    
    # Notion API limits: max 100 blocks per request
    chunk_size = 100
    for i in range(0, len(blocks), chunk_size):
        chunk = blocks[i:i+chunk_size]
        data = {"children": chunk}
        
        response = requests.patch(url, headers=headers, json=data)
        
        if response.status_code != 200:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            return False
        
        print(f"   ✓ Appended blocks {i+1}-{min(i+chunk_size, len(blocks))}")
    
    return True


def clear_notion_page(token, page_id):
    """Clear all blocks from Notion page."""
    url = f"{NOTION_API_BASE}/blocks/{page_id}/children"
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28"
    }
    
    # Get all blocks
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"❌ Failed to get page blocks: {response.status_code}")
        return False
    
    data = response.json()
    blocks = data.get('results', [])
    
    print(f"   Found {len(blocks)} blocks to delete...")
    
    # Delete each block
    for block in blocks:
        block_id = block['id']
        delete_url = f"{NOTION_API_BASE}/blocks/{block_id}"
        requests.delete(delete_url, headers=headers)
    
    print(f"   ✓ Cleared {len(blocks)} blocks")
    return True


def publish_to_notion(token, page_id, date_str=None):
    """Publish arXiv report to Notion page."""
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    report_file = REPORTS_DIR / f"{date_str}-report.md"
    
    if not report_file.exists():
        print(f"❌ Report not found: {report_file}")
        return False
    
    # Read report
    with open(report_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=" * 60)
    print("📤 Notion Publisher")
    print("=" * 60)
    print(f"\n📅 Date: {date_str}")
    print(f"📝 Content length: {len(content)} characters")
    print(f"📄 Page ID: {page_id}")
    print()
    
    # Convert to blocks
    print("🔄 Converting markdown to Notion blocks...")
    blocks = markdown_to_notion_blocks(content)
    print(f"   ✓ Created {len(blocks)} blocks")
    print()
    
    # Clear existing content
    print("🗑️  Clearing existing page content...")
    if not clear_notion_page(token, page_id):
        print("⚠️  Failed to clear page, appending instead...")
    print()
    
    # Append new content
    print("📥 Appending new content...")
    if append_to_notion_page(token, page_id, blocks):
        print()
        print("=" * 60)
        print("✅ Successfully published to Notion!")
        print("=" * 60)
        print(f"\n🔗 View page: https://notion.so/{page_id.replace('-', '')}")
        return True
    else:
        print("❌ Failed to publish")
        return False


def main():
    """Main entry point."""
    if len(sys.argv) < 3:
        print("Usage: python3 publish_notion.py <notion_token> <page_id> [date]")
        print()
        print("Setup:")
        print("1. Create integration at: https://www.notion.so/my-integrations")
        print("2. Copy the 'Internal Integration Token'")
        print("3. Share your page with the integration")
        print("4. Get page ID from URL: notion.so/Page-Name-<PAGE_ID>")
        print()
        print("Example:")
        print("   python3 publish_notion.py secret_xxx 338d86d5-bf05-8012-b351-d9e8f1f8881c 2026-04-04")
        sys.exit(1)
    
    token = sys.argv[1]
    page_id = sys.argv[2]
    date_str = sys.argv[3] if len(sys.argv) > 3 else None
    
    success = publish_to_notion(token, page_id, date_str)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
