#!/usr/bin/env python3
"""
Diagnostic script to help troubleshoot index override issues.
"""

import os
import sys
from urllib.parse import urlparse

def diagnose_override_issue(url, override_file):
    """Diagnose potential issues with index override functionality."""
    print("🔍 Index Override Diagnostic Tool")
    print("=" * 50)
    
    print(f"URL: {url}")
    print(f"Override file: {override_file}")
    print()
    
    # Check URL path
    parsed_url = urlparse(url)
    print(f"Parsed URL components:")
    print(f"  - Scheme: {parsed_url.scheme}")
    print(f"  - Domain: {parsed_url.netloc}")
    print(f"  - Path: '{parsed_url.path}'")
    print()
    
    # Check if override should apply
    is_root = parsed_url.path in ['/', '']
    print(f"Is root URL? {is_root}")
    if is_root:
        print("✅ Override SHOULD be applied for this URL")
    else:
        print("❌ Override will NOT be applied for this URL")
        print("   Override only works for root URLs (path = '/' or '')")
        print("   Examples of root URLs:")
        print("   - https://example.com/")
        print("   - https://example.com")
        print("   Examples of non-root URLs:")
        print("   - https://example.com/about")
        print("   - https://example.com/page.html")
    print()
    
    # Check override file
    print(f"Override file check:")
    if os.path.exists(override_file):
        print(f"✅ Override file exists: {override_file}")
        
        # Check file size
        file_size = os.path.getsize(override_file)
        print(f"   File size: {file_size} bytes")
        
        if file_size == 0:
            print("⚠️  WARNING: Override file is empty!")
        
        # Show first few lines
        try:
            with open(override_file, 'r', encoding='utf-8') as f:
                first_lines = f.read(200)
                print(f"   First 200 characters:")
                print(f"   {repr(first_lines)}")
        except Exception as e:
            print(f"❌ Error reading override file: {e}")
    else:
        print(f"❌ Override file NOT found: {override_file}")
        print("   Make sure the file path is correct and the file exists")
        
        # Check if it's a relative path issue
        if not os.path.isabs(override_file):
            abs_path = os.path.abspath(override_file)
            print(f"   Absolute path would be: {abs_path}")
            if os.path.exists(abs_path):
                print(f"   ✅ File exists at absolute path!")
            else:
                print(f"   ❌ File doesn't exist at absolute path either")
    
    print()
    print("🔧 Troubleshooting Tips:")
    print("1. Make sure you're using a root URL (ending with / or no path)")
    print("2. Verify the override file exists and has content")
    print("3. Use absolute paths for the override file if having issues")
    print("4. Check that --mirror mode is enabled")
    print("5. Look for 'Saved HTML with override' in the log output")
    print()
    print("Example working command:")
    print("python web_scraper.py -u https://example.com/ --mirror --index-override custom_index.html")

def main():
    if len(sys.argv) != 3:
        print("Usage: python diagnose_override.py <url> <override_file>")
        print("Example: python diagnose_override.py https://example.com/ custom_index.html")
        sys.exit(1)
    
    url = sys.argv[1]
    override_file = sys.argv[2]
    
    diagnose_override_issue(url, override_file)

if __name__ == "__main__":
    main()