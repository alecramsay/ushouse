#!/usr/bin/env python3

"""
STATES
"""

from .constants import *


states: list[dict[str, str]] = [
    {"XX": "AL", "State": "Alabama"},
    {"XX": "AK", "State": "Alaska"},
    {"XX": "AZ", "State": "Arizona"},
    {"XX": "AR", "State": "Arkansas"},
    {"XX": "CA", "State": "California"},
    {"XX": "CO", "State": "Colorado"},
    {"XX": "CT", "State": "Connecticut"},
    {"XX": "DE", "State": "Delaware"},
    {"XX": "FL", "State": "Florida"},
    {"XX": "GA", "State": "Georgia"},
    {"XX": "HI", "State": "Hawaii"},
    {"XX": "ID", "State": "Idaho"},
    {"XX": "IL", "State": "Illinois"},
    {"XX": "IN", "State": "Indiana"},
    {"XX": "IA", "State": "Iowa"},
    {"XX": "KS", "State": "Kansas"},
    {"XX": "KY", "State": "Kentucky"},
    {"XX": "LA", "State": "Louisiana"},
    {"XX": "ME", "State": "Maine"},
    {"XX": "MD", "State": "Maryland"},
    {"XX": "MA", "State": "Massachusetts"},
    {"XX": "MI", "State": "Michigan"},
    {"XX": "MN", "State": "Minnesota"},
    {"XX": "MS", "State": "Mississippi"},
    {"XX": "MO", "State": "Missouri"},
    {"XX": "MT", "State": "Montana"},
    {"XX": "NE", "State": "Nebraska"},
    {"XX": "NV", "State": "Nevada"},
    {"XX": "NH", "State": "New Hampshire"},
    {"XX": "NJ", "State": "New Jersey"},
    {"XX": "NM", "State": "New Mexico"},
    {"XX": "NY", "State": "New York"},
    {"XX": "NC", "State": "North Carolina"},
    {"XX": "ND", "State": "North Dakota"},
    {"XX": "OH", "State": "Ohio"},
    {"XX": "OK", "State": "Oklahoma"},
    {"XX": "OR", "State": "Oregon"},
    {"XX": "PA", "State": "Pennsylvania"},
    {"XX": "RI", "State": "Rhode Island"},
    {"XX": "SC", "State": "South Carolina"},
    {"XX": "SD", "State": "South Dakota"},
    {"XX": "TN", "State": "Tennessee"},
    {"XX": "TX", "State": "Texas"},
    {"XX": "UT", "State": "Utah"},
    {"XX": "VT", "State": "Vermont"},
    {"XX": "VA", "State": "Virginia"},
    {"XX": "WA", "State": "Washington"},
    {"XX": "WV", "State": "West Virginia"},
    {"XX": "WI", "State": "Wisconsin"},
    {"XX": "WY", "State": "Wyoming"},
]

state_codes: list = list()
for s in states:
    xx: str = s["XX"]
    state_codes.append(xx)

### END ###
