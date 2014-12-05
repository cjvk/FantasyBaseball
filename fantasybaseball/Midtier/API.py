from FantasyBaseball.Utils import *
DEBUG("./Midtier/API.py")

import Public
from FantasyBaseball import Data

def get_players_by_owner_name(owner_name):
    if Public.CurrentLeague.owners[0]['name'] == owner_name:
        return Public.CurrentLeague.owners[0]['players']
    elif Public.CurrentLeague.owners[1]['name'] == owner_name:
        return Public.CurrentLeague.owners[1]['players']
    else:
        ERROR('no owner found with name: ' + owner_name)
        return {}
    pass

def get_players_by_owner_index(owner_index):
    return Public.CurrentLeague.owners[owner_index]['players']

# Comment out for now --- would we want the API to return the real position or the 'picked' position
#def get_position_by_player_name(player_name):
#    return Data.PlayerInfoDictionary.player_info[player_name]['pos']

def get_position_category_by_position(pos):
    return Data.PlayerInfoDictionary.position_info[pos]['category']

