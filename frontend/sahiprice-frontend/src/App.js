import React, { useState } from "react";
import { Search, Store } from "lucide-react";
import "./styles.css";

const SearchPage = ({ onSearch }) => {
  const [query, setQuery] = useState("");

  return (
    <div className="container center">
      <h1>Find the Best Prices</h1>
      <div className="search-box">
        <input
          type="text"
          placeholder="Search for a product..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button onClick={() => onSearch(query)}>
          <Search className="icon" />
        </button>
      </div>
    </div>
  );
};

const ResultsPage = ({ query, onBack }) => {
  const results = [
    { platform: "Blinkit", price: "500", image: "../logos/blinkit-logo.svg" },
    { platform: "Zepto", price: "$1079", image: "https://via.placeholder.com/50" },

  ];

  return (
    <div className="container">
      <button className="back-button" onClick={onBack}>Back</button>
      <h2>Results for "{query}"</h2>
      <div className="results">
        {results.map((item, index) => (
          <div key={index} className="result-item">
            <img src={item.image} alt={item.platform} className="product-image" />
            <span className="platform">
              <Store className="icon" /> {item.platform}
            </span>
            <span className="price">{item.price}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

const PriceComparisonApp = () => {
  const [query, setQuery] = useState(null);
  return query ? <ResultsPage query={query} onBack={() => setQuery(null)} /> : <SearchPage onSearch={setQuery} />;
};

export default PriceComparisonApp;