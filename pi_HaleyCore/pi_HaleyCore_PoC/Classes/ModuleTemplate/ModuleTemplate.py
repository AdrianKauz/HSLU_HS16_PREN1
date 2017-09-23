#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2017.03.21
# Version:    0.1
#------------------------------------------------------------------------------
# Template for every module which is connected to the core
#------------------------------------------------------------------------------

# Imports
import queue
import threading
import time
from Classes.Cookie import Cookie
from Classes.Enums import Enums

# Variables
LOOP_SLEEP = 0.1
REQUEST_TIME_OUT = 1000


#Class
class ModuleTemplate(threading.Thread):
    # Konstruktor
    #--------------------------------------------------------------------------
    def __init__(self, name, qCoreTasks):
        threading.Thread.__init__(self)
        # Queues for core and module
        self.coreQueue = qCoreTasks
        self.moduleQueue = queue.Queue()

        # Buffer
        self.requestBuffer = list()
        self.responseBuffer = list()

        # Attributes
        self.name = name
        self.alive = True
        self.status = Enums.ModuleStatus.IDLE


    # Funktions
    # --------------------------------------------------------------------------
    def flushQueue(self):
        """
        This function distributes every queue into the correct buffer.
        Cookies must be tagged as a "request" or "reply" type. Otherwise the
        cookie will be rejected
        """
        if(self.moduleQueue.empty()):
            return False
        else:
            while(self.moduleQueue.empty() is False):
                currCookie = self.moduleQueue.get()

                if(currCookie.type == Enums.CookieType.REQUEST):
                    self.requestBuffer.append(currCookie)
                elif(currCookie.type == Enums.CookieType.RESPONSE):
                    self.responseBuffer.append(currCookie)

            return True


    def stop(self):
        """
        Stops current running thread. Useful if core is shutting down.
        Otherwise thread will still run in background and will block
        the shutdown process.
        """
        self.alive = False

        return


    def getCurrTimeInMilli(self):
        return int(round(time.time() * 1000))


    def receiveCookie(self, newCookie):
        self.moduleQueue.put(newCookie)

        return


    def sendCookie(self, newCookie):
        self.coreQueue.put(newCookie)

        return


    def requestCookie(self, destination, task, value = ""):
        """
        FUNCTION IS STILL UNDER CONSTRUCTION!!!
        Starts a new request to another module via core-queue.
        Requests are marked with an unique id, so the function knows which
        response belongs to a request.
        """
        newCookie = Cookie.Cookie(self.name, destination, task, value)
        CookieId = newCookie.setUuid()

        # Passing request to the core
        self.sendCookie(newCookie)

        # and wait for response
        timestamp_ms = self.getCurrTimeInMilli()
        while((self.getCurrTimeInMilli() - timestamp_ms) < REQUEST_TIME_OUT):
            if (self.flushQueue()):
                for x in range(len(self.responseBuffer)):
                    if(self.responseBuffer[x].uuid == CookieId):
                        #cookieValue = self.responseBuffer[x].value
                        self.responseBuffer.remove(x)
                        return
            time.sleep(LOOP_SLEEP)

        # on time out
        return None


    def run(self):
        """
        Running thread which will do all the work for this module.
        Tasks are stored in the requestBuffer.
        """
        while (self.alive):
            self.flushQueue()
            if(len(self.requestBuffer) > 0):
                currCookie = self.requestBuffer.pop(0)
                self.doWork(currCookie)

            time.sleep(LOOP_SLEEP)

        # If thread is forced to stop with stop() then clear queue and lists
        self.flushQueue()
        self.requestBuffer = list()
        self.responseBuffer = list()

        return


    def doWork(self, currCookie):
        print("You should override this function!")
        return