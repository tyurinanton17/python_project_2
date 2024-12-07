class WeatherData:
    def __init__(self, t, v, s):
        self.t = t
        self.h = v
        self.s = s

    def bad_weather(self):
        # Проверяем, плохая ли погода
        if self.t < -30 or self.t > 30:
            return True
        if self.h > 70:
            return True
        if self.s > 20:
            return True
        return False

    def get_dict(self):
        return {
            'temperature': f"{self.t}°C",
            'humidity': f"{self.h}%",
            'speed_wind': f"{self.s} м/с",
            'bad_weather': self.bad_weather()
        }
