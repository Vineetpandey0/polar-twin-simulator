import json
import logging
from datetime import datetime, timezone
import paho.mqtt.client as mqtt
from config import MQTT_HOST, MQTT_PORT

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mqtt_publisher")


class MQTTPublisher:
    def __init__(self) -> None:
        self.client = mqtt.Client()
        self.connected = False
        self.client.on_connect = self._on_connect
        self.client.on_disconnect = self._on_disconnect

    def _on_connect(self, client, userdata, flags, rc) -> None:
        if rc == 0:
            self.connected = True
            logger.info("Connected to MQTT Broker successfully.")
        else:
            logger.error(f"Failed to connect to MQTT Broker, return code: {rc}")

    def _on_disconnect(self, client, userdata, rc) -> None:
        self.connected = False
        logger.warning(f"Disconnected from MQTT Broker (code {rc}). Attempting reconnect...")

    def connect(self) -> None:
        try:
            self.client.connect(MQTT_HOST, MQTT_PORT, 60)
            self.client.loop_start()
        except Exception as e:
            logger.error(f"MQTT connection error: {e}")

    def publish_telemetry(
        self,
        station_id: str,
        domain: str,
        asset_id: str,
        sensor_id: str,
        metric: str,
        value: float,
        unit: str,
    ) -> None:
        topic = f"stations/{station_id.lower()}/{domain}/{asset_id}/{metric}"
        payload = {
            "station_id": station_id.lower(),
            "asset_id": asset_id,
            "sensor_id": sensor_id,
            "metric": metric,
            "value": round(float(value), 2),
            "unit": unit,
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        try:
            self.client.publish(topic, json.dumps(payload))
        except Exception as e:
            logger.error(f"Publish failed for topic {topic}: {e}")

    def disconnect(self) -> None:
        self.client.loop_stop()
        self.client.disconnect()
