from flask import Flask, render_template, request # Flask tools for web pages and form handling
import requests, os, json #to make API calls,access environment variables and json

# -------------------------------
# Load environment variables from .env file
# -------------------------------

from datetime import datetime
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()  # find .env file
load_dotenv(dotenv_path)  # load .env file as environment variables

app = Flask(__name__) # Initialize Flask app
user_api = os.getenv("api-key")
#location = input("Enter the city name: ")

with open('languages.json') as f: #open json file and store language codes
    language_codes = json.load(f)

# Define the main route ('/') - homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    data = None # Initialize data variable for passing to template later
    
    if request.method == 'POST':
        location = request.form['city'] # Get city name input
        lang = request.form['language'].casefold()# Get language input and lowercase it
        lang_code = language_codes.get(lang, 'en') # Check if the language is supported, else default to English
        complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}&lang={lang_code}"
        
        # Make the API request
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()

        # Handle invalid city case
        if api_data['cod']=='404':
            data = {
        "error": f"Invalid City: {location}. Please check your city name."
    } # Render the HTML page and pass the error message
        else:
            temp_city = ((api_data['main']['temp']) - 273.15) # Convert temperature from Kelvin to Celsius
            data = {
                "city": location,
                "date_time": datetime.now().strftime("%d %b %Y | %I:%M:%S %p"),
                "temp": f"{temp_city:.2f}",
                "desc": api_data['weather'][0]['description'],
                "humidity": api_data['main']['humidity'],
                "wind": api_data['wind']['speed']
            }
    return render_template('index.html', data=data) # Render the HTML page and pass the weather data

if __name__ == '__main__': # Run the app
    print("✅ Flask app is starting...")

    app.run(debug=True)
    