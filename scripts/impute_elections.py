#!/usr/bin/env python3

"""
Impute results for uncontested races & revise election results to include them.
"""

from ushouse import *


# Housekeeping

input_root: str = "data/extracted/"
election_root: str = "data/results/"
snapshoot_root: str = "data/results/snapshots/"

results_types: list = [str, str, int, int, int, int, int, int, int, int]
uncontested_types: list = [str, str, str, int, int, int, int, int, int, int]


def file_name(year: str, congress: str, category: str) -> str:
    """
    Congressional Election Results by State (2000 - 107th) RESULTS.csv
    Congressional Election Results by State (2000 - 107th) UNCONTESTED.csv
    """
    return (
        f"Congressional Election Results by State ({year} - {congress}) {category}.csv"
    )


avg_contested_proxies: dict[str, dict[str, int]] = {
    "2008": {"AL": 271654, "VT": 325046},
    "2016": {"SD": 344360},
    "2020": {"SD": 422609},
}

# Revise official election data to include imputed results for uncontested races.

years: list[str] = [
    "2000",
    "2002",
    "2004",
    "2006",
    "2008",
    "2010",
    "2012",
    "2014",
    "2016",
    "2018",
    "2020",
]
congresses: list[str] = [
    "107th",
    "108th",
    "109th",
    "110th",
    "111th",
    "112th",
    "113th",
    "114th",
    "115th",
    "116th",
    "117th",
]

for year, congress in zip(years, congresses):
    print(f"Processing {year} {congress}...")
    results_csv: str = file_name(year, congress, "RESULTS")
    uncontested_csv: str = file_name(year, congress, "UNCONTESTED")

    results: list = read_typed_csv(input_root + results_csv, results_types)
    uncontested: list = read_typed_csv(input_root + uncontested_csv, uncontested_types)

    pass

print("Done.")
pass
