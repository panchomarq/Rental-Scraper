import React, { useState } from 'react';

const ScraperForm = () => {
  const [url, setUrl] = useState('');
  const [site, setSite] = useState('');
  const [results, setResults] = useState([]);
  const [error, setError] = useState('');

  const handleScrape = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/scrape', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url, site })
      });

      const data = await response.json();
      console.log(data, "************************")
      if (response.ok) {
        setResults(data.listings);
        setError('');
      } else {
        setError(data.error);
        setResults([]);
      }
    } catch (error) {
      setError('An error occurred while fetching data.');
      setResults([]);
    }
  };

  return (
    <div className="container mx-auto max-w-lg p-4">
      <h1 className="text-2xl font-bold mb-4">Web Scraping App</h1>
      <input
        type="text"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Enter URL"
        className="w-full p-2 mb-4 border border-gray-300 rounded"
      />
      <select
        value={site}
        onChange={(e) => setSite(e.target.value)}
        className="w-full p-2 mb-4 border border-gray-300 rounded"
      >
        <option value="">Select Site</option>
        <option value="zonaprop">ZonaProp</option>
        <option value="remax">Remax</option>
      </select>
      <button
        onClick={handleScrape}
        className="w-full p-2 bg-green-500 text-white font-semibold rounded hover:bg-green-600"
      >
        Scrape Data
      </button>
      {error && <p className="text-red-500 mt-4">{error}</p>}
      <div className="results mt-4">
        {results.map((listing, index) => (
          <div key={index} className="p-4 border-b">
            <p><strong>URL:</strong> <a href={listing.url} target="_blank" rel="noopener noreferrer" className="text-blue-500">{listing.url}</a></p>
            <p><strong>Price:</strong> {listing.price}</p>
            <p><strong>Expenses:</strong> {listing.expenses}</p>
            <p><strong>Features:</strong> {listing.features.join(', ')}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ScraperForm;
