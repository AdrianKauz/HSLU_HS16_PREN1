# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Autor:      Adrian Kauz
# Datum:      2016.11.15
# Version:    1.0
#------------------------------------------------------------------------------
# Charset for Sense Hat 8x8 RGB-Display
#------------------------------------------------------------------------------


#Methods
def getCharCode(newChar):
    return {
        'A': [11, 12, 18, 21, 26, 29, 34, 35, 36, 37, 42, 45, 50, 53, 58, 61],
        'B': [10, 11, 12, 18, 21, 26, 29, 34, 35, 36, 42, 45, 50, 53, 58, 59, 60],
        'C': [11, 12, 13, 18, 26, 34, 42, 50, 59, 60, 61],
        'D': [10, 11, 12, 18, 21, 26, 29, 34, 37, 42, 45, 50, 53, 58, 59, 60],
        'E': [10, 11, 12, 13, 18, 26, 34, 35, 36, 42, 50, 58, 59, 60, 61]
    }.get(newChar, 0)  # 0 is default