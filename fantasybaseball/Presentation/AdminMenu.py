from FantasyBaseball.Utils import *
DEBUG("./Presentation/AdminMenu.py")

import IOEngine

__intro_msg_ = 'Admin'
__select_msg_ = 'Please select from the following options:'
__path_ = 'Main Menu > Admin'
__choices_ = (('1', {'text' : 'create players from PlayerInfoDictionary',
                     'return_module' : 'LoadExistingLeague' , 'return_function' : 'create_players'},),
              ('2', {'text' : 'update all existing players (long)',
                     'return_module' : 'UpdateAllPlayers' , 'return_function' : 'are_you_sure'},),
              ('3', {'text' : 'save player stats',
                     'return_module' : 'LoadExistingLeague' , 'return_function' : 'save_player_stats'},),
              ('<br>',),
              ('M', {'text' : 'Return to main menu',
                     'return_module' : 'MainMenu' , 'return_function' : 'main',},),
              ('q', {'text' : 'quit',},),
              )


def main():
    next_function_list = IOEngine.display(__intro_msg_, __select_msg_, __choices_, __path_)
    f = IOEngine.next(next_function_list)
    return f

