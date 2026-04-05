#!/usr/bin/env python3
"""
Email Sender with better error handling
"""

import smtplib
import sys
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

BASE_DIR = Path.home() / "Documents" / "arxiv每日阅读"
REPORTS_DIR = BASE_DIR / "reports"


def send_report(sender_email, password, recipient_email, date_str=None):
    """Send arXiv report via Gmail SMTP."""
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
    for line in content.split('\n'):
        if line.startswith('# '):
            subject = line[2:].strip()
            break
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    body = f"""您好，

这是今日的 arXiv 论文精选日报。

📊 报告日期: {date_str}
📄 完整报告请查看附件

---

本邮件由自动化脚本生成
"""
    
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    
    # Attach report
    with open(report_file, 'rb') as f:
        attachment = MIMEText(f.read(), 'plain', 'utf-8')
        attachment.add_header('Content-Disposition', 'attachment', 
                             filename=report_file.name)
        msg.attach(attachment)
    
    try:
        print(f"📧 Connecting to Gmail SMTP...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        print(f"🔐 Logging in...")
        server.login(sender_email, password)
        
        print(f"📤 Sending email to {recipient_email}...")
        server.send_message(msg)
        server.quit()
        
        print(f"✅ Email sent successfully!")
        print(f"   From: {sender_email}")
        print(f"   To: {recipient_email}")
        print(f"   Subject: {subject}")
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ Authentication failed: {e}")
        print("\n💡 Please check:")
        print("1. Use Gmail App Password (16 characters)")
        print("2. Enable 2-Step Verification first")
        print("3. Generate App Password at: https://myaccount.google.com/apppasswords")
        print("4. Use the 16-char password WITHOUT spaces")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: send_email.py <sender_email> <app_password> <recipient_email> [date]")
        sys.exit(1)
    
    sender = sys.argv[1]
    password = sys.argv[2]
    recipient = sys.argv[3]
    date = sys.argv[4] if len(sys.argv) > 4 else None
    
    success = send_report(sender, password, recipient, date)
    sys.exit(0 if success else 1)
