#
# PROCESS CONGRESSIONAL ELECTIONS
#

from pathlib import Path

from states import *
from settings import *
from helpers import *
from utils import *
from metrics import *


def main():
    # Read in elections

    cwd = Path.cwd()
    mod_path = Path(__file__).parent
    relative_path = '../data/analysis/elections.csv'
    filename = (mod_path / relative_path).resolve()
    elections_by_year = read_elections(filename)


    # Process each election

    for item in elections_by_year:
        year = item['YEAR']
        xx = item['XX']
        actual = item['DEM_S']
        rep_s = item['REP_S']
        dem_s = item['DEM_S']
        oth_s = item['OTH_S']
        tot_s = item['TOT_S']
        N = item['TWO_S']       # Two-party seats
        Vf = item['VOTE_%']     # Two-party vote-share
        Sf = item['SEAT_%']     # Two-party seat-share


        # Process each election

        multiple_districts = True if (tot_s > 1) else False
        by_state[xx]['N'] = tot_s                               # HACK - Changes w/ Census, but not for the one CD states

        two_party_seats = True if (N > 0) else False
        count_unearned = multiple_districts and two_party_seats

        # Calculate unearned seats for states with multiple districts, and
        # elections in which there were at least one two-party seat
        if (count_unearned):
            best = best_seats(N, Vf)
            ue = unearned_seats(best, actual)
            tot = 'REP_UE' if (ue > 0) else 'DEM_UE'

        if (year == 2000):
            if (count_unearned):
                by_state[xx]['2000'] = ue

                totals[tot]['2000'] += ue
                totals['NET_UE']['2000'] += ue
            elif (not multiple_districts):
                by_state[xx]['2000'] = single_seat(rep_s, dem_s)

            totals['REP']['2000'] += rep_s
            totals['DEM']['2000'] += dem_s
            totals['OTH']['2000'] += oth_s
            totals['TOT']['2000'] += tot_s
        else:
            cycle = '2012-20' if (year > 2010) else '2002-10'
            base = 2012 if (year > 2010) else 2002
            offset = int((year - base) / 2)
        
            if (count_unearned):
                by_state[xx][cycle][offset] = ue

                totals[tot][cycle][offset] += ue
                totals['NET_UE'][cycle][offset] += ue
            elif (not multiple_districts):
                by_state[xx][cycle][offset] = single_seat(rep_s, dem_s)

            totals['REP'][cycle][offset] += rep_s
            totals['DEM'][cycle][offset] += dem_s
            totals['OTH'][cycle][offset] += oth_s
            totals['TOT'][cycle][offset] += tot_s

        # NOTE - Not that many antimajoritarian results
        # if (isAntimajoritarian(Vf, Sf)):
        #     print("{0} in {1} was antimajoritarian: R = {2:5.2}".format(xx, year, bigR(Vf, Sf)))
    

    # Post-process the totals

    # TODO - Expected R & D
    # TODO - Slack
    # TODO - Margin

    # Format the results as a CSV
    
    print()
    print_header()
    for key in by_state:
        if (by_state[key]['N'] > 1):
            print_row(key, by_state[key])
    for key in by_state:
        if (by_state[key]['N'] < 2):
            print_row(key, by_state[key])
    for key in totals:
        print_row(key, totals[key])
    print()


# Execute the script
main()