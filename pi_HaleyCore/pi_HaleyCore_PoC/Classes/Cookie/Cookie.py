#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2017.03.21
# Version:    0.1
# ------------------------------------------------------------------------------
# Class Cookie
# ------------------------------------------------------------------------------
# (String) Source:      Name of source-module (Sender)
# (String) Destination: Name of destination-module (Receiver)
# (String) Task:        What the destination-module should do.
#                       Ex.: "setStatus1", "getPosition", "turnVehicle"
#                            "drawNumber"
# (String) Value:       Additional data like measurements, infos etc.,
#                       or a roman number "I, II, III, VI, V"
# ------------------------------------------------------------------------------

# Imports
import uuid
from Classes.Enums import Enums

#Class
class Cookie:
    # Konstruktor
    def __init__(self, source = "", destination = "", task = "", value = ""):
        self.source = source
        self.destination = destination
        self.task = task
        self.value = value
        self.uuid = ""
        self.type = Enums.CookieType.REQUEST

    # Functions
    def setUuid(self):
        self.uuid = uuid.uuid4()

        return self.uuid



