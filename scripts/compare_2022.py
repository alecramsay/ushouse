#!/usr/bin/env python3

"""
Compare pairs of revised elections incorporating imputed results for uncontested races:
- What I produced manually using a spreadsheet, and
- What I produced using the new code.

For example:

$ scripts/compare_2022.py

"""

from ushouse import *


### PARSE ARGS ###

year: str = "2022"
congress: str = congresses[year]

# HACK - use local files
election_root: str = "/Users/alecramsay/Downloads/data/results/"
snapshot_root: str = "/Users/alecramsay/Downloads/data/results/OLD/results/"


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
    if not dict_approx_equal(new, old, int_threshold=1):
        new_values: str = ",".join(["New"] + [str(x) for x in list(new.values())])
        old_values: str = ",".join(["Old"] + [str(x) for x in list(old.values())])
        print(new_values)
        print(old_values)

pass
