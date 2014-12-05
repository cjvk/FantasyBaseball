from FantasyBaseball.Utils import *
DEBUG("./Midtier/League.py")

import FantasyBaseball
from FantasyBaseball import Data
import Public

class TwoPlayerLeague:
    'singleton, dictionary'
    def __init__(self):
        self.name = '2007 Fantasy Baseball League'
        self.owners = [{'name' : 'Chris',
                        'role' : 'visitor', # unused?
                        'players' : {'J. Mauer' : {'pos' : 'C'}, 'M. Barrett' : {'pos' : 'C'},
                                     'R. Howard' : {'pos' : '1B'}, 'D. Lee' : {'pos' : '1B'},
                                     'C. Utley' : {'pos' : '2B'}, 'K. Johnson' : {'pos' : '2B'},
                                     'A. Rodriguez' : {'pos' : '3B'}, 'A. Ramirez' : {'pos' : '3B'},
                                     'D. Jeter' : {'pos' : 'SS'}, 'J. Reyes' : {'pos' : 'SS'},
                                     'J. Bay' : {'pos' : 'LF'}, 'M. Alou' : {'pos' : 'LF'},
                                     'A. Soriano' : {'pos' : 'CF'}, 'G. Sizemore' : {'pos' : 'CF'},
                                     'V. Guerrero' : {'pos' : 'RF'}, 'M. Ordonez' : {'pos' : 'RF'},
                                     'J. Guthrie' : {'pos' : 'SP'}, 'B. Webb' : {'pos' : 'SP'},
                                     'D. Matsuzaka' : {'pos' : 'SP'}, 'R. Clemens' : {'pos' : 'SP'},
                                     'D. Haren' : {'pos' : 'SP'}, 'B. Sheets' : {'pos' : 'SP'},
                                     'J. Santana' : {'pos' : 'LSP'}, 'C. Hamels' : {'pos' : 'LSP'},
                                     'J. Nathan' : {'pos' : 'CL'},
                                     'T. Hoffman' : {'pos' : 'CL'},
                                     'J.J. Putz' : {'pos' : 'CL'},
                                     }
                        },
                       {'name' : 'Alexander',
                        'role' : 'home', # unused?
                        'players' : {'V. Martinez' : {'pos' : 'C'}, 'R. Martin' : {'pos' : 'C'},
                                     'A. Pujols' : {'pos' : '1B'}, 'L. Berkman' : {'pos' : '1B'},
                                     'B. Roberts' : {'pos' : '2B'}, 'J. Kent' : {'pos' : '2B'},
                                     'M. Cabrera' : {'pos' : '3B'}, 'C. Jones' : {'pos' : '3B'},
                                     'C. Guillen' : {'pos' : 'SS'}, 'M. Tejada' : {'pos' : 'SS'},
                                     'M. Ramirez' : {'pos' : 'LF'}, 'M. Holliday' : {'pos' : 'LF'},
                                     'C. Beltran' : {'pos' : 'CF'}, 'V. Wells' : {'pos' : 'CF'},
                                     'K. Griffey, Jr.' : {'pos' : 'RF'}, 'J.D. Drew' : {'pos' : 'RF'},
                                     'R. Halladay' : {'pos' : 'SP'}, 'C. Zambrano' : {'pos' : 'SP'},
                                     'F. Hernandez' : {'pos' : 'SP'}, 'R. Harden' : {'pos' : 'SP'},
                                     'J. Peavy' : {'pos' : 'SP'}, 'C.C. Sabathia' : {'pos' : 'LSP'},
                                     'E. Bedard' : {'pos' : 'LSP'}, 'C. Young' : {'pos' : 'SP'},
                                     'M. Rivera' : {'pos' : 'CL'},
                                     'J. Papelbon' : {'pos' : 'CL'},
                                     'T. Saito' : {'pos' : 'CL'},
                                     }
                        }
                       ]
        return
    def validate(self):
        if len(self.owners) == 2:
            return True
        else:
            return False
        pass
    pass

def load_existing():
    DEBUG('Midtier.League.load_existing()')
    # load a league if available
    Public.CurrentLeague = TwoPlayerLeague()
    # validation of selections
    for i in range(0, 2):
        DEBUG('Validating player selections')
        DEBUG('owner name: ' + Public.CurrentLeague.owners[i]['name'])
        DEBUG('role: ' + Public.CurrentLeague.owners[i]['role'])
        for p, d in Public.CurrentLeague.owners[i]['players'].iteritems():
            if not p in Data.PlayerInfoDictionary.player_info:
                WARN('player selection not in main player database: ' + p)
                pass
            elif d['pos'] != Data.PlayerInfoDictionary.player_info[p]['pos']:
                INFO('player selected at mismatching position: ' + p)
                pass
            pass
        pass
    Data.PlayerData.load_existing()
    return

def save_player_stats():
    DEBUG('Midtier.League.save_player_stats()')
    Data.PlayerPickler.pickle()
    return

def update_all_players():
    DEBUG('Midtier.League.update_all_players()')
    Data.Updater.update(Data.Public.PlayersDict)
    return

def create_players():
    DEBUG('Midtier.League.create_players()')
    # add visitor's selections
    for p in Public.CurrentLeague.owners[0]['players']:
        if not p in Data.PlayerInfoDictionary.player_info:
            WARN('no info for player: ' + p)
            pass
        if not p in Data.Public.PlayersDict:
            LOG('adding player to stats dictionary: ' + p)
            Data.Public.PlayersDict[p] = {}
            pass
        pass
    # add home's selections
    for p in Public.CurrentLeague.owners[1]['players']:
        if not p in Data.PlayerInfoDictionary.player_info:
            WARN('no info for player: ' + p)
            pass
        if not p in Data.Public.PlayersDict:
            LOG('adding player to stats dictionary: ' + p)
            Data.Public.PlayersDict[p] = {}
            pass
        pass
    # add others from universe
    for p in Data.PlayerInfoDictionary.player_info:
        if not p in Data.Public.PlayersDict:
            LOG('adding lpayer to stats dictionary: ' + p)
            Data.Public.PlayersDict[p] = {}
            pass
        pass
    return
