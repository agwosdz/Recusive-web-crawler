# Advanced Web Scraper and HTML Parser

A comprehensive Python-based tool for web scraping and HTML file parsing. This tool can extract various types of data from websites and local HTML files, including links, images, contact information, and much more.

## Features

### Core Functionality
- **Dual Mode Operation**: Parse local HTML files or scrape live websites
- **Recursive Web Crawling**: Navigate through website links with configurable depth limits
- **Website Mirroring**: Download entire websites locally with preserved structure
- **Comprehensive Data Extraction**: Extract links, images, scripts, stylesheets, and metadata
- **Multiple Output Formats**: Save results as JSON, CSV, or plain text
- **Smart Content Detection**: Automatically identify and extract various content types

### Advanced Data Extraction
- **Contact Information**: Email addresses and phone numbers
- **Social Media Links**: Facebook, Twitter, LinkedIn, Instagram, YouTube, etc.
- **SEO Data**: Meta descriptions, keywords, titles, and structured data
- **Resource Discovery**: JavaScript files, CSS stylesheets, and image assets
- **Content Analysis**: Text content extraction and organization

### Website Mirroring
- **Complete Site Download**: Save entire websites with original directory structure
- **Resource Management**: Download CSS, JS, and image files preserving original paths
- **Link Processing**: Convert absolute links to relative for offline browsing
- **Mirror Index**: Generate navigation page for mirrored content
- **Structure Preservation**: Maintains original site's folder hierarchy

### Technical Features
- **Error Handling**: Robust error handling with detailed logging
- **Rate Limiting**: Configurable delays between requests
- **Domain Filtering**: Stay within the same domain during recursive crawling
- **Duplicate Prevention**: Avoid revisiting the same URLs
- **Progress Tracking**: Real-time logging and progress updates

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Recusive-web-crawler
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Web Scraping

Scrape a website with default settings:
```bash
python web_scraper.py -u https://example.com
```

Scrape with custom depth and save results:
```bash
python web_scraper.py -u https://example.com -d 3 --save-results -f json
```

Scrape with custom output filename:
```bash
python web_scraper.py -u https://example.com --save-results -o my_results
```

### HTML File Parsing

Parse a local HTML file:
```bash
python web_scraper.py -file index.html
```

Parse and save results in CSV format:
```bash
python web_scraper.py -file index.html -f csv --save-results
```

# Parse local HTML file and save as CSV
python web_scraper.py -file index.html -f csv --save-results

# Scrape website with custom depth and delay
python web_scraper.py -u https://example.com -d 3 --delay 2.0

# Mirror a website locally (download all pages and resources)
python web_scraper.py -u https://example.com --mirror --mirror-dir my_site_backup -d 2

# Mirror with custom settings
python web_scraper.py -u https://blog.example.com --mirror --delay 1.5 -d 3

### Command Line Options

- `-u, --url`: URL to scrape
- `-file, --html-file`: Local HTML file to parse
- `-d, --depth`: Maximum crawling depth (default: 2)
- `-f, --format`: Output format - json, csv, or txt (default: json)
- `--delay`: Delay between requests in seconds (default: 1.0)
- `--save-results`: Save results to file
- `-o, --output`: Output filename (without extension)
- `--mirror`: Enable mirror mode
- `--mirror-dir`: Mirror directory name

## Examples

### Basic Web Scraping
```bash
# Scrape a website with depth 2
python web_scraper.py -u https://example.com -d 2

# Scrape and save as JSON
python web_scraper.py -u https://example.com --save-results

# Scrape with custom delay and CSV output
python web_scraper.py -u https://example.com --delay 2.0 -f csv --save-results
```

### HTML File Analysis
```bash
# Parse local HTML file
python web_scraper.py -file webpage.html

# Parse and export to text format
python web_scraper.py -file webpage.html -f txt --save-results
```

### Legacy Tool Usage

The original recursive crawler is still available:
```bash
python main.py -u https://tryhackme.com -d 2
```

## Output Formats

### JSON Output
Comprehensive structured data including:
- Timestamp and metadata
- All discovered URLs and subdomains
- Images, scripts, and stylesheets
- Contact information (emails, phones)
- Social media profiles
- Text content and SEO data

### CSV Output
Separate CSV files for different data types:
- `*_links.csv`: All discovered links
- `*_content.csv`: Text content with types

### TXT Output
Human-readable format with organized sections for each data type.

## Logging

The tool creates detailed logs in `scraper.log` including:
- Crawling progress
- Error messages
- Performance metrics
- Discovered resources

## Demo Script

Run the included demo to test functionality:

```bash
# Create sample HTML file
python demo.py --create-sample

# Test HTML parsing
python demo.py --html

# Test web scraping
python demo.py --web

# Test website mirroring
python demo.py --mirror

# Run all demos
python demo.py --all
```

## Mirror Mode

The mirror functionality creates a complete local copy of websites:

### Directory Structure
```
mirror_example_com/
├── index.html              # Main page
├── about/
│   └── index.html         # About page
├── css/
│   └── styles.css         # Stylesheets (original paths)
├── js/
│   └── app.js             # JavaScript files (original paths)
├── images/
│   └── logo.png           # Images (original paths)
└── mirror_index.html      # Navigation index
```

### Features
- **Offline Browsing**: All links converted to relative paths
- **Structure Preservation**: Maintains original website directory structure
- **Navigation Index**: Auto-generated page listing all mirrored content
- **Filename Preservation**: Original filenames preserved with minimal sanitization for filesystem compatibility
- **Index Override**: Replace the original index.html with a custom local file while preserving all other mirroring functionality
- **Progress Tracking**: Real-time logging of download progress

### Index Override

The `--index-override` option allows you to replace the original website's index.html with your own custom file while preserving all other mirroring functionality:

```bash
# Mirror a site with custom index.html
python web_scraper.py -u https://example.com --mirror --index-override my_custom_index.html

# Specify custom mirror directory with override
python web_scraper.py -u https://example.com --mirror --mirror-dir custom_site --index-override landing_page.html
```

**Use Cases:**
- Custom landing pages for mirrored sites
- Adding your own branding or modifications
- Creating enhanced versions of existing sites
- Testing different layouts with the same resources

**Requirements:**
- Only works in mirror mode (`--mirror` flag required)
- Override file must exist locally
- All other pages and resources are mirrored normally

## Contributing

If you'd like to contribute to this project, please open an issue or create a pull request.
