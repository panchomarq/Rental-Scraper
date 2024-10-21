import requests
from bs4 import BeautifulSoup
from .base_scraper import BaseScraper

class MercadoLibreScraper(BaseScraper):

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US',
            'Connection': 'keep-alive',
            'Referer': 'https://www.google.com/',
            'DNT': '1',
        }
        self.urls = [
            'https://inmuebles.mercadolibre.com.ar/departamentos/alquiler/2-dormitorios/capital-federal/nunez/_OrderId_PRICE_NoIndex_True_PROPERTY*AGE_1a%C3%B1os-20a%C3%B1os#applied_filter_id%3DPROPERTY_AGE%26applied_filter_name%3DAntig%C3%BCedad%26applied_filter_order%3D13%26applied_value_id%3D%5B1a%C3%B1os-20a%C3%B1os%5D%26applied_value_name%3D1+a+20+a%C3%B1os%26applied_value_order%3D2%26applied_value_results%3D12%26is_custom%3Dfalse'
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
        print(soup)
        return self.extract_data(soup)

    def extract_data(self, soup):
        listings = []
        for div in soup.find_all('div', class_='ui-search-result__content'):
            url = div.find('a', class_='ui-search-link__title-card ui-search-link').get('href')
            title = div.find('h2', class_='ui-search-item__title').text.strip()
            price_symbol = div.find('span', class_='andes-money-amount__currency-symbol').text.strip()
            price = div.find('span', class_='andes-money-amount__fraction').text.strip()
            features = [li.text for li in div.find('ul', {'class': 'ui-search-card-attributes ui-search-item__attributes-grid'}).find_all('li')]
            listings.append({
                'url': url,
                'title': title,
                'price': f"{price_symbol}{price}",
                'features': features
            })
        return listings