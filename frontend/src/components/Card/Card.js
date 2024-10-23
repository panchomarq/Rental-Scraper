function Card({listing, index}) {
    return ( 
        <div key={index} className="border p-2 mb-2">
            <p><strong>Address: how</strong>{listing.address}</p>
            <p><strong>URL:</strong> <a href={listing.url} target="_blank" rel="noopener noreferrer">{listing.url}</a></p>
            <p><strong>Price:</strong> {listing.price}</p>
            <p><strong>Expenses:</strong> {listing.expenses}</p>
            <p><strong>Features:</strong> {listing.features.join(', ')}</p>
        </div>
     );
}

export default Card;