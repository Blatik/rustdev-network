#!/usr/bin/env python3
"""
Update all HTML forms to use full Cloudflare Worker URL
"""

import os
import re
from pathlib import Path

# Configuration
OLD_ACTION = "/api/leads"
NEW_ACTION = "https://rustdev-network-worker.blatik-short.workers.dev/api/leads"

def update_html_file(file_path):
    """Update form action in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file contains the old action
        if OLD_ACTION not in content:
            return False
        
        # Replace old action with new action
        updated_content = content.replace(f'action="{OLD_ACTION}"', f'action="{NEW_ACTION}"')
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✅ Updated: {file_path}")
        return True
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False

def main():
    """Find and update all HTML files"""
    base_dir = Path(__file__).parent
    updated_count = 0
    
    # Find all index.html files in subdirectories
    for html_file in base_dir.rglob("*/index.html"):
        if update_html_file(html_file):
            updated_count += 1
    
    # Also update root HTML files
    for html_file in base_dir.glob("*.html"):
        if update_html_file(html_file):
            updated_count += 1
    
    print(f"\n🎉 Updated {updated_count} files")
    print(f"Old action: {OLD_ACTION}")
    print(f"New action: {NEW_ACTION}")

if __name__ == "__main__":
    main()
