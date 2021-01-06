#
# UTILITIES
#


def areRoughlyEqual(x, y, tolerance):
    delta = abs(x - y);
    return True if (delta < tolerance) else False

