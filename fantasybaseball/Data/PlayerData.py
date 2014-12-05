from FantasyBaseball.Utils import *
DEBUG("./Data/PlayerData.py")

import PlayerPickler

def load_existing():
    DEBUG('Data.PlayerData.load_existing()')

    # unpickle players if available
    PlayerPickler.unpickle()
    
    return
