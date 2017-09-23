#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2016.12.08
# Version:    1.0
#------------------------------------------------------------------------------
# Ultrasonic distance test with UltraBorg-Module
#------------------------------------------------------------------------------

# Imports
import sys
import time
from datetime import datetime
from Modules import UltraBorg

# Use Board 1
UB1 = UltraBorg.UltraBorg()
UB1.i2cAddress = 0x36
UB1.Init()

# Main
distance = int(sys.argv[1])
measuringTime = (sys.argv[2])
endTime = long(round(time.time() * 1000)) + long(sys.argv[2]) * 60000
doLoop = True
oFile = open(datetime.now().strftime("(%Y-%m-%dT%H%M%S)") + "_distance_" + str(distance) + "_measuringTime_" + str(measuringTime) + ".csv",'a')
listMeasurements = list()

listMeasurements.append("Time;Distance\n")

while(doLoop):
    currTime = long(round(time.time() * 1000))
    sEntry = str(round(time.time() * 1000)) + ";" + str(UB1.GetDistance1())

    print("\033c")
    print(sEntry)

    listMeasurements.append("\n" + sEntry)

    if(endTime < currTime):
        doLoop = False
        oFile.writelines(listMeasurements)
        oFile.close()

    time.sleep(1)