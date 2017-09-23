# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2016.11.30
# Version:    1.0
#------------------------------------------------------------------------------
# Char Tools for the Sense Hat 8x8 RGB-Display
# With Quick and Dirty Changes :-P
#------------------------------------------------------------------------------


#Imports
from Charset import getCharCode


#Class
class CharTools:
    #Konstruktor
    def __init__(self):
        self.ForeColor = [0, 0, 0]
        self.BackColor = [0, 0, 0]

    # Funktions
    def drawChar(self, newChar, listBuffer):
        charCode = getCharCode(newChar)
        charCodePosition = 0

        for x in range(0, 64):  # From 0 to 63
            if charCodePosition < len(charCode):
                if charCode[charCodePosition] == x:
                    listBuffer[x] = self.ForeColor
                    charCodePosition = charCodePosition + 1

    def drawPixel(self, xPosition, yPosition, listBuffer, newColor=None):
        currentPositionY = -1
        currentPositionX = 0

        for x in range(0, 64):  # From 0 to 63
            if x % 8 == 0:
                currentPositionY = currentPositionY + 1
                currentPositionX = 0
            else:
                currentPositionX = currentPositionX + 1

            if(int(currentPositionX) == int(xPosition) and int(currentPositionY) == int(yPosition)):
                if(newColor is None):
                    listBuffer[x] = self.ForeColor
                else:
                    listBuffer[x] = newColor
                break

    def setColor(self, newForeColor, newBackColor):
        self.ForeColor = newForeColor
        self.BackColor = newBackColor
