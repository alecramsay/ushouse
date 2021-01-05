#
# METRICS
#

from settings import *
from utils import *


#
# BEST SEATS - CLOSEST TO PROPORTIONAL
#

def best_seats(N, Vf):
    '''
    // ^S# - The # of Democratic seats closest to proportional @ statewide Vf
    // The "expected number of seats" from http://bit.ly/2Fcuf4q
    export function bestSeats(N: number, Vf: number): number
    {
      return Math.round((N * Vf) - S.EPSILON);
    }
    '''

    if (N > 1):
        return round((N * Vf) - EPSILON)
    else:  # Only 1 CD
        if (Vf > 0.75):
            return 1
        elif (Vf > 0.25):
            return 0.5
        else:
            return 0


#
# UNEARNED SEATS (UE)
#

def unearned_seats(best, actual):
    '''
    // UE# - The estimated # of unearned seats
    // UE_# from http://bit.ly/2Fcuf4q
    export function estUnearnedSeats(proportional: number, probable: number): number
    {
    return U.trim(proportional - probable);
    }
    '''

    return best - actual  # R advantage is +; D advantage is –


#
# Antimajoritarian
#

def isAntimajoritarian(Vf, Sf):
    bDem = True if ((Vf < (0.5 - AVGSVERROR)) and (Sf > 0.5)) else False
    bRep = True if (((1 - Vf) < (0.5 - AVGSVERROR)) and ((1 - Sf) > 0.5)) else False

    return bDem or bRep


#
# BIG 'R'
#

def bigR(Vf, Sf):
    '''
    // BIG 'R': Defined in Footnote 22 on P. 10
    export function calcBigR(Vf: number, Sf: number): number | undefined
    {
    let bigR: number | undefined = undefined;

    if (!(U.areRoughlyEqual(Vf, 0.5, S.EPSILON)))
    {
        bigR = (Sf - 0.5) / (Vf - 0.5);
        bigR = U.trim(bigR);
    }

    return bigR;
    }
    '''

    if (not areRoughlyEqual(Vf, 0.5, EPSILON)):
        return (Sf - 0.5) / (Vf - 0.5)

    return None


#
# EFFICIENCY GAP - TODO
#

'''
// EFFICIENCY GAP -- note the formulation used. Also, to accommodate turnout bias,
//   we would need to have D & R votes, not just shares.
export function calcEfficiencyGap(Vf: number, Sf: number, shareType = T.Party.Democratic): number
{
  let efficiencyGap: number;

  if (shareType == T.Party.Republican)
  {
    // NOTE - This is the  common formulation:
    //
    //   EG = (Sf – 0.5)  – (2 × (Vf – 0.5))
    //
    //   in which it is implied that '-' = R bias; '+' = D bias.

    efficiencyGap = U.trim((Sf - 0.5) - (2.0 * (Vf - 0.5)));
  }
  else
  {
    // NOTE - This is the alternate formulation in which '+' = R bias; '-' = D bias,
    //   which is consistent with all our other metrics.

    efficiencyGap = U.trim((2.0 * (Vf - 0.5)) - (Sf - 0.5));
  }

  return U.trim(efficiencyGap);
}
'''