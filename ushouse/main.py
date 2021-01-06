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


    # Analyze each election

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

        two_party_seats = True if (N > 0) else False

        if (two_party_seats):
            best = best_seats(N, Vf)
            ue = unearned_seats(best, actual)
            ue_tot = 'REP_UE' if (ue > 0) else 'DEM_UE'

        if (year == 2000):
            if (two_party_seats):
                by_state[xx]['UE_2000'] = ue
                by_state[ue_tot]['UE_2000'] += ue
                by_state['NET_UE']['UE_2000'] += ue

            by_state['REP']['UE_2000'] += rep_s
            by_state['DEM']['UE_2000'] += dem_s
            by_state['OTH']['UE_2000'] += oth_s
            by_state['TOT']['UE_2000'] += tot_s
        else:
            cycle = 'UE_2012_20' if (year > 2010) else 'UE_2002_10'
            base = 2012 if (year > 2010) else 2002
            offset = int((year - base) / 2)
        
            if (two_party_seats):
                by_state[xx][cycle][offset] = ue
                by_state[ue_tot][cycle][offset] += ue
                by_state['NET_UE'][cycle][offset] += ue

            by_state['REP'][cycle][offset] += rep_s
            by_state['DEM'][cycle][offset] += dem_s
            by_state['OTH'][cycle][offset] += oth_s
            by_state['TOT'][cycle][offset] += tot_s

        # NOTE - Not that many antimajoritarian results
        # if (isAntimajoritarian(Vf, Sf)):
        #     print("{0} in {1} was antimajoritarian: R = {2:5.2}".format(xx, year, bigR(Vf, Sf)))
    

    # Format the results as a CSV
    
    print()
    print('XX, STATE, UE_2000, UE_2002, UE_2004, UE_2006, UE_2008, UE_2010, UE_2012, UE_2014, UE_2016, UE_2018, UE_2020')
    for key in by_state:
        print(
            "{0},".format(key),
            "{0},".format(by_state[key]['Name']),
            "{0},".format(by_state[key]['UE_2000']),
            "{0},".format(by_state[key]['UE_2002_10'][0]),
            "{0},".format(by_state[key]['UE_2002_10'][1]),
            "{0},".format(by_state[key]['UE_2002_10'][2]),
            "{0},".format(by_state[key]['UE_2002_10'][3]),
            "{0},".format(by_state[key]['UE_2002_10'][4]),
            "{0},".format(by_state[key]['UE_2012_20'][0]),
            "{0},".format(by_state[key]['UE_2012_20'][1]),
            "{0},".format(by_state[key]['UE_2012_20'][2]),
            "{0},".format(by_state[key]['UE_2012_20'][3]),
            "{0}".format(by_state[key]['UE_2012_20'][4])
        )
    print()


# Execute the script
main()