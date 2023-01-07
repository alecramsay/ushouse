#!/usr/bin/env python3
#
# READ/WRITE SUPPORT
#

import os
import sys
import csv
from csv import DictReader, DictWriter
import contextlib
from typing import Any, Generator, TextIO


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


def cast(t, v_str) -> str | int | float:
    # HACK - For thease files, treat missing values as 0.
    if t == int and (len(v_str) == 0 or v_str == " "):
        return 0
    return t(v_str)


def write_csv(rel_path, rows, cols) -> None:
    try:
        cf: str | None = FileSpec(rel_path).abs_path if (rel_path is not None) else None

        with smart_open(cf) as f:
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


@contextlib.contextmanager
def smart_open(filename=None) -> Generator[TextIO | TextIO, None, None]:
    """
    Patterned after: https://stackoverflow.com/questions/17602878/how-to-handle-both-with-open-and-sys-stdout-nicely
    """
    if filename and filename != "-":
        fh: TextIO = open(filename, "w")
    else:
        fh = sys.stdout

    try:
        yield fh
    finally:
        if fh is not sys.stdout:
            fh.close()


### ANALYSIS INPUT HELPERS ###


def read_election(rel_path: str, invert: bool = False) -> list:
    """
    Read a CSV of congressional election results with columns;
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


### MISCELLANEOUS ###


class FileSpec:
    def __init__(self, path: str, name=None) -> None:
        file_name: str
        file_extension: str
        file_name, file_extension = os.path.splitext(path)

        self.rel_path: str = path
        self.abs_path: str = os.path.abspath(path)
        self.name: str = name.lower() if (name) else os.path.basename(file_name).lower()
        self.extension: str = file_extension


### END ###
