from typing import Dict, Any
from datetime import datetime
from weather_api_handler import WeatherApi


class WeatherBase:
    def __init__(self):
        self.current_data = {}
        self.forecast = {}
        self.air_quality = None
        self.sun_data = {}

    def process_current_data(self, data: Dict[str, Any]):
        main = data["main"]
        weather = data["weather"][0]
        wind = data["wind"]
        sys = data["sys"]

        self.current_data = {
            "temperature": main["temp"],
            "sensation": main["feels_like"],
            "description": weather["description"],
            "humidity": main["humidity"],
            "pressure": main["pressure"],
            "wind_speed": wind["speed"],
            "visibility": data["visibility"],
            "sunrise": datetime.fromtimestamp(sys["sunrise"]).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "sunset": datetime.fromtimestamp(sys["sunset"]).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        }

    def process_forecast_data(self, data: Dict[str, Any]):
        self.forecast = []
        forecast_list = data["list"]

        for i in range(0, len(forecast_list, 8)):
            day_data = forecast_list[i]
            forecast_entry = {
                "date": day_data["dt_txt"],
                "temp": day_data["main"]["temp"],
                "sensation": day_data["main"]["feels_like"],
                "description": day_data["weather"][0]["description"],
                "humidity": day_data["main"]["humidity"],
                "pressure": day_data["main"]["pressure"],
                "wind_speed": day_data["wind"]["speed"],
                "visibility": day_data["visibility"],
            }
            self.forecast.append(forecast_entry)

    def process_air_data(self, data: Dict[str, Any]):
        self.air_quality = data["list"][0]["main"]["aqi"]


class WeatherLocation(WeatherBase):
    def __init__(self, city_name: str):
        super().__init__()
        self.city_name = city_name
        self.fetch_all_data()

    def fetch_all_data(self):
        current_data = WeatherApi.get_weather_by_city(self.city_name)
        self.lat = current_data["coord"]["lat"]
        self.lon = current_data["coord"]["lon"]
        lat_lon_data = WeatherApi.get_forecast(self.lat, self.lon)

        self.process_current_data(current_data)
        self.process_forecast_data(lat_lon_data)
        self.process_air_data(lat_lon_data)
