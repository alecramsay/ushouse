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
* Then I aggregate uncontested race info by state (using a pivot table).

These are the baseline, unmodified results in the data/extracted/ directory.

## Step 3 - Impute results for uncontested races

For each spreadsheet of raw election results above:

* I make a copy in the data/imputed/ directory.
* I extend the spreadsheet to impute the results for uncontested races, using a 70/30 heuristic. This assumes that the uncontested votes represent 70% of the total vote share and that a losing candidate would have garnered a 30% share of the votes.

The details of this logic are described [here](impute-spreadsheet.md).

## Step 4 - Export the results to CSV

For each imputed election spreadsheet: 

* I export the results into a CSV file in the data/results/ directory. 
* Then I added a year column manually, and
* Combine the individual files into an overall file containing all elections (elections.csv). 

At this point, the results for uncontested races have been imputed.

## Step 5 - Analyze the elections in Python

Then I analyze the election results programmatically:

* I compute the "unearned" seats by election and pivot the results by state (pivot-by-state.csv).

## Step 6 - Analyze the elections in Excel

I import that into Excel and analyze the results longitudinally.

## Notes

* I use R vote & seat shares in this analysis ... because that's how I started years ago, before switching to D vote & seat shares in DRA. 
* For uncontested at-large districts (ND, SD, & VT) and where no districts were contested (AR), I use some statewide race results (e.g., Governor, Senator, President) as proxies.

