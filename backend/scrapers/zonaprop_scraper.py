import requests
from bs4 import BeautifulSoup
from .base_scraper import BaseScraper

class ZonaPropScraper(BaseScraper):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US',
            'Connection': 'keep-alive',
            'Referer': 'https://www.google.com/',
            'DNT': '1',
        }
        self.urls = [
            'https://www.zonaprop.com.ar/departamentos-alquiler-nunez-3-ambientes-hasta-20-anos-orden-precio-ascendente.html',
            'https://www.zonaprop.com.ar/departamentos-alquiler-nunez-3-ambientes-hasta-20-anos-orden-precio-ascendente-pagina-2.html'
        ]

    def scrape(self):
        all_listings = []
        for url in self.urls:
            try:
                listings = self._scrape_page(url)
                print(f"Scraped Listings from {url}: {listings}")
                all_listings.extend(listings)
            except requests.exceptions.RequestException as e:
                print(f"Error scraping {url}: {e}")
        return all_listings

    def _scrape_page(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            response.raise_for_status()
        
        response.encoding = response.apparent_encoding  # Ensure the correct encoding is used
        soup = BeautifulSoup(response.content, 'html.parser')
        return self.extract_data(soup)

    def extract_data(self, soup):
        listings = []
        for div in soup.find_all('div', class_='PostingCardLayout-sc-i1odl-0'):
            url = div.get('data-to-posting')
            if url:
                full_url = f"https://www.zonaprop.com.ar{url}"
                address = div.find('div', {'class': 'LocationAddress-sc-ge2uzh-0 iylBOA postingAddress'}).text.strip()
                price = div.find('div', {'data-qa': 'POSTING_CARD_PRICE'}).text.strip()
                expenses = div.find('div', {'data-qa': 'expensas'}).text.strip()
                features = [span.text for span in div.find('h3', {'data-qa': 'POSTING_CARD_FEATURES'}).find_all('span')]
                listings.append({
                    'address': address,
                    'url': full_url,
                    'price': price,
                    'expenses': expenses,
                    'features': features
                })
        return listings
