import time
import logging
from config import TICK_INTERVAL
from mqtt_publisher import MQTTPublisher
from environment import EnvironmentSimulator
from generators import GeneratorSimulator
from battery import BatterySimulator
from infrastructure import InfrastructureSimulator
from inventory import InventorySimulator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("simulator_main")


def main() -> None:
    publisher = MQTTPublisher()
    publisher.connect()

    env_sim = EnvironmentSimulator()
    gen_sim = GeneratorSimulator()
    bat_sim = BatterySimulator()
    inf_sim = InfrastructureSimulator()
    inv_sim = InventorySimulator()

    logger.info("PolarTwin Telemetry Simulator started ticking...")
    scenario = "normal"

    while True:
        try:
            # 1. Environment
            env_data = env_sim.step(scenario)
            for st, metrics in env_data.items():
                for m, val in metrics.items():
                    unit = "°C" if "temperature" in m else "km/h" if "wind" in m else "km" if "visibility" in m else "hPa"
                    publisher.publish_telemetry(st, "environment", f"ENV-{st.upper()}", f"SEN-ENV-{st.upper()}", m, val, unit)

            # 2. Generators
            gen_data = gen_sim.step(scenario)
            for asset_id, metrics in gen_data.items():
                st = "maitri" if "MAI" in asset_id else "bharati"
                for m, val in metrics.items():
                    if isinstance(val, (int, float)):
                        unit = "RPM" if m == "rpm" else "°C" if m == "temperature" else "L/h" if m == "fuel_consumption" else "V" if m == "voltage" else "%"
                        publisher.publish_telemetry(st, "energy/generator", asset_id, f"SEN-{asset_id}", m, val, unit)

            # 3. Batteries
            bat_data = bat_sim.step(scenario)
            for asset_id, metrics in bat_data.items():
                st = "maitri" if "MAI" in asset_id else "bharati"
                for m, val in metrics.items():
                    unit = "%" if m == "soc" else "kW" if m == "charge_rate" else "°C"
                    publisher.publish_telemetry(st, "energy/battery", asset_id, f"SEN-{asset_id}", m, val, unit)

            # 4. Infrastructure
            inf_data = inf_sim.step(scenario)
            for asset_id, metrics in inf_data.items():
                st = "maitri" if "MAI" in asset_id else "bharati"
                for m, val in metrics.items():
                    if isinstance(val, (int, float)):
                        unit = "°C" if "temp" in m else "bar" if "pressure" in m else "ms" if "latency" in m else "%"
                        publisher.publish_telemetry(st, "infrastructure", asset_id, f"SEN-{asset_id}", m, val, unit)

            # 5. Inventory
            inv_data = inv_sim.step(scenario)
            for st, metrics in inv_data.items():
                for m, val in metrics.items():
                    unit = "L" if "fuel" in m or "diesel" in m else "days" if "food" in m else "%" if "medical" in m else "units"
                    publisher.publish_telemetry(st, "inventory", f"INV-{st.upper()}", f"SEN-INV-{st.upper()}", m, val, unit)

            time.sleep(TICK_INTERVAL)
        except KeyboardInterrupt:
            logger.info("Simulator stopping...")
            publisher.disconnect()
            break
        except Exception as e:
            logger.error(f"Error in simulator loop: {e}")
            time.sleep(TICK_INTERVAL)


if __name__ == "__main__":
    main()
