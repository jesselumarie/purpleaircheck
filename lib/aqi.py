import statistics

ranges = {
    (0, 12.0) : (0.0, 50),
    (12.1, 35.4): (51.0, 100.0),
    (35.5, 55.4): (101.0,150.0),
    (55.5, 150.4): (151.0,200.0),
    (150.5, 250.4): (201.0, 300.0),
    (250.5, 350.4): (301.0, 400.0),
    (350.5, 500.4): (401.0, 500.0)
}

def calc(actual):
    for range_min, range_max in ranges.keys():
        if actual >= range_min and actual<=range_max:
            where_in_range = (actual-range_min)/(range_max-range_min)
            [minaqi, maxaqi] = ranges[(range_min, range_max)]

            return (maxaqi-minaqi) * (where_in_range) + minaqi

    return 0

def get_aqi(sensor):
    # NOTE: USEPA conversion factor
    # source: https://cfpub.epa.gov/si/si_public_record_report.cfm?dirEntryId=349513&Lab=CEMM
    # RH = Relative Humidity
    # PA(cf_1) = PurpleAir higher correction factor data averaged from the A and B channels
    # PM2.5 (µg/m³) = 0.534 x PA(cf_1) - 0.0844 x RH + 5.604

    mean_pm2_5_cf_1 = statistics.mean([sensor.child.current_pm2_5_cf_1, sensor.parent.current_pm2_5_cf_1])
    relative_humidity = sensor.parent.current_humidity/100.0
    converted_pm2_5_cf_1 =  0.534*mean_pm2_5_cf_1 - 0.0844 * relative_humidity + 5.604
    print(sensor.parent.name)
    print(mean_pm2_5_cf_1)
    print('regular aqi', calc(mean_pm2_5_cf_1))
    print(converted_pm2_5_cf_1)
    print('converted aqi', calc(converted_pm2_5_cf_1))

    return calc(converted_pm2_5_cf_1)
