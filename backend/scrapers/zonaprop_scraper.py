import requests
from bs4 import BeautifulSoup
from .base_scraper import BaseScraper
import time
import random

class ZonaPropScraper(BaseScraper):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US',
            'Connection': 'keep-alive',
            'Referer': 'https://www.google.com/',
            'DNT': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
        }
        self.urls = [
            'https://www.zonaprop.com.ar/departamentos-alquiler-caballito-palermo-belgrano-parque-centenario-las-canitas-3-ambientes-publicado-hace-menos-de-1-dia-menos-600000-pesos-orden-precio-ascendente.html'
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
            time.sleep(random.uniform(1, 3))  # Espera aleatoria entre 1 y 3 segundos
        return all_listings

    def _scrape_page(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            response.raise_for_status()
        
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.content, 'html.parser')
        return self.extract_data(soup)

    def extract_data(self, soup):
        listings = []
        for div in soup.find_all('div', class_='CardContainer-sc-1tt2vbg-5 fvuHxG'):
            url = div.find('a')
            if url:
                full_url = f"https://www.zonaprop.com.ar{url.get('href')}"
            else:
                full_url = None

            address = div.find('div', class_='LocationAddress-sc-ge2uzh-0 iylBOA postingAddress')
            if address:
                address = address.text.strip()
            else:
                address = ""

            location = div.find('div', {'data-qa': 'POSTING_CARD_LOCATION'})
            if location:
                location = location.text.strip()
            else:
                location = ""
            
            price_symbol = div.find('span', class_='card__currency')
            if price_symbol:
                price_symbol = price_symbol.text.strip()
            else:
                price_symbol = ""

            price = div.find('div', {'data-qa': 'POSTING_CARD_PRICE'})
            if price:
                price = price.text.strip()
            else:
                price = ""

            expenses = div.find('div', {'data-qa': 'expensas'})
            if expenses:
                expenses = expenses.text.strip()
            else:
                expenses = ""

            features = [span.text for span in div.find('h3', {'data-qa': 'POSTING_CARD_FEATURES'}).find_all('span')]

            listings.append({
                'url': full_url,
                'address': address,
                'location': location,
                'price': f"{price_symbol}{price}",
                'expenses': expenses,
                'features': features
            })
        return listings