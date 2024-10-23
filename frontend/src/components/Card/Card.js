function Card({ listing, index }) {
    return ( 
        <a href={listing.url} target="_blank" rel="noopener noreferrer" key={index} className="block border border-gray-300 rounded-lg shadow-md p-4 mb-4 hover:shadow-lg transition-shadow duration-200">
            <h2 className="text-lg font-semibold text-gray-800 mb-2">Property Details</h2>
            <p className="text-gray-700"><span className="font-bold">Address:</span> {listing.address}</p>
            <p className="text-gray-700"><span className="font-bold">Location:</span> {listing.location}</p>
            <p className="text-gray-700"><span className="font-bold">URL:</span> 
                <a href={listing.url} target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline">
                    {listing.url}
                </a>
            </p>
            <p className="text-gray-700"><span className="font-bold">Price:</span> {listing.price}</p>
            <p className="text-gray-700"><span className="font-bold">Expenses:</span> {listing.expenses}</p>
            <p className="text-gray-700"><span className="font-bold">Features:</span> {listing.features.join(', ')}</p>
        </a>
    );
}

export default Card;