#!/usr/bin/env python3
"""
Feishu Report Publisher - Send arXiv daily report to Feishu group
Creates a Feishu document and sends link to group chat.
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path

BASE_DIR = Path.home() / "Documents" / "arxiv每日阅读"
REPORTS_DIR = BASE_DIR / "reports"
DAILY_DIR = BASE_DIR / "daily"

# Target Feishu chat ID
TARGET_CHAT_ID = "oc_2e444bf6868806df491a6cfcf7ad4a41"


def read_report(date_str=None):
    """Read the generated report file."""
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    report_file = REPORTS_DIR / f"{date_str}-report.md"
    
    if not report_file.exists():
        print(f"❌ 报告文件不存在: {report_file}")
        return None, date_str
    
    with open(report_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return content, date_str


def publish_to_feishu(date_str=None):
    """Publish report to Feishu via document + message."""
    content, date_str = read_report(date_str)
    
    if not content:
        return False
    
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    date_chinese = date_obj.strftime('%Y年%m月%d日')
    title = f"📚 每日 arXiv 论文精选 | {date_chinese}"
    
    print("=" * 60)
    print("📤 飞书发布流程")
    print("=" * 60)
    print(f"\n📅 日期: {date_str}")
    print(f"📰 标题: {title}")
    print(f"📝 内容长度: {len(content)} 字符")
    print()
    
    print("📋 请按以下步骤操作：")
    print()
    print("步骤 1: 创建飞书文档")
    print(f"   使用 feishu_doc create --title '{title}'")
    print()
    print("步骤 2: 写入内容")
    print(f"   使用 feishu_doc write --doc_token <TOKEN> --content <FILE>")
    print(f"   或使用 feishu_doc append 追加内容")
    print()
    print("步骤 3: 发送消息到群聊")
    print(f"   使用 message send --channel feishu --target {TARGET_CHAT_ID}")
    print(f"   消息内容: '📚 每日 arXiv 论文精选 | {date_chinese} 已发布，")
    print(f"            文档链接: https://xxx.feishu.cn/docx/<TOKEN>'")
    print()
    print("=" * 60)
    
    # Save instructions
    guide_file = REPORTS_DIR / f"{date_str}-feishu-publish-guide.txt"
    with open(guide_file, 'w', encoding='utf-8') as f:
        f.write(f"""飞书发布指南
============

日期: {date_str}
标题: {title}

步骤 1: 创建文档
feishu_doc create --title "{title}"

步骤 2: 写入内容 (分批次，每次不超过 5000 字符)
文档创建后会返回 doc_token，使用以下命令写入：
feishu_doc write --doc_token <YOUR_TOKEN> --content "{REPORTS_DIR / f'{date_str}-report.md'}"

或者使用 append 分批追加：
feishu_doc append --doc_token <YOUR_TOKEN> --content "第一部分"

步骤 3: 发送群消息
message send --channel feishu --target {TARGET_CHAT_ID} \\
    --message "📚 每日 arXiv 论文精选 | {date_chinese}\\n\\n文档链接: https://open.feishu.cn/docx/<YOUR_TOKEN>"

注意:
- 飞书文档有单条写入长度限制，建议分批写入
- 或使用 append 操作多次追加内容
- Markdown 格式会被转换为飞书文档格式

报告文件位置:
{REPORTS_DIR / f'{date_str}-report.md'}
""")
    
    print(f"💾 详细指南已保存: {guide_file}")
    print()
    print("✅ 准备就绪！请按照上述步骤操作")
    
    return True


if __name__ == "__main__":
    date = sys.argv[1] if len(sys.argv) > 1 else None
    success = publish_to_feishu(date)
    sys.exit(0 if success else 1)
