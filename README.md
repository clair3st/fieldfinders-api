# Field Finders API

A RESTful Flask API that provides access to Seattle Parks and Recreation park facility data. This API powers the [Field Finders](https://github.com/clair3st/fieldfinders-react) frontend application, allowing users to search and discover sports facilities and park features across Seattle.

## 🌟 Features

- **Comprehensive Park Data**: Access to Seattle Parks and Recreation facility data
- **Flexible Search**: Query all features or filter by specific feature type
- **RESTful Design**: Clean, intuitive API endpoints
- **CORS Enabled**: Ready for frontend integration
- **JSON Responses**: All endpoints return structured JSON data
- **Location Data**: Includes coordinates (latitude/longitude) for mapping features

## 🛠 Tech Stack

- **Python 3.12+**
- **Flask 3.0.3** - Web framework
- **SQLite3** - Lightweight database
- **Flask-CORS** - Cross-origin resource sharing
- **python-dotenv** - Environment variable management

## 📋 Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation

### 1. Clone the Repository
```
sh
git clone https://github.com/clair3st/fieldfinders-api.git
cd fieldfinders-api
```

### 2. Create Virtual Environment

`python3 -m venv venv`

### 3. Activate Virtual Environment

**On macOS/Linux:**
source venv/bin/activate**On Windows:**
venv\Scripts\activate### 4. Install Dependencies

pip install -r requirements.txt## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

DB_URI=parks.db
FLASK_DEBUG=False
PORT=8000**Configuration Options:**
- `DB_URI`: Path to SQLite database file (default: `parks.db`)
- `FLASK_DEBUG`: Enable/disable debug mode (default: `False`)
- `PORT`: Port number to run the server (default: `8000`)

## 🗄️ Database Setup

On first deployment or initial setup, you must populate the database from the CSV file:

`python3 utils/cleanse-raw-data.py`

This script:
- Creates a SQLite database (if it doesn't exist)
- Creates the `ParkFeatures` table
- Imports park feature data from `utils/Seattle_Parks_and_Recreation_Parks_Features.csv`
- Validates and processes the data

**Note:** The CSV file contains raw data from the [Seattle Open Data Portal](https://data.seattle.gov/).

### Database Schema

The `ParkFeatures` table contains the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `id` | INTEGER | Primary key (auto-increment) |
| `name` | TEXT | Park name |
| `feature_desc` | TEXT | Description of the feature (e.g., "Basketball Court", "Tennis Court") |
| `hours` | TEXT | Operating hours |
| `xpos` | REAL | Longitude coordinate |
| `ypos` | REAL | Latitude coordinate |
| `location` | TEXT | Physical location/address |

## 🏃 Running the Application

### Development Mode

# Activate virtual environment
source venv/bin/activate

# Run with Flask CLI
flask run

# Or run directly
python app.pyThe API will be available at `http://localhost:8000`

### Production Mode

Set `FLASK_DEBUG=False` in your `.env` file and use a production WSGI server like Gunicorn:

pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app## 📡 API Documentation

### Base URL

- **Production**: `https://clair3st.pythonanywhere.com/`
- **Local Development**: `http://localhost:8000/`

### Endpoints

#### `GET /`

Returns API information and available endpoints.

**Response:**