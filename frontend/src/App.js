import React, { useState } from 'react';
import axios from 'axios';
import 'tailwindcss/tailwind.css';
import { Button } from '@mantine/core';
import { HeaderSimple } from './components/header/HeaderSimple';

function App() {
  const [listings, setListings] = useState([]);

  const handleScrape = async (site) => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/scrape', { site });
      console.log(response.data);  // Log the response data
      setListings(response.data.listings);
    } catch (error) {
      console.error("There was an error scraping the data!", error);
    }
  };

  const handleScrapeAll = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/scrape_all');
      console.log(response.data);  // Log the response data
      setListings(response.data.listings);
    } catch (error) {
      console.error("There was an error scraping the data!", error);
    }
  };

  return (
    <div className="App p-4">
      <HeaderSimple />
      <h1 className="text-2xl font-bold mb-4">Mantine and Tailwind CSS</h1>

      <Button className="bg-black-500 text-white px-4 py-2 rounded">
        Mantine Button with Tailwind CSS
      </Button>
      <div className="flex space-x-4 mb-4">
        <button 
          onClick={() => handleScrape('zonaprop')} 
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          Scrape ZonaProp
        </button>
        <button 
          onClick={() => handleScrape('remax')} 
          className="bg-red-500 text-white px-4 py-2 rounded"
        >
          Scrape Remax
        </button>
        <button 
          onClick={() => handleScrape('mercadolibre')} 
          className="bg-yellow-500 text-white px-4 py-2 rounded"
        >
          Scrape MercadoLibre
        </button>
        <button 
          onClick={() => handleScrape('argenprop')} 
          className="bg-green-900 text-white px-4 py-2 rounded"
        >
          Scrape ArgenProp
        </button>
        <button 
          onClick={handleScrapeAll} 
          className="bg-green-500 text-white px-4 py-2 rounded"
        >
          Scrape All
        </button>
      </div>
      <div className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4'>
        {listings.length > 0 ? (
          listings.map((listing, index) => (
            <div key={index} className="border p-2 mb-2">
              <p><strong>Address: how</strong>{listing.address}</p>
              <p><strong>URL:</strong> <a href={listing.url} target="_blank" rel="noopener noreferrer">{listing.url}</a></p>
              <p><strong>Price:</strong> {listing.price}</p>
              <p><strong>Expenses:</strong> {listing.expenses}</p>
              <p><strong>Features:</strong> {listing.features.join(', ')}</p>
            </div>
          ))
        ) : (
          <p>No listings to show.</p>
        )}
      </div>
    </div>
  );
}

export default App;
