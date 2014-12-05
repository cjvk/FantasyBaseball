from FantasyBaseball.Utils import *
DEBUG("./Presentation/WelcomeMessage.py")

import IOEngine

__intro_msg2 = """\
Welcome to Fantasy Baseball!
version: 2.0
author: Christopher von Krogh"""

__intro_msg_ = """\
 _____________________________________________
|                                             |
|                                             |
|         Welcome to Fantasy Baseball         |
|                                             |
|_____________________________________________|
|                                             |
| author: Christopher von Krogh               |
| version: 2.0                                |
|_____________________________________________|"""

__select_msg_ = "Please select from the following options:"
__path_ = ''

__choices_ = (('1', {'text' : 'Load existing league',
                     'return_module' : 'LoadExistingLeague' , 'return_function' : 'main'},
               ),
              ('2', {'text' : 'Create new league (draft style)',
                     'return_module' : 'UnderConstruction' , 'return_function' : 'exit'},
               ),
              ('3', {'text' : 'Create new league (bulk)',
                     'return_module' : 'UnderConstruction' , 'return_function' : 'exit'},
               ),
              ('4', {'text' : 'quit'},
               ),
              )

def main():
    next_function_list = IOEngine.display(__intro_msg_, __select_msg_, __choices_, __path_)
    f = IOEngine.next(next_function_list)
    return f
