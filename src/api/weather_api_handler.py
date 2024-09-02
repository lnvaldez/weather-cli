import os
import requests
import sys
from dotenv import load_dotenv
from typing import Dict, Any
from requests.exceptions import HTTPError
from src.utils.error_handling import handle_http_error

load_dotenv()


class API:
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
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except HTTPError as errh:
            sys.exit(handle_http_error(error=errh))

    @classmethod
    def get_weather_by_city(self, city: str) -> Dict[str, Any]:
        url = f"{self.BASE_URLS['weather']}appid={self.WEATHER_API_KEY}&q={city}&units=metric"
        return self.fetch_data(url=url)

    @classmethod
    def get_weather_by_gcs(self, lat: float, lon: float) -> Dict[str, Any]:
        url = f"{self.BASE_URLS['weather']}appid={self.WEATHER_API_KEY}&lat={lat}&lon={lon}&units=metric"
        return self.fetch_data(url=url)

    @classmethod
    def get_forecast(self, lat: float, lon: float) -> Dict[str, Any]:
        url = f"{self.BASE_URLS['forecast']}appid={self.WEATHER_API_KEY}&lat={lat}&lon={lon}&units=metric"
        return self.fetch_data(url=url)

    @classmethod
    def get_air_quality(self, lat: float, lon: float) -> Dict[str, Any]:
        url = f"{self.BASE_URLS['air']}appid={self.WEATHER_API_KEY}&lat={lat}&lon={lon}&units=metric"
        return self.fetch_data(url=url)
