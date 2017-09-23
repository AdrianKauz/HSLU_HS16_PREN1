#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2017.03.21
# Version:    0.1
#------------------------------------------------------------------------------
# Core for Haley-OS
#------------------------------------------------------------------------------

# Imports
import queue
import time
from Classes.Sandbox import Sandbox
from Classes.Display import Display
from Classes.Cookie import Cookie

# Lists & Queues
qCoreTasks = queue.Queue()    # Initialize FIFO-Queue
listModules = list()        # Every module witch is connected to the core


# Variables
CLEAR_SCREEN = "\033c"
LOOP_SLEEP = 0.001


# Functions
def stopModules():
    for modules in listModules:
        modules.stop()
        print("Module \"" + modules.name + "\" stopped!")


def startModules():
    for modules in listModules:
        modules.start()
        print("Module \"" + modules.name + "\" running!")


# Main
try:
    sandbox = Sandbox.Sandbox(qCoreTasks)
    display = Display.Display(qCoreTasks)
    listModules.append(display)
    listModules.append(sandbox)
    startModules()

    newCookie = Cookie.Cookie("Display", "Display", "getPong")
    display.receiveCookie(newCookie)

    # Core will running the whole time in this loop
    # Now every module connected to the core can communicate together :-)
    while(True):
        if(qCoreTasks.empty() is False):
            currCookie = qCoreTasks.get()

            for currModule in listModules:
                if(currModule.name == currCookie.destination):
                    currModule.receiveCookie(currCookie)

        time.sleep(LOOP_SLEEP)

except KeyboardInterrupt:
    print(CLEAR_SCREEN + "Goodbye!\n")
    stopModules()

except:
    print(CLEAR_SCREEN + "Aaaaaaaaargh!\n")
    stopModules()
    raise