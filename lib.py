import matplotlib.pyplot as plt
import numpy as np
import requests_cache, requests
from datetime import timedelta, datetime

cache = requests_cache.CachedSession('weather', expire_after=timedelta(hours=6))
def untitlable(lat = 24.7136, lon = 46.6753):
    if not lat or not lon:
        lat = 24.7136
        lon = 46.6753
    response = cache.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min")
    data = response.json()
    date_strings = data["daily"]["time"]
    dates = [datetime.strptime(date_str, "%Y-%m-%d") for date_str in date_strings]

    dates = [date.strftime("%A") for date in dates]

    max_temps = data["daily"]["temperature_2m_max"]
    min_temps = data["daily"]["temperature_2m_min"]
    fig, ax = plt.subplots(layout='constrained')

    ax.plot(dates, max_temps, label="Max temperature")
    ax.plot(dates, min_temps, label="Min temperature")
    ax.legend()

    plt.xlabel("Time (Days)")
    plt.ylabel("Temperature (Celsius)")
    plt.title("Temprature over 7 days")
    plt.grid()
    plt.savefig('weather.png', bbox_inches='tight')
    if response.status_code == 200:
        return True
    else:
        return False