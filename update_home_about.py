#!/usr/bin/env python3
"""
Update about.html and index.html to premium black theme with gold gradients
"""

import re
from pathlib import Path

# Premium Black Theme CSS for about.html and index.html
PREMIUM_CSS_ABOUT = """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 50%, #0f0f0f 100%);
            min-height: 100vh;
            padding: 40px 20px;
            position: relative;
        }

        body::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 20% 50%, rgba(255, 215, 0, 0.05) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(255, 107, 107, 0.05) 0%, transparent 50%);
            pointer-events: none;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            background: rgba(26, 26, 46, 0.8);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 24px;
            padding: 60px 50px;
            box-shadow: 
                0 8px 32px rgba(0, 0, 0, 0.4),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
            position: relative;
            z-index: 1;
        }

        h1 {
            font-size: 2.5rem;
            background: linear-gradient(135deg, #FFD700 0%, #FFA500 50%, #FFD700 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 20px;
            text-align: center;
            font-weight: 700;
            text-shadow: 0 0 30px rgba(255, 215, 0, 0.3);
        }

        .tagline {
            text-align: center;
            font-size: 1.2rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 600;
            margin-bottom: 40px;
        }

        h2 {
            font-size: 1.8rem;
            background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 40px 0 20px;
            border-left: 4px solid #FFD700;
            padding-left: 15px;
            font-weight: 700;
        }

        p {
            font-size: 1.1rem;
            color: rgba(255, 255, 255, 0.8);
            line-height: 1.8;
            margin-bottom: 20px;
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
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
        }

        .stat-number {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 10px;
        }

        .stat-label {
            font-size: 1rem;
            color: rgba(255, 255, 255, 0.7);
            font-weight: 600;
        }

        .services {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }

        .service {
            padding: 25px;
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            color: white;
            transition: all 0.3s;
        }

        .service:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        }

        .service h3 {
            font-size: 1.3rem;
            margin-bottom: 10px;
            color: #FFD700;
        }

        .service p {
            color: rgba(255, 255, 255, 0.8);
            font-size: 1rem;
        }

        .cta {
            text-align: center;
            margin: 40px 0;
            padding: 40px 30px;
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
        }

        .cta h3 {
            background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
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
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            color: #fff;
        }

        .cta input[type="email"]::placeholder {
            color: rgba(255, 255, 255, 0.4);
        }

        .cta button {
            padding: 15px 30px;
            font-size: 1rem;
            font-weight: 600;
            color: #000;
            background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .cta button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(255, 215, 0, 0.4);
        }

        .main-nav {
            background: rgba(26, 26, 46, 0.8);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
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
            font-weight: bold;
            font-size: 1.2rem;
            background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-decoration: none;
        }

        .nav-links a {
            margin-left: 20px;
            color: rgba(255, 255, 255, 0.9);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s;
        }

        .nav-links a:hover {
            color: #FFD700;
        }

        .nav-links a.active {
            color: #FFD700;
            font-weight: bold;
        }

        /* Mobile Responsiveness */
        @media (max-width: 768px) {
            body {
                padding: 20px 10px;
            }

            .container {
                padding: 40px 20px;
            }

            h1 {
                font-size: 2rem;
            }

            .stats {
                grid-template-columns: 1fr;
                gap: 20px;
            }

            .services {
                grid-template-columns: 1fr;
            }

            .main-nav {
                padding: 15px;
            }

            .nav-container {
                flex-direction: column;
                gap: 15px;
            }

            .nav-links {
                display: flex;
                gap: 10px;
            }

            .nav-links a {
                margin-left: 0;
                font-size: 0.9rem;
                padding: 8px 12px;
            }

            .cta input[type="email"] {
                min-width: 100%;
            }
        }
"""

PREMIUM_CSS_INDEX = """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 50%, #0f0f0f 100%);
            color: rgba(255, 255, 255, 0.9);
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
            min-height: 100vh;
        }

        h1 {
            text-align: center;
            background: linear-gradient(135deg, #FFD700 0%, #FFA500 50%, #FFD700 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 40px;
            font-size: 2.5rem;
            font-weight: 700;
        }

        .card {
            background: rgba(26, 26, 46, 0.6);
            backdrop-filter: blur(10px);
            padding: 20px;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            margin-bottom: 20px;
            transition: all 0.3s;
        }

        .card:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(255, 215, 0, 0.2);
            border-color: rgba(255, 215, 0, 0.3);
        }

        .card h2 {
            margin-top: 0;
            font-size: 1.2rem;
            background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 600;
        }

        .card p {
            color: rgba(255, 255, 255, 0.7);
            margin: 10px 0;
        }

        .card a {
            color: #FFD700;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.2s;
        }

        .card a:hover {
            color: #FFA500;
            text-decoration: underline;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }

        .main-nav {
            background: rgba(26, 26, 46, 0.8);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
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
            font-weight: bold;
            font-size: 1.2rem;
            background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-decoration: none;
        }

        .nav-links a {
            margin-left: 20px;
            color: rgba(255, 255, 255, 0.9);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s;
        }

        .nav-links a:hover {
            color: #FFD700;
        }

        .nav-links a.active {
            color: #FFD700;
            font-weight: bold;
        }

        /* Mobile Responsiveness */
        @media (max-width: 600px) {
            body {
                padding: 20px 10px;
            }

            .grid {
                grid-template-columns: 1fr;
            }

            .nav-container {
                flex-direction: column;
                gap: 15px;
                align-items: center;
            }

            .nav-links {
                display: flex;
                gap: 10px;
            }

            .nav-links a {
                margin-left: 0;
            }
        }
"""

def update_file(file_path, css_content):
    """Update CSS in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the <style> section
        pattern = r'<style>.*?</style>'
        replacement = f'<style>{css_content}    </style>'
        
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
    """Update about.html and index.html"""
    base_dir = Path(__file__).parent
    
    # Update about.html
    about_path = base_dir / "about.html"
    if about_path.exists():
        update_file(about_path, PREMIUM_CSS_ABOUT)
    
    # Update index.html
    index_path = base_dir / "index.html"
    if index_path.exists():
        update_file(index_path, PREMIUM_CSS_INDEX)
    
    print("\n🎉 Updated home and about pages with gold gradients!")

if __name__ == "__main__":
    main()
