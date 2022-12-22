#!/bin/bash
#
# Impute all elections
#
# For example:
#
# scripts/impute_all.sh
#

echo "Imputing results for 2000"
scripts/impute_election.py 2000

echo "Imputing results for 2002"
scripts/impute_election.py 2002

echo "Imputing results for 2004"
scripts/impute_election.py 2004

echo "Imputing results for 2006"
scripts/impute_election.py 2006

echo "Imputing results for 2008"
scripts/impute_election.py 2008

echo "Imputing results for 2010"
scripts/impute_election.py 2010

echo "Imputing results for 2012"
scripts/impute_election.py 2012

echo "Imputing results for 2014"
scripts/impute_election.py 2014

echo "Imputing results for 2016"
scripts/impute_election.py 2016

echo "Imputing results for 2018"
scripts/impute_election.py 2018

echo "Imputing results for 2020"
scripts/impute_election.py 2020

echo "Done"