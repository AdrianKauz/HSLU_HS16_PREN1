#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2016.11.30
# Version:    1.0
#------------------------------------------------------------------------------
# Sense Hat Logger
#------------------------------------------------------------------------------


# Imports
#------------------------------------------------------------------------------
from sense_hat import SenseHat
from Char.CharTools import CharTools
from time import sleep
from datetime import datetime


# Global Variables
#------------------------------------------------------------------------------
sense = SenseHat()
charTools = CharTools()

listGyrMeasurement = list()
listAccMeasurement = list()
listCompMeasurement = list()
fileGyro = None
fileAcc = None
fileComp = None
FILENAME_GYR = "_gyrometer.csv"
FILENAME_ACC = "_accelerometer.csv"
FILENAME_COMP = "_compass.csv"
DIGITS = 4
REFRESHRATE = 4.0  # Measures per second
PAUSE_BETWEEN_MEASUREMENT = 0.0
measureCounter = 0
measureIsRunning = False
displayBuffer = [[0, 0, 0]] * 64
toggleLights = False



# Functions
def joystickIsPressed(sAction, sDirection):
    for event in sense.stick.get_events():
        if (event.action == sAction and event.direction == sDirection):
            return True

    return False


def getGyroValues():
    sleep(PAUSE_BETWEEN_MEASUREMENT)
    dictValues = sense.get_gyroscope()
    sMeasure = datetime.now().strftime("(%Y.%m.%d - %H:%M:%S.%f)")
    sMeasure += ";{0:.{digits}f}".format(dictValues.get('pitch'), digits=DIGITS)
    sMeasure += ";{0:.{digits}f}".format(dictValues.get('roll'), digits=DIGITS)
    sMeasure += ";{0:.{digits}f}".format(dictValues.get('yaw'), digits=DIGITS)

    return sMeasure


def getAccValues():
    sleep(PAUSE_BETWEEN_MEASUREMENT)
    dictValues = sense.get_accelerometer_raw()
    sMeasure = datetime.now().strftime("(%Y.%m.%d - %H:%M:%S.%f)")
    sMeasure += ";{0:.{digits}f}".format(dictValues['x'], digits=DIGITS)
    sMeasure += ";{0:.{digits}f}".format(dictValues['y'], digits=DIGITS)
    sMeasure += ";{0:.{digits}f}".format(dictValues['z'], digits=DIGITS)

    return sMeasure


def getCompValues():
    sleep(PAUSE_BETWEEN_MEASUREMENT)


    sMeasure = datetime.now().strftime("(%Y.%m.%d - %H:%M:%S.%f)")
    sMeasure += ";" + str(sense.get_compass())

    return sMeasure


def drawCounter(bDrawBuffer):
    # Clear area
    charTools.setColor([0, 0, 0], [0, 0, 0])
    charTools.drawChar('!', displayBuffer)

    # Einerstelle
    charTools.setColor([0, 150, 255], [0, 0, 0])
    charTools.drawChar(str(measureCounter % 10), displayBuffer)

    # Zehnerstelle
    if(measureCounter > 9):
        charTools.drawPixel(1, str(8 - (measureCounter / 10) % 10), displayBuffer)

    if(bDrawBuffer):
        sense.set_pixels(displayBuffer)


def setLightSignal(sState):
    if sState == "Start":
        charTools.drawPixel(0, 0, displayBuffer, [255, 0, 0])
        charTools.drawPixel(0, 7, displayBuffer, [255, 0, 0])
        sense.set_pixels(displayBuffer)
        sleep(2)
        charTools.drawPixel(0, 0, displayBuffer, [255, 200, 0])
        charTools.drawPixel(0, 2, displayBuffer, [255, 200, 0])
        charTools.drawPixel(0, 5, displayBuffer, [255, 200, 0])
        charTools.drawPixel(0, 7, displayBuffer, [255, 200, 0])
        sense.set_pixels(displayBuffer)
        sleep(2)
        charTools.drawPixel(0, 0, displayBuffer, [66, 255, 0])
        charTools.drawPixel(0, 2, displayBuffer, [66, 255, 0])
        charTools.drawPixel(0, 3, displayBuffer, [66, 255, 0])
        charTools.drawPixel(0, 4, displayBuffer, [66, 255, 0])
        charTools.drawPixel(0, 5, displayBuffer, [66, 255, 0])
        charTools.drawPixel(0, 7, displayBuffer, [66, 255, 0])

    if sState == "Toggle":
        global toggleLights

        if toggleLights is True:
            charTools.drawPixel(0, 2, displayBuffer, [66, 255, 0])
            charTools.drawPixel(0, 3, displayBuffer, [66, 255, 0])
            charTools.drawPixel(0, 4, displayBuffer, [66, 255, 0])
            charTools.drawPixel(0, 5, displayBuffer, [66, 255, 0])

            toggleLights = False
        else:
            charTools.drawPixel(0, 2, displayBuffer, [0, 0, 0])
            charTools.drawPixel(0, 3, displayBuffer, [0, 0, 0])
            charTools.drawPixel(0, 4, displayBuffer, [0, 0, 0])
            charTools.drawPixel(0, 5, displayBuffer, [0, 0, 0])

            toggleLights = True

    if sState == "Stop":
        charTools.drawPixel(0, 0, displayBuffer, [0, 0, 0])
        charTools.drawPixel(0, 2, displayBuffer, [0, 0, 0])
        charTools.drawPixel(0, 3, displayBuffer, [0, 0, 0])
        charTools.drawPixel(0, 4, displayBuffer, [0, 0, 0])
        charTools.drawPixel(0, 5, displayBuffer, [0, 0, 0])
        charTools.drawPixel(0, 7, displayBuffer, [0, 0, 0])

    sense.set_pixels(displayBuffer)
