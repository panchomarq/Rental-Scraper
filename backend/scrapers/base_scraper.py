import requests
from bs4 import BeautifulSoup

class BaseScraper:
    
    def scrape(self, url, headers):
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            response.raise_for_status()
        
        response.encoding = response.apparent_encoding  # Ensure the correct encoding is used
        soup = BeautifulSoup(response.content, 'html.parser')
        return self.extract_data(soup)
    
    def extract_data(self, soup):
        raise NotImplementedError("Subclasses should implement this method")
