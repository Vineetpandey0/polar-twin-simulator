import random


class GeneratorSimulator:
    def step(self, scenario: str = "normal") -> dict:
        gen1_status = "FAILED" if scenario == "generator_failure" else "RUNNING"
        gen1_rpm = 0.0 if gen1_status == "FAILED" else random.uniform(1480, 1510)
        gen1_load = 0.0 if gen1_status == "FAILED" else random.uniform(65.0, 85.0)

        return {
            "GEN-MAI-001": {
                "status": gen1_status,
                "rpm": gen1_rpm,
                "temperature": 92.5 if gen1_status == "FAILED" else random.uniform(75.0, 88.0),
                "fuel_consumption": 0.0 if gen1_status == "FAILED" else random.uniform(18.0, 24.0),
                "voltage": 0.0 if gen1_status == "FAILED" else random.uniform(395.0, 405.0),
                "load_pct": gen1_load,
            },
            "GEN-MAI-002": {
                "status": "RUNNING",
                "rpm": random.uniform(1490, 1515),
                "temperature": random.uniform(76.0, 89.0),
                "fuel_consumption": random.uniform(19.0, 25.0),
                "voltage": random.uniform(398.0, 402.0),
                "load_pct": random.uniform(70.0, 90.0) if gen1_status == "FAILED" else random.uniform(50.0, 70.0),
            },
            "GEN-MAI-003": {
                "status": "STOPPED",
                "rpm": 0.0,
                "temperature": 15.0,
                "fuel_consumption": 0.0,
                "voltage": 0.0,
                "load_pct": 0.0,
            },
            "GEN-BHA-001": {
                "status": "RUNNING",
                "rpm": random.uniform(1495, 1505),
                "temperature": random.uniform(72.0, 85.0),
                "fuel_consumption": random.uniform(20.0, 26.0),
                "voltage": random.uniform(399.0, 401.0),
                "load_pct": random.uniform(60.0, 75.0),
            },
            "GEN-BHA-002": {
                "status": "RUNNING",
                "rpm": random.uniform(1490, 1510),
                "temperature": random.uniform(74.0, 86.0),
                "fuel_consumption": random.uniform(18.0, 24.0),
                "voltage": random.uniform(398.0, 402.0),
                "load_pct": random.uniform(55.0, 70.0),
            },
        }
