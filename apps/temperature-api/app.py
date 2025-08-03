from flask import Flask, request, jsonify
import random
import time

app = Flask(__name__)

def resolve_location_sensor(location, sensor_id):
    if not location:
        if sensor_id == "1":
            location = "Living Room"
        elif sensor_id == "2":
            location = "Bedroom"
        elif sensor_id == "3":
            location = "Kitchen"
        else:
            location = "Unknown"

    if not sensor_id:
        if location == "Living Room":
            sensor_id = "1"
        elif location == "Bedroom":
            sensor_id = "2"
        elif location == "Kitchen":
            sensor_id = "3"
        else:
            sensor_id = "0"
    return location, sensor_id

@app.route('/temperature')
def temperature():
    location = request.args.get('location', '')
    sensor_id = request.args.get('sensorId', '')

    location, sensor_id = resolve_location_sensor(location, sensor_id)

    random.seed(time.time())
    temperature = round(15 + random.random() * 10, 2)  # от 15 до 25 градусов

    return jsonify({
        "location": location,
        "sensorId": sensor_id,
        "temperature": temperature
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)