import requests

def get_weather_info():
    api_key = "50b7f5cc2921b2461e479faf3dcc4e9f"  
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    city = input("Введіть назву міста: ")

    parameters = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ua'
    }

    response = requests.get(base_url, params=parameters)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather_description = data['weather'][0]['description']
        print(f"Поточна погода у місті {city}: {temp}°C, {weather_description}")
    else:
        print(f"Не вдалося отримати дані про погоду для міста {city}. Перевірте правильність введення.")
