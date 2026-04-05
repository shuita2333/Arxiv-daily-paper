#!/bin/bash
# Daily ArXiv Report - Complete Workflow
# Fetches, analyzes, generates, and sends daily arXiv reports

set -e  # Exit on error

echo "=========================================="
echo "📚 ArXiv Daily Report - Complete Workflow"
echo "=========================================="
echo ""

cd ~/Documents/arxiv每日阅读

# Configuration
DATE=${1:-$(date +%Y-%m-%d)}
SENDER_EMAIL="6011meng@gmail.com"
APP_PASSWORD="unvfelomxgjmddwa"
RECIPIENT_EMAIL="603747072@qq.com"

echo "📅 Date: $DATE"
echo ""

# Step 1: Fetch papers
echo "Step 1/4: 📥 Fetching papers from arXiv..."
python3 scripts/fetch_papers.py
echo ""

# Step 2: Analyze papers
echo "Step 2/4: 🔍 Analyzing and classifying papers..."
python3 scripts/analyze_papers.py
echo ""

# Step 3: Generate report
echo "Step 3/4: 📝 Generating Markdown report..."
python3 scripts/generate_report.py "$DATE"
echo ""

# Step 4: Send email
echo "Step 4/4: 📧 Sending report via email..."
python3 scripts/send_email.py \
    "$SENDER_EMAIL" \
    "$APP_PASSWORD" \
    "$RECIPIENT_EMAIL" \
    "$DATE"
echo ""

echo "=========================================="
echo "✅ Daily ArXiv report completed!"
echo "=========================================="
echo ""
echo "📊 Report sent to: $RECIPIENT_EMAIL"
echo "📄 Report file: reports/$DATE-report.md"
