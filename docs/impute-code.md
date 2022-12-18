# The Code for Imputing Uncontested Elections

The code to impute results for uncontested elections needs two inputs:

- Vote totals (`REP1, DEM1, OTH1, and TOT1`) and seat totals (`REP2, DEM2, OTH2, and TOT2`) by state; and
- The same for each uncontested race.

This is less than what I described in the manual process using a series of spreadsheets. Everything else on the way to revised votes that incorporate imputed results for uncontested races is an intermediate result that can be computed and discarded.

The average votes for contested races in a state *does* depend on the number of seats and the total votes in uncontested races. NOTE: My spreadsheet calculation of *Contested AVG Votes* (Column J) does not include "other" votes -- it should.