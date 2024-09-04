#!/bin/bash

mv .env.sample .env

echo "Installing requirements..."

python -m venv myenv
myenv/Scripts/Activate

pip install -r requirements.txt

read -p "Input OpenWeather API Key: "; weather_api_key

echo "WEATHER_API_KEY='${weather_api_key}'" >> .env

echo "OpenWeather API Key saved to .env file."

read -p "Input OpenCage Geocoding API Key: "; geo_api_key 

echo "GEO_API_KEY='${geo_api_key}'" >> .env 

echo "OpenCage Geocoding API key saved to .env file."

echo "Setup finished."

