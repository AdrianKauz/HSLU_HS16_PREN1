#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2017.03.04
# Version:    1.0
#------------------------------------------------------------------------------
# Short test with the PIGPIO PWM-Output
# PIGPIO is pre-installed with Raspian!
# Start PIGPIO-Daemon with "sudo pigpiod".
# The python-module connects to the daemon and let you use the GPIOs of the Pi.
#
# Documentary: http://abyz.co.uk/rpi/pigpio/python.html
#
# Features
# -----------------------------------------------------------------------------
# - the pigpio Python module can run on Windows, Macs, or Linux
# - controls one or more Pi's
# - hardware timed PWM on any of GPIO 0-31
# - hardware timed servo pulses on any of GPIO 0-31
# - callbacks when any of GPIO 0-31 change state
# - creating and transmitting precisely timed waveforms
# - reading/writing GPIO and setting their modes
# - wrappers for I2C, SPI, and serial links
# - creating and running scripts on the pigpio daemon
#------------------------------------------------------------------------------

# Imports
import pigpio
import time

# Initialize
pi = pigpio.pi()  # Connect to local Pi

# Set GPIO modes
pi.set_mode(4, pigpio.OUTPUT)

# Main
try:
    print(pi.get_pigpio_version())
    pi.set_PWM_frequency(4, 10000)
    pi.set_PWM_dutycycle(4, 20)

    while (1):
        pass  # Do nothing

except KeyboardInterrupt:
    pi.set_PWM_dutycycle(4, 0)
    pi.stop()
    print("\033cGoodbye!\n")

except:
    pi.set_PWM_dutycycle(4, 0)
    pi.stop()
    print("\033cAaaaaaaaargh!\n")

    raise