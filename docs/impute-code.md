# The Code for Imputing Uncontested Elections

The code to impute results for uncontested elections needs two inputs:

- Vote totals (`REP_V, DEM_V, OTH_V, and TOT_V`) and seat totals (`REP_S, DEM_S, OTH_S, and TOT_S`) by state; and
- The vote totals (`REP_V, DEM_V, OTH_V, and TOT_V`) for each uncontested race.

Everything else on the way to revised votes that incorporate imputed results for uncontested races is an intermediate result that can be computed and discarded. 

The average votes for contested races in a state *does*, however, depend on the number of seats and the total votes in uncontested races. 

Once I have those two input files (CSV) for an election, I run the impute_election.py script on them.