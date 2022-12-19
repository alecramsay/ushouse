#!/usr/bin/env python3
#
# The logic for imputing results for uncontested elections.
#

# TODO


"""
INPUT DATA -- for each uncontested race
----------

Uncontested Votes:
- Column D: REP1
- Column E: DEM1
- Column F: OTH1
- Column G: TOT1

Uncontested Seats (Races):
- Column H: REP2
- Column I: DEM2
- Column J: OTH2

Imputed Vote Shares:
- Column K: REP win %
- Column L: DEM win %
- Column M: Contested AVG Votes

example: dict = {
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

"""


"""
RECAST -- Impute the uncontested votes
------

Given a dict of the input data above, recast it into these columns:

- Column N: REP3
- Column O: DEM3
- Column P: OTH3 -- 0
- Column Q: TOT3 -- =SUM(N3:P3)

NOTE - The two formulates are interdependent. They work, because the if/else blocks
complement each other in the two functions.

"""


def recast_uncontested_votes(data: dict) -> dict:
    """
    Recast actual uncontested votes into imputed votes.
    """

    recast: dict = dict()

    recast["REP3"] = recast_rep_votes(data)
    recast["DEM3"] = recast_dem_votes(data)
    recast["OTH3"] = 0
    recast["TOT3"] = recast["REP3"] + recast["DEM3"] + recast["OTH3"]

    return recast


def recast_rep_votes(data: dict, vote_share: float = 0.70) -> int:
    """
    Formula for REP3 (Column N):

    =IF(G3>0,IF(H3>0,MAX(D3,ROUND(K3*M3,0)),MAX(F3,ROUND((1-L3)*(O3/L3),0))),D3)

    -or-

    IF(G3>0,
    IF(H3>0,
        MAX(D3,ROUND(K3*M3,0)),
        MAX(F3,ROUND((1-L3)*(O3/L3),0))),
    D3)
    """

    if data["TOT1"] > 0:  #
        # For states w/ uncontested races
        if data["REP2"] > 0:
            # If a Republican won the uncontested seat,
            # use their actual votes or the imputed votes, whichever is higher
            recast: int = max(
                data["REP1"], round(vote_share * data["Contested_AVG_Votes"])
            )
            return recast
        else:
            # If a Democrat won the uncontested seat,
            # use the actual "other" vote total or the imputed votes, whichever is higher
            # TODO - This total must be at least one less than the winning total
            recast: int = max(
                data["OTH1"],
                round((1 - vote_share) * (recast_dem_votes(data) / vote_share)),
            )
            return recast
    else:
        # For states w/o uncontested races
        return data["REP1"]


def recast_dem_votes(data: dict, vote_share: float = 0.70) -> int:
    """
    Formula for DEM3 (Column O):

    =IF(G3>0,IF(I3>0,MAX(E3,ROUND(L3*M3,0)),MAX(F3,ROUND((1-K3)*(N3/K3),0))),E3)
    """

    if data["TOT1"] > 0:
        # For states w/ uncontested races
        if data["DEM2"] > 0:
            # If a Democrat won the uncontested seat,
            # use their actual votes or the imputed votes, whichever is higher
            recast: int = max(
                data["DEM1"], round(vote_share * data["Contested_AVG_Votes"])
            )
            return recast
        else:
            # If a Republican won the uncontested seat,
            # use the actual "other" vote total or the imputed votes, whichever is higher
            # TODO - This total must be at least one less than the winning total
            recast: int = max(
                data["OTH1"],
                round((1 - vote_share) * recast_rep_votes(data) / vote_share),
            )
            return recast
    else:
        # For states w/o uncontested races
        return data["DEM1"]


"""
ADJUSTMENTS -- Compute offsets to the actual votes to realize the imputed values.
-----------

- Column R: REP4
- Column S: DEM4
- Column T: OTH4
- Column U: TOT4
"""


def calc_imputed_offsets(actual_data: dict, recast_data: dict) -> dict:
    """
    Formulas for REP4, DEM4, OTH4, & TOT4:

    =N3-D3
    =O3-E3
    =P3-F3
    =Q3-G3

    """

    offsets: dict = dict()

    offsets["REP4"] = recast_data["REP3"] - actual_data["REP1"]
    offsets["DEM4"] = recast_data["DEM3"] - actual_data["DEM1"]
    offsets["OTH4"] = recast_data["OTH3"] - actual_data["OTH1"]
    offsets["TOT4"] = recast_data["TOT3"] - actual_data["TOT1"]

    return offsets


"""
REVISED -- Pivot the offsets by state and apply them to the actual votes.
"""

### END ###
