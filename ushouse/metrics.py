#
# METRICS
#

from settings import *

#
# BEST SEATS - CLOSEST TO PROPORTIONAL
#

# TODO - Handle N = 1
def best_seats(N, Vf):
    '''
    // ^S# - The # of Democratic seats closest to proportional @ statewide Vf
    // The "expected number of seats" from http://bit.ly/2Fcuf4q
    export function bestSeats(N: number, Vf: number): number
    {
      return Math.round((N * Vf) - S.EPSILON);
    }
    '''

    return round((N * Vf) - EPSILON)


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
# EFFICIENCY GAP
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


#
# BIG 'R'
#

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
