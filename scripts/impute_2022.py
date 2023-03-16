#!/usr/bin/env python3

"""
>>> 2022 HACK <<<

Impute results for uncontested races & revise election results to include them.

For example:

$ scripts/impute_2022.py

"""

from ushouse import *


### PARSE ARGS ###

year: str = "2022"
congress: str = congresses[year]

avg_contested_proxies: dict[str, dict[str, int]] = {
    "2008": {"AL": 271654, "AR": 271654, "VT": 325046},
    "2016": {"ND": 344360, "SD": 344360},
    "2020": {"SD": 422609},
    "2022": {"ND": 240140, "SD": 348020},
}


# Housekeeping


# HACK - use local files
extracted_root: str = "/Users/alecramsay/Downloads/data/extracted/"
imputed_root: str = "/Users/alecramsay/Downloads/data/imputed/"
election_root: str = "/Users/alecramsay/Downloads/data/results/"

results_types: list = [str, str, int, int, int, int, int, int, int, int]
uncontested_types: list = [str, str, str, int, int, int, int, int, int, int]


# Helpers


def extracted_file(year: str, congress: str, category: str) -> str:
    """
    Congressional Election Results by State (2000 - 107th) RESULTS.csv
    Congressional Election Results by State (2000 - 107th) UNCONTESTED.csv
    """
    return (
        f"Congressional Election Results by State ({year} - {congress}) {category}.csv"
    )


def election_file(year: str, congress: str) -> str:
    """
    Congressional Elections (2000 - 107th).csv
    """
    return f"Congressional Elections ({year} - {congress}).csv"


# Read the data


results_csv: str = extracted_file(year, congress, "RESULTS")
uncontested_csv: str = extracted_file(year, congress, "UNCONTESTED")

results_official: list = read_csv(extracted_root + results_csv, results_types)
uncontested_races: list = read_csv(extracted_root + uncontested_csv, uncontested_types)

### Impute the results for uncontested races ###

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

# Add the year as the first column.
results_out: list = list()
for row in results_revised:
    row_out: dict = {"YEAR": year}
    row_out.update(row)
    results_out.append(row_out)

# Write the revised results to a CSV file.
election_csv: str = election_file(year, congress)
cols: list = ["YEAR"] + list(results_revised[0].keys())
write_csv(election_root + election_csv, results_out, cols)

# Write the imputed results to a CSV file.
uncontested_csv: str = extracted_file(year, congress, "UNCONTESTED")
cols: list = list(uncontested_revised[0].keys())
write_csv(imputed_root + uncontested_csv, uncontested_revised, cols)

pass
