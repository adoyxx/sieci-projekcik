from flask import Flask
from flask_oauthlib.client import OAuth
import config

oauth = OAuth()


def create_app() -> Flask:
    global google

    app = Flask(__name__)
    app.secret_key = config.APP_SECRET_KEY

    oauth.init_app(app)
    google = oauth.remote_app(
        "google",
        consumer_key=config.GOOGLE_CLIENT_ID,
        consumer_secret=config.GOOGLE_CLIENT_SECRET,
        request_token_params={"scope": "email"},
        base_url=config.GOOGLE_BASE_URL,
        request_token_url=None,
        access_token_method=config.GOOGLE_ACCESS_TOKEN_METHOD,
        access_token_url=config.GOOGLE_ACCESS_TOKEN_URL,
        authorize_url=config.GOOGLE_AUTHORIZE_URL,
    )

    @google.tokengetter
    def get_google_oauth_token():
        from flask import session

        return session.get("google_token")

    from .routes import register_routes

    register_routes(app)

    return app
