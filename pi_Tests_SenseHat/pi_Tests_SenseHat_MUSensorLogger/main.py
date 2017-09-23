# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2016.11.25
# Version:    1.0
#------------------------------------------------------------------------------
# Logging test with the Sense Hat Gyro
#------------------------------------------------------------------------------


# Imports
from sense_hat import SenseHat
from time import sleep
import logging


# Global variables
sense = SenseHat()

DIGITS = '0'
REFRESHRATE = 4.0  # Measures per second
MeasureIsRunning = False

# Main Loop
try:
    logger = logging.getLogger('myapp')
    hdlr = logging.FileHandler('/var/tmp/myapp.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)

    sense.set_imu_config(True, True, True)
    sense.set_pixel(0, 0, [255, 0, 0])

    while(MeasureIsRunning is False):
        # Use joystick for starting Measurement
        for event in sense.stick.get_events():
            if (event.action == 'pressed' and event.direction == 'middle'):
                MeasureIsRunning = True

    while(MeasureIsRunning is True):
        sense.set_pixel(0, 0, [0, 255, 0])
        dictValues = sense.get_gyroscope()
        strMessage = "Gyr:"
        strMessage += " Pitch: {0:.{digits}f}°".format(dictValues.get('pitch'), digits=DIGITS)
        strMessage += " Roll: {0:.{digits}f}°".format(dictValues.get('roll'), digits=DIGITS)
        strMessage += " Yaw: {0:.{digits}f}°".format(dictValues.get('yaw'), digits=DIGITS)

        logger.info(strMessage)
        print(strMessage)

        # Use joystick again for stopping Measurement
        for event in sense.stick.get_events():
            if (event.action == 'pressed' and event.direction == 'middle'):
                MeasureIsRunning = False

        sense.set_pixel(0, 0, [0, 0, 0])

        sleep(1.0 / REFRESHRATE)

except KeyboardInterrupt:
    print("Aaaaaargh!!!")
    sense.set_pixel(0, 0, [0, 0, 0])
    pass