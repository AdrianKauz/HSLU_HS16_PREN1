# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2017.03.03
# Version:    1.0
#------------------------------------------------------------------------------
# Short test with the PinOutput. Blink a LED
#------------------------------------------------------------------------------

# Imports
import RPi.GPIO as GPIO
import time

# Config Pinout
GPIO.setmode(GPIO.BOARD)    # Choose Board-Pinout
GPIO.setup(7, GPIO.OUT)     # Set GPIO Pin 7 as Output

# Main
try:
    while (1):
        GPIO.output(7, 1)
        time.sleep(0.5)
        GPIO.output(7, 0)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\033cGoodbye!\n")
    GPIO.output(7, 0)

except:
    print("\033cAaaaaaaaargh!\n")

    raise