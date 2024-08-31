import os
import requests
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()


class WeatherApi:
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    GEO_API_KEY = os.getenv("GEO_API_KEY")
    BASE_URLS = {
        "weather": "http://api.openweathermap.org/data/2.5/weather?",
        "forecast": "http://api.openweathermap.org/data/2.5/forecast?",
        "air": "http://api.openweathermap.org/data/2.5/air_pollution?",
        "geo": "https://api.opencagedata.com/geocode/v1/json?",
    }

    @staticmethod
    def fetch_data(url: str) -> Dict[str, Any]:
        response = requests.get(url)
        return response.json()
