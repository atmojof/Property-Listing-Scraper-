import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

class PropertyScraper:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 20)
        self.data = []
        
    def scrape_url(self, url):
        try:
            self.driver.get(url)
            time.sleep(3)
            
            while True:
                self.scrape_page()
                next_page = self.get_next_page()
                
                if next_page:
                    self.driver.get(next_page)
                    time.sleep(3)
                else:
                    break
                    
        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
            return False
        return True
    
    def scrape_page(self):
        try:
            property_cards = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-cy="listing-card"]'))
            )
            
            for card in property_cards:
                item = {
                    'title': self.get_text(card, 'h2.card__title'),
                    'price': self.get_text(card, 'div.card-price'),
                    'location': self.get_text(card, 'div.card-location'),
                    'bedrooms': self.get_text(card, 'li[aria-label="bedroom"] span'),
                    'bathrooms': self.get_text(card, 'li[aria-label="bathroom"] span'),
                    'land_size': self.get_text(card, 'li[aria-label="land size"] span'),
                    'building_size': self.get_text(card, 'li[aria-label="building size"] span'),
                    'url': card.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                }
                self.data.append(item)
                
        except TimeoutException:
            print("Timeout waiting for property cards")
    
    def get_text(self, parent, selector):
        try:
            return parent.find_element(By.CSS_SELECTOR, selector).text.strip()
        except:
            return ''
    
    def get_next_page(self):
        try:
            next_btn = self.driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Next page"]')
            return next_btn.get_attribute('href')
        except:
            return None
    
    def save_to_csv(self, filename='property_data.csv'):
        if self.data:
            keys = self.data[0].keys()
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(self.data)
            print(f"Data successfully saved to {filename}")
    
    def close(self):
        self.driver.quit()

def main(urls):
    scraper = PropertyScraper()
    
    for url in urls:
        print(f"Scraping {url}...")
        success = scraper.scrape_url(url)
        if not success:
            print(f"Skipping {url} due to errors")
    
    scraper.save_to_csv()
    scraper.close()

if __name__ == "__main__":
    # Example URLs (replace with target URLs)
    sample_urls = [
        'https://www.rumah123.com/jual/depok/rumah/',
        'https://www.rumah123.com/jual/bekasi/rumah/'
    ]
    main(sample_urls) 
