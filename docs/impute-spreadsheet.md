# The Manual Process for Imputing Uncontested Elections

This describes in detail how I imputed results for uncontested races, using a series of spreadsheets.

## Step 1 - Get raw election results

As described [above](process.md), I have used the official results from the Clerk of the House website in the past. This step can be generalized though. The process needs two inputs:

* Statewide vote & seat totals -- Republican, Democratic Other, and Total, and
* Race votes & seats for uncontested races -- Republican, Democratic, Other, and Total, where "uncontested" means only a  Democrat or a Republican ran but not both

## Step 2 - Extract the election results

For each election, create a Excel spreadsheet:

* In the first tab, *Election Results by State*, I collect the vote & seat totals for Republican, Democrat, Other, and Total by state. These are the `REP1, DEM1, OTH1, and TOT1` columns for the *Actual Votes* section and the `REP2, DEM2, OTH2, and TOT2` columns for the *Actual Seats* section, respectively.
* In the second tab, *Uncontested Races*, I collect the race-level results for uncontested races. These are the `REP1, DEM1, OTH1, and TOT1` columns for the *Uncontested Votes* section and the `REP2, DEM2, OTH2, and TOT2` columns for the *Uncontested Races* section. Note: I don't collect the total number of seats (`TOT2`), for some reason.
* If a state doesn't have any uncontested races, I add a row with all zeroes. Tip: It's easiest to start with all 50 states with all zeroes and just replace the entries for the handful of states with uncontested races.
* Then I use a pivot table to aggregate the total uncontested votes, the Republican wins, and Democratic wins by state in a third tab, *Uncontested PIVOT*.
* In the *Election Results by State* tab, I insert a 4-column section between the *Actual Votes* and *Actual Seats* sections called *Uncontested*. I copy the values from the pivot table and paste them into the first three columns as `TOT3, REP3, and DEM3`. Note: 
* I add the 4th column, *Contested AVG Votes*, defined as: `(TOT1-TOT3)/(TOT2-(REP3+DEM3)`. IOW, I deduct any uncontested votes from the total votes and any uncontested seats from the seat total and compute the average number of votes per contested seat.

I save these baseline, unmodified results in the data/extracted/ directory. However you do it, a spreadsheet with these two tabs -- *Election Results by State* and *Uncontested Races* -- is the input data to the imputation step.

## Step 3 - Impute results for uncontested races

Imputing results for uncontested elections is fairly involved: 

* I start by making a copy of the extracted data spreadsheet in the data/imputed/ directory, so I have checkpoint I can fall back to.
* Then in that copy on the *Election Results by State* tab, I make sure every state has a value for *Contested AVG Votes* (Column J). For example, for the 2020 election, the one seat in South Dakota was uncontested, so the formula yields a `#DIV/0!` error. Find the the results for a statewide race at the same time -- e.g., President, Senator, Governor -- and use that vote total as a proxy. 

Then I have a complete set of data from which I can impute results for the uncontested races.

On the *Uncontested Races* tab, I insert a 3-column *Imputed Vote Shares* section after *Uncontested Races*:

* The first two columns, `REP win %` and `DEM win %`, represent how much of the total imputed vote an uncontested winner is assumed to garner. I use a 70/30 heuristic. This assumes that the uncontested votes represent 70% of the total vote share and that a losing candidate would have garnered a 30% share of the total votes.
* In the 3rd column, `Contested AVG Votes`, I use a lookup function to get the average votes per contested district for the state on the *Election Results by State* tab. The formula is `=VLOOKUP(B3,'Election Results by State'!$B$3:$J$52,9,FALSE)`, where Column B in both tabs is the two-character state code.

Next, I insert a 4-column *Recast* section, using `REP3, DEM3, OTH3 and TOT3` column headings. At this point, the tab has these columns:

```
Uncontested Votes:
- Column D: REP1
- Column E: DEM1
- Column F: OTH1
- Column G: TOT1

Uncontested Seats (Races):
- Column H: REP2
- Column I: DEM2
- Column J: OTH2

Imputed Vote Shares:
- Column K: REP win %
- Column L: DEM win %
- Column M: Contested AVG Votes

Recast:
- Column N: REP3
- Column O: DEM3
- Column P: OTH3
- Column Q: TOT3
```

* The Excel formulas for columns N and O (`REP3 and DEM3`) are fairly complex looking.

```
=IF(G3>0,IF(H3>0,MAX(D3,ROUND(K3*M3,0)),MAX(F3,ROUND((1-L3)*(O3/L3),0))),D3)

=IF(G3>0,IF(I3>0,MAX(E3,ROUND(L3*M3,0)),MAX(F3,ROUND((1-K3)*(N3/K3),0))),E3)
```

* What they do is relatively straightforward though. For `REP3`,             if a Republican won the uncontested seat, I use their actual votes or the imputed votes, whichever is higher. If instead a Democrat won the uncontested seat, I use the actual "other" vote total or the imputed votes, whichever is higher. The logic for the `DEM3` column is the reverse. Note: Much more readable Python versions of these functions are in impute.py in the source directory.
* The `OTH3` column is simply 0.
* The `TOT3` column is the sum of the other three (`=SUM(N3:P3)`).

Then I insert another 4-column section, *Adjustments*, using `REP4, DEM4, OTH4 and TOT4` column headings:

* The formulas for these simple--just subtract the actual votes from the recast votes to get offsets.

```
=N3-D3
=O3-E3
=P3-F3
=Q3-G3
```

Then, in a new *Uncontested by State PIVOT* tab, I aggregate the adjusted results by state  using a pivot table that sums the `REP4, DEM4, OTH4, and TOT4` columns.

I copy & paste those values into the *Election Results by State*  tab in the *Imputed Vote Changes* section (Columns K–N)and use them to offset the actual votes in the *Revised Votes* section (Columns O–R, `REP5, DEM5, OTH5, and TOT5`, respectively).

The last part of imputing results for uncontested races is to re-calculate the Republican two-party vote & seat shares in a *Percent Shares* section (Columns W & X).

```
=O3/SUM(O3:P3)
=S3/SUM(S3:T3)
```

## Step 4 - Export the results to CSV

The last step is exporting the revised results to a CSV file: 

* I export the results as a CSV file in the data/results/ directory. 
* Then I open it in a text editor and insert a first year column manually.

At this point, the results for uncontested races have been imputed.

When I've processed all the elections as described, I combine the individual files into an overall file containing all elections (elections.csv) for downstream analysis in Python and then Excel. 