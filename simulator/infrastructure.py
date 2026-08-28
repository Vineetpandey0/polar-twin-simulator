import random


class InfrastructureSimulator:
    def step(self, scenario: str = "normal") -> dict:
        comms_maitri = 0.0 if scenario == "comms_loss" else random.uniform(88.0, 99.0)
        comms_bharati = random.uniform(92.0, 100.0)

        return {
            "BLD-MAI-MAIN": {
                "cabin_temp": random.uniform(21.2, 22.4),
                "relative_humidity": random.uniform(36.0, 42.0),
                "power_demand_kw": random.uniform(65.0, 72.0),
                "status": "RUNNING",
            },
            "HVC-MAI-001": {
                "internal_temp": random.uniform(19.0, 22.0),
                "flow_rate": random.uniform(88.0, 95.0),
                "status": "RUNNING",
            },
            "WTR-MAI-001": {
                "pressure": random.uniform(3.8, 4.2),
                "daily_output": random.uniform(1200.0, 1500.0),
                "status": "RUNNING",
            },
            "PMP-MAI-LAKE": {
                "intake_flow": random.uniform(150.0, 175.0),
                "pipe_trace_temp": random.uniform(7.8, 9.2),
                "status": "RUNNING",
            },
            "PMP-MAI-FUEL": {
                "transfer_rate": random.uniform(30.0, 38.0),
                "line_pressure": random.uniform(3.0, 3.4),
                "status": "RUNNING",
            },
            "COM-MAI-001": {
                "signal_strength": comms_maitri,
                "latency_ms": 650.0 if scenario == "comms_loss" else random.uniform(230.0, 260.0),
                "status": "FAILED" if scenario == "comms_loss" else "RUNNING",
            },
            "AWS-MAI-001": {
                "ambient_temp": random.uniform(-26.0, -24.5),
                "wind_speed": random.uniform(26.0, 32.0),
                "status": "RUNNING",
            },
            "HLP-MAI-001": {
                "deck_status": 1.0,
                "status": "RUNNING",
            },
            "BLD-BHA-MAIN": {
                "cabin_temp": random.uniform(21.8, 22.8),
                "relative_humidity": random.uniform(40.0, 45.0),
                "base_load_kw": random.uniform(130.0, 140.0),
                "status": "RUNNING",
            },
            "HVC-BHA-001": {
                "internal_temp": random.uniform(20.0, 22.5),
                "flow_rate": random.uniform(90.0, 96.0),
                "status": "RUNNING",
            },
            "WTR-BHA-001": {
                "permeate_flow": random.uniform(180.0, 195.0),
                "storage_volume": random.uniform(12000.0, 13000.0),
                "status": "RUNNING",
            },
            "PMP-BHA-SEA": {
                "seawater_flow": random.uniform(400.0, 440.0),
                "intake_pressure": random.uniform(5.0, 5.4),
                "status": "RUNNING",
            },
            "COM-BHA-001": {
                "signal_strength": comms_bharati,
                "downlink_rate": random.uniform(100.0, 110.0),
                "status": "RUNNING",
            },
            "HLP-BHA-001": {
                "deck_status": 1.0,
                "status": "RUNNING",
            },
        }
