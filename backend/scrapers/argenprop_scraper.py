import requests
from bs4 import BeautifulSoup
from .base_scraper import BaseScraper

class ArgenpropScraper(BaseScraper):

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US',
            'Connection': 'keep-alive',
            'Referer': 'https://www.google.com/',
            'DNT': '1',
        }
        self.urls = [
            'https://www.argenprop.com/departamentos/alquiler/nunez/2-dormitorios?hasta-20-anos&orden-menorprecio'
        ]

    def scrape(self):
        all_listing = []
        for url in self.urls:
            try:
                listings = self._scrape_page(url)
                print(f"Scraped Listings from {url}: {listings}")
                all_listing.extend(listings)
            except requests.exceptions.RequestException as e:    
                print(f"Error scraping {url}: {e}")
        return all_listing 

    def _scrape_page(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200: 
            response.raise_for_status()

        response.encoding = response.apparent_encoding  # Ensure the correct encoding is used        
        soup = BeautifulSoup(response.content, 'html.parser')
        print
        return self.extract_data(soup)

    def extract_data(self, soup):
        listings = []
        for div in soup.find_all('div', class_='listing__item'):
            url = div.find('a')
            if url:
                full_url = f"https://www.argenprop.com{url.get('href')}"
            else:
                full_url = None
            
            price_symbol = div.find('span', class_='card__currency')
            if price_symbol:
                price_symbol = price_symbol.text.strip()
            else:
                price_symbol = ""

            price = div.find('p', class_='card__price')
            if price:
                price = price.text.strip()
            else:
                price = ""

            expenses = div.find('span', class_='card__expenses')
            if expenses:
                expenses = expenses.text.strip()
            else:
                expenses = ""

            features_list = div.find('ul', class_='card__main-features')
            if features_list:
                features = [li.text.strip() for li in features_list.find_all('span')]
            else:
                features = []

            listings.append({
                'url': full_url,
                'price': f"{price_symbol}{price}",
                'expenses': expenses,
                'features': features
            })
        return listings