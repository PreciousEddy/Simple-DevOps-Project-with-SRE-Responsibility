from flask import Flask, render_template
import requests
from datetime import datetime
import pytz

app = Flask(__name__)

# Function to get weather data
def get_weather(city):
    api_key = "e47fcf593595b1313116c3430d9dd644"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"]
        }
    return {"description": "N/A", "temperature": "N/A"}

# Function to get current time
def get_time(timezone_str):
    timezone = pytz.timezone(timezone_str)
    return datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")

@app.route('/')
def home():
    weather_east = get_weather("Houston")
    weather_west = get_weather("El Paso")
    weather_north = get_weather("Dallas")
    weather_south = get_weather("San Antonio")
    time_east = get_time("America/Chicago")
    time_west = get_time("America/Denver")

    return render_template("index.html", weather_east=weather_east, weather_west=weather_west, weather_north=weather_north, weather_south=weather_south, time_east=time_east, time_west=time_west)

if __name__ == '__main__':
    app.run(debug=True)