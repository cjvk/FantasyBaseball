from FantasyBaseball.Utils import *
DEBUG("./Presentation/UnderConstruction.py")

import IOEngine

__main_menu_ = ['MainMenu', 'main']


__intro_msg_ = 'This section under construction'
__select_msg_ = 'Check back again later'
__path_ = 'Main Menu > Under Construction'
__choices_main_menu_ = (('1', {'text' : 'Go back to Main Menu',
                               'return_module' : 'MainMenu' , 'return_function' : 'main'},
                         ),
                        )
__choices_exit_ = (('1', {'text' : 'exit',}
                    ),
                   )

def main_menu():
    next_function_list = IOEngine.display(__intro_msg_, __select_msg_, __choices_main_menu_, __path_)
    f = IOEngine.next(next_function_list)
    return f

def exit():
    next_function_list = IOEngine.display(__intro_msg_, __select_msg_, __choices_exit_, __path_)
    f = IOEngine.next(next_function_list)
    return f
