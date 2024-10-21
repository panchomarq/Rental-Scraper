import requests
from bs4 import BeautifulSoup
from .base_scraper import BaseScraper

class RemaxScraper(BaseScraper):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://www.google.com/',
            'DNT': '1',
        }
        self.url = 'https://www.remax.com.ar/listings/rent?page=0&pageSize=24&sort=-createdAt&in:operationId=2&in:typeId=1,2,3,4,5,6,7,8&lte:yearBuilt=10&gte:yearBuilt=20&eq:totalRooms=3&locations=in::::25022@%3Cb%3ENu%C3%B1ez%3C%2Fb%3E:::&filterCount=3&viewMode=listViewMode'

    def scrape(self):
        try:
            listings = self._scrape_page(self.url)
            print(f"Scraped Listings from {self.url}: {listings}")
            return listings
        except requests.exceptions.RequestException as e:
            print(f"Error scraping {self.url}: {e}")
            return []

    def _scrape_page(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            response.raise_for_status()
        
        # Attempt to set the correct encoding
        if response.encoding is None or response.encoding == 'ISO-8859-1':
            # Check if the Content-Type header specifies an encoding
            encoding = response.headers.get('Content-Type', '').lower()
            if 'charset=' in encoding:
                response.encoding = encoding.split('charset=')[-1]
            else:
                # Use apparent_encoding as a fallback
                response.encoding = response.apparent_encoding
        
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
        return self.extract_data(soup)

    def extract_data(self, soup):
        listings = []
        for div in soup.find_all('qr-card-property'):
            url = div.find('a').get('href')
            if url:
                full_url = f"https://www.remax.com.ar{url}"
                price = div.find('p', class_='card__price').text.strip()
                expenses = div.find('p', class_='card__expenses').text.strip()
                features = [
                    feature.text.strip() for feature in div.find_all('div', class_='card__feature--item')
                ]
                listings.append({
                    'url': full_url,
                    'price': price,
                    'expenses': expenses,
                    'features': features
                })
        return listings
