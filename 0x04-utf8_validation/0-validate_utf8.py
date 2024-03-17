#!/usr/bin/python3
"""
a method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    determine if the given data set represents
    a valid UTF-8 encoding
    """
    numberOfBytes = 0
    for i in data:
        mask = 1 << 7
        if not numberOfBytes:
            while mask & i:
                numberOfBytes += 1
                mask >>= 1
            if not numberOfBytes:
                continue
            if numberOfBytes == 1 or numberOfBytes > 4:
                return False
        else:
            if i >> 6 != 0b10:
                return False
        numberOfBytes -= 1
    return numberOfBytes == 0
