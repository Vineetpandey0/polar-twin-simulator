from typing import Dict, Any


class EnergySimulator:
    def calculate_energy_balance(
        self,
        station_id: str,
        generator_readings: Dict[str, Any],
        battery_readings: Dict[str, Any],
        ambient_temp: float,
    ) -> Dict[str, float]:
        # Compute total active generation (kW)
        total_generation = sum(
            float(g.get("load_kw", g.get("power_kw", 70.0)))
            for g in generator_readings.values()
            if g.get("status", 1.0) > 0.0
        )

        # Baseline station load (higher demand in extreme freezing temperatures)
        base_station_load = 110.0 if station_id == "maitri" else 135.0
        thermal_penalty = max(0.0, -ambient_temp - 20.0) * 0.8
        total_demand = base_station_load + thermal_penalty

        # Net grid balance
        net_balance = total_generation - total_demand

        return {
            "total_generation_kw": round(total_generation, 1),
            "total_demand_kw": round(total_demand, 1),
            "net_balance_kw": round(net_balance, 1),
            "grid_frequency_hz": 50.0 + (0.05 if net_balance >= 0 else -0.15),
            "bus_voltage_v": 400.0 if net_balance >= 0 else 388.0,
        }


energy_simulator = EnergySimulator()
