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
                tot_s = int(row['TOT_S'])

                if (tot_s > 1):
                    year = int(row['YEAR'])
                    state = row['STATE']
                    xx = row['XX']
                    # rep_v = int(row['REP_V']) 
                    # dem_v = int(row['DEM_V'])
                    # oth_v = int(row['OTH_V'])
                    # tot_v = int(row['TOT_V']) 
                    # rep_s = int(row['REP_S'])
                    # dem_s = int(row['DEM_S']) 
                    oth_s = int(row['OTH_S']) 

                    vote_share = float(row['VOTE_%'].strip("'"))
                    seat_share = float(row['SEAT_%'].strip("'"))

                    if (oth_s > 0):
                        print("One or more independent reps elected:", xx, year)

                    election = {
                        "YEAR": year,
                        "STATE": state,
                        "XX": xx,
                        # "REP_V": int(row['REP_V']), 
                        # "DEM_V": int(row['DEM_V']), 
                        # "OTH_V": int(row['OTH_V']), 
                        # "TOT_V": int(row['TOT_V']), 
                        # "REP_S": int(row['REP_S']), 
                        # "DEM_S": int(row['DEM_S']), 
                        # "OTH_S": int(row['OTH_S']), 
                        "REPS": tot_s - oth_s,         # Two-party seat total
                        "VOTE_%": vote_share,          # Two-party vote share
                        "SEAT_%": seat_share           # Two-party seat share
                    }
                    elections_by_year.append(election)

    except Exception as e:
        print("Exception reading elections CSV")
        sys.exit(e)

    return elections_by_year 