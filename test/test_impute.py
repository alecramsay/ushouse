#!/usr/bin/env python3
#
# TEST IMPUTING UNCONTESTED ELECTIONS
#

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

        actual: dict = recast_uncontested_race(uncontested, avg_contested_votes)

        assert dict_approx_equal(actual, expected)

        recast: dict[str, int] = expected
        actual: dict = offset_uncontested_race(uncontested, recast)

        assert dict_approx_equal(actual, expected)

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

        actual: dict = recast_uncontested_race(uncontested, avg_contested_votes)

        assert dict_approx_equal(actual, expected)

        recast: dict[str, int] = expected
        actual: dict = offset_uncontested_race(uncontested, recast)

        assert dict_approx_equal(actual, expected)

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

        actual: dict = recast_uncontested_race(uncontested, avg_contested_votes)

        assert dict_approx_equal(actual, expected)

        recast: dict[str, int] = expected
        expected: dict = {
            "REP_V": 0,
            "DEM_V": 108469,
            "OTH_V": -11066,
            "TOT_V": 97403,
        }
        actual: dict = offset_uncontested_race(uncontested, recast)

        assert dict_approx_equal(actual, expected)

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

        actual: dict = recast_uncontested_race(uncontested, avg_contested_votes)

        assert dict_approx_equal(actual, expected)

        recast: dict[str, int] = expected
        expected: dict = {
            "REP_V": 96747,
            "DEM_V": 0,
            "OTH_V": -6589,
            "TOT_V": 90158,
        }
        actual: dict = offset_uncontested_race(uncontested, recast)

        assert dict_approx_equal(actual, expected)

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

        actual: dict = recast_uncontested_race(uncontested, avg_contested_votes)

        assert dict_approx_equal(actual, expected)

        recast: dict[str, int] = expected
        expected: dict = {
            "REP_V": 26432,
            "DEM_V": 160717,
            "OTH_V": -160717,
            "TOT_V": 26432,
        }
        actual: dict = offset_uncontested_race(uncontested, recast)

        assert dict_approx_equal(actual, expected)

    def test_majority_OTH(self) -> None:
        """2010 / NY 29th -- non-winning imputed votes > winning"""
        """2006 / AL / 6th -- non-winning imputed votes > winning <<< ALSO"""
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
            "DEM_V": 115288,
            "OTH_V": 0,
            "TOT_V": 230577,
        }
        """
        # Bad old imputation -- loser > winner
        
        expected: dict = {
            "REP_V": 115289,
            "DEM_V": 116978,
            "OTH_V": 0,
            "TOT_V": 232267,
        }
        """

        actual: int
        actual = recast_uncontested_vote("REP", uncontested, avg_contested_votes)
        assert actual == expected["REP_V"]

        actual = recast_uncontested_vote("DEM", uncontested, avg_contested_votes)
        assert actual == expected["DEM_V"]

        actual: dict = recast_uncontested_race(uncontested, avg_contested_votes)

        assert dict_approx_equal(actual, expected)

        recast: dict[str, int] = expected
        expected: dict = {
            "REP_V": 22122,
            "DEM_V": 115288,
            "OTH_V": -116978,
            "TOT_V": 20432,
        }
        """
        # Bad old imputation -- loser > winner

        expected: dict = {
            "REP_V": 22122,
            "DEM_V": 116978,
            "OTH_V": -116978,
            "TOT_V": 22122,
        }
        """
        actual: dict = offset_uncontested_race(uncontested, recast)

        assert dict_approx_equal(actual, expected)

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

        actual: dict = recast_uncontested_race(uncontested, avg_contested_votes)

        assert dict_approx_equal(actual, expected)

        recast: dict[str, int] = expected
        expected: dict = {
            "REP_V": 69278,
            "DEM_V": 196545,
            "OTH_V": -196545,
            "TOT_V": 69278,
        }
        actual: dict = offset_uncontested_race(uncontested, recast)

        assert dict_approx_equal(actual, expected)

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

        actual: dict = recast_uncontested_race(uncontested, avg_contested_votes)

        assert dict_approx_equal(actual, expected)

        recast: dict[str, int] = expected
        expected: dict = {
            "REP_V": 132478,
            "DEM_V": 0,
            "OTH_V": -8179,
            "TOT_V": 124299,
        }
        actual: dict = offset_uncontested_race(uncontested, recast)

        assert dict_approx_equal(actual, expected)

    def test_2002_NY_5th(self) -> None:
        """
        YEAR,STATE,XX,DISTRICT,REP_V,DEM_V,OTH_V,TOT_V,REP_S,DEM_S,OTH_S,CONTESTED_AVG,REP_VR,DEM_VR,OTH_VR,TOT_VR,REP_VA,DEM_VA,OTH_VA,TOT_VA
        2002,New York,NY,5th,0,68773,63968,132741,0,1,0,167130,63968,116991,0,180959,63968,48218,-63968,48218
        """
        raw: list = [
            "2002",
            "New York",
            "NY",
            "5th",
            0,
            68773,
            63968,
            132741,
            0,
            1,
            0,
            167130,
            63968,
            116991,
            0,
            180959,
            63968,
            48218,
            -63968,
            48218,
        ]

        #
        keys: list = ["REP_V", "DEM_V", "OTH_V", "TOT_V", "REP_S", "DEM_S", "OTH_S"]
        values: list = raw[4:11]

        uncontested: dict = dict(zip(keys, values))
        avg_contested_votes: int = raw[11]

        recast: dict = dict(zip(keys[:4], raw[12:16]))

        adjustments: dict = dict(zip(keys[:4], raw[16:]))

        actual: int
        actual = recast_uncontested_vote("REP", uncontested, avg_contested_votes)
        assert actual == recast["REP_V"]

        actual = recast_uncontested_vote("DEM", uncontested, avg_contested_votes)
        assert actual == recast["DEM_V"]

        actual: dict = recast_uncontested_race(uncontested, avg_contested_votes)

        assert dict_approx_equal(actual, recast)

        actual: dict = offset_uncontested_race(uncontested, recast)

        assert dict_approx_equal(actual, adjustments)

    def test_2006_TX_22nd(self) -> None:
        """
        Imputed > actual for uncontested winner
        Actual (other) > imputed for unconested losing party
        YEAR,STATE,XX,DISTRICT,REP_V,DEM_V,OTH_V,TOT_V,REP_S,DEM_S,OTH_S,CONTESTED_AVG,REP_VR,DEM_VR,OTH_VR,TOT_VR,REP_VA,DEM_VA,OTH_VA,TOT_VA
        2006,Texas,TX,22nd,0,76775,71464,148239,0,1,0,116152,71464,81307,0,152771,71464,4532,-71464,4532
        MODIFIED for rounding difference.
        """
        raw: list = [
            "2006",
            "Texas",
            "TX",
            "22nd",
            0,
            76775,
            71464,
            148239,
            0,
            1,
            0,
            116152,
            71464,
            81306,
            0,
            152770,
            71464,
            4531,
            -71464,
            4531,
        ]

        #
        keys: list = ["REP_V", "DEM_V", "OTH_V", "TOT_V", "REP_S", "DEM_S", "OTH_S"]
        values: list = raw[4:11]

        uncontested: dict = dict(zip(keys, values))
        avg_contested_votes: int = raw[11]

        recast: dict = dict(zip(keys[:4], raw[12:16]))

        adjustments: dict = dict(zip(keys[:4], raw[16:]))

        actual: int
        actual = recast_uncontested_vote("REP", uncontested, avg_contested_votes)
        assert actual == recast["REP_V"]

        actual = recast_uncontested_vote("DEM", uncontested, avg_contested_votes)
        assert actual == recast["DEM_V"]

        actual: dict = recast_uncontested_race(uncontested, avg_contested_votes)

        assert dict_approx_equal(actual, recast)

        actual: dict = offset_uncontested_race(uncontested, recast)

        assert dict_approx_equal(actual, adjustments)

    def test_2016_MN_2nd(self) -> None:
        """
        Actual (other) > imputed for uncontested losing party
        YEAR,STATE,XX,DISTRICT,REP_V,DEM_V,OTH_V,TOT_V,REP_S,DEM_S,OTH_S,CONTESTED_AVG,REP_VR,DEM_VR,OTH_VR,TOT_VR,REP_VA,DEM_VA,OTH_VA,TOT_VA
        2016,Minnesota,MN,2nd,173970,0,196545,370515,1,0,0,347497,243248,196545,0,439793,69278,196545,-196545,69278
        """
        raw: list = [
            "2016",
            "Minnesota",
            "MN",
            "2nd",
            173970,
            0,
            196545,
            370515,
            1,
            0,
            0,
            347497,
            243248,
            196545,
            0,
            439793,
            69278,
            196545,
            -196545,
            69278,
        ]

        #
        keys: list = ["REP_V", "DEM_V", "OTH_V", "TOT_V", "REP_S", "DEM_S", "OTH_S"]
        values: list = raw[4:11]

        uncontested: dict = dict(zip(keys, values))
        avg_contested_votes: int = raw[11]

        recast: dict = dict(zip(keys[:4], raw[12:16]))

        adjustments: dict = dict(zip(keys[:4], raw[16:]))

        actual: int
        actual = recast_uncontested_vote("REP", uncontested, avg_contested_votes)
        assert actual == recast["REP_V"]

        actual = recast_uncontested_vote("DEM", uncontested, avg_contested_votes)
        assert actual == recast["DEM_V"]

        actual: dict = recast_uncontested_race(uncontested, avg_contested_votes)

        assert dict_approx_equal(actual, recast)

        actual: dict = offset_uncontested_race(uncontested, recast)

        assert dict_approx_equal(actual, adjustments)

    def test_2018_WI_2nd(self) -> None:
        """
        Actual > imputed for uncontested winner
        YEAR,STATE,XX,DISTRICT,REP_V,DEM_V,OTH_V,TOT_V,REP_S,DEM_S,OTH_S,CONTESTED_AVG,REP_VR,DEM_VR,OTH_VR,TOT_VR,REP_VA,DEM_VA,OTH_VA,TOT_VA
        2018,Wisconsin,WI,2nd,0,309116,8179,317295,0,1,0,281795,132478,309116,0,441594,132478,0,-8179,124299
        """
        raw: list = [
            "2018",
            "Wisconsin",
            "WI",
            "2nd",
            0,
            309116,
            8179,
            317295,
            0,
            1,
            0,
            281795,
            132478,
            309116,
            0,
            441594,
            132478,
            0,
            -8179,
            124299,
        ]

        #
        keys: list = ["REP_V", "DEM_V", "OTH_V", "TOT_V", "REP_S", "DEM_S", "OTH_S"]
        values: list = raw[4:11]

        uncontested: dict = dict(zip(keys, values))
        avg_contested_votes: int = raw[11]

        recast: dict = dict(zip(keys[:4], raw[12:16]))

        adjustments: dict = dict(zip(keys[:4], raw[16:]))

        actual: int
        actual = recast_uncontested_vote("REP", uncontested, avg_contested_votes)
        assert actual == recast["REP_V"]

        actual = recast_uncontested_vote("DEM", uncontested, avg_contested_votes)
        assert actual == recast["DEM_V"]

        actual: dict = recast_uncontested_race(uncontested, avg_contested_votes)

        assert dict_approx_equal(actual, recast)

        actual: dict = offset_uncontested_race(uncontested, recast)

        assert dict_approx_equal(actual, adjustments)

    def test_2010_NY_29th(self) -> None:
        """
        Actual (other) > imputed for uncontested *winning* party
        Hence, vote capped for uncontested *losing* party
        YEAR,STATE,XX,DISTRICT,REP_V,DEM_V,OTH_V,TOT_V,REP_S,DEM_S,OTH_S,CONTESTED_AVG,REP_VR,DEM_VR,OTH_VR,TOT_VR,REP_VA,DEM_VA,OTH_VA,TOT_VA
        2010,New York,NY,29th,93167,0,116978,210145,1,0,0,164699,115289,115288,0,230577,22122,115288,-116978,20432
        """
        raw: list = [
            "2010",
            "New York",
            "NY",
            "29th",
            93167,
            0,
            116978,
            210145,
            1,
            0,
            0,
            164699,
            115289,
            115288,
            0,
            230577,
            22122,
            115288,
            -116978,
            20432,
        ]

        #
        keys: list = ["REP_V", "DEM_V", "OTH_V", "TOT_V", "REP_S", "DEM_S", "OTH_S"]
        values: list = raw[4:11]

        uncontested: dict = dict(zip(keys, values))
        avg_contested_votes: int = raw[11]

        recast: dict = dict(zip(keys[:4], raw[12:16]))

        adjustments: dict = dict(zip(keys[:4], raw[16:]))

        actual: int
        actual = recast_uncontested_vote("REP", uncontested, avg_contested_votes)
        assert actual == recast["REP_V"]

        actual = recast_uncontested_vote("DEM", uncontested, avg_contested_votes)
        assert actual == recast["DEM_V"]

        actual: dict = recast_uncontested_race(uncontested, avg_contested_votes)

        assert dict_approx_equal(actual, recast)

        actual: dict = offset_uncontested_race(uncontested, recast)

        assert dict_approx_equal(actual, adjustments)


### END ###
