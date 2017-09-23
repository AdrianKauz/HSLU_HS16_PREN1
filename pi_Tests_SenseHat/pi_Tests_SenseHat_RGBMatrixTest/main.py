# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2016.11.15
# Version:    1.0
#------------------------------------------------------------------------------
# Short test with the Sense Hat RGB-Display and Chars
#------------------------------------------------------------------------------


# Imports
from sense_hat import SenseHat
from Char.CharTools import CharTools
import time


# Global Variables
sense = SenseHat()
tools = CharTools()

Red = [255, 0, 0]      # Red
Yellow = [255, 255, 0]  # Yellow
Cyan = [112, 146, 190]  # Cyan
White = [10, 10, 10]  # White
Black = [0, 0, 0]        # Black


# Code
tools.setColor(Cyan, Black)
sense.set_pixels(tools.getChar('A'))
time.sleep(1)
sense.set_pixels(tools.getChar('B'))
time.sleep(1)
sense.set_pixels(tools.getChar('C'))
time.sleep(1)
sense.set_pixels(tools.getChar('D'))
time.sleep(1)
sense.set_pixels(tools.getChar('E'))
time.sleep(1)
sense.clear()
