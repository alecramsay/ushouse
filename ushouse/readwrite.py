#!/usr/bin/env python3

"""
READ/WRITE HELPERS
"""

import sys
import csv
from csv import DictReader
from pyutils import (
    FileSpec,
    file_name,
    path_to_file,
    read_csv,
    write_csv,
    read_shapes,
    write_pickle,
    read_pickle,
    smart_open,
)
from typing import Any


### ANALYSIS INPUT HELPERS ###


def read_election(rel_path: str, invert: bool = False) -> list:
    """Read a CSV of congressional election results & tranform it into the format we need.

    The columns are:
    YEAR, STATE, XX, REP_V, DEM_V, OTH_V, TOT_V, REP_S, DEM_S, OTH_S, TOT_S, VOTE_%, SEAT_%
    """

    abs_path: str = FileSpec(rel_path).abs_path
    elections: list = list()

    try:
        with open(abs_path, mode="r", encoding="utf-8-sig") as f_input:
            csv_file: DictReader[str] = csv.DictReader(f_input)

            for row in csv_file:
                year: str = row["YEAR"]

                state: str = row["STATE"]
                xx: str = row["XX"]

                rep_v: int = int(row["REP_V"])
                dem_v: int = int(row["DEM_V"])
                oth_v: int = int(row["OTH_V"])
                tot_v: int = int(row["TOT_V"])
                rep_s: int = int(row["REP_S"])
                dem_s: int = int(row["DEM_S"])
                oth_s: int = int(row["OTH_S"])
                tot_s: int = int(row["TOT_S"])

                vote_share: float
                seat_share: float
                digits: int = 4
                if oth_s < tot_s:
                    # D and/or R wins
                    if invert:
                        # NOTE - Invert REP shares to DEM shares <<< legacy files
                        vote_share = round(
                            1.0 - float(row["VOTE_%"].strip("'")), digits
                        )
                        seat_share = round(
                            1.0 - float(row["SEAT_%"].strip("'")), digits
                        )
                    else:
                        vote_share = round(float(row["VOTE_%"].strip("'")), digits)
                        seat_share = round(float(row["SEAT_%"].strip("'")), digits)
                else:
                    # Only 3rd-party wins
                    vote_share = None
                    seat_share = None

                election: dict[str, Any] = {
                    "YEAR": year,
                    "STATE": state,
                    "XX": xx,
                    "REP_V": rep_v,
                    "DEM_V": dem_v,
                    "OTH_V": oth_v,
                    "TOT_V": tot_v,
                    "REP_S": rep_s,
                    "DEM_S": dem_s,
                    "OTH_S": oth_s,
                    "TOT_S": tot_s,
                    "VOTE_%": vote_share,
                    "SEAT_%": seat_share,
                }
                elections.append(election)

    except Exception as e:
        print("Exception reading elections CSV")
        sys.exit(e)

    return elections


### ANALYSIS OUTPUT HELPERS ###


def print_header() -> None:
    print("XX, STATE, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020")


# TODO - Update for 2022; bind to N_ELECTIONS
def print_row(key, row) -> None:
    print(
        "{0},".format(key),
        "{0},".format(row["Name"]),
        "{0},".format(row["Elections"][0]),
        "{0},".format(row["Elections"][1]),
        "{0},".format(row["Elections"][2]),
        "{0},".format(row["Elections"][3]),
        "{0},".format(row["Elections"][4]),
        "{0},".format(row["Elections"][5]),
        "{0},".format(row["Elections"][6]),
        "{0},".format(row["Elections"][7]),
        "{0},".format(row["Elections"][8]),
        "{0},".format(row["Elections"][9]),
        "{0}".format(row["Elections"][10]),
    )


### END ###
