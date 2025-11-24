#!/usr/bin/env python3
"""
Update about.html and index.html to premium titanium theme
"""

import re
from pathlib import Path

# Premium Titanium CSS for about.html
TITANIUM_CSS_ABOUT = """
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
            padding: 40px 20px;
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
            max-width: 900px;
            margin: 0 auto;
            background: linear-gradient(135deg, rgba(30, 30, 35, 0.95) 0%, rgba(20, 20, 25, 0.98) 100%);
            backdrop-filter: blur(40px) saturate(180%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 32px;
            padding: 60px 50px;
            box-shadow: 
                0 20px 60px rgba(0, 0, 0, 0.5),
                inset 0 1px 0 rgba(255, 255, 255, 0.06);
            position: relative;
            z-index: 1;
        }

        h1 {
            font-size: 2.75rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            background: linear-gradient(135deg, #e8e8e8 0%, #ffffff 25%, #c0c0c0 50%, #ffffff 75%, #e8e8e8 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 20px;
            text-align: center;
            animation: shimmer 8s linear infinite;
        }

        @keyframes shimmer {
            0% { background-position: 0% center; }
            100% { background-position: 200% center; }
        }

        .tagline {
            text-align: center;
            font-size: 1.2rem;
            color: rgba(200, 200, 210, 0.7);
            font-weight: 500;
            margin-bottom: 40px;
            letter-spacing: 0.02em;
        }

        h2 {
            font-size: 1.8rem;
            font-weight: 700;
            letter-spacing: -0.01em;
            background: linear-gradient(135deg, #e8e8e8 0%, #ffffff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 40px 0 20px;
            border-left: 3px solid rgba(255, 255, 255, 0.3);
            padding-left: 15px;
        }

        p {
            font-size: 1.05rem;
            color: rgba(200, 200, 210, 0.8);
            line-height: 1.8;
            margin-bottom: 20px;
            font-weight: 400;
        }

        strong {
            color: rgba(255, 255, 255, 0.95);
            font-weight: 600;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            margin: 40px 0;
        }

        .stat {
            text-align: center;
            padding: 30px 20px;
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            transition: all 0.3s;
        }

        .stat:hover {
            transform: translateY(-4px);
            border-color: rgba(255, 255, 255, 0.15);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
        }

        .stat-number {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(135deg, #e8e8e8 0%, #ffffff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 10px;
        }

        .stat-label {
            font-size: 1rem;
            color: rgba(200, 200, 210, 0.7);
            font-weight: 500;
        }

        .services {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }

        .service {
            padding: 25px;
            background: rgba(255, 255, 255, 0.04);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            transition: all 0.3s;
        }

        .service:hover {
            transform: translateY(-4px);
            border-color: rgba(255, 255, 255, 0.15);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
        }

        .service h3 {
            font-size: 1.3rem;
            margin-bottom: 10px;
            color: rgba(255, 255, 255, 0.95);
            font-weight: 600;
        }

        .service p {
            color: rgba(200, 200, 210, 0.75);
            font-size: 1rem;
        }

        .cta {
            text-align: center;
            margin: 40px 0;
            padding: 40px 30px;
            background: rgba(255, 255, 255, 0.04);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
        }

        .cta h3 {
            background: linear-gradient(135deg, #e8e8e8 0%, #ffffff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 1.5rem;
            margin-bottom: 20px;
            font-weight: 700;
        }

        .cta form {
            display: flex;
            gap: 10px;
            max-width: 500px;
            margin: 0 auto;
            flex-wrap: wrap;
            justify-content: center;
        }

        .cta input[type="email"] {
            flex: 1;
            min-width: 250px;
            padding: 15px 20px;
            font-size: 1rem;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            color: #e8e8e8;
        }

        .cta input[type="email"]::placeholder {
            color: rgba(200, 200, 210, 0.4);
        }

        .cta button {
            padding: 15px 30px;
            font-size: 1rem;
            font-weight: 600;
            color: #0a0a0a;
            background: linear-gradient(135deg, #e8e8e8 0%, #ffffff 100%);
            border: none;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .cta button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(255, 255, 255, 0.2);
        }

        .main-nav {
            background: rgba(30, 30, 35, 0.9);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
            padding: 15px 0;
            margin-bottom: 40px;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .nav-container {
            max-width: 900px;
            margin: 0 auto;
            padding: 0 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .nav-logo {
            font-weight: 700;
            font-size: 1.2rem;
            background: linear-gradient(135deg, #e8e8e8 0%, #ffffff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-decoration: none;
        }

        .nav-links a {
            margin-left: 20px;
            color: rgba(200, 200, 210, 0.85);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s;
        }

        .nav-links a:hover {
            color: #ffffff;
        }

        .nav-links a.active {
            color: #ffffff;
            font-weight: 600;
        }

        @media (max-width: 768px) {
            body { padding: 20px 10px; }
            .container { padding: 40px 20px; }
            h1 { font-size: 2rem; }
            .stats { grid-template-columns: 1fr; }
            .services { grid-template-columns: 1fr; }
            .nav-container { flex-direction: column; gap: 15px; }
            .nav-links a { margin-left: 0; }
            .cta input[type="email"] { min-width: 100%; }
        }
"""

