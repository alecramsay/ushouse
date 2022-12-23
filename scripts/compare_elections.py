#!/usr/bin/env python3

"""
Compare pairs of revised elections incorporating imputed results for uncontested races:
- What I produced manually using a spreadsheet, and
- What I produced using the new code.

For example:

$ scripts/compare_elections.py 2006
$ scripts/compare_elections.py 2006 > temp/compare (2006).txt

"""

import argparse
from argparse import ArgumentParser, Namespace

from ushouse import *


### PARSE ARGS ###

parser: ArgumentParser = argparse.ArgumentParser(
    description="Compare revised elections"
)

parser.add_argument("year", help="The election year", type=str)
parser.add_argument(
    "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
)

args: Namespace = parser.parse_args()

#

year: str = args.year
congress: str = congresses[year]

election_root: str = "data/results/"
snapshot_root: str = "data/results/OLD/results/"


def input_file(year: str, congress: str) -> str:
    """
    Congressional Elections (2000 - 107th).csv
    """
    return f"Congressional Elections ({year} - {congress}).csv"


print(
    "FILE,YEAR,STATE,XX,REP_V,DEM_V,OTH_V,TOT_V,REP_S,DEM_S,OTH_S,TOT_S,VOTE_%,SEAT_%"
)

new_elections: list[dict[str, Any]] = read_election(
    election_root + input_file(year, congress)
)

old_elections: list[dict[str, Any]] = read_election(
    snapshot_root + input_file(year, congress), invert=True
)

for new, old in zip(new_elections, old_elections):
    if not dict_close(new, old):
        new_values: str = ",".join(["New"] + [str(x) for x in list(new.values())])
        old_values: str = ",".join(["Old"] + [str(x) for x in list(old.values())])
        print(new_values)
        print(old_values)

pass
