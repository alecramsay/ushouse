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

    recast["REP_V"] = recast_rep_votes(actual, avg_contested_vote)
    recast["DEM_V"] = recast_dem_votes(actual, avg_contested_vote)
    recast["OTH_V"] = 0
    recast["TOT_V"] = recast["REP_V"] + recast["DEM_V"] + recast["OTH_V"]

    return recast


"""
NOTE - These two formulates are interdependent. They work, because the if/else blocks
complement each other in the two functions.
"""


def recast_rep_votes(
    actual: dict, avg_contested_vote: int, vote_share: float = 0.70
) -> int:
    """
    For states w/ uncontested races, if a Republican won the uncontested seat,
    use their actual votes or the imputed votes, whichever is higher. If a Democrat won
    the uncontested seat, use the actual "other" vote total or the imputed votes, whichever
    is higher. For states w/o uncontested races (dummy all zeroes), use the actuals.
    """

    if actual["TOT_V"] > 0:
        if actual["REP_V"] > 0:

            recast: int = max(actual["REP_V"], round(vote_share * avg_contested_vote))
            return recast
        else:
            # TODO - This total must be at least one less than the winning total
            recast: int = max(
                actual["OTH_V"],
                round(
                    (1 - vote_share)
                    * (recast_dem_votes(actual, avg_contested_vote) / vote_share)
                ),
            )
            return recast
    else:
        return actual["REP_V"]


def recast_dem_votes(
    actual: dict, avg_contested_vote: int, vote_share: float = 0.70
) -> int:
    """
    The converse of the above:
    For states w/ uncontested races, if a Democrat won the uncontested seat,
    use their actual votes or the imputed votes, whichever is higher. If a Republican won
    the uncontested seat, use the actual "other" vote total or the imputed votes, whichever
    is higher. For states w/o uncontested races (dummy all zeroes), use the actuals.
    """

    if actual["TOT_V"] > 0:
        if actual["DEM_V"] > 0:
            recast: int = max(actual["DEM_V"], round(vote_share * avg_contested_vote))
            return recast
        else:
            # TODO - This total must be at least one less than the winning total
            recast: int = max(
                actual["OTH_V"],
                round(
                    (1 - vote_share)
                    * recast_rep_votes(actual, avg_contested_vote)
                    / vote_share
                ),
            )
            return recast
    else:
        return actual["DEM_V"]


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
