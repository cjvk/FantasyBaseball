from FantasyBaseball.Utils import *
DEBUG("./Presentation/MainMenu.py")

import IOEngine

__intro_msg_ = 'Main Menu'
__select_msg_ = 'Please select from the following options:'
__path_ = 'Main Menu'
__choices_ = (('1', {'text' : 'Statistics',
                     'return_module' : 'StatisticsMenu' , 'return_function' : 'main',},),
              ('2', {'text' : 'Scoring',
                     'return_module' : 'ScoringMenu' , 'return_function' : 'main',},),
              ('3', {'text' : 'Analysis',
                     'return_module' : 'AnalysisMenu' , 'return_function' : 'main',},),
              ('4', {'text' : 'Admin',
                     'return_module' : 'AdminMenu' , 'return_function' : 'main',},),
              ('5', {'text' : 'Display participants',
                     'return_module' : 'Statboard' , 'return_function' : 'display_names',},),
              ('<br>',),
              ('q', {'text' : 'quit',},),
              )

def main():
    next_function_list = IOEngine.display(__intro_msg_, __select_msg_, __choices_, __path_)
    f = IOEngine.next(next_function_list)
    return f

