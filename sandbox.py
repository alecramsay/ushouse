#!/usr/bin/env python3
#
# SANDBOX, THROWAWAY CODE
#

from ushouse import *


def test_run() -> None:
    # Large, fragmented "other" vote (2010 / NY 29th)
    # TODO - This is the wrong imputation!
    uncontested: dict = {
        "REP1": 93167,
        "DEM1": 0,
        "OTH1": 116978,
        "TOT1": 210145,
        "REP2": 1,
        "DEM2": 0,
        "OTH2": 0,
        # "REP_win_pct": 0.70,
        # "DEM_win_pct": 0.70,
        "Contested_AVG_Votes": 164699,
    }
    expected: dict = {
        "REP3": 115289,
        "DEM3": 116978,
        "OTH3": 0,
        "TOT3": 232267,
    }
    actual: dict = recast_uncontested_votes(uncontested)

    assert dict_approx(actual, expected)

    recast: dict[str, int] = expected
    expected: dict = {
        "REP4": 22122,
        "DEM4": 116978,
        "OTH4": -116978,
        "TOT4": 22122,
    }
    actual: dict = calc_imputed_offsets(uncontested, recast)

    assert dict_approx(actual, expected)


test_run()

pass
