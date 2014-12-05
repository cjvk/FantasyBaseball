from FantasyBaseball.Utils import *

DEBUG('./Data/Updater.py')

import PlayerInfoDictionary
import REGEX
import PlayerPickler
import urllib2
import re
import Public

__d_matsuzaka_stats_ = {'OBP' : 0.326,
                        'SLG' : 0.405,
                        'TBF' : 874,
                        'BB'  : 80,
                        'AB'  : 794, # (874 - 80)
                        'SO'  : 201,
                        'IP'  : 204.67,
                        }
__h_pence_stats_ = {'OBP' : 0.360,
                    'SLG' : 0.539,
                    'TPA' : 484,
                    'AB'  : 456,
                    }
__j_soria_stats_ = {'OBP' : 0.245,
                    'SLG' : 0.264,
                    'TBF' : 270,
                    'BB'  : 19,
                    'AB'  : 251, # (270 - 19)
                    'SO'  : 75,
                    'IP'  : 69.0,
                    'G'   : 62,
                    'SV'  : 17,
                    'BLSV': 4,
                    }

def convert_ip_to_number(ip):
    if ip[-2:] == '.1':
        return float(ip[:-2]) + .33
    elif ip[-2:] == '.2':
        return float(ip[:-2]) + .67
    else:
        return float(ip)
    pass

def update(player_dict):
    """
    updates all players in player_dict
    logs '.' for successful imports, and 'E' otherwise
    """
    for p in player_dict:
        DEBUG('updating player: ' + p)

        # get html
        response = urllib2.urlopen(urllib2.Request(PlayerInfoDictionary.player_info[p]['url']))
        html = response.read()
        response.close()

        # get position, category, and stats_list from PlayerInfoDictionary
        pos = PlayerInfoDictionary.player_info[p]['pos']
        cat = PlayerInfoDictionary.position_info[pos]['category']
        stats_list = PlayerInfoDictionary.position_info[pos]['stat_list']

        # check position of player
        matches = re.findall(REGEX.regex['pos'], html)
        if len(matches) != 1:
            INFO('unable to calculate position for player: ' + p)
            pass
        else:
            player_pos = PlayerInfoDictionary.player_info[p]['pos']
            for match in matches:
                if match == 'SP':
                    if player_pos != 'SP' and player_pos != 'LSP':
                        INFO('player updated at mismatching position: ' + p + ' ' + match + ' ' + player_pos)
                        pass
                    pass
                elif match == 'RP':
                    if player_pos != 'CL':
                        INFO('player updated at mismatching position: ' + p + ' ' + match + ' ' + player_pos)
                        pass
                    pass
                else:
                    if match != player_pos:
                        INFO('player updated at mismatching position: ' + p + ' ' + match + ' ' + player_pos)
                        pass
                    pass
                pass
            pass

        # parse the stats
        html_ok = True
        temp_dict = {}
        for stat in stats_list:
            if cat != 'H' and stat == 'AB':
                continue # it gets calculated below
            matches = re.findall(REGEX.regex[stats_list[stat]['regex']], html)
            if len(matches) != 1:
                WARN('unable to parse html for ' + p)
                html_ok = False
                break
            for match in matches:
                if stat == 'IP':
                    temp_dict['IP'] = convert_ip_to_number(match)
                else:
                    # convert using the 'type' field as a function
                    temp_dict[stat] = stats_list[stat]['type'](match)
                    pass
                pass
            pass
        if not html_ok:
            # manually add stats for D. Matsuzaka
            if p == 'D. Matsuzaka':
                temp_dict = __d_matsuzaka_stats_
                pass
            elif p == 'H. Pence':
                temp_dict = __h_pence_stats_
                pass
            elif p == 'J. Soria':
                temp_dict = __j_soria_stats_
                pass
            LOGCHAR('E')
            pass
        else:
            # manually calculate AB for pitchers (TBF - BB)
            if cat != 'H':
                temp_dict['AB'] = temp_dict['TBF'] - temp_dict['BB']
                pass
            LOGCHAR('.')
            pass

        player_dict[p] = temp_dict

        pass
    Public.PlayersDictDirty = True
    return
