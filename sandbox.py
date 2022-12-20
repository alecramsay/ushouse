#!/usr/bin/env python3
#
# SANDBOX, THROWAWAY CODE
#

from ushouse import *


def test_run() -> None:
    """2018 / WI / 2nd -- actual votes > 0.7 average contested vote"""
    uncontested: dict = {
        "REP_V": 0,
        "DEM_V": 309116,
        "OTH_V": 8179,
        "TOT_V": 317295,
        "REP_S": 0,
        "DEM_S": 1,
        "OTH_S": 0,
    }
    avg_contested_votes: int = 281795

    expected: dict = {
        "REP_V": 132478,
        "DEM_V": 309116,
        "OTH_V": 0,
        "TOT_V": 442594,
    }

    actual: int
    actual = recast_uncontested_vote("REP", uncontested, avg_contested_votes)
    assert actual == expected["REP_V"]

    actual = recast_uncontested_vote("DEM", uncontested, avg_contested_votes)
    assert actual == expected["DEM_V"]

    actual: dict = recast_uncontested_votes(uncontested, avg_contested_votes)

    assert dict_approx(actual, expected)

    recast: dict[str, int] = expected
    expected: dict = {
        "REP_V": 132478,
        "DEM_V": 0,
        "OTH_V": -8179,
        "TOT_V": 124299,
    }
    actual: dict = calc_imputed_offsets(uncontested, recast)

    assert dict_approx(actual, expected)


test_run()

pass
