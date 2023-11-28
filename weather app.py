import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        main_info = data['main']
        current_temp = main_info['temp']
        max_temp = main_info['temp_max']
        min_temp = main_info['temp_min']

        return current_temp, max_temp, min_temp
    else:
        return None

# Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
api_key = '735df8c0e5ccfe3eb72ea59f7b896041'
city = 'Kadiri',# Replace with your city and country

weather_data = get_weather(api_key, city)

if weather_data:
    current_temp, max_temp, min_temp = weather_data
    print(f"Current Temperature: {current_temp}°C")
    print(f"Maximum Temperature: {max_temp}°C")
    print(f"Minimum Temperature: {min_temp}°C")
else:
    print("Failed to fetch weather data. Check your API key and city.")
