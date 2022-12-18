#!/usr/bin/env python3
#
# TEST IMPUTING UNCONTESTED ELECTIONS
#

import pytest

from ushouse.impute import *
from ushouse.utils import *


# TODO
# - Combine these two suites into one, so data isn't duplicated
# - Add tests for apply_imputed_offsets()


class TestImputingUncontestedElections:
    def test_no_uncontested(self) -> None:
        # Contested dummy (2020 / AK)
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
            "REP3": 0,
            "DEM3": 0,
            "OTH3": 0,
            "TOT3": 0,
        }
        actual: dict = recast_uncontested_votes(uncontested)

        assert dict_approx(actual, expected)

        recast: dict[str, int] = expected
        expected: dict = {
            "REP4": 0,
            "DEM4": 0,
            "OTH4": 0,
            "TOT4": 0,
        }
        actual: dict = calc_imputed_offsets(uncontested, recast)

        assert dict_approx(actual, expected)

    def test_REP_uncontested(self) -> None:
        # R uncontested (2020 / AL 5th)
        uncontested: dict = {
            "REP1": 253094,
            "DEM1": 0,
            "OTH1": 11066,
            "TOT1": 264160,
            "REP2": 1,
            "DEM2": 0,
            "OTH2": 0,
            # "REP_win_pct": 0.70,
            # "DEM_win_pct": 0.70,
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

        recast: dict[str, int] = expected
        expected: dict = {
            "REP4": 0,
            "DEM4": 108469,
            "OTH4": -11066,
            "TOT4": 97403,
        }
        actual: dict = calc_imputed_offsets(uncontested, recast)

        assert dict_approx(actual, expected)

    def test_DEM_uncontested(self) -> None:
        # D uncontested (2020 / AL 7th)
        uncontested: dict = {
            "REP1": 0,
            "DEM1": 225742,
            "OTH1": 6589,
            "TOT1": 232331,
            "REP2": 0,
            "DEM2": 1,
            "OTH2": 0,
            # "REP_win_pct": 0.70,
            # "DEM_win_pct": 0.70,
            "Contested_AVG_Votes": 318227,
        }
        expected: dict = {
            "REP3": 96747,
            "DEM3": 225742,
            "OTH3": 0,
            "TOT3": 322489,
        }
        actual: dict = recast_uncontested_votes(uncontested)

        assert dict_approx(actual, expected)

        recast: dict[str, int] = expected
        expected: dict = {
            "REP4": 96747,
            "DEM4": 0,
            "OTH4": -6589,
            "TOT4": 90158,
        }
        actual: dict = calc_imputed_offsets(uncontested, recast)

        assert dict_approx(actual, expected)

    def test_large_OTH(self) -> None:
        # Large, fragmented "other" vote (2004 / NY 25th)
        uncontested: dict = {
            "REP1": 155163,
            "DEM1": 0,
            "OTH1": 160717,
            "TOT1": 315880,
            "REP2": 1,
            "DEM2": 0,
            "OTH2": 0,
            # "REP_win_pct": 0.70,
            # "DEM_win_pct": 0.70,
            "Contested_AVG_Votes": 259421,
        }
        expected: dict = {
            "REP3": 181595,
            "DEM3": 160717,
            "OTH3": 0,
            "TOT3": 342312,
        }
        actual: dict = recast_uncontested_votes(uncontested)

        assert dict_approx(actual, expected)

        recast: dict[str, int] = expected
        expected: dict = {
            "REP4": 26432,
            "DEM4": 160717,
            "OTH4": -160717,
            "TOT4": 26432,
        }
        actual: dict = calc_imputed_offsets(uncontested, recast)

        assert dict_approx(actual, expected)

    def test_majority_OTH(self) -> None:
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


### END ###
