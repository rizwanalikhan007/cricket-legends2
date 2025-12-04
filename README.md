# 🏏 Cricket Legends Search

A beautiful, modern web application to search and explore cricket legends and their history.

## Features

- 🔍 **Search Functionality**: Search for cricketers by name
- 🎨 **Modern UI**: Stunning glassmorphism design with smooth animations
- 📱 **Responsive**: Works perfectly on all devices
- 🗄️ **Database**: SQLite database with pre-populated cricket legends
- ⚡ **Fast**: React frontend with Python Flask backend

## Tech Stack

### Frontend
- React (Vite)
- Modern CSS with glassmorphism effects
- Google Fonts (Inter)

### Backend
- Python Flask
- Flask-CORS
- SQLite Database

## Project Structure

```
cricketer_search/
├── backend/
│   ├── app.py              # Flask API server
│   ├── init_db.py          # Database initialization script
│   ├── requirements.txt    # Python dependencies
│   └── cricketers.db       # SQLite database (created after init)
└── frontend/
    ├── src/
    │   ├── App.jsx         # Main React component
    │   ├── App.css         # Styling
    │   └── index.css       # Global styles
    ├── index.html          # HTML template
    └── package.json        # Node dependencies
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

3. Initialize the database:
   ```bash
   python3 init_db.py
   ```

4. Start the Flask server:
   ```bash
   python3 app.py
   ```

   The backend will run on `http://localhost:5001`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install Node dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

   The frontend will run on `http://localhost:5173`

## Usage

1. Start both the backend and frontend servers (in separate terminals)
2. Open your browser to `http://localhost:5173`
3. Search for cricket legends like:
   - Sachin Tendulkar
   - Virat Kohli
   - MS Dhoni
   - Ricky Ponting
   - Brian Lara
   - Shane Warne
4. Click on any card to view detailed information

## API Endpoints

### GET `/api/search`
Search for cricketers by name.

**Query Parameters:**
- `q` (string): Search query

**Response:**
```json
[
  {
    "id": 1,
    "name": "Sachin Tendulkar",
    "country": "India",
    "role": "Batsman",
    "history": "...",
    "image_url": "..."
  }
]
```

## Database Schema

```sql
CREATE TABLE cricketers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT,
    role TEXT,
    history TEXT,
    image_url TEXT
)
```

## Pre-populated Cricketers

The database comes with 6 legendary cricketers:
1. Sachin Tendulkar (India)
2. Virat Kohli (India)
3. MS Dhoni (India)
4. Ricky Ponting (Australia)
5. Brian Lara (West Indies)
6. Shane Warne (Australia)

## Adding More Cricketers

You can add more cricketers directly to the database or modify `init_db.py` to include additional entries.

## License

MIT

## Author

Created with ❤️ for cricket fans worldwide
