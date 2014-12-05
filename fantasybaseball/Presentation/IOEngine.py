from FantasyBaseball.Utils import *
DEBUG("./Presentation/IOEngine.py")

import FantasyBaseball
from FantasyBaseball import Utils

def display_only(str):
    DEBUG('Presentation.IOEngine.display_only()')
    print
    print str
    print

def display(intro, select, choices, path):
    """
    intro (string): message of introduction
    select (string): message introducing choices
    choices (tuple): ((user_choice1, {dict1}), (user_choice2, {dict2}))
         {'text' : <description>, # string, mandatory
          'return_module' : <module_name> # string, optional
          'return_funciton' : <function_name> # string, optional
          }

    Example:
    Welcome to Fantasy Baseball!

    Please select from the following choices:
    1) new league
    2) load existing league
    >> 

    """
    DEBUG('Presentation.IOEngine.display()')

    while True:
        if path != '':
            print
            print 'You are here: ' + path
            print
            pass
        print
        print intro
        print
        print select
        all_choices_dict = {}
        for i in range(0, len(choices)):
            tuple = choices[i]
            c = tuple[0]
            if c == '<br>':
                print
                continue
            d = tuple[1]
            if c in all_choices_dict:
                ERROR('more than one choice with name: ' + c)
                pass
            else:
                all_choices_dict[c] = i
                pass
            print c + ') ' + d['text']
            pass
        print

        user_choice = raw_input(">>> ")

        DEBUG('You chose ' + user_choice)
        if user_choice in all_choices_dict:
            selection_dict = choices[all_choices_dict[user_choice]][1]
            DEBUG('Description: ' + selection_dict['text'])
            if 'return_module' in selection_dict and 'return_function' in selection_dict:
                DEBUG('IOEngine.run(): found a return module.function')
                return [selection_dict['return_module'], selection_dict['return_function']]
            else:
                return [] # if no (return_module, return_function) specified, assume exit
            pass
        # user input is not in the available choices
        if user_choice == 'quit' or user_choice == 'exit' or user_choice == 'quit()' or user_choice == 'exit()':
            return []
        DEBUG('Description: not found!')
        pass
    pass

def next(list):
    if list is None:
        f = Utils.RETURN_ERROR
        pass
    elif list == []:
        f = Utils.RETURN_NO_ERROR
        pass
    else:
        DEBUG('destination module: ' + list[0])
        DEBUG('destination function: ' + list[1])
        module = getattr(FantasyBaseball.Presentation, list[0])
        f = getattr(module, list[1])
    return f
