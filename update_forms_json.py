#!/usr/bin/env python3
"""
Update form handling JavaScript in all HTML files to handle JSON response
"""

import os
import re
from pathlib import Path

def update_html_file(file_path):
    """Update JavaScript in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated = False
        
        # Pattern 1: window.location.href = 'thank-you.html';
        pattern1 = r"if \(response\.ok\) \{\s*// Redirect to thank you page\s*window\.location\.href = 'thank-you\.html';"
        replacement1 = """if (response.ok) {
                        const data = await response.json();
                        if (data.success && data.redirect) {
                            window.location.href = data.redirect;
                        } else {
                            window.location.href = 'thank-you.html';
                        }"""
        
        if re.search(pattern1, content):
            content = re.sub(pattern1, replacement1, content)
            updated = True
        
        # Pattern 2: window.location.href = '../thank-you.html';
        pattern2 = r"if \(response\.ok\) \{\s*// Redirect to thank you page\s*window\.location\.href = '\.\./thank-you\.html';"
        replacement2 = """if (response.ok) {
                        const data = await response.json();
                        if (data.success && data.redirect) {
                            window.location.href = data.redirect;
                        } else {
                            window.location.href = '../thank-you.html';
                        }"""
        
        if re.search(pattern2, content):
            content = re.sub(pattern2, replacement2, content)
            updated = True
        
        if updated:
            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
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
    
    # Also update root HTML files
    for html_file in base_dir.glob("*.html"):
        if update_html_file(html_file):
            updated_count += 1
    
    print(f"\n🎉 Updated {updated_count} files")

if __name__ == "__main__":
    main()
