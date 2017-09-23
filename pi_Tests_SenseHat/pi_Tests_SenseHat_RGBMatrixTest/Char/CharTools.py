# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2016.11.15
# Version:    1.0
#------------------------------------------------------------------------------
# Char Tools for the Sense Hat 8x8 RGB-Display
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
    def getChar(self, newChar):
        charCode = getCharCode(newChar)
        charCodePosition = 0
        newCharList = list()

        for x in range(0, 64):
            if charCodePosition < len(charCode):
                if charCode[charCodePosition] == x:
                    newCharList.append(self.ForeColor)
                    charCodePosition = charCodePosition + 1
                else:
                    newCharList.append(self.BackColor)
            else:
                newCharList.append(self.BackColor)

        return newCharList

    def setColor(self, newForeColor, newBackColor):
        self.ForeColor = newForeColor
        self.BackColor = newBackColor
