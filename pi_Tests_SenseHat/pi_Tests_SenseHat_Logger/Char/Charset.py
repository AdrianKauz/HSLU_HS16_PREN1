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
        '0': [4, 5, 6, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 60, 61, 62],
        '1': [5, 12, 13, 21, 29, 37, 45, 51, 52, 53, 54, 55],
        '2': [4, 5, 6, 11, 15, 23, 31, 38, 45, 52, 59, 60, 61, 62, 63],
        '3': [4, 5, 6, 11, 15, 23, 29, 30, 39, 47, 51, 55, 60, 61, 62],
        '4': [6, 13, 14, 20, 22, 27, 30, 35, 36, 37, 38, 39, 46, 54, 62],
        '5': [3, 4, 5, 6, 7, 11, 19, 20, 21, 22, 31, 39, 47, 51, 55, 60, 61, 62],
        '6': [4, 5, 6, 11, 15, 19, 27, 28, 29, 30, 35, 39, 43, 47, 51, 55, 60, 61, 62],
        '7': [3, 4, 5, 6, 7, 15, 22, 29, 37, 45, 53, 61],
        '8': [4, 5, 6, 11, 15, 19, 23, 28, 29, 30, 35, 39, 43, 47, 51, 55, 60, 61, 62],
        '9': [4, 5, 6, 11, 15, 19, 23, 28, 29, 30, 31, 39, 47, 51, 55, 60, 61, 62],
        '!': [3, 4, 5, 6, 7, 11, 12, 13, 14, 15, 19, 20, 21, 22, 23, 27, 28, 29, 30, 31, 35, 36, 37,
              38, 39, 43, 44, 45, 46, 47, 51, 52, 53, 54, 55, 59, 60, 61, 62, 63]
    }.get(newChar, [0])  # 0 is default