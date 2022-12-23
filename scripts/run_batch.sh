#!/bin/bash
#
# Run a batch of commands
#
# For example:
#
# scripts/run_batch.sh
#

echo "Imputing results for 2006"
scripts/impute_election.py 2006

echo "Comparing elections for 2006"
scripts/compare_elections.py 2006 > temp/compare-2006.txt

echo "Done"