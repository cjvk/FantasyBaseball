from FantasyBaseball.Utils import *

DEBUG('./Midtier/ScoringUtils.py')

def ops18(obp, slg):
    return (1.8*obp) + slg
def k9(k, ip):
    return 9*k/ip
def svp(sv, blsv):
    return sv/(sv+blsv)

