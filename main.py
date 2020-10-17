from purpleair.sensor import Sensor
from lib import aqi, email, message, sensor_data

ALAMO_SQUARE = 65759
LYON_STREET = 17951
UPPER_HAIGHT = 17763
USF_STADIUM = 38725

SENSORS_NEAR_ME = [ALAMO_SQUARE, LYON_STREET, UPPER_HAIGHT, USF_STADIUM]

raw_sensors = [Sensor(id) for id in SENSORS_NEAR_ME]
sensors = [sensor_data.convert_to_sensor_data(Sensor(id)) for id in SENSORS_NEAR_ME]
sorted_sensors = sorted(sensors, key=lambda s: s.aqi)

recipients = ['foo@example.com']

message, subject = message.get_text(sorted_sensors)

email.send_email(message, subject, recipients)
