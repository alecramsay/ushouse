#
# UTILITIES
#


def areRoughlyEqual(x, y, tolerance):
    delta = abs(x - y);
    return True if (delta < tolerance) else False


def filterNone(x):
    x is None


# TODO - Calculate the average of an array of #'s
