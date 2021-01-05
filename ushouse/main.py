#
# PROCESS CONGRESSIONAL ELECTIONS
#

from pathlib import Path

from settings import *
from helpers import *
from metrics import *


def main():
    cwd = Path.cwd()
    mod_path = Path(__file__).parent
    relative_path = '../data/results/Congressional Elections (2000 - 2020).csv'
    filename = (mod_path / relative_path).resolve()
    
    elections_by_year = read_elections(filename)

    for item in elections_by_year:
      best = best_seats(item["REPS"], item["VOTE_%"])
      actual = item["DEM_S"]

      print("Unearned seats =", unearned_seats(best, actual))

    pass


# Execute the script
main()