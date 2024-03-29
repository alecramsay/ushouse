# REVIEW / VERIFICATION

I took snapshots of my previous work (on 12/18/22), so I could make changes if necessary & compare results with my original spreadsheet-based workflow. These notes catalogue peculiarities with the raw data (scenarios) as well as problems I found with my old manual work using a series of spreadsheets. I fixed the problems with my new automated script.

## 2000–2016 Elections

I processed these elections at roughly the same time several years ago.
 
2000 election -- Reviewed automated results.
- AR / 3rd -- No uncontested data (blanks). R win. 
- LA / 2nd -- Ditto. D win.
- LA / 3rd -- Negative "other" votes. <<< FIXED: The total vote was missing a leading '1'

2002 election -- Reviewed automated results.
- FL / 10th, 12th, 14th, 21st -- No uncontested data (blanks). R wins
- FL / 11th, 20th -- Ditto, but D wins
- NY / 5th, 18th, 23rd -- fragmented "other" vote > winner <<< CONFIRMED -- test cast for 2010/NY/29th covers these

2004 election -- Reviewed automated results.
- Several uncontested races with no votes reported.
- NY / 25th -- fragmented "other" vote > winner <<< CONFIRMED -- test cast for 2010/NY/29th covers these

2006 election -- Spot checked results
- Several uncontested races with no votes reported.
- The `OTH1` (Column F) formula in the IMPUTED spreadsheet is wrong--doesn't include the R vote. It's right in the EXTRACTED spreadsheet. This affects every uncontested R win (ugh). This is probably the result of the R/D columns being reversed and trying to update the formulas for that. <<< FIXED by using the EXTRACTED data
- TX / 22nd -- fragmented "other" vote > winner <<< CONFIRMED

2008 election -- Spot checked results
- Several uncontested races with no votes reported.
- The `OTH1` (Column F) formula in the IMPUTED spreadsheet is wrong--doesn't include the R vote. Same as above. <<< FIXED
- AL / all 4 races were uncontested -- So, no AVG contested vote. Used Presidential total (271,654) as a proxy. 
- VT at large district was uncontested -- So, no AVG contested vote. Used the Presidential total (325,046) as a proxy.

2010 election -- Reviewed automated results.
- Several uncontested races with no votes reported.
- NY / 29th -- fragmented "other" vote > winner <<< CONFIRMED -- test case written

2012 election -- Reviewed automated results.
- Several uncontested races with no votes reported.

2014 election -- Reviewed automated results.
- Several uncontested races with no votes reported.

2016 election -- Reviewed automated results.
- Two uncontested races with no votes reported.
- ND at large district was uncontested -- So, no AVG contested vote. Used the Presidential total (344,360) as a proxy.

## 2018 & 2020 Elections

I processed these more recently, after a long time away from the spreadsheet and much file reorganization:

2018 election -- Reviewed automated results.
- Vote totals don't validate on the Results tab, because I included [special election results for the 9th](https://ballotpedia.org/).North_Carolina%27s_9th_Congressional_District_special_election,_2019 <<< OK
- FL / 10th, 14th, 21st, 24th -- No uncontested data (blanks). D wins <<< These were not included in the manual results (sigh).
- MI <<< Data error in manual spreadsheet: uncontested == 0 instead of 1.
- NC / 3rd -- Negative "other" votes. <<< FIXED: The total vote was erroneously zero

2020 election -- Reviewed automated results.
- MA / 1st, 3rd, 7th, 8th uncontested races erroneously coded as R vs. D wins (CONFIRMED). <<< FIXED
- FL -- One no uncontested data (blanks). <<< These were not included in the manual results (sigh).
- SD at large district was uncontested -- So, no AVG contested vote. Used the Presidential total (422,609) as a proxy.

## 2022 Election 

- Reviewed the automated results -- All the "other" vote totals were different. The "other" column had stray 1-N values in the spreadsheet. <<< FIXED

I'm going to process this again, when the Clerk of the House releases the official results.

