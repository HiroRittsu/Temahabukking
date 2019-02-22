#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import urllib.parse
import urllib.request

# weather's API
WEATHER_URL = "http://weather.livedoor.com/forecast/webservice/json/v1?city=%s"
CITY_CODE = "474020"  # TOKYO
TODAY = 0
TOMMOROW = 1


def get_weather_info():
    try:
        url = WEATHER_URL % CITY_CODE
        html = urllib.request.urlopen(url)
        html_json = json.loads(html.read().decode('utf-8'))
    except Exception as e:
        print("Exception Error: ", e)
        sys.exit(1)
    return html_json


def set_weather_info(weather_json, day):
    min_temperature = None
    max_temperature = None
    try:
        date = weather_json['forecasts'][day]['date']
        weather = weather_json['forecasts'][day]['telop']
        max_temperature = weather_json['forecasts'][day]['temperature']['max']['celsius']
        min_temperature = weather_json['forecasts'][day]['temperature']['min']['celsius']
    except TypeError:
        # temperature data is None etc...
        pass
    msg = [min_temperature, max_temperature]
    return msg


def main():
    weather_json = get_weather_info()
    for day in [TODAY, TOMMOROW]:
        msg = set_weather_info(weather_json, day)
        print(msg)


if __name__ == '__main__':
    main()
