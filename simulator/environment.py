import math
import random
import time


class EnvironmentSimulator:
    def __init__(self) -> None:
        self.temp_maitri = -21.5
        self.temp_bharati = -15.8
        self.step_count = 0

    def step(self, scenario: str = "normal") -> dict:
        self.step_count += 1
        mult = 1.8 if scenario == "extreme_weather" else 1.0

        # Antarctic diurnal sun cycle
        hour = (time.gmtime().tm_hour + 4) % 24
        diurnal = math.sin((hour - 6) * math.pi / 12)

        target_maitri = -21.0 + 3.5 * diurnal
        self.temp_maitri = 0.95 * self.temp_maitri + 0.05 * target_maitri + random.uniform(-0.15, 0.15)

        target_bharati = -15.0 + 2.5 * diurnal
        self.temp_bharati = 0.95 * self.temp_bharati + 0.05 * target_bharati + random.uniform(-0.12, 0.12)

        return {
            "maitri": {
                "ambient_temperature": round(self.temp_maitri, 1),
                "wind_speed": round((random.uniform(18, 38) + 4.0 * math.sin(self.step_count / 10)) * mult, 1),
                "visibility": max(0.1, round(10.0 - (5.0 if scenario == "extreme_weather" else 0.0), 1)),
                "atmospheric_pressure": round(random.uniform(972, 992), 1),
            },
            "bharati": {
                "ambient_temperature": round(self.temp_bharati, 1),
                "wind_speed": round((random.uniform(22, 48) + 5.0 * math.cos(self.step_count / 10)) * mult, 1),
                "visibility": max(0.1, round(12.0 - (6.0 if scenario == "extreme_weather" else 0.0), 1)),
                "atmospheric_pressure": round(random.uniform(968, 988), 1),
            },
        }
