#!/usr/bin/env python3
#
# UTILITIES
#

from pytest import approx


def areRoughlyEqual(x: float, y: float, tolerance: float) -> bool:
    delta = abs(x - y)
    return True if (delta < tolerance) else False


def dict_approx(actual: dict, expected: dict) -> bool:
    """Approximately equal"""
    for key in expected:
        if key not in actual:
            return False

        if type(expected[key]) == float:
            if actual[key] != approx(expected[key]):
                return False
        else:
            if actual[key] != expected[key]:
                return False

    return True


def dict_close(actual: dict, expected: dict, threshold: int = 1) -> bool:
    """Close but not necessarily equal"""

    for key in expected:
        if key not in actual:
            return False

        if type(expected[key]) == str:
            if actual[key] != expected[key]:
                return False

        if type(expected[key]) == int:
            # Allow for rounding differences
            if abs(actual[key] - expected[key]) > threshold:
                return False

        if type(expected[key]) == float:
            if actual[key] != approx(expected[key]):
                return False

    return True


### END ###
