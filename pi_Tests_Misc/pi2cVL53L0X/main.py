#!/usr/bin/python

# MIT License
#
# Copyright (c) 2017 John Bryan Moore
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



# Notes: GPIO 23, 24, 25, 26, 27

# Back Left = GPIO23 (Pin 16)
# Front Left = GPIO24 (Pin 18)
# Front = GPIO25 (Pin 22)
# Front Right = GPIO26 (Pin 37)
# Back Right = GPIO27 (Pin 13)

# ------------------------------------------------------------------------------
# VL53L0X-Test for PREN1

import time
from modules import VL53L0X
import RPi.GPIO as GPIO

# Create a VL53L0X object
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

GPIO.output(22, GPIO.LOW)
GPIO.output(21, GPIO.LOW)
GPIO.output(27, GPIO.LOW)

# Reset
time.sleep(0.5)

# Nr 1
GPIO.output(22, GPIO.HIGH)
tof1 = VL53L0X.VL53L0X(address=0x30)
tof1.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
time.sleep(1)
# Nr 2
GPIO.output(21, GPIO.HIGH)
tof2 = VL53L0X.VL53L0X(address=0x31)
tof2.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
time.sleep(1)

# Nr 3
GPIO.output(27, GPIO.HIGH)
tof3 = VL53L0X.VL53L0X(address=0x32)
tof3.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
time.sleep(1)

timing1 = tof1.get_timing()
timing2 = tof2.get_timing()
timing3 = tof3.get_timing()
print("Timing Sensor 1: " + str(timing1))
print("Timing Sensor 2: " + str(timing2))
print("Timing Sensor 3: " + str(timing3))
print("\n--------------------------------------\n")

for count in range(1,20):
    distance1 = tof1.get_distance()
    distance2 = tof2.get_distance()
    distance3 = tof3.get_distance()

    print("S1: {:4d}mm, S2: {:4d}mm, S3: {:4d}mm, {:3d}".format(distance1, distance2, distance3, count))
    time.sleep(0.1)

    """
    print("S1: %d mm, S2: %d mm, S1: %d mm, %d" % (distance1, (distance1 / 10), count))


    if (distance1 > 0):
        print ("Sensor 1: %d mm, %d cm, %d" % (distance1, (distance1 / 10), count))

    distance2 = tof2.get_distance()
    if (distance2 > 0):
        print ("Sensor 2: %d mm, %d cm, %d" % (distance2, (distance2 / 10), count))

    distance3 = tof3.get_distance()
    if (distance3 > 0):
        print ("Sensor 3: %d mm, %d cm, %d" % (distance3, (distance3 / 10), count))
    """

tof1.stop_ranging()
tof2.stop_ranging()
tof3.stop_ranging()

GPIO.output(22, GPIO.LOW)
GPIO.output(21, GPIO.LOW)
GPIO.output(27, GPIO.LOW)


"""
if (timing < 20000):
    timing = 20000
print ("Timing %d ms" % (timing/1000))

for count in range(1,101):
    distance = tof.get_distance()
    if (distance > 0):
        print ("%d mm, %d cm, %d" % (distance, (distance/10), count))

    time.sleep(timing/1000000.00)

tof.stop_ranging()

"""