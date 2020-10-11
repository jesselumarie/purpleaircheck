import statistics
from purpleair.sensor import Sensor
from datetime import date

GREEN = 'green'
YELLOW = 'yellow'
ORANGE = 'orange'
RED = 'red'
PURPLE = 'purple'
MAROON = 'maroon'

color_to_emoji = {
    GREEN: '🟢',
    YELLOW: '🟡',
    ORANGE: '🟠',
    RED: '🔴',
    PURPLE: '🟣',
}


ALAMO_SQUARE = 65759
LYON_STREET = 17951
UPPER_HAIGHT = 17763
USF_STADIUM = 38725


# NOTE: USEPA conversion factor
# source: https://cfpub.epa.gov/si/si_public_record_report.cfm?dirEntryId=349513&Lab=CEMM
# RH = Relative Humidity
# PA(cf_1) = PurpleAir higher correction factor data averaged from the A and B channels
# PM2.5 (µg/m³) = 0.534 x PA(cf_1) - 0.0844 x RH + 5.604

SENSORS_NEAR_ME = [ALAMO_SQUARE, LYON_STREET, UPPER_HAIGHT, USF_STADIUM]

sensors = [Sensor(id) for id in SENSORS_NEAR_ME]

def get_color(aqi):
    if aqi <= 50:
        return GREEN
    if aqi <= 100:
        return YELLOW
    if aqi <= 150:
        return ORANGE
    if aqi <= 200:
        return RED
    if aqi <= 300:
        return PURPLE

    return MAROON

def get_aqi(sensor):
     pm2_5_cf_1 = statistics.mean([sensor.child.current_pm2_5_cf_1, sensor.parent.current_pm2_5_cf_1])
     relative_humidity = sensor.parent.current_humidity/100
     return 0.534*pm2_5_cf_1 - 0.0844 * relative_humidity + 5.604

sorted_sensors = sorted(sensors, key=lambda s: get_aqi(s))
average = statistics.mean([get_aqi(sensor) for sensor in sensors])
avg_color = get_color(average)

def get_text():
    formatted_average = '{:.2f}'.format(average)
    minimum = sorted_sensors[0]
    maximum = sorted_sensors[-1]
    formatted_min = '{:.2f}'.format(get_aqi(minimum))
    formatted_max = '{:.2f}'.format(get_aqi(maximum))

    message = (
        f"{color_to_emoji.get(avg_color)} Avg AQI: {formatted_average}\n\n"
        f"{color_to_emoji.get(get_color(get_aqi(minimum)))} Min AQI: {formatted_min} {minimum.parent_data.get('Label')}\n"
        f"{color_to_emoji.get(get_color(get_aqi(minimum)))} Max AQI: {formatted_max} {maximum.parent_data.get('Label')}\n"
    )

    return [
        message,
        f'{color_to_emoji.get(avg_color)} Purple Air update for {date.today().strftime("%B %d, %Y")}'
    ]

