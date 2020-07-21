# -*- coding: utf-8 -*-
import json
from bme280 import Bme280

sensor = Bme280()

#print("pressure    : %7.2f hPa" % sensor.getPressure())
#print("temperature : %-6.2f ℃" % sensor.getTemperature())
#print("humidity    : %6.2f ％" % sensor.getHumidity())


returned_dict = {
    "temperature": "{0:0.2f}".format(sensor.getTemperature()),
    "pressure": "{0:0.2f}".format(sensor.getPressure()),
    "humidity": "{0:0.2f}".format(sensor.getHumidity())
}

print(json.dumps(returned_dict))
