#!/usr/bin/env python3
"""
Example demonstrating how to use index override to fix JavaScript paths.
This shows a real-world scenario where the original website has incorrect
JS paths, and you provide a corrected version via override.
"""

import os
import tempfile
from web_scraper import WebScraper

def create_corrected_index():
    """Create an index file with corrected JavaScript paths."""
    corrected_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Corrected Paths Example</title>
    
    <!-- Original site might have: /broken/path/style.css -->
    <!-- Corrected version: -->
    <link rel="stylesheet" href="/assets/css/main.css">
    <link rel="stylesheet" href="/static/theme.css">
</head>
<body>
    <h1>Website with Corrected Resource Paths</h1>
    
    <div class="content">
        <p>This override file contains corrected paths for resources that were broken in the original.</p>
        
        <h2>Fixed JavaScript Imports</h2>
        <ul>
            <li>Original: <code>/old/broken/app.js</code> → Fixed: <code>/js/app.js</code></li>
            <li>Original: <code>/wrong/utils.js</code> → Fixed: <code>/lib/utils.js</code></li>
            <li>Original: <code>/missing/api.js</code> → Fixed: <code>/api/client.js</code></li>
        </ul>
    </div>
    
    <!-- Original site might have broken paths like: -->
    <!-- <script src="/old/broken/app.js"></script> -->
    <!-- <script src="/wrong/utils.js"></script> -->
    
    <!-- Corrected JavaScript paths: -->
    <script src="/js/app.js"></script>
    <script src="/lib/utils.js"></script>
    <script src="/api/client.js"></script>
    <script src="/components/ui.js"></script>
    
    <!-- Corrected image paths: -->
    <img src="/images/logo.png" alt="Logo">
    <img src="/assets/banner.jpg" alt="Banner">
    
    <!-- Navigation with corrected links: -->
    <nav>
        <a href="/dashboard">Dashboard</a>
        <a href="/profile">Profile</a>
        <a href="/settings">Settings</a>
    </nav>
    
    <script>
        // This JavaScript would work with the corrected paths
        console.log('Override content loaded with corrected paths!');
        
        // Example of how corrected paths help:
        // Instead of trying to load from /old/broken/app.js (404)
        // We now load from /js/app.js (correct path)
    </script>
</body>
</html>
"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='_corrected.html', delete=False, encoding='utf-8') as f:
        f.write(corrected_content)
        return f.name

def demonstrate_corrected_paths():
    """Demonstrate using override to fix broken JavaScript paths."""
    print("🔧 JavaScript Path Correction Example")
    print("=" * 50)
    
    # Create corrected index file
    corrected_file = create_corrected_index()
    print(f"Created corrected index file: {corrected_file}")
    
    # Create temporary mirror directory
    with tempfile.TemporaryDirectory() as temp_dir:
        mirror_dir = os.path.join(temp_dir, 'corrected_mirror')
        
        print("\n🌐 Scenario:")
        print("  Original website: https://example.com/ (has broken JS paths)")
        print("  Override file: Contains corrected paths")
        print("  Goal: Scraper should use corrected paths for resource discovery")
        
        # Initialize scraper with corrected override
        scraper = WebScraper(
            max_depth=0,
            mirror_mode=True,
            mirror_dir=mirror_dir,
            index_override=corrected_file,
            process_js=True
        )
        
        print("\n🚀 Running scraper with override...")
        results = scraper.scrape_url('https://example.com/')
        
        print("\n📊 DISCOVERED RESOURCES:")
        print("-" * 30)
        
        # Show what resources were discovered from the corrected file
        css_files = results['resources']['css_files']
        js_files = results['resources']['js_files']
        images = results['resources']['images']
        
        print(f"\n✅ CSS Files ({len(css_files)}):")
        for css in css_files:
            print(f"  📄 {css}")
        
        print(f"\n✅ JavaScript Files ({len(js_files)}):")
        for js in js_files:
            print(f"  📜 {js}")
        
        print(f"\n✅ Images ({len(images)}):")
        for img in images:
            print(f"  🖼️  {img}")
        
        # Verify the corrected paths are being used
        corrected_paths = [
            '/js/app.js',
            '/lib/utils.js', 
            '/api/client.js',
            '/components/ui.js',
            '/assets/css/main.css',
            '/static/theme.css'
        ]
        
        print("\n🔍 VERIFICATION:")
        print("-" * 20)
        
        all_resources = css_files + js_files + images
        found_corrected = 0
        
        for path in corrected_paths:
            found = any(path in resource for resource in all_resources)
            status = "✅" if found else "❌"
            print(f"  {status} {path}")
            if found:
                found_corrected += 1
        
        print(f"\n📈 RESULTS:")
        print(f"  Corrected paths found: {found_corrected}/{len(corrected_paths)}")
        
        if found_corrected > 0:
            print("  ✅ SUCCESS! Override is working correctly.")
            print("  The scraper is using your corrected paths instead of broken ones.")
        else:
            print("  ❌ Issue detected. Override may not be applied correctly.")
        
        # Show saved file info
        saved_file = os.path.join(mirror_dir, 'index.html')
        if os.path.exists(saved_file):
            print(f"\n💾 Saved corrected index to: {saved_file}")
            
            with open(saved_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verify corrected content is saved
            if 'Corrected Paths Example' in content:
                print("  ✅ Corrected content successfully saved")
            else:
                print("  ❌ Original content found instead of corrected")
        
        print("\n" + "=" * 50)
        print("💡 KEY BENEFITS:")
        print("  1. Override content is used for PARSING (resource discovery)")
        print("  2. Override content is used for SAVING (final file)")
        print("  3. Broken paths in original are replaced with working paths")
        print("  4. JavaScript processing works with corrected imports")
        print("  5. All other scraper features work normally")
        
        print("\n🎯 USE CASES:")
        print("  • Fix broken JavaScript import paths")
        print("  • Correct CSS file references")
        print("  • Update image URLs")
        print("  • Modify API endpoints in client code")
        print("  • Replace outdated CDN links")
    
    # Cleanup
    os.unlink(corrected_file)

if __name__ == "__main__":
    demonstrate_corrected_paths()