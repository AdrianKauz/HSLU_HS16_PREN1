# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2016.11.23
# Version:    1.0
#------------------------------------------------------------------------------
# Usable test with the Sense Hat Gyro
#------------------------------------------------------------------------------


# Imports
from sense_hat import SenseHat
from time import sleep


# Global variables
sense = SenseHat()
ListGyroData = list()
ListAccData = list()
PointOfOriginGyro = [0.0] * 3

LIST_SIZE = 2
DIGITS = '0'
REFRESHRATE = 4.0  # Measures per second


# Functions
def getGyroData():
    curGyroData = sense.get_gyroscope()
    return [curGyroData.get('pitch'),
        curGyroData.get('roll'),
        curGyroData.get('yaw')]


def getAverage(newList):
    listSize = len(newList)
    tempValue = [0.0] * 3

    for item in newList:
        tempValue[0] = tempValue[0] + item[0]
        tempValue[1] = tempValue[1] + item[1]
        tempValue[2] = tempValue[2] + item[2]

    tempValue[0] = tempValue[0] / listSize
    tempValue[1] = tempValue[1] / listSize
    tempValue[2] = tempValue[2] / listSize

    return tempValue


# Main-Loop
try:
    sense.set_imu_config(False, True, True)

    while(1):
        #Gyrometer
        if len(ListGyroData) == LIST_SIZE:
            ListGyroData.pop(0)
            ListGyroData.append(getGyroData())

            averageGyroData = getAverage(ListGyroData)
            print("\033c")  # Clear Screen
            print("Gyrometer Data (" + str(REFRESHRATE) + " Measurements/sec)")
            print("--------------------------------------------------")
            print("Pitch:\t{0:.{digits}f}°".format(averageGyroData[0], digits=DIGITS))
            print("Roll:\t{0:.{digits}f}°".format(averageGyroData[1], digits=DIGITS))
            print("Yaw:\t{0:.{digits}f}°".format(averageGyroData[2], digits=DIGITS))

            #Use joystick for setting point of origin
            for event in sense.stick.get_events():
                if (event.action == 'pressed' and event.direction == 'middle'):
                    PointOfOriginGyro = averageGyroData
        else:
            ListGyroData.append(getGyroData())

        sleep(1.0 / REFRESHRATE)
except KeyboardInterrupt:
    pass