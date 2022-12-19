#!/usr/bin/env python3
#
# PROCESS CONGRESSIONAL ELECTIONS
#

from pathlib import Path

from ushouse import *

# from .states import *
# from .settings import *
# from .readwrite import *
# from .utils import *
# from .metrics import *


def main():
    # Read in elections

    cwd = Path.cwd()
    mod_path = Path(__file__).parent
    relative_path = "../data/analysis/elections.csv"
    filename = (mod_path / relative_path).resolve()
    elections_by_year = read_election(filename)

    # Process each election

    for item in elections_by_year:
        # Map names
        year = item["YEAR"]
        xx = item["XX"]
        actual = item["DEM_S"]
        rep_s = item["REP_S"]
        dem_s = item["DEM_S"]
        oth_s = item["OTH_S"]
        tot_s = item["TOT_S"]
        N = item["TWO_S"]  # Two-party seats
        Vf = item["VOTE_%"]  # Two-party vote-share
        Sf = item["SEAT_%"]  # Two-party seat-share

        # Calculate the election offset
        base = 2000
        offset = int((year - base) / 2)

        # Accumulate totals
        totals["REP"]["Elections"][offset] += rep_s
        totals["DEM"]["Elections"][offset] += dem_s
        totals["OTH"]["Elections"][offset] += oth_s
        totals["TOT"]["Elections"][offset] += tot_s
        # TODO - More ... <<< Not sure what I was thinking here.

        # Calculate unearned seats for states with multiple districts, and
        # elections in which there were at least one two-party seat.
        # Also capture advantage in single-district states.
        multiple_districts = True if (tot_s > 1) else False
        by_state[xx][
            "N"
        ] = tot_s  # HACK - Changes w/ Census, but not for the one CD states
        two_party_seats = True if (N > 0) else False
        count_unearned = multiple_districts and two_party_seats

        if count_unearned:
            best = best_seats(N, Vf)
            ue = unearned_seats(best, actual)
            tot = "REP_UE" if (ue > 0) else "DEM_UE"

            by_state[xx]["Elections"][offset] = ue
            totals[tot]["Elections"][offset] += ue
            totals["NET_UE"]["Elections"][offset] += ue
        elif not multiple_districts:
            by_state[xx]["Elections"][offset] = single_seat(rep_s, dem_s)

        # NOTE - Not that many antimajoritarian results
        # if (isAntimajoritarian(Vf, Sf)):
        #     print("{0} in {1} was antimajoritarian: R = {2:5.2}".format(xx, year, bigR(Vf, Sf)))

    # Post-process the totals

    for i in range(N_ELECTIONS):
        actual_R = totals["REP"]["Elections"][i]
        actual_D = totals["DEM"]["Elections"][i]
        net_UE = totals["NET_UE"]["Elections"][i]

        expected_R = expected_R_seats(actual_R, net_UE)
        totals["REP_EXP"]["Elections"][i] = expected_R
        totals["DEM_EXP"]["Elections"][i] = expected_D_seats(expected_R)
        totals["SLACK"]["Elections"][i] = slack(expected_R)
        totals["MARGIN"]["Elections"][i] = margin(actual_R, actual_D)

    # Format the results as a CSV

    print()
    print_header()
    for key in by_state:
        if by_state[key]["N"] > 1:
            print_row(key, by_state[key])
    for key in by_state:
        if by_state[key]["N"] < 2:
            print_row(key, by_state[key])
    for key in totals:
        print_row(key, totals[key])
    print()


# Execute the script
main()
