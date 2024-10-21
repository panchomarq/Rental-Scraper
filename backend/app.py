from flask import Flask, request, jsonify
import logging
from scrapers.zonaprop_scraper import ZonaPropScraper
from scrapers.remax_scraper import RemaxScraper
from scrapers.mercadoLibre_scraper import MercadoLibreScraper
from scrapers.argenprop_scraper import ArgenpropScraper
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

SCRAPERS = {
    'zonaprop': ZonaPropScraper(),
    'remax': RemaxScraper(),
    'mercadolibre': MercadoLibreScraper(),
    'argenprop': ArgenpropScraper()
}

@app.route('/')
def index():
    return "Flask server is running"

@app.route('/scrape', methods=['POST'])
def scrape():
    site = request.json.get('site')
    if not site:
        return jsonify({"error": "Site is required"}), 400
    
    scraper = SCRAPERS.get(site)
    if not scraper:
        return jsonify({"error": "No scraper found for the specified site"}), 400

    try:
        listings = scraper.scrape()
        return jsonify({"listings": listings}), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/scrape_all', methods=['POST'])
def scrape_all():
    try:
        all_listings = []
        
        for site, scraper in SCRAPERS.items():
            try:
                listings = scraper.scrape()
                all_listings.extend(listings)
            except Exception as e:
                logging.error(f"Error scraping {site}: {e}")

        logging.info(f"Scraped Listings: {all_listings}")
        return jsonify({"listings": all_listings}), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
