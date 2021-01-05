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
    # Setup by-state pivot
    by_state = {}
    for s in states:
        xx = s['XX']
        by_state[xx] = {}
        by_state[xx]['Name'] = s['State']
        by_state[xx]['UE_2000'] = None
        by_state[xx]['UE_2002_10'] = [None] * 5
        by_state[xx]['UE_2012_20'] = [None] * 5

    # Read in elections
    cwd = Path.cwd()
    mod_path = Path(__file__).parent
    relative_path = '../data/results/Congressional Elections (2000 - 2020).csv'
    filename = (mod_path / relative_path).resolve()
    elections_by_year = read_elections(filename)

    # Analyze each election
    for item in elections_by_year:
        year = item['YEAR']
        xx = item['XX']

        best = best_seats(item['REPS'], item['VOTE_%'])
        actual = item['DEM_S']
        ue = unearned_seats(best, actual)

        if (year == 2000):
            by_state[xx]['UE_2000'] = ue
        elif ((year > 2000) and (year < 2012)):
            i = int((year - 2002) / 2)
            by_state[xx]['UE_2002_10'][i] = ue
        else:  # 2012–2020
            i = int((year - 2012) / 2)
            by_state[xx]['UE_2012_20'][i] = ue
    
    # TODO

    # Format the results as a CSV
    print('XX', 'STATE', 'UE_2000', 'UE_2002', 'UE_2004', 'UE_2006', 'UE_2008', 'UE_2010', 'UE_2012', 'UE_2014', 'UE_2016', 'UE_2018', 'UE_2020')
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