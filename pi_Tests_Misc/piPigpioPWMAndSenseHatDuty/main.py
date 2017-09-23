#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2017.03.07
# Version:    1.0
#------------------------------------------------------------------------------
# Short test with the PIGPIO-Daemon, DMA-PWM-Output and SenseHat Devices
# Everything works on its own, but we need to test it, how they work at the
# same time on the Rasp.
#
# The user can manipulate the PWM-Output with the direction of the
# sense-hat's joystick. The actual level (0-255) wil be shown on
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
PWM_FREQUENCY = 10000
PWM_DUTYCYCLE_STARTVALUE = 50
PWM_STEP_DOWN_DUTYCYCLE = -5  # Steps in %
PWM_STEP_UP_DUTYCYCLE = 5  # Steps in %
pwm_isActive = False
displayTools = DisplayTools()
displayBuffer = [[0, 0, 0]] * 64

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

def set_Dutycycle(iBCMNumber, iDelta):
    currentDutycycle = pi.get_PWM_dutycycle(iBCMNumber)

    # Down
    if (iDelta < 0) and (currentDutycycle > 0):
        pi.set_PWM_dutycycle(iBCMNumber, currentDutycycle + iDelta)
        print(str(currentDutycycle + iDelta))

    # Up
    if (iDelta > 0) and (currentDutycycle < 100):
        pi.set_PWM_dutycycle(iBCMNumber, currentDutycycle + iDelta)
        print(str(currentDutycycle + iDelta))

    return

# Main
try:
    pi.set_PWM_frequency(BCM_PWM1, PWM_FREQUENCY)
    pi.set_PWM_frequency(BCM_PWM2, PWM_FREQUENCY)
    pi.set_PWM_dutycycle(BCM_PWM1, 0)
    pi.set_PWM_dutycycle(BCM_PWM2, 0)
    displayTools.initBar(displayBuffer)
    sense.set_pixels(displayBuffer)

    while (1):
        current_Joystick_Direction = get_Pressed_Joystick_Direction()

        if pwm_isActive:
            # Set PWM 1
            if (current_Joystick_Direction == "left") or (current_Joystick_Direction == "right"):
                if current_Joystick_Direction == "left":
                    set_Dutycycle(BCM_PWM1, PWM_STEP_DOWN_DUTYCYCLE)

                if current_Joystick_Direction == "right":
                    set_Dutycycle(BCM_PWM1, PWM_STEP_UP_DUTYCYCLE)

                displayTools.drawBar(1, pi.get_PWM_dutycycle(BCM_PWM1), displayBuffer)
                sense.set_pixels(displayBuffer)

            # Set PWM 2
            if (current_Joystick_Direction == "down") or (current_Joystick_Direction == "up"):
                if current_Joystick_Direction == "down":
                    set_Dutycycle(BCM_PWM2, PWM_STEP_DOWN_DUTYCYCLE)

                if current_Joystick_Direction == "up":
                    set_Dutycycle(BCM_PWM2, PWM_STEP_UP_DUTYCYCLE)

                displayTools.drawBar(2, pi.get_PWM_dutycycle(BCM_PWM2), displayBuffer)
                sense.set_pixels(displayBuffer)

            if current_Joystick_Direction == "middle":
                pi.set_PWM_dutycycle(BCM_PWM1, 0)
                pi.set_PWM_dutycycle(BCM_PWM2, 0)

                displayTools.drawBar(1, 0, displayBuffer)
                displayTools.drawBar(2, 0, displayBuffer)
                sense.set_pixels(displayBuffer)

                pwm_isActive = False
        else:
            if current_Joystick_Direction == "middle":
                pi.set_PWM_dutycycle(BCM_PWM1, PWM_DUTYCYCLE_STARTVALUE)
                pi.set_PWM_dutycycle(BCM_PWM2, PWM_DUTYCYCLE_STARTVALUE)

                displayTools.drawBar(1, PWM_DUTYCYCLE_STARTVALUE, displayBuffer)
                displayTools.drawBar(2, PWM_DUTYCYCLE_STARTVALUE, displayBuffer)
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
