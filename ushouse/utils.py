#!/usr/bin/env python3
#
# UTILITIES
#

from pytest import approx


def areRoughlyEqual(x: float, y: float, tolerance: float) -> bool:
    delta = abs(x - y)
    return True if (delta < tolerance) else False


def dict_approx(actual: dict, expected: dict) -> bool:
    for key in expected:
        if key not in actual:
            return False

        a: float | int = actual[key]
        e: float | int = expected[key]

        if type(e) == float:
            if a != approx(e):
                return False
        else:
            if a != e:
                return False

    return True


### END ###
