# Imputing Results for Uncontested Races

To impute votes for the winning party of an uncontested race:

- Calculate the average total votes per contested district in the state
- When the state doesn't have any contested seats -- i.e., only has one seat and it was uncontested -- use a statewide election (e.g., President, Senator, Governor) as a proxy for the total votes per district
- Make the winning votes by 70% of the average total votes per district or the *actual* votes the winning party received, whichever is higher

To impute votes for the losing party of an uncontested race:

- Make the losing total 30% of the winning total or the actual "other" vote total whichever is higher
- But cap the losing total at one less than the winning total -- occasionally, a number of independent or 3rd-party candidates run and their *combined* total exceeds the winning party's votes

