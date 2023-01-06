#!/usr/bin/env python3
#
# ANALYZE CONGRESSIONAL ELECTIONS OVER TIME
#


from .settings import *
from .states import *
from .readwrite import *
from .metrics import *


def analyze_elections(rel_path: str):
    abs_path: str = FileSpec(rel_path).abs_path

    elections_by_year: list = read_election(abs_path)

    # Setup by-state pivot
    by_state: dict = dict()
    for s in states:
        xx: str = s["XX"]
        by_state[xx] = {}
        by_state[xx]["Name"] = s["State"]
        by_state[xx]["Elections"] = [None] * N_ELECTIONS

    # Setup totals accumulators
    totals: dict = dict()
    for t in [
        "REP",
        "DEM",
        "OTH",
        "TOT",
        "REP_UE",
        "DEM_UE",
        "NET_UE",
        "REP_EXP",
        "DEM_EXP",
        "SLACK",
        "MARGIN",
    ]:
        totals[t] = dict()
        totals[t]["Name"] = ""
        totals[t]["Elections"] = [0] * N_ELECTIONS

    # Process each election

    for election in elections_by_year:
        # Map names (to some previous usage)
        year: int = int(election["YEAR"])
        xx: str = election["XX"]
        actual: int = election["DEM_S"]
        rep_s: int = election["REP_S"]
        dem_s: int = election["DEM_S"]
        oth_s: int = election["OTH_S"]
        tot_s: int = election["TOT_S"]
        N: int = rep_s + dem_s  # election["TWO_S"]  # Two-party seats
        Vf: float = election["VOTE_%"]  # Two-party vote-share
        Sf: float = election["SEAT_%"]  # Two-party seat-share

        if xx not in by_state:
            by_state[xx] = [0] * N_ELECTIONS

        # Calculate the election offset for pivoting by election
        base: int = 2000
        offset: int = int((year - base) / 2)

        # Accumulate totals
        totals["REP"]["Elections"][offset] += rep_s
        totals["DEM"]["Elections"][offset] += dem_s
        totals["OTH"]["Elections"][offset] += oth_s
        totals["TOT"]["Elections"][offset] += tot_s

        # Calculate unearned seats for states with multiple districts, and
        # elections in which there were at least one two-party seat.
        # Also capture advantage in single-district states.
        multiple_districts: bool = True if (tot_s > 1) else False

        two_party_seats: bool = True if (N > 0) else False
        count_unearned: bool = multiple_districts and two_party_seats

        if count_unearned:
            best: int = best_seats(N, Vf)
            ue: int = unearned_seats(best, actual)
            tot: str = "REP_UE" if (ue > 0) else "DEM_UE"

            by_state[xx]["Elections"][offset] = ue
            totals[tot]["Elections"][offset] += ue
            totals["NET_UE"]["Elections"][offset] += ue
        elif not multiple_districts:
            by_state[xx]["Elections"][offset] = single_seat(rep_s, dem_s)

    # Post-process the totals

    for i in range(N_ELECTIONS):
        actual_R: int = totals["REP"]["Elections"][i]
        actual_D: int = totals["DEM"]["Elections"][i]
        # NOTE - NET_UE here accumulates net state results. It does *not* look
        # total national vote by party.
        net_UE: int = totals["NET_UE"]["Elections"][i]

        expected_R: int = expected_R_seats(actual_R, net_UE)
        totals["REP_EXP"]["Elections"][i] = expected_R
        totals["DEM_EXP"]["Elections"][i] = expected_D_seats(expected_R)
        totals["SLACK"]["Elections"][i] = slack(expected_R)
        totals["MARGIN"]["Elections"][i] = margin(actual_R, actual_D)

    return by_state, totals


### END ###
