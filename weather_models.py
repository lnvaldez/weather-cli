from typing import Dict, Any
from datetime import datetime


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
