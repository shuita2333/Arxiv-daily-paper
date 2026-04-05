#!/usr/bin/env python3
"""
Feishu Publisher - Send arXiv daily report to Feishu group chat
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# Configuration
BASE_DIR = Path.home() / "Documents" / "arxiv每日阅读"
REPORTS_DIR = BASE_DIR / "reports"
DAILY_DIR = BASE_DIR / "daily"

# Target Feishu chat ID
TARGET_CHAT_ID = "oc_2e444bf6868806df491a6cfcf7ad4a41"


def read_report(date_str=None):
    """Read the generated report file and daily data."""
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    report_file = REPORTS_DIR / f"{date_str}-report.md"
    daily_file = DAILY_DIR / f"{date_str}.json"
    
    if not report_file.exists():
        print(f"❌ 报告文件不存在: {report_file}")
        return None, None, date_str
    
    with open(report_file, 'r', encoding='utf-8') as f:
        report_content = f.read()
    
    # Read daily data for statistics
    daily_data = None
    if daily_file.exists():
        with open(daily_file, 'r', encoding='utf-8') as f:
            daily_data = json.load(f)
    
    return report_content, daily_data, date_str


def truncate_content(content, max_length=8000):
    """Truncate content to fit Feishu message limits."""
    if len(content) <= max_length:
        return content
    
    # Find a good break point
    truncated = content[:max_length]
    # Try to end at a section break
    last_break = truncated.rfind('\n## ')
    if last_break > max_length * 0.7:  # If we can keep at least 70%
        return truncated[:last_break] + "\n\n...（内容已截断，完整报告请查看文件）"
    
    return truncated.rsplit('\n\n', 1)[0] + "\n\n...（内容已截断，完整报告请查看文件）"


def send_to_feishu(date_str=None):
    """Send report to Feishu group chat."""
    report_content, daily_data, date_str = read_report(date_str)
    
    if not report_content:
        return False
    
    # Generate summary message
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    date_chinese = date_obj.strftime('%Y年%m月%d日')
    
    # Count papers by correlation
    stats = {1: 0, 2: 0, 3: 0, 4: 0}
    if daily_data:
        for paper in daily_data:
            stats[paper.get('correlation', 4)] += 1
    
    total = stats[1] + stats[2] + stats[3]
    
    # Build summary
    summary = f"""📚 每日 arXiv 论文精选 | {date_chinese}

🔐 安全研究: {stats[1]} 篇
🧠 能力研究: {stats[2]} 篇  
🔬 相关技术: {stats[3]} 篇
📊 总计: {total} 篇

---

"""
    
    # Truncate full content
    full_message = summary + report_content
    final_message = truncate_content(full_message, 9000)  # Leave some margin
    
    print("=" * 60)
    print("📤 飞书消息发送")
    print("=" * 60)
    print(f"\n📅 日期: {date_str}")
    print(f"📊 统计: {total} 篇论文")
    print(f"📝 消息长度: {len(final_message)} 字符")
    print(f"💬 目标群聊: {TARGET_CHAT_ID}")
    print()
    
    # Save message to file for inspection
    msg_file = REPORTS_DIR / f"{date_str}-feishu-message.txt"
    with open(msg_file, 'w', encoding='utf-8') as f:
        f.write(final_message)
    print(f"💾 消息预览已保存: {msg_file}")
    print()
    
    # Instructions for sending
    print("=" * 60)
    print("📋 发送说明")
    print("=" * 60)
    print("""
由于飞书 API 限制，请使用以下方式发送：

方式一: 通过 OpenClaw message 工具
   运行命令:
   message send --channel feishu --target oc_2e444bf6868806df491a6cfcf7ad4a41 \\
       --file ~/Documents/arxiv每日阅读/reports/YYYY-MM-DD-feishu-message.txt

方式二: 手动复制发送
   1. 打开飞书群聊
   2. 复制文件内容: {msg_file}
   3. 粘贴到群聊发送

方式三: 使用飞书文档
   1. 创建飞书文档
   2. 导入 Markdown 报告
   3. 分享文档链接到群聊
""")
    
    return True


if __name__ == "__main__":
    date = sys.argv[1] if len(sys.argv) > 1 else None
    success = send_to_feishu(date)
    sys.exit(0 if success else 1)
