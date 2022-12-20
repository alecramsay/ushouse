#!/usr/bin/env python3
#
# SANDBOX, THROWAWAY CODE
#

from ushouse import *


def test_run() -> None:
    # Contested dummy (2020 / AK)
    uncontested: dict = {
        "REP_V": 0,
        "DEM_V": 0,
        "OTH_V": 0,
        "TOT_V": 0,
        "REP_S": 0,
        "DEM_S": 0,
        "OTH_S": 0,
    }
    expected: dict = {
        "REP_V": 0,
        "DEM_V": 0,
        "OTH_V": 0,
        "TOT_V": 0,
        "REP_S": 0,
        "DEM_S": 0,
        "OTH_S": 0,
    }
    actual: dict = recast_rep_votes(uncontested, 353165)
    assert dict_approx(actual, expected)

    # Contested dummy (2020 / AK)
    uncontested: dict = {
        "REP_V": 0,
        "DEM_V": 0,
        "OTH_V": 0,
        "TOT_V": 0,
        "REP_S": 0,
        "DEM_S": 0,
        "OTH_S": 0,
    }
    expected: dict = {
        "REP_V": 0,
        "DEM_V": 0,
        "OTH_V": 0,
        "TOT_V": 0,
        "REP_S": 0,
        "DEM_S": 0,
        "OTH_S": 0,
    }
    actual: dict = recast_dem_votes(uncontested, 353165)
    assert dict_approx(actual, expected)


test_run()

pass
