# sieci-projekcik

A Flask-based student management system with Google OAuth authentication.

## Description

This project is a simple web application for managing student records with grades. It provides RESTful API endpoints for CRUD operations on student data and includes Google OAuth authentication for secure access to certain endpoints.

## Features

- **Student Management**: Create, read, update, and delete student records
- **Grade Management**: Update student grades (protected endpoint)
- **Google OAuth Authentication**: Secure login using Google accounts
- **TinyDB Integration**: Lightweight JSON-based database for data storage
- **Pydantic Validation**: Data validation for student and grade models

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sieci-projekcik.git
   cd sieci-projekcik
   ```

2. Install dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
   or using uv:
   ```bash
   uv sync
   ```

3. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Set `APP_SECRET_KEY` for Flask session security
   - Set `AUTH_USERNAME` and `AUTH_PASSWORD` for basic authentication

4. Set up Google OAuth:
   - Place your `client_secret.json` file in the project root
   - Ensure the file contains valid Google OAuth credentials

5. Set up SSL certificates:
   - Place `ssl.crt` and `ssl.key` files in the project root for HTTPS

## Usage

### Running the Application

### Testing with Postman

A Postman collection is available in the `tests/` folder to help you test the API endpoints:
- File: `tests/projekcik-sieci.postman_collection.json`

You can import this collection into Postman to easily test all the API endpoints and authentication flows.

```bash
python run.py
```
or using uv:
   ```bash
uv run run.py
   ```

The application will start on `https://localhost:5000` with SSL enabled.

### API Endpoints

- **GET** `/students` - Get all students
- **GET** `/students/<id>` - Get a specific student by ID
- **POST** `/students` - Create a new student
  - Requires JSON body: `{"first_name": "John", "last_name": "Doe", "grade": 4.5}`
- **PUT** `/students/<id>` - Update a student's grade (requires authentication)
  - Requires JSON body: `{"grade": 4.8}`
- **DELETE** `/students/<id>` - Delete a student

### Authentication Endpoints

- **GET** `/login` - Initiate Google OAuth login
- **GET** `/callback` - Google OAuth callback endpoint
- **GET** `/google-profile` - Get user profile information after login

## Project Structure

```
.
├── app/
│   ├── __init__.py       # Flask app initialization and OAuth setup
│   ├── models.py         # Pydantic models for Student and Grade
│   └── routes.py         # API route definitions
├── tests/               # Test files
├── utils/
│   ├── auth.py           # Authentication utilities
│   └── db.py             # Database connection
├── config.py            # Configuration and environment variables
├── db.json              # TinyDB database file
├── run.py               # Application entry point
└── pyproject.toml        # Project dependencies and configuration
```

## Dependencies

- Flask 1.1.4
- Flask-OAuthlib 0.9.6
- TinyDB 4.8.2+
- Pydantic 2.12.5+
- Python-dotenv 0.9.9+

## Configuration

The application uses environment variables for configuration:

- `APP_SECRET_KEY`: Flask secret key for session management
- `AUTH_USERNAME`: Username for basic authentication
- `AUTH_PASSWORD`: Password for basic authentication
- `DB_PATH`: Path to the TinyDB database file (default: `db.json`)

Google OAuth credentials are loaded from `client_secret.json`.

## Development

The project uses:
- Python 3.10+
- Type hints for better code clarity
- Pydantic for data validation
- TinyDB for simple JSON storage

## License

[Add your license information here]
