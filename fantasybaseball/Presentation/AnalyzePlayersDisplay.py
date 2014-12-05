from FantasyBaseball.Utils import *
DEBUG("./Presentation/AnalyzePlayers.py")

import IOEngine
import AnalyzePlayersDisplayHelper

__main_menu_ = ['MainMenu', 'main']
__analysis_main_menu_ = ['AnalysisMenu', 'main']

def under_construction():
    str = """
This section under construction
"""
    IOEngine.display_only(str)
    f = IOEngine.next(__analysis_main_menu_)
    return f

def overall_simple():
    str = """\
         ____________________________________________________________
        |            |       |                   |                   |
        |   Owner    |  Pos  |        out        |        in         |
        |____________|_______|___________________|___________________|
        |            |       |                   |                   |
        | %-10s |  %3s  | %-17s | %-17s |
        |____________|_______|___________________|___________________|
        |            |       |                   |                   |
        | %-10s |  %3s  | %-17s | %-17s |
        |____________|_______|___________________|___________________|
""" % AnalyzePlayersDisplayHelper.custom_1()

    IOEngine.display_only(str)
    return IOEngine.next(__analysis_main_menu_)

def catchers():
    return generic_offense_pitching('C', 'Catchers')

def first_basemen():
    return generic_offense_pitching('1B', 'First Basemen')

def second_basemen():
    return generic_offense_pitching('2B', 'Second Basemen')

def third_basemen():
    return generic_offense_pitching('3B', 'Third Basemen')

def shortstops():
    return generic_offense_pitching('SS', 'Shortstops')

def left_fielders():
    return generic_offense_pitching('LF', 'Left fielders')

def center_fielders():
    return generic_offense_pitching('CF', 'Center fielders')

def right_fielders():
    return generic_offense_pitching('RF', 'Right fielders')

def starting_pitching():
    return generic_offense_pitching('SP', 'Starting pitching')

def closers():
    return generic_offense_pitching('CL', 'Closers')

def generic_offense_pitching(pos_chars, pos_long):

    str1 = """\
         _______________________________________________
        |                   |                   |       |
        | %-17s |       Name        | 18OPS |
        |___________________|___________________|_______|""" % (pos_long)

    str2 = """
        |                   |                   |       |
        | %-17s | %-17s | %5.3f |
        |___________________|___________________|_______|
        |                   |                   |       |
        | %-17s | %-17s | %5.3f |
        |___________________|___________________|_______|
        |                   |                   |       |
        | %-17s | %-17s | %5.3f |
        |___________________|___________________|_______|
        |                   |                   |       |
        | %-17s | %-17s | %5.3f |
        |___________________|___________________|_______|
""" % AnalyzePlayersDisplayHelper.custom_2(pos_chars)

    IOEngine.display_only(str1 + str2)
    return IOEngine.next(__analysis_main_menu_)

def overall_search_1():
    str = """\
         __________________________________________________________________________
        |                  |       |                   |                   |       |
        |      Owner       |  Pos  |        out        |        in         | delta |
        |__________________|_______|___________________|___________________|_______|
        |                  |       |                   |                   |       |
        | %-16s |  %3s  | %-17s | %-17s | %5.2f |
        |__________________|_______|___________________|___________________|_______|
        |                  |       |                   |                   |       |
        | %-16s |  %3s  | %-17s | %-17s | %5.2f |
        |__________________|_______|___________________|___________________|_______|
        |                  |       |                   |                   |       |
        | %-16s |  %3s  | %-17s | %-17s | %5.2f |
        |__________________|_______|___________________|___________________|_______|
        |                  |       |                   |                   |       |
        | %-16s |  %3s  | %-17s | %-17s | %5.2f |
        |__________________|_______|___________________|___________________|_______|
        |                  |       |                   |                   |       |
        | %-16s |  %3s  | %-17s | %-17s | %5.2f |
        |__________________|_______|___________________|___________________|_______|
        |                  |       |                   |                   |       |
        | %-16s |  %3s  | %-17s | %-17s | %5.2f |
        |__________________|_______|___________________|___________________|_______|
""" % AnalyzePlayersDisplayHelper.custom_3()

    IOEngine.display_only(str)
    return IOEngine.next(__analysis_main_menu_)

