from FantasyBaseball.Utils import *
DEBUG("./Presentation/ScoringMenu.py")

import IOEngine

__intro_msg_ = 'Scoring'
__select_msg_ = 'Please select from the following options:'
__path_ = 'Main Menu > Scoring'
__choices_ = (('1', {'text' : 'Overall score',
                     'return_module' : 'Scoreboard' , 'return_function' : 'overall_score',},),
              ('2', {'text' : 'Hitter detail score',
                     'return_module' : 'Scoreboard' , 'return_function' : 'hitter_detail_score',},),
              ('3', {'text' : 'Starter detail score',
                     'return_module' : 'Scoreboard' , 'return_function' : 'starter_detail_score',},),
              ('4', {'text' : 'Closer detail score',
                     'return_module' : 'Scoreboard' , 'return_function' : 'closer_detail_score',},),
              ('<br>',),
              ('5', {'text' : 'Display historical scores',
                     'return_module' : 'Scoreboard' , 'return_function' : 'read_scores_from_disk',},),
              ('6', {'text' : 'Add current score to historical scores',
                     'return_module' : 'Scoreboard' , 'return_function' : 'write_scores_to_disk',},),
              ('<br>',),
              ('M', {'text' : 'Return to main menu',
                     'return_module' : 'MainMenu' , 'return_function' : 'main',},),
              ('q', {'text' : 'quit',},),
              )


def main():
    next_function_list = IOEngine.display(__intro_msg_, __select_msg_, __choices_, __path_)
    f = IOEngine.next(next_function_list)
    return f

