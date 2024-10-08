from typing import Dict, Any
from datetime import datetime
from src.api.weather_api_handler import API


class Base:
    def __init__(self):
        self.current_data = {}
        self.forecast = {}
        self.air_quality = {}
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
        }

        self.sunrise = datetime.fromtimestamp(sys["sunrise"]).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        self.sunset = datetime.fromtimestamp(sys["sunset"]).strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        self.sun_data = {"sunrise": self.sunrise, "sunset": self.sunset}

    def process_forecast_data(self, data: Dict[str, Any]):
        self.forecast = []
        forecast_list = data["list"]

        for i in range(0, len(forecast_list), 8):
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
        qualitative_name = {
            1: "Good",
            2: "Fair",
            3: "Moderate",
            4: "Poor",
            5: "Very Poor",
        }
        self.air_quality_index = data["list"][0]["main"]["aqi"]
        self.air_quality_name = qualitative_name[self.air_quality_index]
        self.air_quality = {
            "Index": self.air_quality_index,
            "Qualitative Name": self.air_quality_name,
        }


class Location(Base):
    def __init__(self, city_name: str):
        super().__init__()
        self.city_name = city_name
        self.fetch_all_data()

    def fetch_all_data(self):
        current_data = API.get_weather_by_city(self.city_name)
        self.lat = current_data["coord"]["lat"]
        self.lon = current_data["coord"]["lon"]
        forecast_data = API.get_forecast(self.lat, self.lon)
        air_data = API.get_air_quality(self.lat, self.lon)

        self.process_current_data(current_data)
        self.process_forecast_data(forecast_data)
        self.process_air_data(air_data)


class Coordinate(Base):
    def __init__(self, lat: float, lon: float):
        super().__init__()
        self.lat = lat
        self.lon = lon
        self.reverse_gcs = {}
        self.fetch_all_data()

    def process_gcs_data(self, data: Dict[str, Any]):
        self.formatted = data["results"][0]["formatted"]
        self.category = data["results"][0]["components"]["_category"]
        self.reverse_gcs = {
            "location": self.formatted,
            "category": self.category,
        }

    def fetch_all_data(self):
        self.process_current_data(API.get_weather_by_gcs(self.lat, self.lon))
        self.process_forecast_data(API.get_forecast(self.lat, self.lon))
        self.process_air_data(API.get_air_quality(self.lat, self.lon))
        self.process_gcs_data(API.get_reverse_gcs(self.lat, self.lon))
