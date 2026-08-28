# PolarTwin — Simulator

MQTT-based sensor data simulator for the PolarTwin Digital Twin system.
Publishes realistic telemetry for Indian Antarctic Stations (Maitri & Bharati).

## Stack
- **Python 3.11**
- **paho-mqtt** — MQTT client

## Project Structure
```
simulator/      All simulator source files
Dockerfile      Docker image
docker-compose.yml  Standalone compose (simulator only)
```

## Quick Start

```bash
# 1. Copy env file and fill in your MQTT broker address
cp .env.example .env

# 2. Run
docker-compose up --build
```

## Environment Variables

| Variable | Description |
|---|---|
| `MQTT_HOST` | IP or domain of the MQTT broker (backend server) |
| `MQTT_PORT` | MQTT port (default: `1883`) |

## Notes

The MQTT broker is hosted by [`polar-twin-backend`](https://github.com/your-org/polar-twin-backend).
When running on the **same server**, set `MQTT_HOST` to the backend container IP or `host.docker.internal`.
When running on a **different machine**, expose port `1883` on the backend server and point here.
