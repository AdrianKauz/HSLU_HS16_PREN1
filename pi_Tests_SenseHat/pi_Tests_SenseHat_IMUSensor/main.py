# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2016.11.15
# Version:    1.0
#------------------------------------------------------------------------------
# Short test with the Sense Hat Gyro
#------------------------------------------------------------------------------


# Imports
from sense_hat import SenseHat
from time import sleep

selectedSensor = "Gyro"


# Global variables
sense = SenseHat()


while(1):
    if selectedSensor == "Gyro":
        gyro_only = sense.get_gyroscope()
        print(" (G) p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))

    if selectedSensor == "Accelerator":
        acc_only = sense.get_accelerometer()
        print(" (A) p: {pitch}, r: {roll}, y: {yaw}".format(**acc_only))

    sleep(0.125)
    print("\033c")