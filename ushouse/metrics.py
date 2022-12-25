#!/usr/bin/env python3
#
# METRICS
#

from .settings import *
from .utils import *


def best_seats(N: int, Vf: float) -> int:
    """
    The # of seats closest to proportional @ statewide Vf, which is
    the "expected number of seats" from http://bit.ly/2Fcuf4q.
    """

    if N > 1:
        return round((N * Vf) - EPSILON)

    return 0

    # TODO - Only 1 CD <<< Not sure what I was thinking here.
    # if (Vf > 0.75):
    #     return 1
    # elif (Vf > 0.25):
    #     return 0.5
    # else:
    #     return 0


def single_seat(rep: int, dem: int) -> int:
    return 1 if (rep == 1) else (-1 if (dem == 1) else 0)


def unearned_seats(best: int, actual: int) -> int:
    """
    The # of "unearned" seats won beyond proportional, based on statewide Vf.
    which is UE_# from http://bit.ly/2Fcuf4q.
    """

    return best - actual  # R advantage is +; D advantage is –


### RELATED CONCEPTS & HELPERS ###


def expected_R_seats(actual_R: int, net_UE: int) -> int:
    return actual_R - net_UE


def expected_D_seats(expected_R: int) -> int:
    return 435 - expected_R


def margin(R_total: int, D_total: int) -> int:
    return (R_total - 218) if (R_total > D_total) else ((D_total - 218) * -1)


def slack(expected_R: int) -> int:
    return (expected_R - 218) if (expected_R >= 218) else (expected_R - 218 + 1)


def isAntimajoritarian(Vf: int, Sf: float) -> bool:
    bDem: bool = True if ((Vf < (0.5 - AVGSVERROR)) and (Sf > 0.5)) else False
    bRep: bool = (
        True if (((1 - Vf) < (0.5 - AVGSVERROR)) and ((1 - Sf) > 0.5)) else False
    )

    return bDem or bRep


### END ###
