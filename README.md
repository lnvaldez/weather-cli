<h1 align='center'>☁️ Weather CLI </h1>

Command-line interface application to fetch current weather, forecasts, air quality, and more using location names or coordinates. It supports various output formats and can display results in the terminal or save them to files.

<h2 align='center'>🤖 Installation</h2>

### Clone the repo and navigate to the project folder:

```
git clone https://github.com/lnvaldez/weather-cli.git
cd weather-cli
```

### Install the required dependencies:

```
bash install_requirements.sh
```

### Basic usage

```
python -m src.cli [command] [arguments] [options]
```

For a detailed list of commands and options, refer to the [User Guide](/docs/user_guide.md).

<h2 align='center'>✍🏼 Example</h2>

Get current weather for Asuncion in JSON format:

```
python -m src.cli location Asuncion --current
```

### Output

```
{
    "temperature": 32.69,
    "sensation": 34.64,
    "description": "smoke",
    "humidity": 46,
    "pressure": 1006,
    "wind_speed": 0,
    "visibility": 4000
}
```

<h2 id="contributing" align="center">🤝 Contributing 🤝</h2>

See [CONTRIBUTING.md](/docs/CONTRIBUTING.md) for instructions on contributing to the project.

<p id="license" align="center"><a href="https://choosealicense.com/licenses/mit/">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License">
  </a></p>
