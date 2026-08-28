import random


class BatterySimulator:
    def step(self, scenario: str = "normal") -> dict:
        return {
            "BAT-MAI-001": {
                "soc": random.uniform(82.0, 95.0),
                "charge_rate": random.uniform(-2.0, 5.0),
                "temperature": random.uniform(18.0, 24.0),
            },
            "BAT-MAI-002": {
                "soc": random.uniform(80.0, 92.0),
                "charge_rate": random.uniform(-1.5, 4.5),
                "temperature": random.uniform(19.0, 25.0),
            },
            "BAT-BHA-001": {
                "soc": random.uniform(88.0, 98.0),
                "charge_rate": random.uniform(0.0, 6.0),
                "temperature": random.uniform(20.0, 23.0),
            },
        }
