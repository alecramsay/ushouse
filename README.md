# ushouse

Election results for the US House (2000 – 2020)

## Data

### Step 1 - Download reports

For each election 2000–2020, I downloaded two PDF reports from the Clerk of the
House website:

* "Statistics of the Presidential and Congressional Election" and
* "Official List of Members of the House of Representatives of the United States"

They are in the elections/ and members/ directories in the data/
directory, respectively.

### Step 2 - Extract the election results

For each election report, I created an associated Excel spreadsheet:

* The first tab "Election Results by State" extracts the vote & seat totals for
Republican, Democrat, Other, and Total by state.
* I used the official list of members to crosscheck the number of Republican &
Democratic members.
* I also extracted the race-level results for uncontested races in the "Uncontested
Races" tab.
* Then I aggregated uncontested race info by state (using a pivot table).

These are the baseline, unmodified results in the data/extracted/ directory.

### Step 3 - Impute results for uncontested races

For each spreadsheet of raw election results above:

* I made a copy in the data/imputed/ directory.
* I extended the spreadsheet to impute the results for uncontested races, using
a 70/30 heuristic. This assumes that the uncontested votes represent 70% of the
total vote share and that a losing candidate would have garnered a 30% share of
the votes.

* TODO - Review & document the logic for imputing uncontested elections

### Step 4 - Export the results to CSV

Finally, for each imputed election spreadsheet, I exported select results into
corresponding CSV files in the data/results/ directory. Then I added a year column manually, and
combined individual files into an overall file containing all elections (elections.csv). 

### Step 5 - Analyze the elections in Python

Then I analyzed the election results programmatically
computing the "unearned" seats by election and pivoting the results by state
(pivot-by-state.csv).

### Step 6 - Analyze the elections in Excel

I imported that into Excel and analyzed the results longitudinally.

* I use R vote & seat shares in this analysis ... because that's how I started years ago, before switching to D vote & seat shares in DRA. 

## TODO

* TODO - Handle missing data in Vermont & document two-party results
