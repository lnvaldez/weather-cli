import typer
from src.models.weather_models import WeatherLocation, Coordinate
from src.utils.enum import OutputFormat
from src.utils.output_format import output_format

app = typer.Typer()


@app.command()
def location(
    city: str,
    current: bool = False,
    forecast: bool = False,
    aqi: bool = False,
    sun: bool = False,
    format: OutputFormat = OutputFormat.json,
):
    weather = WeatherLocation(city_name=city)

    if current:
        print(output_format(data=weather.current_data, format_type=format))
    if forecast:
        print(output_format(data=weather.forecast, format_type=format))
    if aqi:
        print(output_format(data=weather.air_quality, format_type=format))
    if sun:
        print(output_format(data=weather.sun_data, format_type=format))


@app.command()
def coordinate(
    latitude: float,
    longitude: float,
    current: bool = False,
    forecast: bool = False,
    aqi: bool = False,
    sun: bool = False,
    format: OutputFormat = OutputFormat.json,
):
    weather = Coordinate(lat=latitude, lon=longitude)

    if current:
        print(output_format(data=weather.current_data, format_type=format))
    if forecast:
        print(output_format(data=weather.forecast, format_type=format))
    if aqi:
        print(output_format(data=weather.air_quality, format_type=format))
    if sun:
        print(output_format(data=weather.sun_data, format_type=format))


if __name__ == "__main__":
    app()
