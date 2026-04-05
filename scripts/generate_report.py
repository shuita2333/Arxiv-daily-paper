#!/usr/bin/env python3
"""
ArXiv Daily Report Generator
Generates formatted Markdown reports from daily arXiv paper JSON files.
"""

import json
import re
from datetime import datetime
from pathlib import Path

# Configuration
BASE_DIR = Path.home() / "Documents" / "arxiv每日阅读"
DAILY_DIR = BASE_DIR / "daily"
REPORTS_DIR = BASE_DIR / "reports"

# Ensure reports directory exists
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# Font color definitions (fixed)
FONT_COLORS = {
    "authors": "#1a73e8",    # 蓝色
    "subject": "#188038",    # 绿色
    "type": "#c5221f",       # 红色
    "abstract": "#5f6368",   # 灰色
}

# Module headers
MODULES = {
    1: {"emoji": "🔐", "title": "一、大模型安全相关研究", "desc": "探索大模型在安全性、可靠性、对齐等方面的最新进展"},
    2: {"emoji": "🧠", "title": "二、大模型内生能力研究", "desc": "挖掘大模型在推理、规划、学习等方面的能力边界"},
    3: {"emoji": "🔬", "title": "三、大模型相关研究", "desc": "涵盖架构、训练、优化等大模型核心技术"},
}


def extract_arxiv_id_last5(link):
    """Extract last 5 digits from arXiv ID for sorting."""
    # Link format: https://arxiv.org/abs/2604.01234
    match = re.search(r'/abs/(\d+)\.(\d+)', link)
    if match:
        # Return the last 5 digits of the full ID
        full_id = match.group(1) + match.group(2)
        return full_id[-5:].zfill(5)
    return "00000"


def sort_papers(papers):
    """Sort papers by correlation (ascending), then by arXiv ID last 5 digits (ascending)."""
    return sorted(papers, key=lambda p: (p.get('correlation', 4), extract_arxiv_id_last5(p.get('link', ''))))


def format_authors(authors):
    """Format authors list."""
    if not authors:
        return "Unknown"
    if len(authors) <= 3:
        return ", ".join(authors)
    return ", ".join(authors[:3]) + f" 等 {len(authors)} 位作者"


def truncate_abstract(abstract, max_len=400):
    """Truncate abstract if too long."""
    if len(abstract) <= max_len:
        return abstract
    return abstract[:max_len].rsplit(' ', 1)[0] + "..."


def generate_paper_section(paper, index):
    """Generate Markdown section for a single paper."""
    title = paper.get('title', 'Untitled')
    link = paper.get('link', '')
    authors = paper.get('authors', [])
    subject = paper.get('subject', 'Unknown')
    abstract = paper.get('abstract', '')
    submission_type = paper.get('submission_type', 'new')
    
    type_str = "Cross Submission" if submission_type == "cross" else "New Submission"
    
    # Truncate abstract
    abstract_short = truncate_abstract(abstract)
    
    section = f"""### {index}. [{title}]({link})

**<font color={FONT_COLORS['authors']}>作者：</font>** {format_authors(authors)}  
**<font color={FONT_COLORS['subject']}>arXiv所属领域：</font>** {subject}

**<font color={FONT_COLORS['abstract']}>摘要：</font>**
> {abstract_short}

---

"""
    return section


def generate_report(date_str=None):
    """Generate daily report for specified date."""
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    input_file = DAILY_DIR / f"{date_str}.json"
    output_file = REPORTS_DIR / f"{date_str}-report.md"
    
    if not input_file.exists():
        print(f"Error: Input file not found: {input_file}")
        return None
    
    # Load papers
    with open(input_file, 'r', encoding='utf-8') as f:
        papers = json.load(f)
    
    print(f"Generating report for {date_str}...")
    print(f"Total papers: {len(papers)}")
    
    # Sort papers
    sorted_papers = sort_papers(papers)
    
    # Count by correlation
    stats = {1: 0, 2: 0, 3: 0, 4: 0}
    for p in sorted_papers:
        stats[p.get('correlation', 4)] += 1
    
    total_llm = stats[1] + stats[2] + stats[3]
    
    # Generate date string in Chinese format
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    date_chinese = date_obj.strftime('%Y年%m月%d日')
    
    # Generate report content
    report_lines = []
    
    # Header
    report_lines.append(f"# 📚 每日 arXiv 论文精选 | {date_chinese}")
    report_lines.append("")
    report_lines.append(f"> 🎯 今日精选 **{total_llm}** 篇大模型相关论文")
    report_lines.append("> ")
    report_lines.append("> 🔐 安全研究 · 🧠 能力探索 · 🔬 相关技术")
    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")
    
    # Generate modules for levels 1, 2, 3
    paper_counter = 1
    for level in [1, 2, 3]:
        if stats[level] == 0:
            continue
            
        module = MODULES[level]
        report_lines.append(f"## {module['emoji']} {module['title']}")
        report_lines.append("")
        report_lines.append(f"> {module['desc']}")
        report_lines.append("")
        report_lines.append("---")
        report_lines.append("")
        
        # Add papers for this level
        level_papers = [p for p in sorted_papers if p.get('correlation') == level]
        for paper in level_papers:
            report_lines.append(generate_paper_section(paper, paper_counter))
            paper_counter += 1
    
    # Statistics section
    report_lines.append("## 📊 今日统计")
    report_lines.append("")
    report_lines.append("| 类别 | 数量 | 占比 |")
    report_lines.append("|------|------|------|")
    
    categories = [
        ("🔐 安全研究", stats[1]),
        ("🧠 能力研究", stats[2]),
        ("🔬 相关技术", stats[3]),
    ]
    
    for name, count in categories:
        percentage = (count / total_llm * 100) if total_llm > 0 else 0
        report_lines.append(f"| {name} | {count} | {percentage:.1f}% |")
    
    report_lines.append(f"| **总计** | **{total_llm}** | **100%** |")
    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")
    report_lines.append("*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*")
    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")
    report_lines.append("## 🏷️ 标签说明")
    report_lines.append("")
    report_lines.append("- **🔐 安全研究**：大模型安全、对齐、鲁棒性、隐私保护等")
    report_lines.append("- **🧠 能力研究**：推理、规划、知识获取、工具使用等能力探索")
    report_lines.append("- **🔬 相关技术**：架构设计、训练方法、优化技术等基础研究")
    
    # Write report
    report_content = "\n".join(report_lines)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"\nReport generated: {output_file}")
    print(f"\nStatistics:")
    print(f"  Level 1 (安全研究): {stats[1]} papers")
    print(f"  Level 2 (能力研究): {stats[2]} papers")
    print(f"  Level 3 (相关技术): {stats[3]} papers")
    print(f"  Total: {total_llm} papers")
    
    return output_file


def main():
    """Main entry point."""
    import sys
    
    date_str = None
    if len(sys.argv) > 1:
        date_str = sys.argv[1]
    
    output_file = generate_report(date_str)
    
    if output_file:
        print(f"\n✅ Report saved to: {output_file}")
    else:
        print("\n❌ Failed to generate report")


if __name__ == "__main__":
    main()
