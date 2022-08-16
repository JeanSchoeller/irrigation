import json
import requests
from datetime import datetime
def showWeather():
        print("start") 
        city_name= "Menaggio"
        weather_url = "https://api.openweathermap.org/data/2.5/weather?q=menaggio&appid=31ceae673776cf2e67748b7fe00057e1" 
        response = requests.get(weather_url)
        weather_info = response.json()
        print("setup") 
        if weather_info['cod'] == 200:
            print("Fetched") 
            temp = int(weather_info['main']['temp'])
            feels_like_temp = int(weather_info['main']['feels_like'])
            pressure = weather_info['main']['pressure']
            humidity = weather_info['main']['humidity']
            wind_speed = weather_info['wind']['speed'] * 3.6
            sunrise = weather_info['sys']['sunrise']
            sunset = weather_info['sys']['sunset']
            timezone = weather_info['timezone']
            cloudy = weather_info['clouds']['all']
            description = weather_info['weather'][0]['description']
 
            sunrise_time = time_format_for_location(sunrise + timezone)
            sunset_time = time_format_for_location(sunset + timezone)

                 
            weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
            print(weather)
        else:
            weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
    

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

showWeather()
