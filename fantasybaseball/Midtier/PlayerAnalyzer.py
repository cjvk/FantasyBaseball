from FantasyBaseball.Utils import *
DEBUG("./Midtier/PlayerAnalyzer.py")

from FantasyBaseball import Data
import Stats
import Scorer
import Public
import FantasyBaseball

def raw_analysis():
    """
    returns analysis catch-all dictionary
    1 Hitting
      1.1 Worst performing player at each position
      1.2 Best and second-best available at each position
    2 Pitching
      2.1 Under construction
    3 Closers
      3.1 Under construction
    
      
    """

    # example return dictionary

    example = {'simple_18ops' : {'worst_per_position' : {'C'  : {0 : ['M. Barrett',],
                                                                 1 : ['R. Martin',]},
                                                         '1B' : {},
                                                         '2B' : {},
                                                         '3B' : {},
                                                         'SS' : {},
                                                         'LF' : {},
                                                         'CF' : {},
                                                         'RF' : {},
                                                         'SP' : {0 : ['name_worst', 'name_next',],
                                                                 1 : ['name_worst', 'name_next',],},
                                                         'CL' : {0 : ['name_worst',],
                                                                 1 : ['name_worst',],},},
                                 'best_available'     : {'C'  : ['J. Posada', 'J. Varitek',],
                                                         '1B' : [],
                                                         '2B' : [],
                                                         '3B' : [],
                                                         'SS' : [],
                                                         'LF' : [],
                                                         'CF' : [],
                                                         'RF' : [],
                                                         'SP' : ['name_best', 'name_2', 'name_3',],
                                                         'CL' : ['name_best', 'name_2',],},
                                 'best_trade'         : {0 : {'pos' : 'C',
                                                              'out' : 'M. Barrett',
                                                              'in'  : 'J. Posada',
                                                              },
                                                         1 : {},},
                                 }}

    return_dict = {}
    return_dict['simple_18ops'] = {}
    return_dict['simple_18ops']['worst_per_position'] = {}
    return_dict['simple_18ops']['best_available'] = {}
    ops18 = Stats.player_stat_18ops

    hitting_pos_tuple = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF')
    for pos in hitting_pos_tuple:
        return_dict['simple_18ops']['worst_per_position'][pos] = {}
        return_dict['simple_18ops']['best_available'][pos] = []
        for i in range(0, 2):
            return_dict['simple_18ops']['worst_per_position'][pos][i] = []

        # find worst players per owner
        for i in range(0, 2): # owner
            for p, d in Public.CurrentLeague.owners[i]['players'].iteritems():
                if Data.PlayerInfoDictionary.player_info[p]['pos'] != pos:
                    continue
                worst_list = return_dict['simple_18ops']['worst_per_position'][pos][i]
                inserted = False
                for loc in range(0, len(worst_list)):
                    if ops18(p) < ops18(worst_list[loc]):
                        worst_list.insert(loc, p)
                        inserted = True
                        break
                if not inserted:
                    worst_list.append(p)
                if len(worst_list) > 1:
                    worst_list.pop()

        # find best players out there
        for p, d in Data.PlayerInfoDictionary.player_info.iteritems():
            if d['pos'] != pos:
                continue
            if p in Public.CurrentLeague.owners[0]['players']:
                continue
            if p in Public.CurrentLeague.owners[1]['players']:
                continue
            best_list = return_dict['simple_18ops']['best_available'][pos]
            inserted = False
            for loc in range(0, len(best_list)):
                if ops18(p) > ops18(best_list[loc]):
                    best_list.insert(loc, p)
                    break
            if not inserted:
                best_list.append(p)
            if len(best_list) > 2:
                best_list.pop()

    # add pitchers

    pitching_category_tuple = ('SP', 'CL')
    for pos in pitching_category_tuple:
        return_dict['simple_18ops']['worst_per_position'][pos] = {}
        return_dict['simple_18ops']['best_available'][pos] = []
        for i in range(0, 2):
            return_dict['simple_18ops']['worst_per_position'][pos][i] = []

        # worst per owner
        for i in range(0, 2): # owner
            for p, d in Public.CurrentLeague.owners[i]['players'].iteritems():
                player_position = Data.PlayerInfoDictionary.player_info[p]['pos']
                if Data.PlayerInfoDictionary.position_info[player_position]['category'] != pos:
                    continue
                worst_list = return_dict['simple_18ops']['worst_per_position'][pos][i]
                inserted = False
                for loc in range(0, len(worst_list)):
                    if ops18(p) > ops18(worst_list[loc]):
                        worst_list.insert(loc, p)
                        inserted = True
                        break
                if not inserted:
                    worst_list.append(p)
                if len(worst_list) > 3:
                    worst_list.pop()
        # find best players
        for p, d in Data.PlayerInfoDictionary.player_info.iteritems():
            if Data.PlayerInfoDictionary.position_info[d['pos']]['category'] != pos:
                continue
            if p in Public.CurrentLeague.owners[0]['players']:
                continue
            if p in Public.CurrentLeague.owners[1]['players']:
                continue
            best_list = return_dict['simple_18ops']['best_available'][pos]
            inserted = False
            for loc in range(0, len(best_list)):
                if ops18(p) < ops18(best_list[loc]):
                    best_list.insert(loc, p)
                    break
            if not inserted:
                best_list.append(p)
            if len(best_list) > 3:
                best_list.pop()
    
    # Now that we have the worst performing (by simple ops) at every position,
    # calculate the best trade by difference in simple ops
    return_dict['simple_18ops']['best_trade'] = {}
    best_simple = return_dict['simple_18ops']['best_trade']
    for i in range(0, 2):
        best_simple[i] = {}
        pass

    # expand to pitching and closers after their inclusion
    ops18 = Stats.player_stat_18ops
    for pos in hitting_pos_tuple:
        for i in range(0, 2):
            if not 'pos' in best_simple[i]:
                best_simple[i]['pos'] = pos
                best_simple[i]['out'] = return_dict['simple_18ops']['worst_per_position'][pos][i][0]
                best_simple[i]['in']  = return_dict['simple_18ops']['best_available'][pos][0]
                continue
            else:
                diff_so_far = ops18(best_simple[i]['in']) - ops18(best_simple[i]['out'])
                candidate_out = return_dict['simple_18ops']['worst_per_position'][pos][i][0]
                candidate_in  = return_dict['simple_18ops']['best_available'][pos][0]
                diff_candidate = ops18(candidate_in) - ops18(candidate_out)
                if diff_candidate > diff_so_far:
                    best_simple[i]['pos'] = pos
                    best_simple[i]['out'] = candidate_out
                    best_simple[i]['in']  = candidate_in
                    pass
                pass
            pass
        pass

    return return_dict

