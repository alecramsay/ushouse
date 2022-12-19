#!/usr/bin/env python3

"""
Impute results for uncontested races & revise election results to include them.
"""

from ushouse import *


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


# 2000
results_csv: str = file_name("2000", "107th", "RESULTS")
uncontested_csv: str = file_name("2000", "107th", "UNCONTESTED")

results: list = read_typed_csv(input_root + results_csv, results_types)
uncontested: list = read_typed_csv(input_root + uncontested_csv, uncontested_types)

pass

# 2002

# 2004

# 2006

# 2008
avg_uncontested_proxies: dict[str, int] = {"AL": 271654, "VT": 325046}

# 2010

# 2012

# 2014

# 2016
avg_uncontested_proxies: dict[str, int] = {"SD": 344360}

# 2018

# 2020
avg_uncontested_proxies: dict[str, int] = {"SD": 422609}

pass
