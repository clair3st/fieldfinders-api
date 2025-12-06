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

```bash
git clone https://github.com/clair3st/fieldfinders-api.git
cd fieldfinders-api
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
DB_URI=parks.db
FLASK_DEBUG=False
PORT=8000
```

**Configuration Options:**
- `DB_URI`: Path to SQLite database file (default: `parks.db`)
- `FLASK_DEBUG`: Enable/disable debug mode (default: `False`)
- `PORT`: Port number to run the server (default: `8000`)

## 🗄️ Database Setup

On first deployment or initial setup, you must populate the database from the CSV file:

```bash
python3 utils/cleanse-raw-data.py
```

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

```bash
# Activate virtual environment
source venv/bin/activate

# Run with Flask CLI
flask run

# Or run directly
python app.py
```

The API will be available at `http://localhost:8000`

### Production Mode

Set `FLASK_DEBUG=False` in your `.env` file and use a production WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## 📡 API Documentation

### Base URL

- **Production**: `https://clair3st.pythonanywhere.com/`
- **Local Development**: `http://localhost:8000/`

### Endpoints

#### `GET /`

Returns API information and available endpoints.

**Response:**
```
Field Finders. This site is a prototype API for park facility data.
```

---

#### `GET /features/all`

Retrieves all park features from the database.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Green Lake Park",
    "feature_desc": "Basketball Court",
    "hours": "5:00 AM - 11:30 PM",
    "xpos": -122.327,
    "ypos": 47.679,
    "location": "7201 E Green Lake Dr N, Seattle, WA 98115"
  },
  ...
]
```

**Example Request:**
```bash
curl http://localhost:8000/features/all
```

---

#### `GET /features/<feature>`

Search for park features by feature type. Returns matching features grouped by location.

**Parameters:**
- `feature` (path parameter, required): Feature type to search for (e.g., "basketball", "tennis", "baseball")

**Response:**
```json
[
  {
    "xpos": -122.327,
    "ypos": 47.679,
    "name": "Green Lake Park",
    "feature_desc": "Basketball Court",
    "location": "7201 E Green Lake Dr N, Seattle, WA 98115",
    "id": 1,
    "hours": "5:00 AM - 11:30 PM"
  },
  ...
]
```

**Example Requests:**
```bash
# Search for basketball courts
curl http://localhost:8000/features/basketball

# Search for tennis courts
curl http://localhost:8000/features/tennis

# Search for baseball fields
curl http://localhost:8000/features/baseball
```

**Note:** The search is case-insensitive and uses pattern matching. For example, searching for "ball" will match "Basketball", "Baseball", "Volleyball", etc.

---

### Error Responses

All errors are returned as JSON:

```json
{
  "code": 404,
  "name": "Not Found",
  "description": "The requested URL was not found on the server."
}
```

Common HTTP status codes:
- `200` - Success
- `404` - Resource not found
- `500` - Internal server error

## 📁 Project Structure

```
fieldfinders-api/
├── app.py                          # Main Flask application
├── parks.db                        # SQLite database (gitignored)
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── LICENSE                         # MIT License
├── .env                            # Environment variables (gitignored)
├── utils/
│   ├── cleanse-raw-data.py        # Database population script
│   └── Seattle_Parks_and_Recreation_Parks_Features.csv  # Raw data
└── venv/                           # Virtual environment (gitignored)
```

## 🚢 Deployment

The API is currently deployed on [PythonAnywhere](https://clair3st.pythonanywhere.com/).


## 📝 TODO

- [ ] Filter CSV import to only include relevant features
- [ ] Add input validation and sanitization
- [ ] Add comprehensive error handling
- [ ] Implement response caching
- [ ] Write unit tests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2023 Claire Gatenby

## 🙏 Acknowledgments

- Data provided by the [City of Seattle Open Data Portal](https://data.seattle.gov/)
- Inspired by tutorial from [Nordic APIs](https://nordicapis.com/how-to-create-an-api-from-a-dataset-using-python-and-flask/)
- Frontend application: [Field Finders React](https://github.com/clair3st/fieldfinders-react)

## 🔗 Links

- **Frontend Application**: [Field Finders React](https://github.com/clair3st/fieldfinders-react)
- **Live API**: [https://clair3st.pythonanywhere.com/](https://clair3st.pythonanywhere.com/)
- **Data Source**: [Seattle Open Data Portal](https://data.seattle.gov/)