# Main
try:
    sense.set_rotation(90)
    drawCounter(True)

    while(1):
        if measureIsRunning is False:
            # Use joystick for starting measurement
            if joystickIsPressed("pressed", "middle"):
                measureIsRunning = True
        else:
            oToday = datetime.now()
            measureCounter = measureCounter + 1
            drawCounter(True)
            setLightSignal("Start")

            # Gyro part
            fileGyro = open(oToday.strftime("(%Y-%m-%dT%H%M%S)") + "_{:03d}".format(measureCounter) + FILENAME_GYR, 'a')
            listGyrMeasurement.append("Gyro Measurement " + "Nr.{:03d} ".format(measureCounter)  + oToday.strftime("(%Y.%m.%d - %H:%M:%S)" + ";;;"))
            listGyrMeasurement.append("\n;;;")
            listGyrMeasurement.append("\nDate;Pitch;Roll;Yaw")

            # Acc part
            fileAcc = open(oToday.strftime("(%Y-%m-%dT%H%M%S)") + "_{:03d}".format(measureCounter) + FILENAME_ACC, 'a')
            listAccMeasurement.append("Accelerator Measurement " + "Nr.{:03d} ".format(measureCounter)  + oToday.strftime("(%Y.%m.%d - %H:%M:%S)" + ";;;"))
            listAccMeasurement.append("\n;;;")
            listAccMeasurement.append("\nDate;X;Y;Z")

            # Comp part
            fileComp = open(oToday.strftime("(%Y-%m-%dT%H%M%S)") + "_{:03d}".format(measureCounter) + FILENAME_COMP, 'a')
            listCompMeasurement.append("Compass Measurement " + "Nr.{:03d} ".format(measureCounter)  + oToday.strftime("(%Y.%m.%d - %H:%M:%S)" + ";"))
            listCompMeasurement.append("\n;;;")
            listCompMeasurement.append("\nDate;North-Position")

            # Starte Mess-Loop
            print("Starting measurement Nr.{:03d} ".format(measureCounter))
            while(measureIsRunning):
                # Starting measurement
                listGyrMeasurement.append("\n" + getGyroValues())
                listAccMeasurement.append("\n" + getAccValues())
                listCompMeasurement.append("\n" + getCompValues())
                setLightSignal("Toggle")

                # Use joystick for stopping measurement
                if joystickIsPressed("pressed", "middle"):
                    print("Stopping measurement Nr.{:03d} ".format(measureCounter))
                    measureIsRunning = False

                    # Gyro part
                    fileGyro.writelines(listGyrMeasurement)
                    fileGyro.close()
                    listGyrMeasurement = list()

                    # Acc part
                    fileAcc.writelines(listAccMeasurement)
                    fileAcc.close()
                    listAccMeasurement = list()

                    # Comp part
                    fileComp.writelines(listCompMeasurement)
                    fileComp.close()
                    listCompMeasurement = list()

                    setLightSignal("Stop")

                sleep(1.0 / REFRESHRATE)

        # Avoid high CPU usage
        sleep(0.0625)
except KeyboardInterrupt:
    print("\033c")
    print("Goodbye!")
    sense.clear()
except:
    print("\033c")
    print("Aaaaaargh!")
    sense.clear(255, 0, 0)
    sleep(0.5)
    sense.clear(0, 0, 0)
    sleep(0.5)
    sense.clear(255, 0, 0)
    sleep(0.5)
    sense.clear(0, 0, 0)
    raise





