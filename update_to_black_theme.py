#!/usr/bin/env python3
"""
Update all HTML files to premium black theme
"""

import re
from pathlib import Path

# Premium Black Theme CSS
PREMIUM_BLACK_CSS = """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 50%, #0f0f0f 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            position: relative;
            overflow-x: hidden;
        }

        body::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 20% 50%, rgba(120, 119, 198, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(255, 107, 107, 0.1) 0%, transparent 50%);
            pointer-events: none;
        }

        .container {
            background: rgba(26, 26, 46, 0.8);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 24px;
            padding: 60px 40px;
            max-width: 600px;
            box-shadow: 
                0 8px 32px rgba(0, 0, 0, 0.4),
                0 0 0 1px rgba(255, 255, 255, 0.05),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
            text-align: center;
            position: relative;
            z-index: 1;
        }

        h1 {
            font-size: 2.5rem;
            background: linear-gradient(135deg, #fff 0%, #a8a8a8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 20px;
            line-height: 1.2;
            font-weight: 700;
        }

        p {
            font-size: 1.1rem;
            color: rgba(255, 255, 255, 0.7);
            margin-bottom: 40px;
            line-height: 1.6;
        }

        form {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        input[type="email"] {
            padding: 18px 20px;
            font-size: 1rem;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            color: #fff;
            transition: all 0.3s;
        }

        input[type="email"]:focus {
            outline: none;
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(120, 119, 198, 0.5);
            box-shadow: 0 0 0 3px rgba(120, 119, 198, 0.1);
        }

        input[type="email"]::placeholder {
            color: rgba(255, 255, 255, 0.4);
        }

        button {
            padding: 18px 20px;
            font-size: 1.1rem;
            font-weight: 600;
            color: #fff;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border: none;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }

        button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s;
        }

        button:hover::before {
            left: 100%;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        }

        button:active {
            transform: translateY(0);
        }

        .badge {
            display: inline-block;
            background: rgba(102, 126, 234, 0.1);
            color: #667eea;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 600;
            margin-bottom: 20px;
            border: 1px solid rgba(102, 126, 234, 0.2);
        }

        .main-nav {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            padding: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            z-index: 10;
        }

        .nav-logo {
            font-weight: bold;
            font-size: 1.2rem;
            color: #fff;
            text-decoration: none;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        }

        .nav-links a {
            margin-left: 20px;
            color: rgba(255, 255, 255, 0.9);
            text-decoration: none;
            font-weight: 600;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 8px 16px;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s;
        }

        .nav-links a:hover {
            background: rgba(255, 255, 255, 0.15);
            border-color: rgba(255, 255, 255, 0.2);
        }

        /* Mobile Responsiveness */
        @media (max-width: 600px) {
            .container {
                padding: 40px 20px;
                margin-top: 60px;
            }

            h1 {
                font-size: 1.8rem;
            }

            p {
                font-size: 1rem;
                margin-bottom: 30px;
            }

            .main-nav {
                padding: 15px;
                flex-direction: column;
                gap: 15px;
            }

            .nav-links a {
                margin-left: 0;
                display: block;
                text-align: center;
            }
        }
"""

def update_html_file(file_path):
    """Update CSS in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the <style> section
        pattern = r'<style>.*?</style>'
        replacement = f'<style>{PREMIUM_BLACK_CSS}    </style>'
        
        if re.search(pattern, content, re.DOTALL):
            updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            
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
    
    print(f"\n🎉 Updated {updated_count} files to Premium Black Theme")

if __name__ == "__main__":
    main()
