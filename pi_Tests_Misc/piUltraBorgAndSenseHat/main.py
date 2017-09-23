#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2017.03.08
# Version:    1.0
#------------------------------------------------------------------------------
# Short test with the UltraBorg-Module, DMA-PWM-Output and SenseHat Devices
# Everything works on its own, but we need to test it, how they work at the
# same time on the Rasp.
#
# The user can manipulate the PWM-Output with the direction of the
# sense-hat's joystick. The actual level (-1..0..1) wil be shown on
# the RGB-Display of the sense-hat.
# From an example of "https://www.piborg.org/ultraborg/examples":
#           --> 0 is central, -1 is maximum left, +1 is maximum right
#
# Used Pins:
# ---------------------------------------
# UltraBorg = 3.3V   (Pin  1)
#             BCM  2 (Pin  3) -> I2C1_SDA
#             BCM  5 (Pin  5) -> I2C1_SCL
#             5.0V   (Pin  2)
#             5.0V   (Pin  4)
#             GND    (Pin  6)
# Sense Hat = BCM 23 (Pin 16)
#             BCM 24 (Pin 18)
#             BCM 25 (Pin 22)
#             BCM  8 (Pin 24)
#------------------------------------------------------------------------------

# Imports
from sense_hat import SenseHat
from UltraBorg import UltraBorg
from Display.DisplayTools import DisplayTools
import time

# Variables
BCM_PWM1 = 4
BCM_PWM2 = 17
PWM_FREQUENCY = 10000
PWM_DUTYCYCLE_STARTVALUE = 0.0
PWM_STEP_DOWN_DUTYCYCLE = -0.10  # Steps
PWM_STEP_UP_DUTYCYCLE = 0.10  # Steps
pwm_isActive = False
displayTools = DisplayTools()
displayBuffer = [[0, 0, 0]] * 64

# Initialize
sense = SenseHat()
UB1 = UltraBorg.UltraBorg()
UB1.i2cAddress = 0x36
UB1.Init()

# Functions
def get_Pressed_Joystick_Direction():
    for event in sense.stick.get_events():
        if(event.action == "pressed"):
            return event.direction

    return

def set_Dutycycle(iBCMNumber, fDelta):
    if iBCMNumber == 1:
        currentDutycycle = UB1.GetServoPosition1()
        newDutycycle = round(currentDutycycle + fDelta, 2)

        # Down
        if (fDelta < 0) and (currentDutycycle > -1.0):
            UB1.SetServoPosition1(newDutycycle)
            print("PWM 1: " + str(newDutycycle))

        # Up
        if (fDelta > 0) and (currentDutycycle < 1.0):
            UB1.SetServoPosition1(newDutycycle)
            print("PWM 1: " + str(newDutycycle))

    if iBCMNumber == 2:
        currentDutycycle = UB1.GetServoPosition2()
        newDutycycle = round(currentDutycycle + fDelta, 2)

        # Down
        if (fDelta < 0) and (currentDutycycle > -1.0):
            UB1.SetServoPosition2(newDutycycle)
            print("PWM 2: " + str(newDutycycle))

        # Up
        if (fDelta > 0) and (currentDutycycle < 1.0):
            UB1.SetServoPosition2(newDutycycle)
            print("PWM 2: " + str(newDutycycle))

    return

# Main
try:
    UB1.SetServoPosition1(PWM_DUTYCYCLE_STARTVALUE)
    UB1.SetServoPosition2(PWM_DUTYCYCLE_STARTVALUE)

    displayTools.initBar(displayBuffer)
    sense.set_pixels(displayBuffer)

    while (1):
        current_Joystick_Direction = get_Pressed_Joystick_Direction()

        if pwm_isActive:
            # Set PWM 1
            if (current_Joystick_Direction == "left") or (current_Joystick_Direction == "right"):
                if current_Joystick_Direction == "left":
                    set_Dutycycle(1, PWM_STEP_DOWN_DUTYCYCLE)

                if current_Joystick_Direction == "right":
                    set_Dutycycle(1, PWM_STEP_UP_DUTYCYCLE)

                displayTools.drawBar(1, UB1.GetServoPosition1(), displayBuffer)
                sense.set_pixels(displayBuffer)

            # Set PWM 2
            if (current_Joystick_Direction == "down") or (current_Joystick_Direction == "up"):
                if current_Joystick_Direction == "down":
                    set_Dutycycle(2, PWM_STEP_DOWN_DUTYCYCLE)

                if current_Joystick_Direction == "up":
                    set_Dutycycle(2, PWM_STEP_UP_DUTYCYCLE)

                displayTools.drawBar(2, UB1.GetServoPosition2(), displayBuffer)
                sense.set_pixels(displayBuffer)

            if current_Joystick_Direction == "middle":
                UB1.SetServoPosition1(PWM_DUTYCYCLE_STARTVALUE)
                UB1.SetServoPosition2(PWM_DUTYCYCLE_STARTVALUE)

                displayTools.drawBar(1, 0, displayBuffer)
                displayTools.drawBar(2, 0, displayBuffer)
                sense.set_pixels(displayBuffer)

                pwm_isActive = False
        else:
            if current_Joystick_Direction == "middle":
                displayTools.drawBar(1, PWM_DUTYCYCLE_STARTVALUE, displayBuffer)
                displayTools.drawBar(2, PWM_DUTYCYCLE_STARTVALUE, displayBuffer)
                sense.set_pixels(displayBuffer)

                pwm_isActive = True

        time.sleep(0.25)
        pass  # Do nothing

except KeyboardInterrupt:
    sense.clear(0, 0, 0)
    print("\033cGoodbye!\n")

except:
    sense.clear(0, 0, 0)
    print("\033cAaaaaaaaargh!\n")

    raise