def total_score(owner_index):
    raw_scores = Scorer.get_raw_scores()
    if owner_index == 0:
        my_scores = raw_scores['VIS']
    else:
        my_scores = raw_scores['HOME']
    total = my_scores['H']['18OPS'] + my_scores['H']['PA']
    total += my_scores['SP']['18OPS'] + my_scores['SP']['IP'] + my_scores['SP']['K/9']
    total += my_scores['CL']['18OPS'] + my_scores['CL']['G'] + my_scores['CL']['SV%'] + my_scores['CL']['K/9']
    return total

def raw_analysis_search():
    """
    returns dictionary similar to raw_analysis
    separated because search may take awhile
    """

    # example return dictionary

    example = {'search_replace' : {'best_trade' : {0 : [{'pos' : 'C',
                                                         'out' : 'M. Barrett',
                                                         'in'  : 'J. Posada',
                                                         'diff': 3.3284,},
                                                        {},],
                                                   1 : [],},},}

    # construct return_dict
    return_dict = {}
    return_dict['search_replace'] = {}
    return_dict['search_replace']['best_trade'] = {}
    for i in range(0, 2):
        return_dict['search_replace']['best_trade'][i] = []

    for i in range(0, 2):
        # get the current score
        current_score = total_score(i)

        players_original = Public.CurrentLeague.owners[i]['players'].items()
        # [('J. Mauer', {'pos' : 'C'}),]
        for player_tuple in players_original:

            # unpick the player
            del Public.CurrentLeague.owners[i]['players'][player_tuple[0]]

            # go through available players, calculate diffs
            for p, d in Data.PlayerInfoDictionary.player_info.iteritems():
                if d['pos'] != player_tuple[1]['pos']:
                    # account for 'LSP' peculiarity
                    if d['pos'] != 'LSP' or player_tuple[1]['pos'] != 'SP':
                        if d['pos'] != 'SP' or player_tuple[1]['pos'] != 'LSP':
                            continue
                if p in Public.CurrentLeague.owners[0]['players']:
                    continue
                if p in Public.CurrentLeague.owners[1]['players']:
                    continue

                # temporarily pick the new player and calculate new score
                Public.CurrentLeague.owners[i]['players'][p] = {'pos' : d['pos']}
                new_score = total_score(i)

                # construct a node for this player
                node = {}
                node['pos'] = d['pos']
                node['out'] = player_tuple[0]
                node['in']  = p
                node['diff']= new_score - current_score

                # insert this player in the proper location, and trim if necessary
                best_list = return_dict['search_replace']['best_trade'][i]
                inserted = False
                for loc in range(0, len(best_list)):
                    if new_score - current_score > best_list[loc]['diff']:
                        best_list.insert(loc, node)
                        break
                if not inserted:
                    best_list.append(node)
                if len(best_list) > 4:
                    best_list.pop()

                # unpick this new player
                del Public.CurrentLeague.owners[i]['players'][p]

            # re-pick the player unpicked from earlier
            Public.CurrentLeague.owners[i]['players'][player_tuple[0]] = player_tuple[1]

    return return_dict

