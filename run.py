from app import create_app
import config

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, ssl_context=(config.SSL_CRT_PATH, config.SSL_KEY_PATH))
