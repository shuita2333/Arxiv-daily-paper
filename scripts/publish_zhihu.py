#!/usr/bin/env python3
"""
Zhihu Article Publisher
Automates publishing arXiv daily reports to Zhihu using the Markdown import feature.
"""

import argparse
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
        print(f"❌ Error: Report file not found: {report_file}")
        print(f"Please run generate_report.py first.")
        return None, None
    
    with open(report_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return content, date_str


def extract_title_from_content(content):
    """Extract title from markdown content."""
    lines = content.strip().split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    return "每日 arXiv 论文精选"


def publish_to_zhihu(date_str=None, headless=False):
    """
    Publish report to Zhihu using Markdown import feature.
    
    Workflow:
    1. Open https://zhuanlan.zhihu.com/write
    2. Fill in title
    3. Click "导入文章" button
    4. Upload/paste Markdown content
    5. Wait for import completion
    6. Add topics
    7. Publish
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("❌ Playwright not installed.")
        print("Please install: pip install playwright")
        print("Then run: playwright install chromium")
        return False
    
    content, date_str = read_report(date_str)
    if not content:
        return False
    
    title = extract_title_from_content(content)
    
    print("=" * 70)
    print("🚀 知乎文章自动发布")
    print("=" * 70)
    print(f"\n📄 报告日期: {date_str}")
    print(f"📰 文章标题: {title}")
    print(f"📝 内容长度: {len(content)} 字符")
    print()
    
    with sync_playwright() as p:
        # Launch browser
        print("🌐 启动浏览器...")
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context(viewport={'width': 1400, 'height': 900})
        page = context.new_page()
        
        try:
            # Navigate to Zhihu write page
            print("🔗 打开知乎编辑器...")
            page.goto('https://zhuanlan.zhihu.com/write', wait_until='networkidle')
            time.sleep(2)
            
            # Check if login is needed
            if 'login' in page.url or page.is_visible('text=登录'):
                print("\n⚠️  请先登录知乎账号")
                print("请在浏览器窗口中完成登录...")
                
                # Wait for successful navigation to write page
                max_wait = 120  # 2 minutes
                waited = 0
                while ('login' in page.url or '/write' not in page.url) and waited < max_wait:
                    time.sleep(1)
                    waited += 1
                
                if waited >= max_wait:
                    print("❌ 登录超时，请重试")
                    browser.close()
                    return False
                
                print("✅ 登录成功！")
                time.sleep(2)
            
            # Fill in title
            print("📝 填写文章标题...")
            title_selectors = [
                'input[placeholder*="标题"]',
                'input[placeholder*="请输入标题"]',
                '.WriteIndex-titleInput input',
                '[data-za-detail-view-path-module="TitleInput"] input',
                'textarea[placeholder*="标题"]'
            ]
            
            title_filled = False
            for selector in title_selectors:
                try:
                    if page.is_visible(selector, timeout=3000):
                        page.fill(selector, title)
                        print(f"   ✓ 标题已填写")
                        title_filled = True
                        break
                except:
                    continue
            
            if not title_filled:
                print("⚠️  未能自动填写标题，请手动输入")
                input("按回车继续...")
            
            # Method 1: Try to use Markdown import feature
            print("\n📥 尝试使用 Markdown 导入功能...")
            
            # Look for import button
            import_button_selectors = [
                'text=导入文章',
                'button:has-text("导入")',
                '[data-za-detail-view-path-module="ImportArticle"]',
                '.WriteIndex-importButton',
                'text=Markdown',
            ]
            
            import_found = False
            for selector in import_button_selectors:
                try:
                    if page.is_visible(selector, timeout=2000):
                        page.click(selector)
                        print(f"   ✓ 点击导入按钮")
                        import_found = True
                        time.sleep(1)
                        break
                except:
                    continue
            
            if import_found:
                # Look for file upload or text paste area
                print("📋 准备导入内容...")
                
                # Try to find textarea for pasting markdown
                text_area_selectors = [
                    'textarea[placeholder*="粘贴"]',
                    'textarea[placeholder*="内容"]',
                    '.WriteImport-textarea',
                    'textarea'
                ]
                
                for selector in text_area_selectors:
                    try:
                        if page.is_visible(selector, timeout=3000):
                            # Paste content
                            page.fill(selector, content)
                            print(f"   ✓ 内容已粘贴")
                            time.sleep(1)
                            
                            # Look for confirm/import button
                            confirm_selectors = [
                                'button:has-text("导入")',
                                'button:has-text("确认")',
                                'button:has-text("确定")',
                                '.WriteImport-confirmButton'
                            ]
                            
                            for confirm_sel in confirm_selectors:
                                try:
                                    if page.is_visible(confirm_sel, timeout=2000):
                                        page.click(confirm_sel)
                                        print(f"   ✓ 确认导入")
                                        time.sleep(3)  # Wait for import
                                        break
                                except:
                                    continue
                            break
                    except:
                        continue
            else:
                print("⚠️  未找到导入按钮，尝试直接粘贴到编辑器...")
                
                # Click on editor area
                editor_selectors = [
                    '[contenteditable="true"]',
                    '.RichContent-editor',
                    '.WriteIndex-editor',
                    'div[role="textbox"]'
                ]
                
                for selector in editor_selectors:
                    try:
                        if page.is_visible(selector, timeout=3000):
                            page.click(selector)
                            print(f"   ✓ 点击编辑器")
                            
                            # Paste content
                            page.keyboard.type(content, delay=0.01)
                            print(f"   ✓ 内容已输入")
                            break
                    except:
                        continue
            
            print("\n" + "=" * 70)
            print("🎉 文章已导入到知乎编辑器！")
            print("=" * 70)
            print("\n请完成以下步骤：")
            print("1️⃣  检查文章格式是否正确")
            print("2️⃣  添加相关话题标签（建议：人工智能、大语言模型、论文解读）")
            print("3️⃣  设置文章属性（原创/转载）")
            print("4️⃣  点击「发布」按钮")
            print()
            
            if not headless:
                print("💡 浏览器窗口保持打开，请手动完成发布")
                print("按 Ctrl+C 关闭浏览器...")
                try:
                    while True:
                        time.sleep(1)
                except KeyboardInterrupt:
                    pass
            
            browser.close()
            return True
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("\n⚠️  自动发布遇到错误，请手动完成发布：")
            print(f"   1. 打开: https://zhuanlan.zhihu.com/write")
            print(f"   2. 标题: {title}")
            print(f"   3. 内容请从文件复制: {REPORTS_DIR / f'{date_str}-report.md'}")
            
            if not headless:
                print("\n浏览器保持打开，请手动完成操作")
                input("按回车关闭浏览器...")
            
            browser.close()
            return False


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Publish arXiv daily report to Zhihu')
    parser.add_argument('date', nargs='?', help='Date string (YYYY-MM-DD), defaults to today')
    parser.add_argument('--headless', action='store_true', help='Run browser in headless mode (not recommended for login)')
    
    args = parser.parse_args()
    
    success = publish_to_zhihu(args.date, args.headless)
    
    if success:
        print("\n✅ 文章已成功导入知乎编辑器！")
    else:
        print("\n❌ 发布过程遇到问题")


if __name__ == "__main__":
    main()
