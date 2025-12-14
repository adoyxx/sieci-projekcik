import os
import json
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DB_PATH = os.path.join(BASE_DIR, "db.json")

APP_SECRET_KEY = os.environ.get("APP_SECRET_KEY")

CLIENT_SECRET_PATH = os.path.join(BASE_DIR, "client_secret.json")

with open(CLIENT_SECRET_PATH, "r") as f:
    CREDENTIALS = json.load(f)

GOOGLE_CLIENT_ID = CREDENTIALS["web"]["client_id"]
GOOGLE_CLIENT_SECRET = CREDENTIALS["web"]["client_secret"]
GOOGLE_REDIRECT_URI = CREDENTIALS["web"]["redirect_uris"][0]

GOOGLE_BASE_URL = "https://www.googleapis.com/oauth2/v1/"
GOOGLE_REQUEST_TOKEN_URL = None
GOOGLE_ACCESS_TOKEN_METHOD = "POST"
GOOGLE_ACCESS_TOKEN_URL = "https://accounts.google.com/o/oauth2/token"
GOOGLE_AUTHORIZE_URL = "https://accounts.google.com/o/oauth2/auth"

SSL_CRT_PATH = os.path.join(BASE_DIR, "ssl.crt")
SSL_KEY_PATH = os.path.join(BASE_DIR, "ssl.key")

AUTH_USERNAME = os.environ.get("AUTH_USERNAME")
AUTH_PASSWORD = os.environ.get("AUTH_PASSWORD")
