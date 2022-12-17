#!/usr/bin/env python3
#
# TEST IMPUTING UNCONTESTED ELECTIONS
#

import pytest

from ushouse.impute import *
from ushouse.utils import *


class TestImpute:
    def test_recast_uncontested_votes(self) -> None:
        # Contested dummy
        uncontested: dict = {
            "REP1": 0,
            "DEM1": 0,
            "OTH1": 0,
            "TOT1": 0,
            "REP2": 1,
            "DEM2": 0,
            "OTH2": 0,
            "REP_win_pct": 0.70,
            "DEM_win_pct": 0.70,
            "Contested_AVG_Votes": 353165,
        }
        expected: dict = {
            "REP3": 0.0,
            "DEM3": 0.0,
            "OTH3": 0.0,
            "TOT3": 0.0,
        }
        actual: dict = recast_uncontested_votes(uncontested)

        assert dict_approx(actual, expected)

        # R uncontested
        uncontested: dict = {
            "REP1": 253094,
            "DEM1": 0,
            "OTH1": 11066,
            "TOT1": 264160,
            "REP2": 1,
            "DEM2": 0,
            "OTH2": 0,
            "REP_win_pct": 0.70,
            "DEM_win_pct": 0.70,
            "Contested_AVG_Votes": 318227,
        }
        expected: dict = {
            "REP3": 253094,
            "DEM3": 108469,
            "OTH3": 0,
            "TOT3": 361563,
        }
        actual: dict = recast_uncontested_votes(uncontested)

        assert dict_approx(actual, expected)

        # D uncontested
        uncontested: dict = {
            "REP1": 253094,
            "DEM1": 0,
            "OTH1": 11066,
            "TOT1": 264160,
            "REP2": 1,
            "DEM2": 0,
            "OTH2": 0,
            "REP_win_pct": 0.70,
            "DEM_win_pct": 0.70,
            "Contested_AVG_Votes": 318227,
        }
        expected: dict = {
            "REP3": 253094,
            "DEM3": 108469,
            "OTH3": 0,
            "TOT3": 361563,
        }
        actual: dict = recast_uncontested_votes(uncontested)

        assert dict_approx(actual, expected)


### END ###
