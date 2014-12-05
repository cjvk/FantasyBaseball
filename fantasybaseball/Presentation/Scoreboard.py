from FantasyBaseball.Utils import *
DEBUG("./Presentation/Scoreboard.py")

import IOEngine
import ScoreboardHelper
from FantasyBaseball import Midtier

__main_menu_ = ['MainMenu', 'main']
__scoring_menu_ = ['ScoringMenu', 'main']

def hitter_detail_score():
    str = """\
         _____________________________
        |     |       |       |       |
        |  H  | 18OPS |  PA   | Total |
        |_____|_______|_______|_______|
        |     |       |       |       |
        | Vis | %5.2f | %5.2f | %5.2f |
        |_____|_______|_______|_______|
        |     |       |       |       |
        | Hom | %5.2f | %5.2f | %5.2f |
        |_____|_______|_______|_______|
        |     |       |       |       |
        |  +  | %5.2f | %5.2f | %5.2f |
        |_____|_______|_______|_______|
""" % ScoreboardHelper.custom_1()
    
    IOEngine.display_only(str)
    return IOEngine.next(__scoring_menu_)

def starter_detail_score():
    str = """\
         _____________________________________
        |     |       |       |       |       |
        | SP  | 18OPS |  IP   |  K/9  | Total |
        |_____|_______|_______|_______|_______|
        |     |       |       |       |       |
        | Vis | %5.2f | %5.2f | %5.2f | %5.2f |
        |_____|_______|_______|_______|_______|
        |     |       |       |       |       |
        | Hom | %5.2f | %5.2f | %5.2f | %5.2f |
        |_____|_______|_______|_______|_______|
        |     |       |       |       |       |
        |  +  | %5.2f | %5.2f | %5.2f | %5.2f |
        |_____|_______|_______|_______|_______|
""" % ScoreboardHelper.custom_2()
    
    IOEngine.display_only(str)
    return IOEngine.next(__scoring_menu_)

def closer_detail_score():
    str = """\
         _____________________________________________
        |     |       |       |       |       |       |
        | CL  | 18OPS |   G   |  SV%%  |  K/9  | Total |
        |_____|_______|_______|_______|_______|_______|
        |     |       |       |       |       |       |
        | Vis | %5.2f | %5.2f | %5.2f | %5.2f | %5.2f |
        |_____|_______|_______|_______|_______|_______|
        |     |       |       |       |       |       |
        | Hom | %5.2f | %5.2f | %5.2f | %5.2f | %5.2f |
        |_____|_______|_______|_______|_______|_______|
        |     |       |       |       |       |       |
        |  +  | %5.2f | %5.2f | %5.2f | %5.2f | %5.2f |
        |_____|_______|_______|_______|_______|_______|
""" % ScoreboardHelper.custom_3()
    
    IOEngine.display_only(str)
    return IOEngine.next(__scoring_menu_)

def overall_score():
    str = """\
         _____________________________________
        |     |       |       |       |       |
        | Tot |   H   |  SP   |  CL   | Total |
        |_____|_______|_______|_______|_______|
        |     |       |       |       |       |
        | Vis | %5.2f | %5.2f | %5.2f | %5.2f |
        |_____|_______|_______|_______|_______|
        |     |       |       |       |       |
        | Hom | %5.2f | %5.2f | %5.2f | %5.2f |
        |_____|_______|_______|_______|_______|
        |     |       |       |       |       |
        |  +  | %5.2f | %5.2f | %5.2f | %5.2f |
        |_____|_______|_______|_______|_______|
""" % ScoreboardHelper.custom_4()
    
    IOEngine.display_only(str)
    return IOEngine.next(__scoring_menu_)

def read_scores_from_disk():

    initial_str = """\
         ________________________________________________
        |                                                |
        |                Previous scores                 |
        |_______________________________________________ |
"""
    repeating_str = """\
        |     |                          |               |
        | Hom | %s | %s |
        |_____|__________________________|_______________|
"""

    date_score_tuple_list = Midtier.Scorer.get_historical_home_scores()
    str = initial_str
    for dt_tuple in date_score_tuple_list:
        str += (repeating_str % dt_tuple)
        pass
    IOEngine.display_only(str)

    return IOEngine.next(__scoring_menu_)

def write_scores_to_disk():
    str = """\
         ________________________________________________
        |                                                |
        |             Saving scores to disk              |
        |_______________________________________________ |
"""
    IOEngine.display_only(str)
    Midtier.Scorer.write_historical_home_score()
    return IOEngine.next(__scoring_menu_)

