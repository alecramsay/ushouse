#!/usr/bin/env python3

import sys
import csv


def read_elections(elections_csv):
    """
    Read a CSV of congressional election results with columns;
    YEAR, STATE, XX, REP_V, DEM_V, OTH_V, TOT_V, REP_S, DEM_S, OTH_S, TOT_S, VOTE_%, SEAT_%
    """

    elections_by_year = []

    try:
        with open(elections_csv, mode="r", encoding="utf-8-sig") as f_input:
            csv_file = csv.DictReader(f_input)

            count = 0
            for row in csv_file:
                elections_by_year.append(row)
                count += 1

    except Exception as e:
        print("Exception reading elections CSV")
        sys.exit(e)

    print("")
    print(count, "election rows read.")
    print("")

    return elections_by_year 