from flask import Flask, request, render_template
import weather_service

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/process', methods=['GET'])
def process():
    # Получение данных из формы
    start_latitude = request.args.get('start_latitude')
    start_longitude = request.args.get('start_longitude')
    end_latitude = request.args.get('end_latitude')
    end_longitude = request.args.get('end_longitude')

    # Проверка заполненности всех полей
    if not (start_latitude and start_longitude and end_latitude and end_longitude):
        return render_template('result.html', error="Все поля должны быть заполнены!")

    # Получение данных о погоде
    start_weather = weather_service.get_weather_info(start_latitude, start_longitude)
    end_weather = weather_service.get_weather_info(end_latitude, end_longitude)

    # Проверка на ошибки в данных
    if "error" in start_weather or "error" in end_weather:
        return render_template(
            'result.html',
            error="Ошибка при получении данных о погоде! Проверьте координаты."
        )

    # Передача данных в шаблон
    return render_template(
        'result.html',
        start_latitude=start_latitude,
        start_longitude=start_longitude,
        end_latitude=end_latitude,
        end_longitude=end_longitude,
        start_weather=start_weather,
        end_weather=end_weather
    )


if __name__ == '__main__':
    app.run(debug=True)
