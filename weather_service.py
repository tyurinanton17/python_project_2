import requests
from WeatherData import WeatherData

API_KEY = "1LqMQsIZGG9NcjwfzY7Hxge4X8HkAIF7"


def get_weather_info(latitude, longitude):
    try:
        # URL для получения Location Key
        location_url = f"http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={API_KEY}&q={latitude},{longitude}"
        response = requests.get(location_url)
        response.raise_for_status()  # Проверяем статус ответа

        if response.status_code == 200:
            location_data = response.json()
            if "Key" in location_data:
                location_key = location_data['Key']
            else:
                return {"error": "Location Key не найден в ответе от API"}
        else:
            return {"error": f"Ошибка получения Location Key: {response.json().get('Message', 'Неизвестная ошибка')}"}

        # URL для получения погодных данных
        weather_url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={API_KEY}&details=true"
        response = requests.get(weather_url)
        response.raise_for_status()  # Проверяем статус ответа

        data = response.json()
        if not data:
            return {"error": "Данные о погоде отсутствуют"}
        data = data[0]

        weather_info = WeatherData(
            t=data["Temperature"]["Metric"]["Value"],
            v=data["RelativeHumidity"],
            s=data["Wind"]["Speed"]["Metric"]["Value"],
        )
        return weather_info.get_dict()
    except requests.exceptions.RequestException as req_err:
        return {"error": f"Сетевая ошибка: {req_err}"}
    except KeyError as key_err:
        return {"error": f"Ошибка данных: отсутствует ключ {key_err}"}
    except Exception as e:
        return {"error": f"Неизвестная ошибка: {e}"}
