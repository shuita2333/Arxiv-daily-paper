#!/usr/bin/env python3
"""
Send email via QQ Mail SMTP
"""

import smtplib
import sys
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

BASE_DIR = Path.home() / "Documents" / "arxiv每日阅读"
REPORTS_DIR = BASE_DIR / "reports"


def send_via_qq(qq_number, auth_code, recipient, date_str=None):
    """Send report via QQ Mail."""
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    report_file = REPORTS_DIR / f"{date_str}-report.md"
    
    if not report_file.exists():
        print(f"❌ Report not found: {report_file}")
        return False
    
    # Read report
    with open(report_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    subject = f"📚 每日 arXiv 论文精选 | {date_str}"
    
    msg = MIMEMultipart()
    msg['From'] = f"{qq_number}@qq.com"
    msg['To'] = recipient
    msg['Subject'] = subject
    
    body = f"这是今日的 arXiv 论文精选日报。\n\n报告日期: {date_str}\n\n请查看附件。"
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    
    # Attach report
    with open(report_file, 'rb') as f:
        attachment = MIMEText(f.read(), 'plain', 'utf-8')
        attachment.add_header('Content-Disposition', 'attachment', 
                             filename=report_file.name)
        msg.attach(attachment)
    
    try:
        print(f"📧 Connecting to QQ Mail...")
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        
        print(f"🔐 Logging in...")
        server.login(f"{qq_number}@qq.com", auth_code)
        
        print(f"📤 Sending to {recipient}...")
        server.send_message(msg)
        server.quit()
        
        print(f"✅ Email sent successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n获取 QQ 邮箱授权码：")
        print("1. 登录 QQ 邮箱网页版")
        print("2. 设置 → 账户 → 开启 SMTP")
        print("3. 获取 16 位授权码")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: send_qq.py <qq_number> <auth_code> <recipient_email> [date]")
        print("\nExample:")
        print("  send_qq.py 603747072 your_auth_code 603747072@qq.com 2026-04-04")
        sys.exit(1)
    
    qq = sys.argv[1]
    auth = sys.argv[2]
    recipient = sys.argv[3]
    date = sys.argv[4] if len(sys.argv) > 4 else None
    
    success = send_via_qq(qq, auth, recipient, date)
    sys.exit(0 if success else 1)
