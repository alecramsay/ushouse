#!/usr/bin/env python3
#
# SETTINGS
#

congresses: dict = {
    "2000": "107th",
    "2002": "108th",
    "2004": "109th",
    "2006": "110th",
    "2008": "111th",
    "2010": "112th",
    "2012": "113th",
    "2014": "114th",
    "2016": "115th",
    "2018": "116th",
    "2020": "117th",
    "2022": "118th",
}

# TODO - DELETE
# years: list[str] = [
#     "2000",
#     "2002",
#     "2004",
#     "2006",
#     "2008",
#     "2010",
#     "2012",
#     "2014",
#     "2016",
#     "2018",
#     "2020",
# ]
# TODO - DELETE
# congresses: list[str] = [
#     "107th",
#     "108th",
#     "109th",
#     "110th",
#     "111th",
#     "112th",
#     "113th",
#     "114th",
#     "115th",
#     "116th",
#     "117th",
# ]

EPSILON: float = 1 / (10**6)

AVGSVERROR: float = 0.02

N_ELECTIONS: int = 11

### END ###
