#!/usr/bin/env python3
"""
ArXiv Daily Complete Workflow
End-to-end automation: Fetch → Analyze → Generate → Publish to GitHub
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Configuration
BASE_DIR = Path.home() / "Documents" / "arxiv每日阅读"
DAILY_DIR = BASE_DIR / "daily"
PAPERS_DIR = BASE_DIR / "papers"
SCRIPTS_DIR = BASE_DIR / "scripts"


def run_step(step_name, script_name, *args, check=True):
    """Run a workflow step and handle errors."""
    print(f"\n{'='*60}")
    print(f"📌 {step_name}")
    print(f"{'='*60}")
    
    cmd = [sys.executable, str(SCRIPTS_DIR / script_name)] + list(args)
    
    try:
        result = subprocess.run(
            cmd,
            cwd=BASE_DIR,
            check=check,
            capture_output=False,
            text=True
        )
        print(f"✅ {step_name} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {step_name} failed with exit code {e.returncode}")
        return False


def check_prerequisites():
    """Check if required directories and files exist."""
    print("🔍 Checking prerequisites...")
    
    required_paths = [
        BASE_DIR,
        DAILY_DIR,
        PAPERS_DIR,
        SCRIPTS_DIR,
    ]
    
    for path in required_paths:
        if not path.exists():
            print(f"  Creating: {path}")
            path.mkdir(parents=True, exist_ok=True)
    
    # Check if Git repo is initialized
    git_dir = BASE_DIR / ".git"
    if not git_dir.exists():
        print("⚠️  Git repository not initialized. Running git init...")
        subprocess.run(["git", "init"], cwd=BASE_DIR, check=True)
    
    # Check remote
    result = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        cwd=BASE_DIR,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print("⚠️  GitHub remote not configured. Adding...")
        subprocess.run(
            ["git", "remote", "add", "origin", 
             "https://github.com/shuita2333/Arxiv-daily-paper.git"],
            cwd=BASE_DIR,
            check=True
        )
    
    print("✅ Prerequisites check passed\n")
    return True


def workflow(date_str=None, skip_fetch=False, skip_analyze=False, 
             skip_generate=False, skip_publish=False):
    """Run complete workflow."""
    
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    print(f"\n🚀 ArXiv Daily Complete Workflow")
    print(f"📅 Date: {date_str}")
    print(f"{'='*60}\n")
    
    # Check prerequisites
    if not check_prerequisites():
        return False
    
    success = True
    
    # Step 1: Fetch
    if not skip_fetch:
        if not run_step("Step 1: Fetch Papers from ArXiv", "fetch_papers.py"):
            print("\n⚠️  Fetch failed. Stopping workflow.")
            return False
    else:
        print("⏭️  Skipping Step 1 (Fetch)")
    
    # Step 2: Analyze
    if not skip_analyze:
        if not run_step("Step 2: AI Semantic Analysis (Kimi)", 
                       "analyze_papers.py", date_str):
            print("\n⚠️  Analysis failed. Stopping workflow.")
            return False
    else:
        print("⏭️  Skipping Step 2 (Analyze)")
    
    # Step 3: Generate
    if not skip_generate:
        if not run_step("Step 3: Generate Markdown Report",
                       "generate_report.py", date_str):
            print("\n⚠️  Generation failed. Stopping workflow.")
            return False
    else:
        print("⏭️  Skipping Step 3 (Generate)")
    
    # Step 4: Publish
    if not skip_publish:
        if not run_step("Step 4: Publish to GitHub",
                       "publish_to_github.py", date_str):
            print("\n⚠️  Publish failed. Report saved locally.")
            print(f"   Manual push: cd {BASE_DIR} && git push origin main")
            success = False
    else:
        print("⏭️  Skipping Step 4 (Publish)")
    
    # Summary
    print(f"\n{'='*60}")
    if success:
        print("✅ Workflow completed successfully!")
        print(f"\n📊 Output:")
        print(f"   JSON data:  {DAILY_DIR}/{date_str}.json")
        print(f"   Report:     {PAPERS_DIR}/{date_str}.md")
        print(f"\n🔗 GitHub:")
        print(f"   https://github.com/shuita2333/Arxiv-daily-paper")
    else:
        print("⚠️  Workflow completed with warnings")
    print(f"{'='*60}\n")
    
    return success


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="ArXiv Daily Complete Workflow",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run complete workflow for today
  %(prog)s
  
  # Run for specific date
  %(prog)s 2026-04-06
  
  # Skip fetching (use existing data)
  %(prog)s --skip-fetch
  
  # Only analyze and generate
  %(prog)s --skip-fetch --skip-publish
        """
    )
    
    parser.add_argument("date", nargs="?", help="Date in YYYY-MM-DD format")
    parser.add_argument("--skip-fetch", action="store_true",
                       help="Skip fetching from ArXiv")
    parser.add_argument("--skip-analyze", action="store_true",
                       help="Skip AI analysis")
    parser.add_argument("--skip-generate", action="store_true",
                       help="Skip report generation")
    parser.add_argument("--skip-publish", action="store_true",
                       help="Skip GitHub publishing")
    
    args = parser.parse_args()
    
    success = workflow(
        date_str=args.date,
        skip_fetch=args.skip_fetch,
        skip_analyze=args.skip_analyze,
        skip_generate=args.skip_generate,
        skip_publish=args.skip_publish
    )
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
