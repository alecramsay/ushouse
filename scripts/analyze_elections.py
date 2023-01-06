#!/usr/bin/env python3

"""
Analyze congressional elections over time.

For example:

$ scripts/analyze_elections.py

"""

from ushouse import *

input_file: str = "data/analysis/elections.csv"

by_state: dict
totals: dict
by_state, totals = analyze_elections(input_file)

# Write the results in a format suitable for saving to a CSV file

print_header()
for key in by_state:
    print_row(key, by_state[key])
for key in totals:
    print_row(key, totals[key])
print()

pass
