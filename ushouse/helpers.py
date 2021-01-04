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

            for row in csv_file:
                n = int(row['TOT_S'])
                if (n > 1):
                    election = {
                        "YEAR": int(row['YEAR']),
                        "STATE": row['STATE'],
                        "XX": row['XX'],
                        # "REP_V": int(row['REP_V']), 
                        # "DEM_V": int(row['DEM_V']), 
                        # "OTH_V": int(row['OTH_V']), 
                        # "TOT_V": int(row['TOT_V']), 
                        # "REP_S": int(row['REP_S']), 
                        # "DEM_S": int(row['DEM_S']), 
                        # "OTH_S": int(row['OTH_S']), 
                        "NREPS": n, 
                        "VOTE_%": float(row['VOTE_%'].strip("'")), 
                        "SEAT_%": float(row['SEAT_%'].strip("'"))
                    }
                    elections_by_year.append(election)

    except Exception as e:
        print("Exception reading elections CSV")
        sys.exit(e)

    return elections_by_year 