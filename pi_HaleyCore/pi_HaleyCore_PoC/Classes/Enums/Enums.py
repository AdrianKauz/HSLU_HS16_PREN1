#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2017.03.21
# Version:    0.1
# ------------------------------------------------------------------------------
# Enums
# ------------------------------------------------------------------------------

# Imports
from enum import Enum

# Classes
class CookieType(Enum):
    REQUEST = 0
    RESPONSE = 1


class ModuleStatus(Enum):
    IDLE = 0
    RUNNING = 1
    STOPPED = 2
    FAILURE = 3