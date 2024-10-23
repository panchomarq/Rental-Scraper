import React, { useState } from 'react';
import axios from 'axios';
import 'tailwindcss/tailwind.css';
import Card from './components/Card/Card';
import Button from './components/Button/Button';

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
      <div className='h-20 flex justify-center'>
        <h1 className="text-4xl font-bold mb-4">Apartment search scraper</h1>
      </div>
      <div className="flex justify-center space-x-4 mb-4">
        <Button styles={"bg-blue-500 text-white px-4 py-2 rounded"} onClick={() => handleScrape('zonaprop')} >ZonaProp</Button>
        <Button styles={"bg-red-500 text-white px-4 py-2 rounded"} onClick={() => handleScrape('remax')} >Remax</Button>
        <Button styles={"bg-yellow-500 text-white px-4 py-2 rounded"} onClick={() => handleScrape('mercadolibre')} >Mercado Libre</Button>
        <Button styles={"bg-green-900 text-white px-4 py-2 rounded"} onClick={() => handleScrape('argenprop')} >ArgenProp</Button>
        <Button styles={"bg-green-500 text-white px-4 py-2 rounded"} onClick={handleScrapeAll} >Scrap All</Button>
      </div>
      <div className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4'>
        {listings.length ? (
          listings.map((listing, index) => (
           <Card listing={listing} index={index} />
          ))
        ) : (
          <p>No listings to show.</p>
        )}
      </div>
    </div>
  );
}

export default App;
