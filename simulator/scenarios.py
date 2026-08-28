"""
Simulator Scenario Configuration Registry
Defines nominal and fault conditions for Antarctic digital twin simulations.
"""

SCENARIOS = {
    "normal": {
        "description": "Standard nominal Antarctic operational conditions",
        "ambient_temp_offset": 0.0,
        "wind_speed_multiplier": 1.0,
        "generator_failures": [],
        "comms_degraded": False,
        "fuel_consumption_multiplier": 1.0,
    },
    "generator_failure": {
        "description": "Primary Generator 1 emergency mechanical failure",
        "ambient_temp_offset": 0.0,
        "wind_speed_multiplier": 1.0,
        "generator_failures": ["GEN-MAI-001", "GEN-BHA-001"],
        "comms_degraded": False,
        "fuel_consumption_multiplier": 0.7,
    },
    "extreme_weather": {
        "description": "Extreme Antarctic blizzard (-45°C ambient, 95 km/h gusts)",
        "ambient_temp_offset": -20.0,
        "wind_speed_multiplier": 3.2,
        "generator_failures": [],
        "comms_degraded": False,
        "fuel_consumption_multiplier": 1.35,
    },
    "comms_loss": {
        "description": "Ku-band satellite ground station antenna blackout",
        "ambient_temp_offset": 0.0,
        "wind_speed_multiplier": 1.0,
        "generator_failures": [],
        "comms_degraded": True,
        "fuel_consumption_multiplier": 1.0,
    },
    "fuel_critical": {
        "description": "Severe polar diesel leak - reserve drops to 15% threshold",
        "ambient_temp_offset": 0.0,
        "wind_speed_multiplier": 1.0,
        "generator_failures": [],
        "comms_degraded": False,
        "fuel_critical_level": 6000.0,
        "fuel_consumption_multiplier": 1.0,
    },
}


def get_scenario_config(name: str) -> dict:
    return SCENARIOS.get(name, SCENARIOS["normal"])
