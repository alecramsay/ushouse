#
# PROCESS CONGRESSIONAL ELECTIONS
#

from pathlib import Path

from helpers import *


def main():
    print()

    cwd = Path.cwd()
    mod_path = Path(__file__).parent
    relative_path = '../data/results/Congressional Elections (2000 - 2020).csv'
    filename = (mod_path / relative_path).resolve()
    
    elections_by_year = read_elections(filename)

    count = 0
    for item in elections_by_year:
      count += 1

    print()
    print(count, "elections with two or more congressional districts. ")

    print()
    pass


# Execute the script
main()