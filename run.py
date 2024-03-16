import logging
from app import create_app
from dotenv import load_dotenv

# Configuring logging
logging.basicConfig(level=logging.DEBUG)

load_dotenv()  # loads the environment variables from a .env file

app = create_app()  # creates the flask application instance

if __name__ == "__main__":
    logging.debug("Starting Flask application...")
    app.run(debug=True)  # runs the flask application with debug mode enabled
