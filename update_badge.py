#!/usr/bin/env python3
"""
Update badge text to remove emoji and make it more sophisticated
"""

import re
from pathlib import Path

def update_html_file(file_path):
    """Update badge text in HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace badge with emoji to elegant text-only version
        old_badge = r'<div class="badge">🦀 Rust Development</div>'
        new_badge = '<div class="badge">RUST DEVELOPMENT</div>'
        
        if old_badge in content:
            updated_content = content.replace(old_badge, new_badge)
            
            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print(f"✅ Updated: {file_path}")
            return True
        
        return False
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
    
    print(f"\n✨ Updated {updated_count} files - removed emoji from badges")

if __name__ == "__main__":
    main()
