# Weather CLI User Guide

This guide provides instructions on how to use the Weather CLI application to retrieve various weather-related information for locations and coordinates.

## Table of Contents

1. [Installation](#installation)
2. [Basic Usage](#basic-usage)
3. [Commands](#commands)
   - [location](#location)
   - [coordinate](#coordinate)
4. [Options](#options)
5. [Output Formats](#output-formats)
6. [Examples](#examples)

## Installation

- Get [OpenWeather](https://openweathermap.org/) and [OpenCage](https://opencagedata.com/) API keys
- Run the following command `bash install_requirements.sh`
- Install Git-hooks if you want to contribute to the project.

## Basic Usage

The basic syntax for using the Weather CLI is:

```
python -m src.cli [command] [argument] [options]
```

## Commands

### location

Use the `location` command to retrieve weather information for a specific city.

Syntax:

```
python -m src.cli location [city_name] [options]
```

### coordinate

Use the `coordinate` command to retrieve weather information for specific geographic coordinates.

Syntax:

```
python -m src.cli coordinate [latitude] [longitude] [options]
```

## Options

- `--current`: Get current weather conditions
- `--forecast`: Get a 5-day weather forecast
- `--aqi`: Get current air quality information
- `--sun`: Get sunrise and sunset times
- `--translate`: (For coordinate command) Translate coordinates to location name
- `--format [format]`: Specify output format (json, csv, or txt)
- `--target [target]`: Specify output target (terminal or file)

## Examples

1. Get current weather for Asuncion in JSON format:

   ```
   python -m src.cli location Asuncion --current
   ```

2. Get 5-day forecast for Asuncion in CSV format:

   ```
   python -m src.cli location Asuncion --forecast --format "csv"
   ```

3. Get air quality information for specific coordinates in TXT format:

   ```
   python -m src.cli coordinate 41.4086874 -75.6621294 --translate --aqi --format "txt"
   ```

4. Get sunrise and sunset times for Asuncion and save to a file:
   ```
   python -m src.cli location Asuncion --sun --target "file"
   ```

---
