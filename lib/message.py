import statistics
from lib import aqi
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


def get_text(sorted_sensors):
    average = statistics.mean([sensor.aqi for sensor in sorted_sensors])
    avg_color = get_color(average)

    formatted_average = '{:.2f}'.format(average)
    minimum = sorted_sensors[0]
    maximum = sorted_sensors[-1]
    formatted_min = '{:.2f}'.format(minimum.aqi)
    formatted_max = '{:.2f}'.format(maximum.aqi)

    message = (
        f"{color_to_emoji.get(avg_color)} Avg AQI: {formatted_average}\n\n"
        f"{color_to_emoji.get(get_color(minimum.aqi))} Min AQI: {formatted_min} {minimum.name}\n"
        f"{color_to_emoji.get(get_color(maximum.aqi))} Max AQI: {formatted_max} {maximum.name}\n"
    )

    return [
        message,
        f'{color_to_emoji.get(avg_color)} Purple Air update for {date.today().strftime("%B %d, %Y")}'
    ]

