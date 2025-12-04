import { useState } from 'react';
import './App.css';

function App() {
  const [searchQuery, setSearchQuery] = useState('');
  const [cricketers, setCricketers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [searched, setSearched] = useState(false);
  const [selectedCricketer, setSelectedCricketer] = useState(null);

  const handleSearch = async () => {
    if (!searchQuery.trim()) return;

    setLoading(true);
    setSearched(true);

    try {
      const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:5001';
      const response = await fetch(`${apiUrl}/api/search?q=${encodeURIComponent(searchQuery)}`);
      const data = await response.json();
      setCricketers(data);
    } catch (error) {
      console.error('Error fetching cricketers:', error);
      setCricketers([]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSearch();
    }
  };

  return (
    <div className="app">
      <div className="container">
        <header className="header">
          <h1>🏏 Cricket Legends</h1>
          <p>Discover the history of cricket's greatest players</p>
        </header>

        <div className="search-section">
          <div className="search-container">
            <div className="search-input-wrapper">
              <span className="search-icon">🔍</span>
              <input
                type="text"
                className="search-input"
                placeholder="Search for a cricketer..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                onKeyPress={handleKeyPress}
              />
              <button className="search-button" onClick={handleSearch}>
                Search
              </button>
            </div>
          </div>
        </div>

        <div className="results-section">
          {loading ? (
            <div className="loading">
              <div className="spinner"></div>
              <p>Searching for cricket legends...</p>
            </div>
          ) : searched && cricketers.length === 0 ? (
            <div className="no-results">
              <div className="no-results-icon">🔍</div>
              <h3>No cricketers found</h3>
              <p>Try searching for another name</p>
            </div>
          ) : (
            <div className="results-grid">
              {cricketers.map((cricketer, index) => (
                <div
                  key={cricketer.id}
                  className="cricketer-card"
                  style={{ animationDelay: `${index * 0.1}s` }}
                  onClick={() => setSelectedCricketer(cricketer)}
                >
                  <div className="card-image-container">
                    <img
                      src={cricketer.image_url}
                      alt={cricketer.name}
                      className="card-image"
                      onError={(e) => {
                        e.target.src = 'https://via.placeholder.com/400x300/667eea/ffffff?text=Cricket+Legend';
                      }}
                    />
                    <div className="card-overlay"></div>
                  </div>
                  <div className="card-content">
                    <div className="card-header">
                      <h2 className="card-name">{cricketer.name}</h2>
                    </div>
                    <div className="card-meta">
                      <span className="meta-badge">
                        🌍 {cricketer.country}
                      </span>
                      <span className="meta-badge">
                        🎯 {cricketer.role}
                      </span>
                    </div>
                    <p className="card-history">{cricketer.history}</p>
                    <span className="read-more">
                      Read more →
                    </span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {selectedCricketer && (
        <div className="modal-overlay" onClick={() => setSelectedCricketer(null)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <button className="modal-close" onClick={() => setSelectedCricketer(null)}>
              ×
            </button>
            <div className="modal-image-container">
              <img
                src={selectedCricketer.image_url}
                alt={selectedCricketer.name}
                className="modal-image"
                onError={(e) => {
                  e.target.src = 'https://via.placeholder.com/700x350/667eea/ffffff?text=Cricket+Legend';
                }}
              />
              <div className="card-overlay"></div>
            </div>
            <div className="modal-body">
              <h2 className="modal-name">{selectedCricketer.name}</h2>
              <div className="modal-meta">
                <span className="meta-badge">
                  🌍 {selectedCricketer.country}
                </span>
                <span className="meta-badge">
                  🎯 {selectedCricketer.role}
                </span>
              </div>
              <p className="modal-history">{selectedCricketer.history}</p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
