# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2016.11.15
# Version:    1.0
#------------------------------------------------------------------------------
# Short test with the humidity and pressure sensors
#------------------------------------------------------------------------------

# Imports
from sense_hat import SenseHat
from time import sleep


#Global variables
sense = SenseHat()


# Use both sensors
while(1):
    humidity = sense.get_humidity()
    print("-----------------------------------------------------------------------")
    print("Humidity: %s %%rH" % humidity)

    temp = sense.get_temperature_from_humidity()
    print("Temperature (H): %s C" % temp)

    temp = sense.get_temperature_from_pressure()
    print("Temperature (P): %s C" % temp)

    press = sense.get_pressure()
    print("Pressure: %s Millibars" % press)
    print("-----------------------------------------------------------------------")
    sleep(0.125)
    print("\033c")