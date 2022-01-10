# Identi Drunk

## Project Structure

- `backend` with three Docker containers:
  - REST API service (with Deno)
  - PostgreSQL
  - Grafana
- `raspi` Python project executed in the Raspberry Pi.

## Sensors and Actuators

- RFID Reader
- Alcohol Sensor / Gas Sensor
- LCD

## Installation

### Raspberry Pi

- Install [pi-rc522](https://github.com/ondryaso/pi-rc522).
