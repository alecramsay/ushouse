# Detailed Process

This describes in detail how I impute results for uncontested races.

## Step 1 - Get raw election results

As described [above](process.md), I have used the official results from the Clerk of the House website in the past. This step can be generalized though. The process needs two inputs:

* Statewide vote & seat totals -- Republican, Democratic Other, and Total, and
* Race votes & seats for uncontested races -- Republican, Democratic, Other, and Total, where "uncontested" means only a  Democrat or a Republican ran but not both

## Step 2 - Extract the election results

For each election, create a Excel spreadsheet:

* In the first tab, *Election Results by State*, collect the vote & seat totals for Republican, Democrat, Other, and Total by state. These are the `REP1, DEM1, OTH1, and TOT1` columns for the *Actual Votes* section and the `REP2, DEM2, OTH2, and TOT2` columns for the *Actual Seats* section, respectively.
* In the second tab, *Uncontested Races*, collect the race-level results for uncontested races. These are the `REP1, DEM1, OTH1, and TOT1` columns for the *Uncontested Votes* section and the `REP2, DEM2, OTH2, and TOT2` columns for the *Uncontested Races* section. Note: I don't collect the total number of seats (`TOT2`), for some reason.
* If a state doesn't have any uncontested races, add a row with all zeroes. Tip: It's easiest to start with all 50 states with all zeroes and just replace the entries for the handful of states with uncontested races.
* Then use a pivot table to aggregate the total uncontested votes, the Republican wins, and Democratic wins by state in a third tab, *Uncontested PIVOT*.
* In the *Election Results by State* tab, insert a 4-column section between the *Actual Votes* and *Actual Seats* sections called *Uncontested*. Copy the values from the pivot table and paste them into the first three columns as `TOT3, REP3, and DEM3`. 
* As a 4th column to the section, *Contested AVG Votes*, defined as: `(TOT1-TOT3)/(TOT2-(REP3+DEM3)`. IOW, deduct any uncontested votes from the total votes and any uncontested seats from the seat total and compute the average number of votes per contested seat.

Save these are the baseline, unmodified results in the data/extracted/ directory. However you do it, a spreadsheet with these two tabs -- *Election Results by State* and *Uncontested Races* -- is the input to the next step.

## Step 3 - Impute results for uncontested races

First:

* Make a copy of the extracted data spreadsheet in the data/imputed/ directory, and
* On the *Election Results by State* tab, make sure every state has a value for *Contested AVG Votes* (Column J). For example, for the 2020 election, the one seat in South Dakota was uncontested, so the formula yields a `#DIV/0!` error. Find the the results for a statewide race at the same time -- e.g., President, Senator, Governor -- and use that vote total as a proxy. 

Now you have a complete set of data from which you can impute results for the uncontested races.

On the *Uncontested Races* tab, insert a 3-column *Imputed Vote Shares* section after *Uncontested Races*:

* The first two columns, `REP win %` and `DEM win %`, represent how much of the total imputed vote an uncontested winner is assumed to garner. I use a 70/30 heuristic. This assumes that the uncontested votes represent 70% of the total vote share and that a losing candidate would have garnered a 30% share of the total votes.
* In the 3rd column, `Contested AVG Votes`, lookup the average votes per contested district for the state on the *Election Results by State* tab. The formula is `=VLOOKUP(B3,'Election Results by State'!$B$3:$J$52,9,FALSE)`, where Column B in both tabs is the two-character state code.

Next insert a 4-column *Recast* section: 

* Use `REP3, DEM3, OTH3 and TOT3` column headings.
* >>> HERE <<<
* `=IF(G3>0,IF(H3>0,MAX(D3,ROUND(K3*M3,0)),MAX(F3,ROUND((1-L3)*(O3/L3),0))),D3)`
* `=IF(G3>0,IF(I3>0,MAX(E3,ROUND(L3*M3,0)),MAX(F3,ROUND((1-K3)*(N3/K3),0))),E3)`
* The `OTH3` column is simply 0.
* The `TOT3` column is the sum of the other three (`=SUM(N3:P3)`).

Insert another 4-column section, *Adjustments*:

* Use `REP4, DEM4, OTH4 and TOT4` column headings.
* `=N3-D3`
* `=O3-E3`
* `=P3-F3`
* `=Q3-G3`
* TODO

Create a pivot table in an *Uncontested by State PIVOT* tab:

* Sum the `REP4, DEM4, OTH4, and TOT4` columns
* TODO

Copy the results into the *Election Results by State* tab as the `REP4, DEM4, OTH4, and TOT4` columns in an *Imputed Vote Changes* section (Columns K–N).

TODO: *Revised Votes*

TODO: *Percent Shares*

## Step 4 - Export the results to CSV

For each imputed election spreadsheet: 

* I export the results into a CSV file in the data/results/ directory. 
* Then I added a year column manually, and
* Combine the individual files into an overall file containing all elections (elections.csv). 

At this point, the results for uncontested races have been imputed.