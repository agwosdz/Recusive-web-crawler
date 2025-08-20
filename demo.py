#!/usr/bin/env python3
"""
Demo script for the Advanced Web Scraper and HTML Parser
Shows various usage examples and capabilities.
"""

import os
import sys
import json
import argparse
from web_scraper import WebScraper
from termcolor import colored

def demo_html_parsing():
    """Demonstrate HTML file parsing capabilities."""
    print(colored("\n=== HTML FILE PARSING DEMO ===", "yellow", attrs=['bold']))
    
    # Check if there are any HTML files in the current directory
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    if html_files:
        html_file = html_files[0]
        print(f"Parsing HTML file: {html_file}")
        
        scraper = WebScraper(output_format='json')
        results = scraper.parse_html_file(html_file)
        
        if results:
            scraper.print_summary(results)
            
            # Save results
            scraper.save_results(results, f"demo_html_parse")
            print(colored(f"Results saved to demo_html_parse.json", "green"))
        else:
            print(colored("No results obtained from HTML parsing", "red"))
    else:
        print(colored("No HTML files found in current directory", "yellow"))
        print("You can test with: python demo.py --create-sample")

def demo_web_scraping():
    """Demonstrate web scraping capabilities."""
    print(colored("\n=== WEB SCRAPING DEMO ===", "yellow", attrs=['bold']))
    
    # Use a simple, reliable test site
    test_url = "https://httpbin.org/html"
    print(f"Scraping test website: {test_url}")
    
    try:
        scraper = WebScraper(max_depth=1, output_format='json')
        results = scraper.scrape_website(test_url)
        
        if results:
            scraper.print_summary(results)
            
            # Save results
            scraper.save_results(results, "demo_web_scrape")
            print(colored(f"Results saved to demo_web_scrape.json", "green"))
        else:
            print(colored("No results obtained from web scraping", "red"))
            
    except Exception as e:
        print(colored(f"Error during web scraping: {str(e)}", "red"))
        print(colored("This might be due to network connectivity issues", "yellow"))

def demo_mirror_functionality():
    """Demonstrate website mirroring functionality."""
    print(colored("\n=== WEBSITE MIRROR DEMO ===", "yellow", attrs=['bold']))
    
    # Use a simple test site for mirroring
    test_url = "https://httpbin.org/html"
    mirror_dir = "demo_mirror_site"
    
    print(f"Testing website mirroring with: {test_url}")
    print(f"Mirror directory: {mirror_dir}")
    print("This will download the page and any resources to create a local copy.")
    
    try:
        scraper = WebScraper(
            max_depth=1, 
            delay=0.5, 
            output_format='json',
            mirror_mode=True,
            mirror_dir=mirror_dir
        )
        
        results = scraper.scrape_website(test_url)
        
        print(colored("\nWebsite mirroring completed successfully!", "green"))
        
        if hasattr(scraper, 'downloaded_files'):
            html_files = [f for f in scraper.downloaded_files.values() if f.endswith('.html')]
            resource_files = [f for f in scraper.downloaded_files.values() if not f.endswith('.html')]
            
            print(f"Pages mirrored: {len(html_files)}")
            print(f"Resources downloaded: {len(resource_files)}")
            print(f"Mirror directory: {scraper.mirror_dir}")
            
            # List downloaded files
            if scraper.downloaded_files:
                print("\nDownloaded files:")
                for url, local_path in scraper.downloaded_files.items():
                    print(f"  {local_path} <- {url}")
            
            # Check if mirror index was created
            index_path = os.path.join(scraper.mirror_dir, 'mirror_index.html')
            if os.path.exists(index_path):
                print(f"\nMirror index created: {index_path}")
                print("You can open this file in a web browser to browse the mirrored site.")
        
        # Also save the scraping results
        output_file = "demo_mirror_results.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            # Convert sets to lists for JSON serialization
            json_results = {}
            for key, value in results.items():
                if isinstance(value, set):
                    json_results[key] = list(value)
                else:
                    json_results[key] = value
            json.dump(json_results, f, indent=2, ensure_ascii=False)
        
        print(colored(f"Scraping results also saved to: {output_file}", "green"))
        
    except Exception as e:
        print(colored(f"Error during website mirroring: {str(e)}", "red"))
        print(colored("This might be due to network connectivity or the test site being unavailable.", "yellow"))

