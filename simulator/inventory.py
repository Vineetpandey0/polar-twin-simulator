import random


class InventorySimulator:
    def __init__(self) -> None:
        self.fuel_maitri = 45000.0
        self.fuel_bharati = 60000.0

    def step(self, scenario: str = "normal") -> dict:
        if scenario == "fuel_critical":
            self.fuel_maitri = 12000.0

        self.fuel_maitri = max(0.0, self.fuel_maitri - random.uniform(5.0, 15.0))
        self.fuel_bharati = max(0.0, self.fuel_bharati - random.uniform(6.0, 18.0))

        return {
            "maitri": {
                "diesel_reserve": self.fuel_maitri,
                "food_days": random.uniform(115.0, 120.0),
                "medical_pct": 100.0,
                "spare_parts_units": 25,
            },
            "bharati": {
                "diesel_reserve": self.fuel_bharati,
                "food_days": random.uniform(175.0, 180.0),
                "medical_pct": 100.0,
                "spare_parts_units": 30,
            },
        }
