#!/usr/bin/env python3
#
# TEST IMPUTING UNCONTESTED ELECTIONS
#

import pytest

from ushouse.impute import *
from ushouse.utils import *


class TestImputingOneUncontestedElection:
    def test_contested_dummy(self) -> None:
        """2020 / AK -- Contested dummy"""
        uncontested: dict = {
            "REP_V": 0,
            "DEM_V": 0,
            "OTH_V": 0,
            "TOT_V": 0,
            "REP_S": 0,
            "DEM_S": 0,
            "OTH_S": 0,
        }
        avg_contested_votes: int = 353165

        expected: dict = {
            "REP_V": 0,
            "DEM_V": 0,
            "OTH_V": 0,
            "TOT_V": 0,
        }

        actual: int
        actual = recast_uncontested_vote("REP", uncontested, avg_contested_votes)
        assert actual == expected["REP_V"]

        actual = recast_uncontested_vote("DEM", uncontested, avg_contested_votes)
        assert actual == expected["DEM_V"]

        actual: dict = recast_uncontested_votes(uncontested, avg_contested_votes)

        assert dict_approx(actual, expected)

        recast: dict[str, int] = expected
        actual: dict = calc_imputed_offsets(uncontested, recast)

        assert dict_approx(actual, expected)

    def test_blank_uncontested(self) -> None:
        """2016 / FL 24th -- Uncontested, no votes recorded"""
        uncontested: dict = {
            "REP_V": 0,
            "DEM_V": 0,
            "OTH_V": 0,
            "TOT_V": 0,
            "REP_S": 0,
            "DEM_S": 1,
            "OTH_S": 0,
        }
        avg_contested_votes: int = 339901

        expected: dict = {
            "REP_V": 101970,
            "DEM_V": 237931,
            "OTH_V": 0,
            "TOT_V": 339901,
        }

        actual: int
        actual = recast_uncontested_vote("REP", uncontested, avg_contested_votes)
        assert actual == expected["REP_V"]

        actual = recast_uncontested_vote("DEM", uncontested, avg_contested_votes)
        assert actual == expected["DEM_V"]

        actual: dict = recast_uncontested_votes(uncontested, avg_contested_votes)

        assert dict_approx(actual, expected)

        recast: dict[str, int] = expected
        actual: dict = calc_imputed_offsets(uncontested, recast)

        assert dict_approx(actual, expected)

    def test_REP_uncontested(self) -> None:
        """2020 / AL 5th -- R uncontested"""
        uncontested: dict = {
            "REP_V": 253094,
            "DEM_V": 0,
            "OTH_V": 11066,
            "TOT_V": 264160,
            "REP_S": 1,
            "DEM_S": 0,
            "OTH_S": 0,
        }
        avg_contested_votes: int = 318227

        expected: dict = {
            "REP_V": 253094,
            "DEM_V": 108469,
            "OTH_V": 0,
            "TOT_V": 361563,
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
            "REP_V": 0,
            "DEM_V": 108469,
            "OTH_V": -11066,
            "TOT_V": 97403,
        }
        actual: dict = calc_imputed_offsets(uncontested, recast)

        assert dict_approx(actual, expected)

    def test_DEM_uncontested(self) -> None:
        """2020 / AL 7th -- D uncontested"""
        uncontested: dict = {
            "REP_V": 0,
            "DEM_V": 225742,
            "OTH_V": 6589,
            "TOT_V": 232331,
            "REP_S": 0,
            "DEM_S": 1,
            "OTH_S": 0,
        }
        avg_contested_votes: int = 318227

        expected: dict = {
            "REP_V": 96747,
            "DEM_V": 225742,
            "OTH_V": 0,
            "TOT_V": 322489,
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
            "REP_V": 96747,
            "DEM_V": 0,
            "OTH_V": -6589,
            "TOT_V": 90158,
        }
        actual: dict = calc_imputed_offsets(uncontested, recast)

        assert dict_approx(actual, expected)

    def test_large_OTH(self) -> None:
        """2004 / NY 25th -- fragmented "other" votes > winning"""
        uncontested: dict = {
            "REP_V": 155163,
            "DEM_V": 0,
            "OTH_V": 160717,
            "TOT_V": 315880,
            "REP_S": 1,
            "DEM_S": 0,
            "OTH_S": 0,
        }
        avg_contested_votes: int = 259421

        expected: dict = {
            "REP_V": 181595,
            "DEM_V": 160717,
            "OTH_V": 0,
            "TOT_V": 342312,
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
            "REP_V": 26432,
            "DEM_V": 160717,
            "OTH_V": -160717,
            "TOT_V": 26432,
        }
        actual: dict = calc_imputed_offsets(uncontested, recast)

        assert dict_approx(actual, expected)

    def test_majority_OTH(self) -> None:
        """2010 / NY 29th -- non-winning imputed votes > winning"""
        # Also 2006 / AL / 6th -- non-winning imputed votes > winning
        # TODO - This is the wrong imputation!
        uncontested: dict = {
            "REP_V": 93167,
            "DEM_V": 0,
            "OTH_V": 116978,
            "TOT_V": 210145,
            "REP_S": 1,
            "DEM_S": 0,
            "OTH_S": 0,
        }
        avg_contested_votes: int = 164699

        expected: dict = {
            "REP_V": 115289,
            "DEM_V": 116978,
            "OTH_V": 0,
            "TOT_V": 232267,
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
            "REP_V": 22122,
            "DEM_V": 116978,
            "OTH_V": -116978,
            "TOT_V": 22122,
        }
        actual: dict = calc_imputed_offsets(uncontested, recast)

        assert dict_approx(actual, expected)

    def test_imputed_gt_actual(self) -> None:
        """2016 / MN / 2nd -- imputed > actual"""
        uncontested: dict = {
            "REP_V": 173970,
            "DEM_V": 0,
            "OTH_V": 196545,
            "TOT_V": 370515,
            "REP_S": 1,
            "DEM_S": 0,
            "OTH_S": 0,
        }
        avg_contested_votes: int = 347497

        expected: dict = {
            "REP_V": 243248,
            "DEM_V": 196545,
            "OTH_V": 0,
            "TOT_V": 439793,
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
            "REP_V": 69278,
            "DEM_V": 196545,
            "OTH_V": -196545,
            "TOT_V": 69278,
        }
        actual: dict = calc_imputed_offsets(uncontested, recast)

        assert dict_approx(actual, expected)

    def test_actual_gt_imputed(self) -> None:
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
            "TOT_V": 441594,
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


class TestAggregatingImputedOffsets:
    def test_placeholder(self) -> None:
        pass  # TODO


### END ###
