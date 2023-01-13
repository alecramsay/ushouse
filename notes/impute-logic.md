# Imputing Results for Uncontested Races

"Uncontested races" are races won by one of the major parties (Democrats or Republicans) but not contested by the other. They frequently have lower turnout / vote totals than for contested races. To make overall vote shares more reflective, we impute results for uncontested races.

To impute votes for the winning party of an uncontested race:

- We calculate the average total votes per contested district in the state
- When the state doesn't have any contested seats -- e.g., only has one seat and it was uncontested -- we use a statewide election (e.g., President, Senator, Governor) as a proxy for the total votes per district
- We set the winning votes to be 70% of the average total votes per district or the *actual* votes the winning party received, whichever is higher

To impute votes for the losing party of an uncontested race:

- We set the losing total to 30% of the winning total or the actual "other" vote total, whichever is higher
- However, we cap the losing total be no more than one less than the winning total -- occasionally, a number of independent or 3rd-party candidates run and their *combined* total exceeds the winning party's votes

