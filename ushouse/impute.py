#!/usr/bin/env python3
#
# The logic for imputing results for uncontested elections.
#

"""
PROCESSING STEPS:
-----------------

There are three major processing steps:

1. Calculate the average number of votes, for contested races by state.
2. Recast (impute) the votes for uncontested, for each uncontested race.
3. Aggregate the imputed uncontested results for each state, and
   apply the changes to the official results.

INPUT DATA
----------

There are two input data sets:

(1) RESULTS -- one record per state:
- Actual election results, for each state
- Fields: STATE,XX,REP_V,DEM_V,OTH_V,TOT_V,REP_S,DEM_S,OTH_S,TOT_S

Alabama,AL,1416012,608809,26838,2051659,6,1,0,7
results: dict = {
    "STATE": "Alabama",
    "XX": "AL",
    "REP_V": 1416012,
    "DEM_V": 608809,
    "OTH_V": 26838,
    "TOT_V": 2051659,
    "REP_S": 6,
    "DEM_S": 1,
    "OTH_S": 0,
    "TOT_S": 7,
}

(2) UNCONTESTED -- one record per uncontested race:
- Actual election results for uncontested races,
- Optional dummy record (all zeroes) for states with no uncontested races
- Fields: STATE,XX,DISTRICT,REP_V,DEM_V,OTH_V,TOT_V,REP_S,DEM_S,OTH_S

uncontested: dict = {
    "STATE": "Alabama",
    "XX": "AL",
    "DISTRICT": "5th",
    "REP_V": 253094,
    "DEM_V": 0,
    "OTH_V": 11066,
    "TOT_V": 264160,
    "REP_S": 1,
    "DEM_S": 0,
    "OTH_S": 0,
}

"""

### AVERAGE CONTESTED VOTES ###

# TODO


### IMPUTE UNCONTESTED RESULTS ###


def recast_uncontested_votes(actual: dict, avg_contested_vote: int) -> dict:
    """
    Recast actual uncontested votes into imputed votes for one uncontested race.
    """

    recast: dict = dict()

    recast["REP_V"] = recast_uncontested_vote("REP", actual, avg_contested_vote)
    recast["DEM_V"] = recast_uncontested_vote("DEM", actual, avg_contested_vote)
    recast["OTH_V"] = 0
    recast["TOT_V"] = recast["REP_V"] + recast["DEM_V"] + recast["OTH_V"]

    return recast


def votes_key(party: str) -> str:
    """Return the votes key for a party."""
    return party + "_V"


def recast_uncontested_vote(
    party1: str, actual: dict, avg_contested_vote: int, vote_share: float = 0.70
) -> int:
    """
    For the imputed Republican vote in an uncontested race:
    - If a Republican won the uncontested seat, use their actual votes or the imputed votes,
      whichever is higher.
    - If a Democrat won the uncontested seat, use the actual "other" vote total or the imputed votes,
      again whichever is higher.

    Vice versa, for the imputed Democrat vote in an uncontested race.

    For a contested race (i.e., all zeroes dummy record), do nothing.
    """

    assert party1 in ["REP", "DEM"]

    # Not uncontested, i.e., contested -- dummy is all zeroes
    if actual["REP_V"] == 0 and actual["DEM_V"] == 0:
        return 0

    # Uncontested

    party2: str = "DEM" if party1 == "REP" else "REP"

    if actual[votes_key(party1)] > 0:
        recast: int = max(
            actual[votes_key(party1)], round(vote_share * avg_contested_vote)
        )
        return recast
    else:
        # TODO - This total must be at least one less than the winning total
        recast: int = max(
            actual[votes_key("OTH")],
            round(
                (1 - vote_share)
                * (
                    recast_uncontested_vote(party2, actual, avg_contested_vote)
                    / vote_share
                )
            ),
        )
        return recast


def calc_imputed_offsets(actual: dict, recast: dict) -> dict:
    """
    For one uncontested race, compute offsets for the imputed votes from the actual votes.
    """

    offsets: dict = dict()

    offsets["REP_V"] = recast["REP_V"] - actual["REP_V"]
    offsets["DEM_V"] = recast["DEM_V"] - actual["DEM_V"]
    offsets["OTH_V"] = recast["OTH_V"] - actual["OTH_V"]
    offsets["TOT_V"] = recast["TOT_V"] - actual["TOT_V"]

    return offsets


### AGGREGATE IMPUTED RESULTS & REVISE THE OFFICIAL RESULTS TO REFLECT THEM ###

# TODO -- Pivot the offsets by state

# TODO -- Apply the aggregated offsets to the actual votes


def apply_imputed_offsets(actual: dict, offsets: dict) -> dict:
    pass  # TODO


### END ###
