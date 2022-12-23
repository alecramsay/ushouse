#!/usr/bin/env python3
#
# The logic for imputing results for uncontested elections.
#

from .states import state_codes

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


def agg_uncontested(uncontested: list, cols: list[str]) -> dict:
    """Aggregate uncontested races by state."""

    by_state: dict = dict()
    for xx in state_codes:
        by_state[xx] = dict.fromkeys(cols, 0)

    for row in uncontested:
        xx: str = row["XX"]

        for c in cols:
            by_state[xx][c] += row[c]

    return by_state


def calc_avg_contested_votes(
    results: list, uncontested: list, proxies: dict
) -> dict[str, int]:
    """Calculate the average contested vote by state."""

    uncontested_by_state: dict = agg_uncontested(
        uncontested,
        ["REP_V", "DEM_V", "OTH_V", "TOT_V", "REP_S", "DEM_S", "OTH_S"],
    )

    avg_contested_vote: dict[str, int] = dict.fromkeys(state_codes, None)

    for row in results:
        xx: str = row["XX"]
        uncontested: dict = uncontested_by_state[xx]

        contested_seats: int = (
            row["TOT_S"] - uncontested["REP_S"] - uncontested["DEM_S"]
        )
        contested_votes: int = row["TOT_V"] - uncontested["TOT_V"]

        if contested_seats > 0:
            avg_contested_vote[xx] = round(contested_votes / contested_seats)
        else:
            # No contested seats. Use a proxy.
            if xx in proxies:
                avg_contested_vote[xx] = proxies[xx]
            else:
                raise Exception(f"No contested seats in and no proxy for {xx}")

    return avg_contested_vote


### IMPUTE UNCONTESTED RESULTS ###


def revise_uncontested_races(uncontested: list, avg_contested_vote: dict) -> list:
    """Impute uncontested votes for each race, *and* convert them into offsets."""

    uncontested_offsets: list = list()
    for row in uncontested:
        xx: str = row["XX"]
        recast: dict = recast_uncontested_race(row, avg_contested_vote[xx])
        offsets: dict = offset_uncontested_race(row, recast)

        row_out: dict = dict()
        row_out["STATE"] = row["STATE"]
        row_out["XX"] = row["XX"]
        row_out.update(offsets)

        uncontested_offsets.append(row_out)

    return uncontested_offsets


def recast_uncontested_race(actual: dict, avg_contested_vote: int) -> dict:
    """
    Recast actual uncontested votes into imputed votes for one uncontested race.
    """

    recast: dict = dict()

    recast["REP_V"] = recast_uncontested_vote("REP", actual, avg_contested_vote)
    recast["DEM_V"] = recast_uncontested_vote("DEM", actual, avg_contested_vote)
    recast["OTH_V"] = 0
    recast["TOT_V"] = recast["REP_V"] + recast["DEM_V"] + recast["OTH_V"]

    return recast


def v_key(party: str) -> str:
    """Return the votes key for a party."""
    return party + "_V"


def s_key(party: str) -> str:
    """Return the seats key for a party."""
    return party + "_S"


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
    if actual["REP_S"] == 0 and actual["DEM_S"] == 0:
        return 0

    # Uncontested

    party2: str = "DEM" if party1 == "REP" else "REP"

    if actual[s_key(party1)] == 1:
        # Uncontested winner
        recast: int = max(actual[v_key(party1)], round(vote_share * avg_contested_vote))
        return recast
    else:
        # Uncontested 'loser' -- must be less than the winning total
        recast: int = min(
            max(
                actual[v_key("OTH")],
                round(
                    (1 - vote_share)
                    * (
                        recast_uncontested_vote(party2, actual, avg_contested_vote)
                        / vote_share
                    )
                ),
            ),
            recast_uncontested_vote(party2, actual, avg_contested_vote) - 1,
        )
        return recast


### CALCULATE OFFSETS TO REFLECT IMPUTED VOTES ###


def offset_uncontested_race(actual: dict, recast: dict) -> dict:
    """
    For one uncontested race, compute offsets for the imputed votes from the actual votes.
    """

    offsets: dict = dict()

    offsets["REP_V"] = recast["REP_V"] - actual["REP_V"]
    offsets["DEM_V"] = recast["DEM_V"] - actual["DEM_V"]
    offsets["OTH_V"] = recast["OTH_V"] - actual["OTH_V"]
    offsets["TOT_V"] = recast["TOT_V"] - actual["TOT_V"]

    return offsets


### APPLY THE OFFSETS TO THE OFFICIAL RESULTS ###


def apply_imputed_offsets(results: list, uncontested_offsets: dict) -> dict:
    revised_results: list = list()

    for row in results:
        row_out: dict = row.copy()
        offsets: dict = uncontested_offsets[row["XX"]]
        for key in offsets:
            row_out[key] += offsets[key]

        # Add two-party D vote & seat share
        vote_share: float = None  # Handle other/independent-only case
        seat_share: float = None
        if (row_out["DEM_V"] + row_out["REP_V"]) > 0 and (
            row_out["DEM_S"] + row_out["REP_S"]
        ) > 0:
            vote_share = row_out["DEM_V"] / (row_out["DEM_V"] + row_out["REP_V"])
            seat_share = row_out["DEM_S"] / (row_out["DEM_S"] + row_out["REP_S"])

        row_out["VOTE_%"] = vote_share  # Two-party DEM vote share
        row_out["SEAT_%"] = seat_share  # Two-party DEM seat share

        revised_results.append(row_out)

    return revised_results


### END ###
