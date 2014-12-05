from FantasyBaseball.Utils import *
DEBUG("./Presentation/AnalyzePlayersDisplayHelper.py")

import IOEngine
from FantasyBaseball import Midtier

def custom_1():
    raw_analysis = Midtier.PlayerAnalyzer.raw_analysis()

    m11 = Midtier.Public.CurrentLeague.owners[0]['name']
    m12 = raw_analysis['simple_18ops']['best_trade'][0]['pos']
    m13 = raw_analysis['simple_18ops']['best_trade'][0]['out']
    m14 = raw_analysis['simple_18ops']['best_trade'][0]['in']

    m21 = Midtier.Public.CurrentLeague.owners[1]['name']
    m22 = raw_analysis['simple_18ops']['best_trade'][1]['pos']
    m23 = raw_analysis['simple_18ops']['best_trade'][1]['out']
    m24 = raw_analysis['simple_18ops']['best_trade'][1]['in']

    return (m11, m12, m13, m14,
            m21, m22, m23, m24,
            )

def custom_2(pos):
    raw_analysis = Midtier.PlayerAnalyzer.raw_analysis()

    m11 = Midtier.Public.CurrentLeague.owners[0]['name'] + ' worst'
    m12 = raw_analysis['simple_18ops']['worst_per_position'][pos][0][0]
    m13 = Midtier.Stats.player_stat_18ops(m12)

    m21 = Midtier.Public.CurrentLeague.owners[1]['name'] + ' worst'
    m22 = raw_analysis['simple_18ops']['worst_per_position'][pos][1][0]
    m23 = Midtier.Stats.player_stat_18ops(m22)

    m31 = '#1 Available'
    m32 = raw_analysis['simple_18ops']['best_available'][pos][0]
    m33 = Midtier.Stats.player_stat_18ops(m32)

    m41 = '#2 Available'
    m42 = raw_analysis['simple_18ops']['best_available'][pos][1]
    m43 = Midtier.Stats.player_stat_18ops(m42)

    return (m11, m12, m13,
            m21, m22, m23,
            m31, m32, m33,
            m41, m42, m43,
            )

def custom_3():
    raw_analysis_search = Midtier.PlayerAnalyzer.raw_analysis_search()

    return_list = []

    for i in range(0, 2): # owner
        for j in range(0, 3): # number of trades to display
            m_1 = Midtier.Public.CurrentLeague.owners[i]['name'] + ' ' + str(j+1)
            m_2 = raw_analysis_search['search_replace']['best_trade'][i][j]['pos']
            m_3 = raw_analysis_search['search_replace']['best_trade'][i][j]['out']
            m_4 = raw_analysis_search['search_replace']['best_trade'][i][j]['in']
            m_5 = raw_analysis_search['search_replace']['best_trade'][i][j]['diff']
            return_list.extend([m_1, m_2, m_3, m_4, m_5])

    #    return ('Chris', 'C', 'M. Barrett', 'J. Posada', 3.2456,
    #            'Alexander', 'CF', 'V. Wells', 'B.J. Upton', 1.98244343)

    return tuple(return_list)

