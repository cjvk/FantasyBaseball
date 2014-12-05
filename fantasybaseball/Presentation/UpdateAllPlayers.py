from FantasyBaseball.Utils import *
DEBUG("./Presentation/UpdateAllPlayers.py")

import IOEngine
from FantasyBaseball import Midtier

__main_menu_ = ['MainMenu', 'main']
__admin_menu_ = ['AdminMenu', 'main']

__intro_msg_ = 'Updating all players may take a long time'
__select_msg_ = 'Are you sure you want to continue?'
__path_ = 'Main Menu > Admin > Update all players'
__choices_ = (('1', {'text' : 'yes',
                     'return_module' : 'UpdateAllPlayers' , 'return_function' : 'main'},),
              ('2', {'text' : 'no',
                     'return_module' : 'AdminMenu' , 'return_function' : 'main'},),
              )

def main():
    DEBUG('LoadExistingLeague.update_all_players()')
    Midtier.League.update_all_players()
    return IOEngine.next(__admin_menu_)

def are_you_sure():
    next_function_list = IOEngine.display(__intro_msg_, __select_msg_, __choices_, __path_)
    f = IOEngine.next(next_function_list)
    return f

