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
    The # of seats closest to proportional @ statewide Vf, which is
    the "expected number of seats" from http://bit.ly/2Fcuf4q.
    '''

    if (N > 1):
        return round((N * Vf) - EPSILON)
    
    # Only 1 CD
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
    The # of "unearned" seats won beyond proportional, based on statewide Vf.
    which is UE_# from http://bit.ly/2Fcuf4q.
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
# BIG 'R' - IMPLEMEMNTED BUT NOT USED
#

def bigR(Vf, Sf):
    '''
    Defined in Footnote 22 on P. 10. See dra-score & Nagle and Ramsay 2021.
    '''

    if (not areRoughlyEqual(Vf, 0.5, EPSILON)):
        return (Sf - 0.5) / (Vf - 0.5)

    return None


#
# EFFICIENCY GAP - NOT IMPLEMENTED YET
#

'''
NOTE the formulation used.
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