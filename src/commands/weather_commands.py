from src.models.weather_models import WeatherLocation, Coordinate
from src.utils.enum import OutputFormat, Target
from src.utils.output_format import output_format


def location(
    city: str,
    current: bool = False,
    forecast: bool = False,
    aqi: bool = False,
    sun: bool = False,
    format: OutputFormat = OutputFormat.json,
    target: Target = Target.terminal,
):
    weather = WeatherLocation(city_name=city)

    if target == "terminal":
        if current:
            print(
                output_format(
                    data=weather.current_data, format_type=format, target_output=target
                )
            )
        if forecast:
            print(
                output_format(
                    data=weather.forecast, format_type=format, target_output=target
                )
            )
        if aqi:
            print(
                output_format(
                    data=weather.air_quality, format_type=format, target_output=target
                )
            )
        if sun:
            print(
                output_format(
                    data=weather.sun_data, format_type=format, target_output=target
                )
            )
    else:
        if current:
            output_format(
                data=weather.current_data, format_type=format, target_output=target
            )
        if forecast:
            output_format(
                data=weather.forecast, format_type=format, target_output=target
            )
        if aqi:
            output_format(
                data=weather.air_quality, format_type=format, target_output=target
            )
        if sun:
            output_format(
                data=weather.sun_data, format_type=format, target_output=target
            )


def coordinate(
    latitude: float,
    longitude: float,
    current: bool = False,
    forecast: bool = False,
    aqi: bool = False,
    sun: bool = False,
    format: OutputFormat = OutputFormat.json,
    target: Target = Target.terminal,
):
    weather = Coordinate(lat=latitude, lon=longitude)

    if target == "terminal":
        if current:
            print(
                output_format(
                    data=weather.current_data, format_type=format, target_output=target
                )
            )
        if forecast:
            print(
                output_format(
                    data=weather.forecast, format_type=format, target_output=target
                )
            )
        if aqi:
            print(
                output_format(
                    data=weather.air_quality, format_type=format, target_output=target
                )
            )
        if sun:
            print(
                output_format(
                    data=weather.sun_data, format_type=format, target_output=target
                )
            )
    else:
        if current:
            output_format(
                data=weather.current_data, format_type=format, target_output=target
            )
        if forecast:
            output_format(
                data=weather.forecast, format_type=format, target_output=target
            )
        if aqi:
            output_format(
                data=weather.air_quality, format_type=format, target_output=target
            )
        if sun:
            output_format(
                data=weather.sun_data, format_type=format, target_output=target
            )
