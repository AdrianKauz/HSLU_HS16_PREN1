#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2017.03.24
# Version:    0.1
# ------------------------------------------------------------------------------
# Class Display
# ------------------------------------------------------------------------------

# Imports
from Classes.ModuleTemplate import ModuleTemplate
from Classes.Cookie import Cookie

# Variables


#Class
class Display(ModuleTemplate.ModuleTemplate):
    # Konstruktor
    #--------------------------------------------------------------------------
    def __init__(self, qCoreTasks):
        super(Display, self).__init__("Display", qCoreTasks)


    # Funktions
    # --------------------------------------------------------------------------
    def setNumber(self, newValue):
        print("Module: \"" + self.name + "\","
              "Task: \"setNumber()\","
              "Value: " + str(newValue))

        return


    def setStatus(self, newValue):
        print("Module: \"" + self.name + "\","
              "Task: \"setStatus()\","
              "Value: " + str(newValue))

        return

    # For testing
    def getPong(self, newValue):
        print("Module \"" + self.name + "\": Pong!")

        self.sendCookie(Cookie.Cookie(self.name, "Sandbox", "getPing"))

        return


    def doWork(self, currCookie):
        if(currCookie is not None):
            getattr(self,currCookie.task)(currCookie.value)

        return