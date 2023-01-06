# High-Level Process

This describes the manual workflow of extracting, imputing, and analyzing the election results at a high level using a series of spreadsheets.

## Step 1 - Get raw election results

For each election, I download two PDF reports from the Clerk of the House website:

* "Statistics of the Presidential and Congressional Election" and
* "Official List of Members of the House of Representatives of the United States"

They are in the data/elections/ and data/members/ directories, respectively.

## Step 2 - Extract the election results

For each election report, I create an associated Excel spreadsheet:

* The first tab *Election Results by State* extracts the vote & seat totals for Republican, Democrat, Other, and Total by state.
* I use the official list of members and online info (e.g., Wikipedia) to crosscheck the number of  elected Republican & Democratic members by state and overall, to make sure I didn't miss any races. (It's easy to do with larger states.)
* I also extract the race-level results for uncontested races in the *Uncontested Races* tab.
* I export these into similarly named *RESULTS* and *UNCONTESTED* CSV files.

These are the baseline, unmodified results in the data/extracted/ directory.

## Step 3 - Impute results for uncontested races

For each election, I run the impute_election.py script. The details of this process are described [here](impute-code.md).

## Step 4 - Analyze the elections in Python

Then I analyze the election results programmatically:

* I compute the "unearned" seats by election and pivot the results by state (pivot-by-state.csv), using the analyze_elections.py script.

## Step 5 - Analyze the elections in Excel

I import that into Excel and analyze the results longitudinally.

## Notes

* I use R vote & seat shares in this analysis ... because that's how I started years ago, before switching to D vote & seat shares in DRA. 
* Where there no contested districts to use as a baseline, I use some statewide race results (e.g., Governor, Senator, President) as proxies.

