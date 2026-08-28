import random


class EnvironmentSimulator:
    def __init__(self) -> None:
        self.temp_maitri = -25.0
        self.temp_bharati = -18.0

    def step(self, scenario: str = "normal") -> dict:
        mult = 1.8 if scenario == "extreme_weather" else 1.0

        self.temp_maitri += random.uniform(-0.5, 0.5)
        self.temp_bharati += random.uniform(-0.4, 0.4)

        return {
            "maitri": {
                "ambient_temperature": self.temp_maitri,
                "wind_speed": random.uniform(15, 35) * mult,
                "visibility": max(0.1, 10.0 - (5.0 if scenario == "extreme_weather" else 0.0)),
                "atmospheric_pressure": random.uniform(970, 995),
            },
            "bharati": {
                "ambient_temperature": self.temp_bharati,
                "wind_speed": random.uniform(20, 45) * mult,
                "visibility": max(0.1, 12.0 - (6.0 if scenario == "extreme_weather" else 0.0)),
                "atmospheric_pressure": random.uniform(965, 990),
            },
        }
