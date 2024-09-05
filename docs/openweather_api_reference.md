# OpenWeather API Reference

## OpenWeather API Reference for Current Weather, Forecast, and Air Pollution

### Current Weather

**Endpoint:** `http://api.openweathermap.org/data/2.5/weather?`

**Parameters:**

- `q`: City name
- `appid`: Your API key
- `units`: Metric or imperial
- `lang`: Language for the weather description (e.g., en, ru, fr)

**Response**

```
{
  "coord": {
    "lon": -57.6358,
    "lat": -25.2637
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "Clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 28.61,
    "feels_like": 27.84,
    "pressure": 1013,
    "humidity": 76,
    "temp_min": 28.61,
    "temp_max": 28.61
  },
  "visibility": 10000,
  "wind": {
    "speed": 1.98,
    "deg": 240
  },
  "clouds": {
    "all": 0
  },
  "dt": 1693807200,
  "sys": {
    "type": 1,
    "id": 11003,
    "country": "PY",
    "sunrise": 1693766275,
    "sunset": 1693815340
  },
  "timezone": -14400,
  "id": 3436549,
  "name": "Asunción",
  "cod": 200
}
```

### Forecast API

**Endpoint:** `https://api.openweathermap.org/data/2.5/forecast`

**Parameters:**

- `q`: City name
- `appid`: Your API key
- `units`: Metric or imperial

**Response:**

```
{
  "cod": "200",
  "message": 0,
  "cnt": 40,
  "list": [
    // ... forecast data for each 3-hour interval
  ]
}
```

### Air Pollution API

**Endpoint:** `https://api.openweathermap.org/data/2.5/air_pollution`

**Parameters:**

- `lat`: Latitude
- `lon`: Longitude
- `appid`: Your API key

**Response:**

```
{
  "coord": {
    "lon": -57.6358,
    "lat": -25.2637
  },
  "list": [
    {
      "main": {
        "aqi": 4
      },
      "components": {
        "co": 201.94,
        "no": 0,
        "no2": 0.15,
        "o3": 68.67,
        "so2": 0.18,
        "pm2_5": 31.11,
        "pm10": 135.74,
        "nh3": 0
      },
      "dt": 1725467475
    }
  ]
}
```

---
