#!/usr/bin/env python3
"""
Update all pages to Premium Titanium Theme - Solid & Sophisticated
"""

import re
from pathlib import Path

# Premium Titanium Theme CSS - Solid & Sophisticated
TITANIUM_CSS = """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0a0a0a;
            background-image: 
                radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.03) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(168, 85, 247, 0.03) 0px, transparent 50%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            position: relative;
        }

        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.01) 50%, transparent 100%),
                repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(255,255,255,0.01) 2px, rgba(255,255,255,0.01) 4px);
            pointer-events: none;
            opacity: 0.5;
        }

        .container {
            background: linear-gradient(135deg, rgba(30, 30, 35, 0.95) 0%, rgba(20, 20, 25, 0.98) 100%);
            backdrop-filter: blur(40px) saturate(180%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 32px;
            padding: 60px 40px;
            max-width: 600px;
            box-shadow: 
                0 20px 60px rgba(0, 0, 0, 0.5),
                0 0 0 1px rgba(255, 255, 255, 0.03),
                inset 0 1px 0 rgba(255, 255, 255, 0.06),
                inset 0 -1px 0 rgba(0, 0, 0, 0.4);
            text-align: center;
            position: relative;
            z-index: 1;
        }

        .container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        }

        h1 {
            font-size: 2.75rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            background: linear-gradient(135deg, 
                #e8e8e8 0%, 
                #ffffff 25%, 
                #c0c0c0 50%, 
                #ffffff 75%, 
                #e8e8e8 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 16px;
            line-height: 1.1;
            animation: shimmer 8s linear infinite;
            text-shadow: 0 0 40px rgba(255, 255, 255, 0.1);
        }

        @keyframes shimmer {
            0% { background-position: 0% center; }
            100% { background-position: 200% center; }
        }

        p {
            font-size: 1.05rem;
            color: rgba(200, 200, 210, 0.85);
            margin-bottom: 40px;
            line-height: 1.7;
            font-weight: 400;
            letter-spacing: 0.01em;
        }

        form {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        input[type="email"] {
            padding: 18px 24px;
            font-size: 1rem;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            color: #e8e8e8;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            font-weight: 400;
            letter-spacing: 0.01em;
        }

        input[type="email"]:focus {
            outline: none;
            background: rgba(255, 255, 255, 0.05);
            border-color: rgba(200, 200, 210, 0.3);
            box-shadow: 
                0 0 0 4px rgba(200, 200, 210, 0.08),
                0 8px 24px rgba(0, 0, 0, 0.3);
            transform: translateY(-1px);
        }

        input[type="email"]::placeholder {
            color: rgba(200, 200, 210, 0.4);
        }

        button {
            padding: 18px 32px;
            font-size: 1.05rem;
            font-weight: 600;
            letter-spacing: 0.02em;
            color: #0a0a0a;
            background: linear-gradient(135deg, #e8e8e8 0%, #ffffff 50%, #e8e8e8 100%);
            background-size: 200% auto;
            border: none;
            border-radius: 16px;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            box-shadow: 
                0 4px 16px rgba(255, 255, 255, 0.15),
                inset 0 1px 0 rgba(255, 255, 255, 0.4);
        }

        button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
            transition: left 0.6s;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 
                0 8px 32px rgba(255, 255, 255, 0.25),
                inset 0 1px 0 rgba(255, 255, 255, 0.6);
            background-position: 100% center;
        }

        button:hover::before {
            left: 100%;
        }

        button:active {
            transform: translateY(0);
        }

        .badge {
            display: inline-block;
            background: rgba(200, 200, 210, 0.08);
            color: rgba(200, 200, 210, 0.9);
            padding: 10px 20px;
            border-radius: 24px;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            margin-bottom: 24px;
            border: 1px solid rgba(200, 200, 210, 0.12);
        }

        .main-nav {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            padding: 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            z-index: 10;
        }

        .nav-logo {
            font-weight: 700;
            font-size: 1.25rem;
            letter-spacing: -0.01em;
            background: linear-gradient(135deg, #e8e8e8 0%, #ffffff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-decoration: none;
        }

        .nav-links a {
            margin-left: 24px;
            color: rgba(200, 200, 210, 0.85);
            text-decoration: none;
            font-weight: 500;
            font-size: 0.95rem;
            background: rgba(255, 255, 255, 0.04);
            backdrop-filter: blur(10px);
            padding: 10px 20px;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.06);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            letter-spacing: 0.01em;
        }

        .nav-links a:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(255, 255, 255, 0.12);
            color: #ffffff;
            transform: translateY(-1px);
        }

        /* Mobile Responsiveness */
        @media (max-width: 600px) {
            .container {
                padding: 40px 24px;
                margin-top: 80px;
                border-radius: 24px;
            }

            h1 {
                font-size: 2rem;
            }

            p {
                font-size: 0.95rem;
                margin-bottom: 32px;
            }

            .main-nav {
                padding: 16px;
                flex-direction: column;
                gap: 16px;
            }

            .nav-links a {
                margin-left: 0;
                display: block;
                text-align: center;
            }

            button {
                padding: 16px 28px;
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
        replacement = f'<style>{TITANIUM_CSS}    </style>'
        
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
    
    print(f"\n✨ Updated {updated_count} files to Premium Titanium Theme")

if __name__ == "__main__":
    main()
