#!/usr/bin/env python3

"""
Impute results for uncontested races & revise election results to include them.
"""

from ushouse import *


# Housekeeping

input_root: str = "data/extracted/"
# election_root: str = "data/results/"
election_root: str = "temp/"  # TODO: Change this back to "data/results/"
snapshoot_root: str = "data/results/snapshots/"

results_types: list = [str, str, int, int, int, int, int, int, int, int]
uncontested_types: list = [str, str, str, int, int, int, int, int, int, int]


def input_file(year: str, congress: str, category: str) -> str:
    """
    Congressional Election Results by State (2000 - 107th) RESULTS.csv
    Congressional Election Results by State (2000 - 107th) UNCONTESTED.csv
    """
    return (
        f"Congressional Election Results by State ({year} - {congress}) {category}.csv"
    )


def output_file(year: str, congress: str) -> str:
    """
    Congressional Elections (2000 - 107th).csv
    """
    return f"Congressional Elections ({year} - {congress}).csv"


avg_contested_proxies: dict[str, dict[str, int]] = {
    "2008": {"AL": 271654, "AR": 271654, "VT": 325046},
    "2016": {"ND": 344360, "SD": 344360},
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

    # Read the data
    results_csv: str = input_file(year, congress, "RESULTS")
    uncontested_csv: str = input_file(year, congress, "UNCONTESTED")

    results_official: list = read_typed_csv(input_root + results_csv, results_types)
    uncontested_races: list = read_typed_csv(
        input_root + uncontested_csv, uncontested_types
    )

    # Calculate the average contested votes by state.
    proxies: dict = avg_contested_proxies[year] if year in avg_contested_proxies else {}
    avg_contested_vote: dict = calc_avg_contested_votes(
        results_official, uncontested_races, proxies
    )

    # Impute revised votes for uncontested races & convert them to offsets.
    uncontested_revised: list = revise_uncontested_races(
        uncontested_races, avg_contested_vote
    )

    # Aggregate the offsets by state.
    uncontested_offsets: dict = agg_uncontested(
        uncontested_revised, ["REP_V", "DEM_V", "OTH_V", "TOT_V"]
    )

    # Apply the offsets to the official results by state.
    results_revised: list = apply_imputed_offsets(results_official, uncontested_offsets)

    # Make sure the output is sorted by state (name).
    results_revised = sorted(results_revised, key=lambda x: x["STATE"])
    cols: list = results_revised[0].keys()

    # Write the revised results to a CSV file.
    election_csv: str = output_file(year, congress)
    write_csv(election_root + election_csv, results_revised, cols)

print("Done.")
pass
