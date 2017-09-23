# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2016.11.1
# Version:    1.0
#------------------------------------------------------------------------------
# Short test with the Sense Hat Compass
#------------------------------------------------------------------------------


# Imports
from sense_hat import SenseHat
from time import sleep


#Global Variables
sense = SenseHat()


#Use compass
while(1):
    north = sense.get_compass()
    print("North: %s" % north)
    sleep(0.125)
    print("\033c")