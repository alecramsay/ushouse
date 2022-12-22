#!/bin/bash
#
# Compare all elections
#
# For example:
#
# scripts/compare_all.sh
#

echo "Comparing elections for 2000"
scripts/compare_elections.py 2000 > temp/compare-2000.txt

echo "Comparing elections for 2002"
scripts/compare_elections.py 2002 > temp/compare-2002.txt

echo "Comparing elections for 2004"
scripts/compare_elections.py 2004 > temp/compare-2004.txt

echo "Comparing elections for 2006"
scripts/compare_elections.py 2006 > temp/compare-2006.txt

echo "Comparing elections for 2008"
scripts/compare_elections.py 2008 > temp/compare-2008.txt

echo "Comparing elections for 2010"
scripts/compare_elections.py 2010 > temp/compare-2010.txt

echo "Comparing elections for 2012"
scripts/compare_elections.py 2012 > temp/compare-2012.txt

echo "Comparing elections for 2014"
scripts/compare_elections.py 2014 > temp/compare-2014.txt

echo "Comparing elections for 2016"
scripts/compare_elections.py 2016 > temp/compare-2016.txt

echo "Comparing elections for 2018"
scripts/compare_elections.py 2018 > temp/compare-2018.txt

echo "Comparing elections for 2020"
scripts/compare_elections.py 2020 > temp/compare-2020.txt

echo "Done"