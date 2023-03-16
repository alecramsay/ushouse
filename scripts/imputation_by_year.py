#!/usr/bin/env python3

"""
Summarize the results of imputing uncontested races by year.

For example:

$ scripts/imputation_by_year.py

For documentation, type:

$ scripts/impute_election.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

from ushouse import *


### ARGS ###

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
    "2022",
]

extracted_root: str = "data/extracted/"
election_root: str = "data/results/"
output_root: str = "data/analysis/"

official_types: list = [str, str, int, int, int, int, int, int, int, int]
uncontested_types: list = [str, str, str, int, int, int, int, int, int, int]
imputed_types: list = [str] * 3 + [int] * 8 + [float] * 2


### HELPERS ###


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


def sum_national_totals(elections: list) -> None:
    """Aggregate national election totals"""

    totals: dict = {
        "REP_V": 0,
        "DEM_V": 0,
        "REP_S": 0,
        "DEM_S": 0,
        "OTH_S": 0,
    }

    for state in elections:
        totals["REP_V"] += state["REP_V"]
        totals["DEM_V"] += state["DEM_V"]
        totals["REP_S"] += state["REP_S"]
        totals["DEM_S"] += state["DEM_S"]
        totals["OTH_S"] += state["OTH_S"]

    return totals


### SUMMARIZE EACH YEAR

rows: list = list()
for year in years:
    # Read the data

    if year == "2022":
        extracted_root = "/Users/alecramsay/Downloads/"
        election_root = "/Users/alecramsay/Downloads/"

    congress: str = congresses[year]

    official_csv: str = extracted_file(year, congress, "RESULTS")
    uncontested_csv: str = extracted_file(year, congress, "UNCONTESTED")
    imputed_csv: str = election_file(year, congress)

    official_results: list = read_csv(extracted_root + official_csv, official_types)
    uncontested_races: list = read_csv(
        extracted_root + uncontested_csv, uncontested_types
    )

    imputed_results: list = read_csv(election_root + imputed_csv, imputed_types)

    # Summarize the data

    row: dict = {"YEAR": year}

    n_uncontesteds: int = 0
    for i, item in enumerate(uncontested_races):
        if item["REP_S"] == 1 or item["DEM_S"] == 1:
            n_uncontesteds += 1

    row["UNCONTESTED"] = n_uncontesteds

    totals: dict = sum_national_totals(official_results)
    official_Vf: float = totals["DEM_V"] / (totals["REP_V"] + totals["DEM_V"])
    row["VOTE_%"] = official_Vf

    totals: dict = sum_national_totals(imputed_results)
    imputed_Vf: float = totals["DEM_V"] / (totals["REP_V"] + totals["DEM_V"])
    row["VOTE_%'"] = imputed_Vf

    rows.append(row)

# Write the results to a CSV file

report_csv: str = "uncontested_imputation_by_year.csv"
cols: list = list(rows[0].keys())
write_csv(output_root + report_csv, rows, cols)

### END ###
