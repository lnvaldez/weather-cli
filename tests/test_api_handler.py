import requests
from src.api.weather_api_handler import API

WEATHER_API_KEY = API.WEATHER_API_KEY
GEO_API_KEY = API.GEO_API_KEY

BASE_URLS = API.BASE_URLS

city = "Asuncion"

lat = 25.123
lon = 36.234


def test_get_weather_by_city():
    url = f"{BASE_URLS['weather']}appid={WEATHER_API_KEY}&q={city}&units=metric"
    response = requests.get(url=url)
    assert response.status_code == 200

    data = response.json()

    assert "main" in data
    assert "weather" in data
    assert "wind" in data

    assert "temp" in data["main"]
    assert "feels_like" in data["main"]
    assert "description" in data["weather"][0]


def test_get_weather_by_gcs():
    url = f"{BASE_URLS['weather']}appid={WEATHER_API_KEY}&lat={lat}&lon={lon}&units=metric"
    response = requests.get(url=url)
    assert response.status_code == 200

    data = response.json()

    assert "coord" in data
    assert "main" in data
    assert "weather" in data
    assert "wind" in data

    assert "temp" in data["main"]
    assert "feels_like" in data["main"]
    assert "description" in data["weather"][0]


def test_get_forecast():
    url = f"{BASE_URLS['forecast']}appid={WEATHER_API_KEY}&q={city}&units=metric"
    response = requests.get(url=url)
    assert response.status_code == 200

    data = response.json()

    assert "list" in data

    assert "dt_txt" in data["list"][0]
    assert "temp" in data["list"][0]["main"]
    assert "feels_like" in data["list"][0]["main"]


def test_get_air_quality():
    url = f"{BASE_URLS['air']}appid={WEATHER_API_KEY}&lat={lat}&lon={lon}&units=metric"
    response = requests.get(url=url)
    assert response.status_code == 200

    data = response.json()

    assert "coord" in data

    assert "aqi" in data["list"][0]["main"]
