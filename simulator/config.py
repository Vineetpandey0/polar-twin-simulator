import os
from dotenv import load_dotenv

load_dotenv()

MQTT_HOST: str = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT: int = int(os.getenv("MQTT_PORT", "1883"))
TICK_INTERVAL: float = float(os.getenv("TICK_INTERVAL", "600.0"))
STATIONS: list[str] = ["maitri", "bharati"]
