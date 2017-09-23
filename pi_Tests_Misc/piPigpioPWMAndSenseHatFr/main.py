#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2017.03.10
# Version:    0.8
#------------------------------------------------------------------------------
# Short test with the PIGPIO-Daemon, DMA-PWM-Output and SenseHat Devices
# Everything works on its own, but we need to test it, how they work at the
# same time on the Rasp.
#
# The user can manipulate the PWM-Output with the direction of the
# sense-hat's joystick. The actual frequency level (0-800) wil be shown on
# the RGB-Display of the sense-hat.
#
# Used Pins:
# PWM 1     = BCM  4 (Pin 7)
# PWM 2     = BCM 17 (Pin 11)
# Sense Hat = BCM 23 (Pin 16)
#             BCM 24 (Pin 18)
#             BCM 25 (Pin 22)
#             BCM  8 (Pin 24)
#------------------------------------------------------------------------------

# Imports
from sense_hat import SenseHat
from Display.DisplayTools import DisplayTools
import pigpio
import time

# Variables
BCM_PWM1 = 4
BCM_PWM2 = 17
PWM_FRQ_START_VALUE = 400
PWM_DUTYCYCLE = 127 # Dutycycle in %
FRQ_MIN = 0
FRQ_MAX = 800
FRQ_STEP_SMALL = 1
FRQ_STEP_BIG = 10
pwm_isActive = False
displayTools = DisplayTools()
displayBuffer = [[0, 0, 0]] * 64
currentPWM1Freq = PWM_FRQ_START_VALUE
currentPWM2Freq = PWM_FRQ_START_VALUE

# Initialize
sense = SenseHat()
pi = pigpio.pi()  # Connect to local Pi

# Set GPIO modes
pi.set_mode(4, pigpio.OUTPUT)
pi.set_mode(17, pigpio.OUTPUT)

# Functions
def get_Pressed_Joystick_Direction():
    for event in sense.stick.get_events():
        if(event.action == "pressed"):
            return event.direction

    return


def inc_Frequency(iBCMNumber):
    currentFrequency = 0

    if (iBCMNumber == BCM_PWM1):
        currentFrequency = currentPWM1Freq
    else:
        currentFrequency = currentPWM2Freq

    if (currentFrequency < 20):
        set_Frequency(iBCMNumber, currentFrequency, FRQ_STEP_SMALL)
    else:
        set_Frequency(iBCMNumber, currentFrequency, FRQ_STEP_BIG)

    return


def dec_Frequency(iBCMNumber):
    currentFrequency = 0

    if (iBCMNumber == BCM_PWM1):
        currentFrequency = currentPWM1Freq
    else:
        currentFrequency = currentPWM2Freq

    if currentFrequency < 20:
        set_Frequency(iBCMNumber, currentFrequency, 0 - FRQ_STEP_SMALL)
    else:
        set_Frequency(iBCMNumber, currentFrequency, 0 - FRQ_STEP_BIG)

    return


def set_Frequency(iBCMNumber, currentFrequency, iDelta):

    # Down
    if (iDelta < 0) and (currentFrequency > FRQ_MIN):
        pi.set_PWM_frequency(iBCMNumber, currentFrequency + iDelta)

        if (iBCMNumber == BCM_PWM1):
            global currentPWM1Freq
            currentPWM1Freq = currentFrequency + iDelta
        else:
            global currentPWM2Freq
            currentPWM2Freq = currentFrequency + iDelta

    # Up
    if (iDelta > 0) and (currentFrequency < FRQ_MAX):
        pi.set_PWM_frequency(iBCMNumber, currentFrequency + iDelta)

        if (iBCMNumber == BCM_PWM1):
            global currentPWM1Freq
            currentPWM1Freq = currentFrequency + iDelta
        else:
            global currentPWM2Freq
            currentPWM2Freq = currentFrequency + iDelta

    #print(str(currentFrequency + iDelta))
    print(currentPWM1Freq)
    print(currentPWM2Freq)

    return


# Main
try:
    pi.set_PWM_frequency(BCM_PWM1, currentPWM1Freq)
    pi.set_PWM_frequency(BCM_PWM2, currentPWM2Freq)
    pi.set_PWM_dutycycle(BCM_PWM1, PWM_DUTYCYCLE)
    pi.set_PWM_dutycycle(BCM_PWM2, PWM_DUTYCYCLE)
    displayTools.initBar(displayBuffer)
    sense.set_pixels(displayBuffer)

    while (1):
        current_Joystick_Direction = get_Pressed_Joystick_Direction()

        if pwm_isActive:
            # Set PWM 1
            if (current_Joystick_Direction == "left") or (current_Joystick_Direction == "right"):
                if current_Joystick_Direction == "left":
                    dec_Frequency(BCM_PWM1)

                if current_Joystick_Direction == "right":
                    inc_Frequency(BCM_PWM1)

                #displayTools.drawBar(1, pi.get_PWM_frequency(BCM_PWM1), displayBuffer)
                sense.set_pixels(displayBuffer)

            # Set PWM 2
            if (current_Joystick_Direction == "down") or (current_Joystick_Direction == "up"):
                if current_Joystick_Direction == "down":
                    dec_Frequency(BCM_PWM2)

                if current_Joystick_Direction == "up":
                    inc_Frequency(BCM_PWM2)

                #displayTools.drawBar(2, pi.get_PWM_frequency(BCM_PWM2), displayBuffer)
                sense.set_pixels(displayBuffer)

            if current_Joystick_Direction == "middle":
                pi.set_PWM_dutycycle(BCM_PWM1, 0)
                pi.set_PWM_dutycycle(BCM_PWM2, 0)

                #displayTools.drawBar(1, 0, displayBuffer)
                #displayTools.drawBar(2, 0, displayBuffer)
                sense.set_pixels(displayBuffer)

                pwm_isActive = False
        else:
            if current_Joystick_Direction == "middle":
                currentPWM1Freq = PWM_FRQ_START_VALUE
                currentPWM2Freq = PWM_FRQ_START_VALUE
                pi.set_PWM_frequency(BCM_PWM1, currentPWM1Freq)
                pi.set_PWM_frequency(BCM_PWM2, currentPWM2Freq)
                pi.set_PWM_dutycycle(BCM_PWM1, PWM_DUTYCYCLE)
                pi.set_PWM_dutycycle(BCM_PWM2, PWM_DUTYCYCLE)

                #displayTools.drawBar(1, PWM_FRQ_START_VALUE, displayBuffer)
                #displayTools.drawBar(2, PWM_FRQ_START_VALUE, displayBuffer)
                sense.set_pixels(displayBuffer)

                pwm_isActive = True

        time.sleep(0.25)
        pass  # Do nothing

except KeyboardInterrupt:
    pi.set_PWM_dutycycle(BCM_PWM1, 0)
    pi.set_PWM_dutycycle(BCM_PWM2, 0)
    pi.stop()
    sense.clear(0, 0, 0)
    print("\033cGoodbye!\n")

except:
    pi.set_PWM_dutycycle(BCM_PWM1, 0)
    pi.set_PWM_dutycycle(BCM_PWM2, 0)
    pi.stop()
    sense.clear(0, 0, 0)
    print("\033cAaaaaaaaargh!\n")

    raise
