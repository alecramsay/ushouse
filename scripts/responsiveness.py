#!/usr/bin/env python3

"""
ESTIMATE RESPONSIVENESS FOR 2012-202O ELECTIONS BY STATE
"""

import scipy.stats
from ushouse import *


input_root: str = "data/results/"
output_root: str = "data/analysis/"


def input_file(year: str, congress: str) -> str:
    """
    Congressional Elections (2000 - 107th).csv
    """
    return f"Congressional Elections ({year} - {congress}).csv"


### PIVOT Vf & Sf BY STATE (LONGITUDINALLY) ###

by_state: dict = dict()
for xx in state_codes:
    by_state[xx] = {"Vf": [], "Sf": []}

for year in [
    "2012",
    "2014",
    "2016",
    "2018",
    "2020",
]:
    congress: str = congresses[year]
    election: list[dict[str, Any]] = read_election(
        input_root + input_file(year, congress)
    )

    for row in election:
        xx: str = row["XX"]
        Vf: int = row["VOTE_%"]
        Sf: int = row["SEAT_%"]
        by_state[xx]["Vf"].append(Vf)
        by_state[xx]["Sf"].append(Sf)


### LINEAR REGRESSION TO FIND RESPONSIVENESS ###

responsiveness: list = list()

for k, v in by_state.items():
    xx: str = k
    Vf: tuple[float, ...] = tuple(v["Vf"])
    Sf: tuple[float, ...] = tuple(v["Sf"])
    res = scipy.stats.linregress(Vf, Sf)

    responsiveness.append({"XX": xx, "SLOPE": res.slope, "INTERCEPT": res.intercept})


pass

### WRITE RESULTS TO CSV ###

r_csv: str = "responsiveness_by_state_2012-2020.csv"
cols: list = ["XX", "SLOPE", "INTERCEPT"]
write_csv(output_root + r_csv, responsiveness, cols)

pass  # TODO