TITANIUM_CSS_INDEX = """
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
            color: rgba(200, 200, 210, 0.9);
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
            min-height: 100vh;
        }

        h1 {
            text-align: center;
            font-size: 2.75rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            background: linear-gradient(135deg, #e8e8e8 0%, #ffffff 25%, #c0c0c0 50%, #ffffff 75%, #e8e8e8 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 40px;
            animation: shimmer 8s linear infinite;
        }

        @keyframes shimmer {
            0% { background-position: 0% center; }
            100% { background-position: 200% center; }
        }

        .card {
            background: linear-gradient(135deg, rgba(30, 30, 35, 0.6) 0%, rgba(20, 20, 25, 0.8) 100%);
            backdrop-filter: blur(20px);
            padding: 24px;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
            margin-bottom: 20px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .card:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
            border-color: rgba(255, 255, 255, 0.15);
        }

        .card h2 {
            margin-top: 0;
            font-size: 1.3rem;
            font-weight: 600;
            background: linear-gradient(135deg, #e8e8e8 0%, #ffffff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 8px;
        }

        .card p {
            color: rgba(200, 200, 210, 0.7);
            margin: 10px 0;
            line-height: 1.6;
        }

        .card a {
            color: rgba(255, 255, 255, 0.9);
            text-decoration: none;
            font-weight: 600;
            transition: color 0.2s;
        }

        .card a:hover {
            color: #ffffff;
            text-decoration: underline;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }

        .main-nav {
            background: rgba(30, 30, 35, 0.9);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
            padding: 15px 0;
            margin-bottom: 40px;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .nav-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 0 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .nav-logo {
            font-weight: 700;
            font-size: 1.2rem;
            background: linear-gradient(135deg, #e8e8e8 0%, #ffffff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-decoration: none;
        }

        .nav-links a {
            margin-left: 20px;
            color: rgba(200, 200, 210, 0.85);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s;
        }

        .nav-links a:hover {
            color: #ffffff;
        }

        .nav-links a.active {
            color: #ffffff;
            font-weight: 600;
        }

        @media (max-width: 600px) {
            body { padding: 20px 10px; }
            .grid { grid-template-columns: 1fr; }
            .nav-container { flex-direction: column; gap: 15px; }
            .nav-links a { margin-left: 0; }
        }
"""

def update_file(file_path, css_content):
    """Update CSS in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        pattern = r'<style>.*?</style>'
        replacement = f'<style>{css_content}    </style>'
        
        if re.search(pattern, content, re.DOTALL):
            updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print(f"✅ Updated: {file_path}")
            return True
        
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    base_dir = Path(__file__).parent
    
    about_path = base_dir / "about.html"
    if about_path.exists():
        update_file(about_path, TITANIUM_CSS_ABOUT)
    
    index_path = base_dir / "index.html"
    if index_path.exists():
        update_file(index_path, TITANIUM_CSS_INDEX)
    
    print("\n✨ Updated home and about to Premium Titanium Theme!")

if __name__ == "__main__":
    main()
