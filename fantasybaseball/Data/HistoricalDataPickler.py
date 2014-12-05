from FantasyBaseball.Utils import *

DEBUG('./Data/HistoricalDataPickler.py')

import cPickle
import FantasyBaseball
import Public

#    Dictionary of historical scores
#    handles all pickling/unpickling
#    init() unpickles dictionary from disk

FILE = 'cvonkrogh/FantasyBaseball/HistoricalScores_v20.txt'
# historical_scores_dict = {}

def unpickle():
    DEBUG('unpickling historical scores')
    try:
        file = open(FILE, 'r')
    except IOError:
        DEBUG('HistoricalDataPickler.unpickle(): no file found')
        return True
    Public.HistoricalScoresDict = cPickle.load(file)
    file.close()
    return True

def pickle():
    try:
        file = open(FILE, 'w')
    except IOError:
        return False
    DEBUG('pickling historical scores')
    cPickle.dump(Public.HistoricalScoresDict, file)
    file.close()
    return True

