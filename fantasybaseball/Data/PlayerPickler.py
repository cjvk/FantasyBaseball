from FantasyBaseball.Utils import *

DEBUG('./Data/PlayerPickler.py')

import cPickle
import FantasyBaseball
import Public

#    Dictionary of player statistics
#    handles all pickling/unpickling
#    init() unpickles dictionary from disk

FILE = 'cvonkrogh/FantasyBaseball/PlayerDictionary_v20.txt'
dirty = False

def unpickle():
    if Public.PlayersDictDirty:
        WARN("PlayerPickler dirty, aborting unpickle operation!")
        return False
    DEBUG('unpickling players')
    try:
        file = open(FILE, 'r')
    except IOError:
        DEBUG('PlayerPickler.unpickle(): no file found')
        return True
    Public.PlayersDict = cPickle.load(file)
    file.close()
    return True

def pickle():
    if not Public.PlayersDictDirty:
        DEBUG('nothing to save')
        return True
    try:
        file = open(FILE, 'w')
    except IOError:
        return False
    DEBUG('pickling players')
    cPickle.dump(Public.PlayersDict, file)
    Public.PlayersDictDirty = False
    file.close()
    return True

