#!/usr/bin/env python3
"""
Zhihu Publisher - Clipboard Edition
Copies report content to clipboard and provides step-by-step publishing guide.
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path

BASE_DIR = Path.home() / "Documents" / "arxiv每日阅读"
REPORTS_DIR = BASE_DIR / "reports"


def copy_to_clipboard(text):
    """Copy text to system clipboard (macOS)."""
    try:
        process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        process.communicate(text.encode('utf-8'))
        return True
    except Exception as e:
        print(f"❌ 复制到剪贴板失败: {e}")
        return False


def publish_guide(date_str=None):
    """Generate publishing guide and copy content to clipboard."""
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    report_file = REPORTS_DIR / f"{date_str}-report.md"
    
    if not report_file.exists():
        print(f"❌ 报告文件不存在: {report_file}")
        print("请先运行: python3 generate_report.py")
        return False
    
    with open(report_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title = "每日 arXiv 论文精选"
    for line in content.split('\n'):
        if line.startswith('# '):
            title = line[2:].strip()
            break
    
    print("=" * 70)
    print("📤 知乎文章发布助手")
    print("=" * 70)
    print(f"\n📄 日期: {date_str}")
    print(f"📰 标题: {title}")
    print(f"📝 内容: {len(content)} 字符")
    print()
    
    # Copy to clipboard
    print("📋 正在复制内容到剪贴板...")
    if copy_to_clipboard(content):
        print("✅ 内容已复制到剪贴板！")
    else:
        print("⚠️  自动复制失败，请手动复制文件内容")
        print(f"   文件路径: {report_file}")
    
    print()
    print("=" * 70)
    print("🚀 发布步骤")
    print("=" * 70)
    print()
    print("第 1 步: 打开知乎编辑器")
    print("   👉 https://zhuanlan.zhihu.com/write")
    print()
    print("第 2 步: 填写标题")
    print(f"   📌 {title}")
    print()
    print("第 3 步: 导入 Markdown")
    print("   方法一（推荐）:")
    print("   - 点击「导入文章」按钮")
    print("   - 选择 Markdown 格式")
    print("   - 粘贴内容（已自动复制到剪贴板）")
    print()
    print("   方法二:")
    print("   - 直接粘贴到编辑器")
    print()
    print("第 4 步: 添加话题标签")
    print("   建议标签:")
    print("   - 人工智能")
    print("   - 大语言模型")
    print("   - 论文解读")
    print("   - arXiv")
    print("   - 机器学习")
    print()
    print("第 5 步: 发布")
    print("   - 检查格式无误后点击「发布」")
    print()
    print("=" * 70)
    print("💡 提示: 内容已复制，直接粘贴即可！")
    print("=" * 70)
    
    # Try to open browser
    print("\n🌐 正在尝试打开浏览器...")
    try:
        subprocess.Popen(['open', 'https://zhuanlan.zhihu.com/write'])
        print("✅ 浏览器已打开")
    except:
        print("⚠️  无法自动打开浏览器，请手动访问上述链接")
    
    return True


if __name__ == "__main__":
    date = sys.argv[1] if len(sys.argv) > 1 else None
    success = publish_guide(date)
    sys.exit(0 if success else 1)
