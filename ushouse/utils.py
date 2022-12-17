#!/usr/bin/env python3
#
# UTILITIES
#


def areRoughlyEqual(x, y, tolerance):
    delta = abs(x - y)
    return True if (delta < tolerance) else False
