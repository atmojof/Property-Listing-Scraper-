# Property Listing Scraper

A Selenium-based web scraper for extracting property listings from Rumah123.com

## Features
- Scrape data from single or multiple URLs
- Automatic pagination handling
- Save results in CSV format
- Skip failed URLs automatically
- Headless browser mode for efficient scraping

## Requirements
1. Python 3.6+
2. Chrome Browser
3. ChromeDriver (matching your Chrome version)

## Installation
1. Clone or download the code
2. Install required packages:
```bash
pip install selenium
```
3. Ensure ChromeDriver is installed and available in your PATH

## Usage
1. Edit the `sample_urls` list in `property_scraper.py` with your target URLs
   Example URL format:
   ```
   'https://www.rumah123.com/jual/[location]/rumah/'
   ```
2. Run the script:
```bash
python property_scraper.py
```

## Output
Data will be saved to `property_data.csv` with the following columns:
- title
- price
- location
- bedrooms
- bathrooms
- land_size
- building_size
- url

## Notes
- The scraper uses headless mode to improve performance
- Delays are optimized to prevent server overload and detection
- Element selectors might need adjustment if the website structure changes
```

Key changes from original version:
1. Translated all comments and text to English
2. Renamed class to `PropertyScraper`
3. Updated documentation in English
4. Maintained all core functionality from original version
5. Improved code comments and error messages

To use this scraper:
1. Ensure ChromeDriver matches your Chrome browser version
2. Replace sample URLs with your target property listing pages
3. Adjust timeouts/delays if needed (lines 25 and 31)
4. Verify CSS selectors match current website structure

The scraper will handle:
- Multi-page listings automatically
- Multiple URLs input
- Error recovery and skipping failed URLs
- Structured data export to CSV


Remember to use this scraper responsibly and in compliance with the target website's terms of service.
