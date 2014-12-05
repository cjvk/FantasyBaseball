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
                        'players' : {'A.J. Pierzynski' : {'pos' : 'C'}, 'B. McCann' : {'pos' : 'C'},
#                                     'R. Howard' : {'pos' : '1B'}, 'D. Lee' : {'pos' : '1B'},
                                     'L. Berkman' : {'pos' : '1B'}, 'D. Lee' : {'pos' : '1B'},                                     
                                     'C. Utley' : {'pos' : '2B'}, 'M. DeRosa' : {'pos' : '2B'},                                     
                                     'A. Rodriguez' : {'pos' : '3B'}, 'C. Jones' : {'pos' : '3B'},
                                     'J. Rollins' : {'pos' : 'SS'}, 'M. Tejada' : {'pos' : 'SS'},
                                     'P. Burrell' : {'pos' : 'LF'}, 'A. Dunn' : {'pos' : 'LF'},
                                     'C. Granderson' : {'pos' : 'CF'}, 'C. Beltran' : {'pos' : 'CF'},
                                     'J. Upton' : {'pos' : 'RF'}, 'K. Fukudome' : {'pos' : 'RF'},
                                     'J. Santana' : {'pos' : 'LSP'}, 'R. Halladay' : {'pos' : 'SP'},
                                     'C. Hamels' : {'pos' : 'LSP'}, 'B. Sheets' : {'pos' : 'SP'},
#                                     'J. Smoltz' : {'pos' : 'SP'}, 'J. Beckett' : {'pos' : 'SP'},
                                     'J. Smoltz' : {'pos' : 'SP'}, 'J. Duchscherer' : {'pos' : 'SP'},
#                                     'E. Bedard' : {'pos' : 'LSP'}, 'F. Hernandez' : {'pos' : 'SP'},
                                     'Cl. Lee' : {'pos' : 'LSP'}, 'F. Hernandez' : {'pos' : 'SP'},                                     
                                     'M. Rivera' : {'pos' : 'CL'},
                                     'B. Jenks' : {'pos' : 'CL'},
#                                     'F. Cordero' : {'pos' : 'CL'},
                                     'J. Soria' : {'pos' : 'CL'},
                                     }
                        },
                       {'name' : 'Alexander',
                        'role' : 'home', # unused?
#                        'players' : {'V. Martinez' : {'pos' : 'C'}, 'G. Soto' : {'pos' : 'C'},
                        'players' : {'J. Mauer' : {'pos' : 'C'}, 'G. Soto' : {'pos' : 'C'},
                                     'A. Pujols' : {'pos' : '1B'}, 'M. Teixeira' : {'pos' : '1B'},
#                                     'D. Pedroia' : {'pos' : '2B'}, 'J. Kent' : {'pos' : '2B'},
                                     'D. Pedroia' : {'pos' : '2B'}, 'I. Kinsler' : {'pos' : '2B'},
                                     'M. Cabrera' : {'pos' : '3B'}, 'D. Wright' : {'pos' : '3B'},
                                     'H. Ramirez' : {'pos' : 'SS'}, 'Y. Escobar' : {'pos' : 'SS'},
                                     'M. Ramirez' : {'pos' : 'LF'}, 'M. Holliday' : {'pos' : 'LF'},
                                     'B.J. Upton' : {'pos' : 'CF'}, 'J. Hamilton' : {'pos' : 'CF'},
                                     'V. Guerrero' : {'pos' : 'RF'}, 'J.D. Drew' : {'pos' : 'RF'},
                                     'J. Peavy' : {'pos' : 'SP'}, 'B. Webb' : {'pos' : 'SP'},
                                     'T. Hudson' : {'pos' : 'SP'}, 'T. Lincecum' : {'pos' : 'SP'},
                                     'D. Haren' : {'pos' : 'SP'}, 'S. Kazmir' : {'pos' : 'LSP'},
#                                     'Ol. Perez' : {'pos' : 'LSP'}, 'A. Harang' : {'pos' : 'SP'},
#                                     'C.C. Sabathia' : {'pos' : 'LSP'}, 'A. Harang' : {'pos' : 'SP'},
                                     'C.C. Sabathia' : {'pos' : 'LSP'}, 'R. Harden' : {'pos' : 'SP'},
                                     'J. Nathan' : {'pos' : 'CL'},
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
            LOG('adding player to stats dictionary: ' + p)
            Data.Public.PlayersDict[p] = {}
            pass
        pass
    return
