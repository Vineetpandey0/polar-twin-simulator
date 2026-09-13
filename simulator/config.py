import os
from dotenv import load_dotenv

load_dotenv()

raw_host = os.getenv("MQTT_HOST", "").strip().rstrip("/")
is_dev = os.getenv("ENV", "").lower() == "development" or os.getenv("NODE_ENV", "").lower() == "development"
MQTT_HOST: str = raw_host or ("localhost" if is_dev else "polar-twin-backend.up.railway.app") or "localhost"
MQTT_PORT: int = int(os.getenv("MQTT_PORT", "1883"))
TICK_INTERVAL: float = float(os.getenv("TICK_INTERVAL", "4.0"))
STATIONS: list[str] = ["maitri", "bharati"]
