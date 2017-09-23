#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2017.03.24
# Version:    0.1
#------------------------------------------------------------------------------
# Class Sandbox
#------------------------------------------------------------------------------

# Imports
from Classes.ModuleTemplate import ModuleTemplate
from Classes.Cookie import Cookie

# Variables


#Class
class Sandbox(ModuleTemplate.ModuleTemplate):
    # Konstruktor
    #--------------------------------------------------------------------------
    def __init__(self, qCoreTasks):
        super(Sandbox, self).__init__("Sandbox", qCoreTasks)


    # Funktions
    # --------------------------------------------------------------------------
    def toConsole(self, newValue):
        print("Module: \"" + self.name + "\", "
              "Task: \"toConsole()\", "
              "Value: \"" + str(newValue) + "\"")

        return


    def getPing(self, newValue):
        print("Module \"" + self.name + "\": Ping!")

        self.sendCookie(Cookie.Cookie(self.name, "Display", "getPong"))

        return


    def doWork(self, currCookie):
        if (currCookie is not None):
            getattr(self, currCookie.task)(currCookie.value)

        return