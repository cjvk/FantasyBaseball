from FantasyBaseball.Utils import *
DEBUG("./Presentation/Statboard.py")

import IOEngine
import StatboardHelper

__main_menu_ = ['MainMenu', 'main']
__statistics_menu_ = ['StatisticsMenu', 'main']

def hitting_statistics_summary():
    str = """\
         _____________________________________
        |     |       |       |       |       |
        |  H  |  OBP  |  SLG  |  TPA  |  AB   |
        |_____|_______|_______|_______|_______|
        |     |       |       |       |       |
        | Vis | %.3f | %.3f | %5d | %5d |
        |_____|_______|_______|_______|_______|
        |     |       |       |       |       |
        | Hom | %.3f | %.3f | %5d | %5d |
        |_____|_______|_______|_______|_______|
""" % StatboardHelper.custom_1()
    
    IOEngine.display_only(str)
    return IOEngine.next(__statistics_menu_)

def starting_pitching_statistics_summary():
    str = """\
         _____________________________________________________________
        |     |       |       |       |       |       |       |       |
        | SP  |  OBP  |  SLG  |  TBF  |  BB   | "AB"  |  SO   |  IP   |
        |_____|_______|_______|_______|_______|_______|_______|_______|
        |     |       |       |       |       |       |       |       |
        | Vis | %.3f | %.3f | %4d  |  %3d  | %4d  | %4d  |%7.2f|
        |_____|_______|_______|_______|_______|_______|_______|_______|
        |     |       |       |       |       |       |       |       |
        | Hom | %.3f | %.3f | %4d  |  %3d  | %4d  | %4d  |%7.2f|
        |_____|_______|_______|_______|_______|_______|_______|_______|
""" % StatboardHelper.custom_2()
    
    IOEngine.display_only(str)
    return IOEngine.next(__statistics_menu_)

def closers_statistics_summary():
    str = """\
         _____________________________________________________________________________________
        |     |       |       |       |       |       |       |       |       |       |       |
        | CL  |  OBP  |  SLG  |  TBF  |  BB   | "AB"  |  SO   |  IP   |  SV   | BLSV  |   G   |
        |_____|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|
        |     |       |       |       |       |       |       |       |       |       |       |
        | Vis | %.3f | %.3f | %4d  |  %3d  | %4d  |  %3d  | %6.2f|  %3d  |  %2d   |  %3d  |
        |_____|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|
        |     |       |       |       |       |       |       |       |       |       |       |
        | Hom | %.3f | %.3f | %4d  |  %3d  | %4d  |  %3d  | %6.2f|  %3d  |  %2d   |  %3d  |
        |_____|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|
""" % StatboardHelper.custom_3()
    
    IOEngine.display_only(str)
    return IOEngine.next(__statistics_menu_)

def display_names():
    str = """\
         __________________
        |     |            |
        | Vis | %-10s |
        |_____|____________|
        |     |            |
        | Hom | %-10s |
        |_____|____________|
""" % StatboardHelper.custom_4()
    
    IOEngine.display_only(str)
    return IOEngine.next(__main_menu_)

def hitting_statistics_vis():
    return internal_hitting_statistics(0) # 0 is visitor

def hitting_statistics_home():
    return internal_hitting_statistics(1) # 1 is home

def internal_hitting_statistics(owner_index):
    return_tuple = StatboardHelper.custom_5(owner_index)
    number_of_players = len(return_tuple) / 6
    str1 = """\
         ____________________________________________________________
        |                   |       ||       |       |       |       |
        |       Name        |  Pos  ||  OBP  |  SLG  |  TPA  |  AB   |
        |___________________|_______||_______|_______|_______|_______|
"""
    str2 = """\
        |                   |       ||       |       |       |       |
        | %-17s |  %3s  || %.3f | %.3f | %4d  | %4d  |
        |___________________|_______||_______|_______|_______|_______|
"""
    display_string = str1
    for i in range(0, number_of_players):
        display_string += str2
        pass

    IOEngine.display_only(display_string % return_tuple)
    return IOEngine.next(__statistics_menu_)

def starting_pitching_statistics_vis():
    return internal_starting_pitching_statistics(0)

def starting_pitching_statistics_home():
    return internal_starting_pitching_statistics(1)

def internal_starting_pitching_statistics(owner_index):
    return_tuple = StatboardHelper.custom_6(owner_index)
    number_of_players = len(return_tuple) / 9
    str1 = """\
         ____________________________________________________________________________________
        |                   |       ||       |       |       |       |       |       |       |
        |       Name        |  Pos  ||  OBP  |  SLG  |  TBF  |  BB   | "AB"  |  SO   |  IP   |
        |___________________|_______||_______|_______|_______|_______|_______|_______|_______|
"""
    str2 = """\
        |                   |       ||       |       |       |       |       |       |       |
        | %-17s |  %3s  || %.3f | %.3f | %4d  |  %3d  | %4d  | %4d  |%7.2f|
        |___________________|_______||_______|_______|_______|_______|_______|_______|_______|
"""
    display_string = str1
    for i in range(0, number_of_players):
        display_string += str2
        pass

    IOEngine.display_only(display_string % return_tuple)
    return IOEngine.next(__statistics_menu_)

def closers_statistics_vis():
    return internal_closer_statistics(0)

def closers_statistics_home():
    return internal_closer_statistics(1)

def internal_closer_statistics(owner_index):
    return_tuple = StatboardHelper.custom_7(owner_index)
    number_of_players = len(return_tuple) / 12
    str1 = """\
         ____________________________________________________________________________________________________________
        |                   |       ||       |       |       |       |       |       |       |       |       |       |
        |       Name        |  Pos  ||  OBP  |  SLG  |  TBF  |  BB   | "AB"  |  SO   |  IP   |  SV   | BLSV  |   G   |
        |___________________|_______||_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|
"""
    str2 = """\
        |                   |       ||       |       |       |       |       |       |       |       |       |       |
        | %-17s |  %3s  || %.3f | %.3f | %4d  |  %3d  | %4d  | %4d  |%7.2f|  %3d  |  %2d   |  %3d  |
        |___________________|_______||_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|
"""
    display_string = str1
    for i in range(0, number_of_players):
        display_string += str2
        pass

    IOEngine.display_only(display_string % return_tuple)
    return IOEngine.next(__statistics_menu_)

