from lib import aqi

# NOTE: Helper class for the information I care about
class SensorData():
    def __init__(self, name, aqi):
        self.name = name
        self.aqi = aqi

    def __repr__(self):
        return f'<SensorData name={self.name} aqi={self.aqi}>'

    def __str__(self):
        return f'<SensorData name={self.name} aqi={self.aqi}>'

def convert_to_sensor_data(sensor):
    return SensorData(
        name=sensor.parent.name,
        aqi=aqi.get_aqi(sensor)
    )

