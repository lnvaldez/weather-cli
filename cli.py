import typer
from weather_models import WeatherLocation

app = typer.Typer()


@app.command()
def location(
    city: str,
    current: bool = False,
    forecast: bool = False,
    aqi: bool = False,
    sun: bool = False,
):
    weather = WeatherLocation(city_name=city)

    if current:
        print(weather.current_data)
    if forecast:
        print(weather.forecast)
    if aqi:
        print(weather.air_quality)
    if sun:
        print(weather.sun_data)


if __name__ == "__main__":
    app()
