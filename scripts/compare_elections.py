#!/usr/bin/env python3

"""
Compare pairs of revised elections incorporating imputed results for uncontested races:
- What I produced manually using a spreadsheet, and
- What I produced using the new code.

For example:

$ scripts/compare_elections.py
$ scripts/compare_elections.py > temp/comparisons.txt

"""

from ushouse import *

election_root: str = "temp/"  # TODO: Change this back to "data/results/"
snapshot_root: str = "data/results/snapshot/"


def input_file(year: str, congress: str) -> str:
    """
    Congressional Elections (2000 - 107th).csv
    """
    return f"Congressional Elections ({year} - {congress}).csv"


for year, congress in zip(years, congresses):
    print(f"Comparing {year} {congress} ...")
    print()

    new_elections: list[dict[str, Any]] = read_election(
        election_root + input_file(year, congress)
    )

    old_elections: list[dict[str, Any]] = read_election(
        snapshot_root + input_file(year, congress), invert=True
    )

    for new, old in zip(new_elections, old_elections):
        if not dict_close(new, old):
            print(f"New: {new}")
            print(f"Old: {old}")

    print()
    # break  # TODO: Remove this line

print("Done.")
pass
