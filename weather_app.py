import streamlit as st
import requests

API_KEY = "ce6c1d206a81800798b78c781d4e0ff1"
CURRENT_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"

def get_current_weather(city):
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(CURRENT_URL, params=params)
    return response.json()

def get_forecast(city):
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(FORECAST_URL, params=params)
    return response.json()

# Streamlit UI
st.set_page_config(page_title="Weather Forecast App", layout="centered")
st.title("🌤️ Weather Forecast App")

city = st.text_input("Enter a city name")

if city:
    current = get_current_weather(city)
    forecast = get_forecast(city)

    if current.get("cod") == 200:
        st.subheader(f"📍 Current Weather in {city.title()}")
        st.metric("Temperature", f"{current['main']['temp']}°C")
        st.write(f"**Description:** {current['weather'][0]['description'].title()}")
        st.write(f"**Humidity:** {current['main']['humidity']}%")
        st.write(f"**Wind Speed:** {current['wind']['speed']} m/s")
    else:
        st.error(f"Error: {current.get('message', 'Unable to fetch weather.')}")

    if forecast.get("cod") == "200":
        st.subheader("📅 3-Day Forecast at 12:00 PM")
        count = 0
        for entry in forecast['list']:
            if "12:00:00" in entry['dt_txt']:
                date = entry['dt_txt'].split()[0]
                temp = entry['main']['temp']
                desc = entry['weather'][0]['description'].title()
                st.info(f"{date}: {temp}°C, {desc}")
                count += 1
                if count == 3:
                    break
    else:
        st.error(f"Forecast error: {forecast.get('message', 'Unable to fetch forecast.')}")
