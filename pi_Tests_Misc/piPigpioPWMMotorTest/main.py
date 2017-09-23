#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2017.03.15
# Version:    0.5
#------------------------------------------------------------------------------
# Short test with the PIGPIO-Daemon, DMA-PWM-Output
# This little script will change the PWM-Frequency like a sinus-loop to test,
# how the motors of "Heiri" react to this change.
# Note for me: Läuft so halbbatzig, aber hauptsache es funzt
#
# Used Pins:
# PWM 1     = BCM  4 (Pin  7)
# PWM 2     = BCM 17 (Pin 11)
# GND       = GND    (Pin  6)
#------------------------------------------------------------------------------

# Imports
import pigpio
import time
import math
import sys

# Variables
BCM_PWM1 = 4
BCM_PWM2 = 17
CLEAR_TERMINAL = "\033c"
DEFAULT_DUTYCYCLE = 128 # 50%
DEFAULT_FREQUENCY = 500
DEFAULT_MIN_PWM_FREQUENCY = 0
DEFAULT_MAX_PWM_FREQUENCY = 1000
DEFAULT_OFFSET = 1
DEFAULT_PERIODE_IN_SECONDS = 2.0
DEFAULT_STEPS_PER_PERIODE = 10.0

# Initialize
pi = pigpio.pi()  # Connect to local Pi

# Main
try:
    deltaFreq = 0
    counter = 0.0
    step = 1.0 / (DEFAULT_STEPS_PER_PERIODE * DEFAULT_PERIODE_IN_SECONDS)
    currValue = 0

    print(str(step))

    pi.set_PWM_frequency(BCM_PWM1, DEFAULT_FREQUENCY)
    pi.set_PWM_frequency(BCM_PWM2, DEFAULT_FREQUENCY)
    pi.set_PWM_dutycycle(BCM_PWM1, DEFAULT_DUTYCYCLE)
    pi.set_PWM_dutycycle(BCM_PWM2, DEFAULT_DUTYCYCLE)

    # Define range of frequency
    if(len(sys.argv) == 0):
        deltaFreq = int(sys.argv[1]) - int(sys.argv[0])
    else:
        deltaFreq = DEFAULT_MAX_PWM_FREQUENCY - DEFAULT_MIN_PWM_FREQUENCY

    while(1):
        currValue = deltaFreq/2 - int(deltaFreq/2 * math.sin(math.pi * counter))

        if(currValue < 0):
            currValue = 0

        pi.set_PWM_frequency(BCM_PWM1, currValue)
        print(str(currValue) + ", " + str(pi.get_PWM_frequency(BCM_PWM1)))
        counter = counter + step

        # Safety
        time.sleep(1.0 / DEFAULT_STEPS_PER_PERIODE)

except KeyboardInterrupt:
    pi.set_PWM_dutycycle(BCM_PWM1, 0)
    pi.set_PWM_dutycycle(BCM_PWM2, 0)
    pi.stop()
    #print(CLEAR_TERMINAL + "Goodbye!\n")

except:
    pi.set_PWM_dutycycle(BCM_PWM1, 0)
    pi.set_PWM_dutycycle(BCM_PWM2, 0)
    pi.stop()
    print(CLEAR_TERMINAL + "Aaaaaaaaargh!\n")

    raise

