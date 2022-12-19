# REVISION HISTORY

I took snapshots of all the previous work (on 12/18/22), so I can make changes if necessary and compare results.

## 2000–2016 Elections

I did these all at roughly the same time several years ago.
 
2000 election:
- AR / 3rd -- No uncontested data (blanks). R win. 
- LA / 2nd -- Ditto. D win.
- LA / 3rd -- Negative "other" votes. <<< FIXED: The total vote was missing a leading '1'.

2002 election:
- FL / 10th, 12th, 14th, 21st -- No uncontested data (blanks). R wins (CONFIRMED).
- FL / 11th, 20th -- Ditto, but D wins (CONFIRMED).
- NY / 5th, 18th, 23rd -- large fragmented "other" vote used (CONFIRMED) (TODO).

2004 election:
- Several uncontested races with no votes reported.
- NY / 25th -- large fragmented "other" vote used (CONFIRMED) (TODO).

2006 election:
- Several uncontested races with no votes reported.
- The `OTH1` (Column F) formula in the IMPUTED spreadsheet is wrong--doesn't include the R vote. It's right in the EXTRACTED spreadsheet. This affects every uncontested R win (ugh). <<< FIXED (TODO)
- TX / 22nd -- large fragmented "other" vote used (CONFIRMED) (TODO)
- TODO: Export RESULTS & UNCONTESTED

2008 election:
- TODO: Export RESULTS & UNCONTESTED

2010 election:
- TODO: Export RESULTS & UNCONTESTED

2012 election:
- TODO: Export RESULTS & UNCONTESTED

2014 election:
- TODO: Export RESULTS & UNCONTESTED

2016 election:
- TODO: Export RESULTS & UNCONTESTED

## 2018 & 2020 Elections

I did this more recently, after a long time away from the spreadsheet and much file reorganization:

2018 election:
- Vote totals don't validate on the Results tab, because I included [special election results for the 9th](https://ballotpedia.org/).North_Carolina%27s_9th_Congressional_District_special_election,_2019
- FL / 10th, 14th, 21st, 24th -- No uncontested data (blanks). D wins (CONFIRMED).
- NC / 3rd -- Negative "other" votes. <<< FIXED: The total vote was erroneously zero.

2020 election:
- MA / 1st, 3rd, 7th, 8th uncontested races erroneously coded as R vs. D wins (CONFIRMED). <<< FIXED
- SD at large district was uncontested -- So, no AVG contested vote. Used the Presidential total (422,609) as a proxy. <<< TODO

## 2022 Election

I'm going this now ...

## Issues

- How to insert a proxy for the AVG contest votes in the process?

## Special Test Cases

- 2006 / AL / 6th -- non-winning imputed votes > winning
- TX / 22nd -- fragmented "other" votes > winning
- 2018 / WI / 2nd -- actual votes > 0.7 average contested vote
