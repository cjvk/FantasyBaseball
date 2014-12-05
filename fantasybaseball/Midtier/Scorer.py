from FantasyBaseball.Utils import *

DEBUG('./Midtier/Scorer.py')

from FantasyBaseball import Data
import Stats
import Public
import FantasyBaseball
import ScoringUtils
from datetime import date
from datetime import datetime

__scoring_stats_ = {'H' : {'18OPS' : {'points_per_stat' : 37.5,
                                      'lower_threshold' : 0.0,
                                      'upper_threshold' : 0.0963,
                                      'complex_function': {'function': 'ops18',
                                                           'arg1': 'OBP',
                                                           'arg2': 'SLG',},},
                           'PA'    : {'points_per_stat' : 12.5,
                                      'lower_threshold' : 325.0,
                                      'upper_threshold' : 975.0,
                                      'simple_function' : 'TPA',},
                           },
                    'SP' : {'18OPS': {'points_per_stat' : 22.5,
                                      'lower_threshold' : 0.0,
                                      'upper_threshold' : 0.0698,
                                      'invert'          : '',
                                      'complex_function': {'function': 'ops18',
                                                           'arg1': 'OBP',
                                                           'arg2': 'SLG',},},
                            'IP'   : {'points_per_stat' : 11.25,
                                      'lower_threshold' : 110.0,
                                      'upper_threshold' : 220.0,
                                      'simple_function' : 'IP'},
                            'K/9'  : {'points_per_stat' : 3.75,
                                      'lower_threshold' : 0.0,
                                      'upper_threshold' : 1.72,
                                      'complex_function': {'function': 'k9',
                                                           'arg1': 'SO',
                                                           'arg2': 'IP',},},
                            },
                    'CL' : {'18OPS': {'points_per_stat' : 5.625,
                                      'lower_threshold' : 0.0,
                                      'upper_threshold' : 0.125,
                                      'invert'          : '',
                                      'complex_function': {'function': 'ops18',
                                                           'arg1': 'OBP',
                                                           'arg2': 'SLG',},},
                            'G'    : {'points_per_stat' : 3.75,
                                      'lower_threshold' : 22.0,
                                      'upper_threshold' : 44.0,
                                      'simple_function' : 'G'},
                            'SV%'  : {'points_per_stat' : 1.875,
                                      'lower_threshold' : 0.0,
                                      'upper_threshold' : 0.0564,
                                      'complex_function': {'function': 'svp',
                                                           'arg1': 'SV',
                                                           'arg2': 'BLSV',},},
                            'K/9'  : {'points_per_stat' : 1.25,
                                      'lower_threshold' : 0.0,
                                      'upper_threshold' : 2.74,
                                      'complex_function': {'function': 'k9',
                                                           'arg1': 'SO',
                                                           'arg2': 'IP',},},
                            },
                    }

def internal_get_score_inverted(category, score_stat, visitor_value, home_value):
    return internal_get_score(category, score_stat, home_value, visitor_value)

def internal_get_score(category, score_stat, visitor_value, home_value):
    """
    return_dict = {'visitor_score': <float>, 'home_score': <float>, 'home+': <float>}
    """
    delta = home_value - visitor_value
    pts = __scoring_stats_[category][score_stat]['points_per_stat']
    lt = __scoring_stats_[category][score_stat]['lower_threshold']
    ut = __scoring_stats_[category][score_stat]['upper_threshold']
    home_score = 0
    if delta <= -1*ut:
        # all points to visitor
        pass
    elif delta >= -1*ut and delta <= -1*lt:
        # partial points to visitor
        # pretend home is winning, then invert back
        delta *= -1
        home_score = pts/2 + ((pts / 2) * (delta - lt) / (ut - lt))
        home_score = pts - home_score
        pass
    elif delta >= -1*lt and delta <= lt:
        # tie
        home_score = pts/2
        pass
    elif delta >= lt and delta <= ut:
        # partial points to home
        home_score = pts/2 + ((pts / 2) * (delta - lt) / (ut - lt))
        pass
    else:
        # all points to home
        home_score = pts
        pass
    visitor_score = pts - home_score
    return_dict = {'visitor_score' : visitor_score,
                   'home_score'    : home_score,
                   'home+'         : (home_score-visitor_score)/2,
                   }
    
    return return_dict

def get_raw_scores():
    """
    returns a dictionary of all scores
    """
    vis = Public.CurrentLeague.owners[0]['name']
    home = Public.CurrentLeague.owners[1]['name']
    return_dict = {'HOME' : {'H' : {} ,
                             'SP': {} ,
                             'CL': {} ,
                             },
                   'VIS' : {'H' : {} ,
                            'SP': {} ,
                            'CL': {} ,
                            },
                   '+' : {'H' : {} ,
                          'SP': {} ,
                          'CL': {} ,
                          },
                   }
    for c in __scoring_stats_.keys(): # category
        for s in __scoring_stats_[c].keys(): # scoring stat
            stat_dict = __scoring_stats_[c][s]
            if 'invert' in stat_dict:
                score_func = internal_get_score_inverted
            else:
                score_func = internal_get_score
                pass
            if 'simple_function' in stat_dict:
                vis_stat = Stats.team_stat(vis, c, stat_dict['simple_function'])
                home_stat = Stats.team_stat(home, c, stat_dict['simple_function'])
            elif 'complex_function' in stat_dict:
                f = getattr(ScoringUtils, stat_dict['complex_function']['function'])
                arg1 = stat_dict['complex_function']['arg1']
                arg2 = stat_dict['complex_function']['arg2']
                vis_stat = f(Stats.team_stat(vis, c, arg1), Stats.team_stat(vis, c, arg2))
                home_stat = f(Stats.team_stat(home, c, arg1), Stats.team_stat(home, c, arg2))
            else:
                ERROR('error in stat_dict')
                return {}

            score_dict = score_func(c, s, vis_stat, home_stat)

            return_dict['VIS'][c][s] = score_dict['visitor_score']
            return_dict['HOME'][c][s] = score_dict['home_score']
            return_dict['+'][c][s] = score_dict['home+']
            pass
        pass
    return return_dict
    
def get_historical_home_scores():
    """
    return a sorted list of (date, home_score) tuples
    e.g. [(date1, score1), (date2, score2)]
    """
    # get historical scores
    Data.HistoricalDataPickler.unpickle()
    unpickled_scores = Data.Public.HistoricalScoresDict
#    unpickled_scores = {'20070113' : ('Tue Jan 13 2007 12341234', '0.43234333234'),
#                        '20070112' : ('Mon Jan 12 2007 12341234', '0.87348738123')}
    the_dates = unpickled_scores.keys()
    the_dates.sort()
    return_list = []
    for d in the_dates:
        return_list.insert(0, unpickled_scores[d])
        pass
    return return_list

def write_historical_home_score():
    all_scores = get_raw_scores()
    total_score = float(0)
    for cat in all_scores['HOME']:
        for stat in all_scores['HOME'][cat]:
            total_score += all_scores['HOME'][cat][stat]
            pass
        pass
    Data.HistoricalDataPickler.unpickle()
    Data.Public.HistoricalScoresDict[datetime.now()] = (datetime.now().ctime(), total_score,)
    Data.HistoricalDataPickler.pickle()
    return

