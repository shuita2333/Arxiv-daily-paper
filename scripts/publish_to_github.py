#!/usr/bin/env python3
"""
ArXiv Daily Report Publisher
Commits and pushes daily reports to GitHub repository.
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Configuration
BASE_DIR = Path.home() / "Documents" / "arxiv每日阅读"
PAPERS_DIR = BASE_DIR / "papers"

# GitHub Repository
GITHUB_REPO = "https://github.com/shuita2333/Arxiv-daily-paper.git"


def run_git_command(cmd, cwd=None):
    """Run a git command and return success status."""
    if cwd is None:
        cwd = BASE_DIR
    
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr


def check_git_status():
    """Check if there are changes to commit."""
    success, output = run_git_command(["git", "status", "--porcelain"])
    if not success:
        print(f"❌ Error checking git status: {output}")
        return False
    
    # If output is empty, no changes
    return bool(output.strip())


def stage_files(date_str):
    """Stage the daily report file."""
    report_file = PAPERS_DIR / f"{date_str}.md"
    
    if not report_file.exists():
        print(f"❌ Report file not found: {report_file}")
        return False
    
    success, output = run_git_command(["git", "add", str(report_file)])
    if not success:
        print(f"❌ Error staging file: {output}")
        return False
    
    print(f"✅ Staged: {report_file.name}")
    return True


def commit_changes(date_str):
    """Commit the changes."""
    commit_message = f"Add daily report for {date_str}"
    
    success, output = run_git_command(["git", "commit", "-m", commit_message])
    if not success:
        # Check if it's "nothing to commit" error
        if "nothing to commit" in output.lower():
            print("ℹ️  Nothing to commit (file may already be committed)")
            return True
        print(f"❌ Error committing: {output}")
        return False
    
    print(f"✅ Committed: {commit_message}")
    return True


def push_to_github():
    """Push changes to GitHub."""
    print("🚀 Pushing to GitHub...")
    
    success, output = run_git_command(["git", "push", "origin", "main"])
    if not success:
        print(f"❌ Error pushing: {output}")
        return False
    
    print("✅ Successfully pushed to GitHub!")
    print(f"📎 Repository: {GITHUB_REPO}")
    return True


def verify_remote():
    """Verify GitHub remote is configured."""
    success, output = run_git_command(["git", "remote", "-v"])
    if not success:
        return False
    
    if GITHUB_REPO not in output:
        print(f"⚠️  Remote not found. Adding...")
        success, _ = run_git_command(["git", "remote", "add", "origin", GITHUB_REPO])
        if not success:
            print("❌ Failed to add remote")
            return False
    
    return True


def publish(date_str=None):
    """Main publish workflow."""
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    print("=" * 60)
    print(f"📤 Publishing daily report for {date_str}")
    print("=" * 60)
    print()
    
    # Change to base directory
    if not BASE_DIR.exists():
        print(f"❌ Directory not found: {BASE_DIR}")
        return False
    
    # Verify remote
    print("🔍 Verifying GitHub remote...")
    if not verify_remote():
        return False
    print("✅ Remote verified")
    print()
    
    # Stage files
    print("📦 Staging files...")
    if not stage_files(date_str):
        return False
    print()
    
    # Commit
    print("📝 Committing changes...")
    if not commit_changes(date_str):
        return False
    print()
    
    # Push
    if not push_to_github():
        return False
    print()
    
    print("=" * 60)
    print("✅ Publish complete!")
    print("=" * 60)
    return True


def main():
    """Main entry point."""
    date_str = None
    if len(sys.argv) > 1:
        date_str = sys.argv[1]
    
    success = publish(date_str)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
