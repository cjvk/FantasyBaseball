from FantasyBaseball.Utils import *
DEBUG("./Presentation/StatisticsMenu.py")

import IOEngine

__intro_msg_ = 'Statistics'
__select_msg_ = 'Please select from the following options:'
__path_ = 'Main Menu > Statistics'
__choices_ = (('1', {'text' : 'Hitting statistics summary',
                     'return_module' : 'Statboard' , 'return_function' : 'hitting_statistics_summary',},),
              ('2', {'text' : 'Starting pitching statistics summary',
                     'return_module' : 'Statboard' , 'return_function' : 'starting_pitching_statistics_summary',},),
              ('3', {'text' : 'Closers statistics summary',
                     'return_module' : 'Statboard' , 'return_function' : 'closers_statistics_summary',},),
              ('4', {'text' : 'Hitting statistics, visitor',
                     'return_module' : 'Statboard' , 'return_function' : 'hitting_statistics_vis',},),
              ('5', {'text' : 'Hitting statistics, home',
                     'return_module' : 'Statboard' , 'return_function' : 'hitting_statistics_home',},),
              ('6', {'text' : 'Starting pitching statistics, visitor',
                     'return_module' : 'Statboard' , 'return_function' : 'starting_pitching_statistics_vis',},),
              ('7', {'text' : 'Starting pitching statistics, home',
                     'return_module' : 'Statboard' , 'return_function' : 'starting_pitching_statistics_home',},),
              ('8', {'text' : 'Closer statistics, visitor',
                     'return_module' : 'Statboard' , 'return_function' : 'closers_statistics_vis',},),
              ('9', {'text' : 'Closer statistics, home',
                     'return_module' : 'Statboard' , 'return_function' : 'closers_statistics_home',},),
              ('<br>',),
              ('M', {'text' : 'Return to main menu',
                     'return_module' : 'MainMenu' , 'return_function' : 'main',},),
              ('q', {'text' : 'quit',},),
              )

def main():
    next_function_list = IOEngine.display(__intro_msg_, __select_msg_, __choices_, __path_)
    f = IOEngine.next(next_function_list)
    return f