def create_sample_html():
    """Create a sample HTML file for testing."""
    sample_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Sample HTML page for web scraper testing">
    <meta name="keywords" content="web scraping, html parsing, demo">
    <title>Sample HTML Page for Web Scraper Demo</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to the Web Scraper Demo</h1>
        <nav>
            <a href="https://example.com">Example Link</a>
            <a href="https://github.com">GitHub</a>
            <a href="mailto:demo@example.com">Contact Us</a>
        </nav>
    </header>
    
    <main>
        <section>
            <h2>About This Demo</h2>
            <p>This is a sample HTML page created to demonstrate the capabilities of our web scraper.</p>
            <p>Contact us at: demo@example.com or call (555) 123-4567</p>
            
            <h3>Features Demonstrated</h3>
            <ul>
                <li>Link extraction</li>
                <li>Image detection</li>
                <li>Contact information parsing</li>
                <li>Social media link discovery</li>
            </ul>
        </section>
        
        <section>
            <h2>Sample Images</h2>
            <img src="sample1.jpg" alt="Sample Image 1">
            <img src="https://via.placeholder.com/300x200" alt="Placeholder Image">
        </section>
        
        <section>
            <h2>Social Media Links</h2>
            <p>Follow us on:</p>
            <a href="https://twitter.com/example">Twitter</a>
            <a href="https://facebook.com/example">Facebook</a>
            <a href="https://instagram.com/example">Instagram</a>
            <a href="https://linkedin.com/company/example">LinkedIn</a>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2024 Web Scraper Demo. All rights reserved.</p>
        <p>Phone: 555.987.6543 | Email: info@example.com</p>
    </footer>
    
    <script src="script.js"></script>
    <script src="https://cdn.example.com/analytics.js"></script>
</body>
</html>
    """
    
    with open('sample_demo.html', 'w', encoding='utf-8') as f:
        f.write(sample_html)
    
    print(colored("Sample HTML file 'sample_demo.html' created successfully!", "green"))
    print("You can now run: python demo.py --html to test HTML parsing")

def show_usage():
    """Show usage instructions."""
    print(colored("\n=== WEB SCRAPER DEMO USAGE ===", "cyan", attrs=['bold']))
    print("\nAvailable demo options:")
    print("  python demo.py --html          # Demo HTML file parsing")
    print("  python demo.py --web           # Demo web scraping")
    print("  python demo.py --mirror        # Demo website mirroring")
    print("  python demo.py --all           # Run all demos")
    print("  python demo.py --create-sample # Create sample HTML file")
    print("  python demo.py --help          # Show this help")
    
    print("\nMain web scraper usage:")
    print("  python web_scraper.py -u https://example.com")
    print("  python web_scraper.py -file sample.html")
    print("  python web_scraper.py --help")

def main():
    """Main demo function."""
    print(colored("Advanced Web Scraper and HTML Parser - Demo", "cyan", attrs=['bold']))
    print(colored("=" * 50, "cyan"))
    
    parser = argparse.ArgumentParser(description="Web Scraper Demo - Test HTML parsing, web scraping, and mirror functionality")
    parser.add_argument('--create-sample', action='store_true', help='Create a sample HTML file for testing')
    parser.add_argument('--html', action='store_true', help='Test HTML file parsing')
    parser.add_argument('--web', action='store_true', help='Test web scraping')
    parser.add_argument('--mirror', action='store_true', help='Test website mirroring functionality')
    parser.add_argument('--all', action='store_true', help='Run all demos')
    
    args = parser.parse_args()
    
    if args.all:
        create_sample_html()
        demo_html_parsing()
        demo_web_scraping()
        demo_mirror_functionality()
    elif args.create_sample:
        create_sample_html()
    elif args.html:
        demo_html_parsing()
    elif args.web:
        demo_web_scraping()
    elif args.mirror:
        demo_mirror_functionality()
    else:
        print("Please specify a demo option. Use --help for available options.")

if __name__ == "__main__":
    main()