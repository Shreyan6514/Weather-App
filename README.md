# 🌦️ Weather App (Python + API + Multilingual)

A Python-based weather application that fetches real-time weather data using a public API.  
The app allows users to enter any city name and displays the current weather details in multiple languages.

---

## 📌 Features

- 🌍 **City-based Weather Search** – Enter any city to get real-time weather info  
- 🌐 **Multilingual Support** – Displays results in multiple languages  
- ⚡ **API Integration** – Uses a weather API to fetch live data  
- 🧠 **Error Handling** – Handles invalid inputs
- 💻 **Simple UI (Console-based)** – Minimal, user-friendly input/output flow  

---

## 🛠️ Tech Stack

- **Python 3.13.2**
- **Requests** (for API calls)
- **JSON** (for parsing API responses)
- **Translation library** 

---

## 🚀 How to Run

### 1. Clone the repository:
	git clone https://github.com/Shreyan6514/Weather-App.git

### 2. Navigate into the project folder:
	cd Weather-App
### 3. Install required dependencies:
	pip install -r requirements.txt

### 4. Run the app:
	python weather.py

## ⚙️ Configuration
•	The app uses a Weather API key (OpenWeatherMap).
•	By default, the app looks for an environment variable named api-key.
•	If you don’t want to use environment variables, open weather.py and replace **os.getenv("api-key")** with your own key directly.

Example:
  **user_api = "your_api_key_here"**

You can get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
