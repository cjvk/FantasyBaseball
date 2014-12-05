from FantasyBaseball.Utils import *

DEBUG('./Midtier/Stats.py')

from FantasyBaseball import Data
import Public

def player_stat(player_name, stat):
    if not player_name in Data.Public.PlayersDict:
        WARN('no data for player: ' + player_name)
        return 0
    if not stat in Data.Public.PlayersDict[player_name]:
        WARN('missing stat ' + stat + ' for player ' + player_name)
        return 0
    return Data.Public.PlayersDict[player_name][stat]

def player_stat_18ops(player_name):
    return (player_stat(player_name, 'OBP') * 1.8) + player_stat(player_name, 'SLG')

def team_stat(owner, category, stat):
    """
    owner: name of owner, e.g. 'Chris'
    category: 'H', 'SP', or 'CL'
    stat: name of stat, e.g. 'TPA'
    """
    if Public.CurrentLeague.owners[0]['name'] == owner:
        playerlist = Public.CurrentLeague.owners[0]['players']
    elif Public.CurrentLeague.owners[1]['name'] == owner:
        playerlist = Public.CurrentLeague.owners[1]['players']
    else:
        ERROR('no owner found: ' + owner)
        return 0
    if category != 'H' and category != 'SP' and category != 'CL':
        ERROR('incorrect category: ' + category)
        return 0

    # position_info provides the ratio info
    position_info = Data.PlayerInfoDictionary.position_info
    stat_description = Data.PlayerInfoDictionary.get_stat_description(category, stat)
    if 'ratio' in stat_description:
        total = 0
        ratio_stat = stat_description['ratio']
        for p in playerlist:
            pos = playerlist[p]['pos']
            if position_info[pos]['category'] != category:
                continue
            total += Data.Public.PlayersDict[p][ratio_stat]
            pass
        pass
    team_total = stat_description['type'](0)
    for p in playerlist:
        pos = playerlist[p]['pos']
        if position_info[pos]['category'] != category:
            continue
        if 'ratio' in stat_description:
            ratio = float(player_stat(p, ratio_stat)) / float(total)
            pass
        else:
            ratio = 1
            pass
        team_total += ratio * player_stat(p, stat)
        pass
    return team_total

 
