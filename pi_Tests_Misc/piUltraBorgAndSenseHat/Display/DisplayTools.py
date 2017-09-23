#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2017.03.08
# Version:    1.0
#------------------------------------------------------------------------------
# Some functions to draw stuff on the display (UltraBorg-Scale)
#------------------------------------------------------------------------------

#Class
class DisplayTools:
    # Konstruktor
    def __init__(self):
        self.ColorBar1Full = [255, 0, 0]
        self.ColorBar1Half = [64, 0, 0]
        self.ColorBar2Full = [0, 255, 0]
        self.ColorBar2Half = [0, 64, 0]
        self.ColorBarEmpty = [0, 0, 0]


    # Funktions
    def initBar(self, listBuffer):
        for x in range(24, 32):
            listBuffer[x] = self.ColorBar1Full

        for x in range(56, 64):
            listBuffer[x] = self.ColorBar2Full


    def drawBar(self, iBarNumber, fValue, listBuffer):

        # Calculate number of bars
        fBarSize = self.getBarSize(fValue)
        bHalfBar = (fBarSize % 1) > 0

        if iBarNumber == 1:
            for x in range(8, 16):
                if x < (8 + int(fBarSize)):
                    listBuffer[x] = self.ColorBar1Full
                    listBuffer[x + 8] = self.ColorBar1Full
                else:
                    listBuffer[x] = self.ColorBarEmpty
                    listBuffer[x + 8] = self.ColorBarEmpty

            if bHalfBar:
                listBuffer[8 + int(fBarSize)] = self.ColorBar1Half
                listBuffer[8 + int(fBarSize) + 8] = self.ColorBar1Half

        if iBarNumber == 2:
            for x in range(40, 48):
                if x < (40 + int(fBarSize)):
                    listBuffer[x] = self.ColorBar2Full
                    listBuffer[x + 8] = self.ColorBar2Full
                else:
                    listBuffer[x] = self.ColorBarEmpty
                    listBuffer[x + 8] = self.ColorBarEmpty

            if bHalfBar:
                listBuffer[40 + int(fBarSize)] = self.ColorBar2Half
                listBuffer[40 + int(fBarSize) + 8] = self.ColorBar2Half


    def getBarSize(self, fValue):
        listBarState = [0, 0.5, 1, 1, 1.5, 2, 2.5, 3, 3, 3.5, 4, 4.5, 5, 5, 5.5, 6, 6.5, 7, 7, 7.5, 8]

        return listBarState[int((fValue + 1.0) * 10)]