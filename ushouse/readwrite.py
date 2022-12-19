#!/usr/bin/env python3
#
# READ/WRITE SUPPORT
#

import os
import sys
import csv
from csv import DictReader, DictWriter


### GENERIC CSV READ/WRITE FUNCTIONS ###


def read_typed_csv(rel_path, field_types) -> list:
    """
    Read a CSV with DictReader
    Patterned after: https://stackoverflow.com/questions/8748398/python-csv-dictreader-type
    """

    abs_path: str = FileSpec(rel_path).abs_path

    try:
        rows: list = []
        with open(abs_path, "r", encoding="utf-8-sig") as file:
            reader: DictReader[str] = DictReader(
                file, fieldnames=None, restkey=None, restval=None, dialect="excel"
            )

            for row_in in reader:
                if len(field_types) >= len(reader.fieldnames):
                    # Extract the values in the same order as the csv header
                    ivalues = map(row_in.get, reader.fieldnames)

                    # Apply type conversions
                    iconverted: list = [
                        cast(x, y) for (x, y) in zip(field_types, ivalues)
                    ]

                    # Pass the field names and the converted values to the dict constructor
                    row_out: dict = dict(zip(reader.fieldnames, iconverted))

                rows.append(row_out)

        return rows

    except:
        raise Exception("Exception reading CSV with explicit types.")


def write_csv(rel_path, rows, cols) -> None:
    try:
        abs_path: str = FileSpec(rel_path).abs_path

        with open(abs_path, "w") as f:
            writer: DictWriter = DictWriter(f, fieldnames=cols)
            writer.writeheader()

            for row in rows:
                mod: dict = {}
                for (k, v) in row.items():
                    if isinstance(v, float):
                        mod[k] = "{:.6f}".format(v)
                    else:
                        mod[k] = v
                writer.writerow(mod)

    except:
        raise Exception("Exception writing CSV.")


def cast(t, v_str) -> str | int | float:
    # HACK - For thease files, treat missing values as 0.
    if v_str == " " and t == int:
        return 0
    return t(v_str)


class FileSpec:
    def __init__(self, path: str, name=None) -> None:
        file_name: str
        file_extension: str
        file_name, file_extension = os.path.splitext(path)

        self.rel_path: str = path
        self.abs_path: str = os.path.abspath(path)
        self.name: str = name.lower() if (name) else os.path.basename(file_name).lower()
        self.extension: str = file_extension


### ANALYTSIS INPUT HELPERS ###


def read_election(elections_csv):
    """
    Read a CSV of congressional election results with columns;
    YEAR, STATE, XX, REP_V, DEM_V, OTH_V, TOT_V, REP_S, DEM_S, OTH_S, TOT_S, VOTE_%, SEAT_%
    """

    elections_by_year = []

    try:
        with open(elections_csv, mode="r", encoding="utf-8-sig") as f_input:
            csv_file = csv.DictReader(f_input)

            print()
            n_elections = 0
            n_other = 0
            for row in csv_file:
                year = int(row["YEAR"])

                bElections = True if (year != 2000) else False
                if bElections:
                    n_elections += 1

                state = row["STATE"]
                xx = row["XX"]

                rep_v = int(row["REP_V"])
                dem_v = int(row["DEM_V"])
                oth_v = int(row["OTH_V"])
                tot_v = int(row["TOT_V"])
                rep_s = int(row["REP_S"])
                dem_s = int(row["DEM_S"])
                oth_s = int(row["OTH_S"])
                tot_s = int(row["TOT_S"])

                """
                # NOTE - Not dropping elections w/ 'other' wins or significant showings
                bOtherWins = (oth_s > 0)
                bOtherSignificant = (oth_v / tot_v) > 0.1
                if (bOtherWins):
                    n_other += 1
                    print("Dropping the {0} election for {1}, because of 'other' vote: seats = {2}, vote % = {3:4.2}. ".format(year, xx, oth_s, oth_v / tot_v))
                """

                # Don't filter out any elections
                if True:
                    """
                    # To filter out results w/ 'other' wins:
                    if (not bOtherWins):

                    # To filter out states w/ only 1 CD:
                    if (tot_s > 1):
                    """

                    if oth_s < tot_s:
                        # NOTE - Convert REP shares to DEM shares
                        vote_share = 1.0 - float(row["VOTE_%"].strip("'"))
                        seat_share = 1.0 - float(row["SEAT_%"].strip("'"))
                    else:
                        vote_share = None
                        seat_share = None

                    # All these elections will have two-party vote- & seat-shares
                    election = {
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
                        "TWO_S": tot_s - oth_s,  # Two-party seats
                        "VOTE_%": vote_share,  # Two-party DEM vote share
                        "SEAT_%": seat_share,  # Two-party DEM seat share
                    }
                    elections_by_year.append(election)

        print()
        print("There are {0} year-state election combinations.".format(n_elections))
        # print("less {0} elections with 'other' wins,".format(n_other))
        # print("which leaves a sample of {0} elections.".format(n_elections - n_other))
        print()

    except Exception as e:
        print("Exception reading elections CSV")
        sys.exit(e)

    return elections_by_year


### ANALYSIS OUTPUT HELPERS ###


def print_header() -> None:
    print("XX, STATE, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020")


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
