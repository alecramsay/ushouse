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

            n_elections = 0
            n_other_significant = 0
            for row in csv_file:
                year = int(row['YEAR'])

                bElections = True if (year != 2000) else False
                if (bElections):
                    n_elections += 1

                state = row['STATE']
                xx = row['XX']
  
                rep_v = int(row['REP_V']) 
                dem_v = int(row['DEM_V'])
                oth_v = int(row['OTH_V'])
                tot_v = int(row['TOT_V']) 
                rep_s = int(row['REP_S'])
                dem_s = int(row['DEM_S']) 
                oth_s = int(row['OTH_S'])
                tot_s = int(row['TOT_S'])

                # TODO - Figure out what to do about NY
                bOtherSignificant = True if ((oth_s > 0) or ((oth_v / tot_v) > 0.1)) else False
                if (bOtherSignificant):
                    n_other_significant += 1
                    print("Dropping the {0} election for {1}, because 'other' vote was significant. ".format(year, xx))

                if (not bOtherSignificant):
                    vote_share = float(row['VOTE_%'].strip("'"))
                    seat_share = float(row['SEAT_%'].strip("'"))

                    # All these elections will have two-party vote- & seat-shares
                    election = {
                        "YEAR": year,
                        "STATE": state,
                        "XX": xx,
                        # "REP_V": int(row['REP_V']), 
                        # "DEM_V": int(row['DEM_V']), 
                        # "OTH_V": int(row['OTH_V']), 
                        # "TOT_V": int(row['TOT_V']), 
                        # "REP_S": int(row['REP_S']), 
                        "DEM_S": int(row['DEM_S']), 
                        # "OTH_S": int(row['OTH_S']), 
                        "REPS": tot_s - oth_s,         # Two-party seat total
                        "VOTE_%": vote_share,          # Two-party DEM vote share
                        "SEAT_%": seat_share           # Two-party DEM seat share
                    }
                    elections_by_year.append(election)

        print()
        print(n_elections, "year-state election combinations.")
        print("Less", n_other_significant, "elections with 'other' wins or significant 'other' showings.")
        print("Leaving a sample of", n_elections - n_other_significant, "elections.")
        print()

    except Exception as e:
        print("Exception reading elections CSV")
        sys.exit(e)

    return elections_by_year 
