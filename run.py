from app import create_app 
from dotenv import load_dotenv

load_dotenv() # loads the environment variables from a .env file

app = create_app() # creates the flask application instance

if __name__ == "__main__":
    app.run(debug=True) # runs the flask application with debug mode enabled