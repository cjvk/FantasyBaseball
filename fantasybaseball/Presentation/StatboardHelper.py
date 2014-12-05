from FantasyBaseball.Utils import *
DEBUG("./Presentation/StatboardHelper.py")

from FantasyBaseball import Midtier

def custom_1():
    v = Midtier.Public.CurrentLeague.owners[0]['name']
    h = Midtier.Public.CurrentLeague.owners[1]['name']
    ts = Midtier.Stats.team_stat

    return (ts(v,'H','OBP'), ts(v,'H','SLG'), ts(v,'H','TPA'), ts(v,'H','AB'),
            ts(h,'H','OBP'), ts(h,'H','SLG'), ts(h,'H','TPA'), ts(h,'H','AB'),
            )

def custom_2():
    v = Midtier.Public.CurrentLeague.owners[0]['name']
    h = Midtier.Public.CurrentLeague.owners[1]['name']
    ts = Midtier.Stats.team_stat

    return (ts(v,'SP','OBP'), ts(v,'SP','SLG'), ts(v,'SP','TBF'), ts(v,'SP','BB'),
            ts(v,'SP','AB'), ts(v,'SP','SO'), ts(v,'SP','IP'),
            ts(h,'SP','OBP'), ts(h,'SP','SLG'), ts(h,'SP','TBF'), ts(h,'SP','BB'),
            ts(h,'SP','AB'), ts(h,'SP','SO'), ts(h,'SP','IP'),
            )

def custom_3():
    v = Midtier.Public.CurrentLeague.owners[0]['name']
    h = Midtier.Public.CurrentLeague.owners[1]['name']
    ts = Midtier.Stats.team_stat

    return (ts(v,'CL','OBP'), ts(v,'CL','SLG'), ts(v,'CL','TBF'), ts(v,'CL','BB'),
            ts(v,'CL','AB'), ts(v,'CL','SO'), ts(v,'CL','IP'), ts(v,'CL','SV'),
            ts(v,'CL','BLSV'), ts(v,'CL','G'),
            ts(h,'CL','OBP'), ts(h,'CL','SLG'), ts(h,'CL','TBF'), ts(h,'CL','BB'),
            ts(h,'CL','AB'), ts(h,'CL','SO'), ts(h,'CL','IP'), ts(h,'CL','SV'),
            ts(h,'CL','BLSV'), ts(h,'CL','G'),
            )

def custom_4():
    return (Midtier.Public.CurrentLeague.owners[0]['name'],
            Midtier.Public.CurrentLeague.owners[1]['name'],
            )

def custom_5(owner_index):
    return_list = []
    ps = Midtier.Stats.player_stat
    for p, d in Midtier.API.get_players_by_owner_index(owner_index).iteritems():
        cat = Midtier.API.get_position_category_by_position(d['pos'])
        if cat != 'H':
            continue
        return_list.append(p)             # Name
        return_list.append(d['pos'])      # Pos
        return_list.append(ps(p, 'OBP'))  # OBP
        return_list.append(ps(p, 'SLG'))  # SLG
        return_list.append(ps(p, 'TPA'))  # TPA
        return_list.append(ps(p, 'AB'))   # AB
        pass
    return_tuple = tuple(return_list)
    return return_tuple

def custom_6(owner_index):
    return_list = []
    ps = Midtier.Stats.player_stat
    for p, d in Midtier.API.get_players_by_owner_index(owner_index).iteritems():
        cat = Midtier.API.get_position_category_by_position(d['pos'])
        if cat != 'SP':
            continue
        return_list.append(p)             # Name
        return_list.append(d['pos'])      # Pos
        return_list.append(ps(p, 'OBP'))  # OBP
        return_list.append(ps(p, 'SLG'))  # SLG
        return_list.append(ps(p, 'TBF'))  # TBF
        return_list.append(ps(p, 'BB'))   # BB
        return_list.append(ps(p, 'AB'))   # AB
        return_list.append(ps(p, 'SO'))   # SO
        return_list.append(ps(p, 'IP'))   # IP
        pass
    return_tuple = tuple(return_list)
    return return_tuple

def custom_7(owner_index):
    return_list = []
    ps = Midtier.Stats.player_stat
    for p, d in Midtier.API.get_players_by_owner_index(owner_index).iteritems():
        cat = Midtier.API.get_position_category_by_position(d['pos'])
        if cat != 'CL':
            continue
        return_list.append(p)             # Name
        return_list.append(d['pos'])      # Pos
        return_list.append(ps(p, 'OBP'))  # OBP
        return_list.append(ps(p, 'SLG'))  # SLG
        return_list.append(ps(p, 'TBF'))  # TBF
        return_list.append(ps(p, 'BB'))   # BB
        return_list.append(ps(p, 'AB'))   # AB
        return_list.append(ps(p, 'SO'))   # SO
        return_list.append(ps(p, 'IP'))   # IP
        return_list.append(ps(p, 'SV'))   # SV
        return_list.append(ps(p, 'BLSV')) # BLSV
        return_list.append(ps(p, 'G'))    # G
        pass
    return_tuple = tuple(return_list)
    return return_tuple

