from FantasyBaseball.Utils import *
DEBUG("./Presentation/AnalysisMenu.py")

import IOEngine

__intro_msg_ = 'Analysis'
__select_msg_ = 'Please select from the following options:'
__path_ = 'Main Menu > Analysis'
__choices_ = (('A', {'text' : '-------- Simple 18OPS --------',
                     'return_module' : 'AnalysisMenu' , 'return_function' : 'main',},),
              ('1', {'text' : 'Starting pitching analysis',
                     'return_module' : 'AnalyzePlayersDisplay' , 'return_function' : 'starting_pitching',},),
              ('1a',{'text' : 'Closers analysis',
                     'return_module' : 'AnalyzePlayersDisplay' , 'return_function' : 'closers',},),
              ('2', {'text' : 'Catcher analysis',
                     'return_module' : 'AnalyzePlayersDisplay' , 'return_function' : 'catchers'},),
              ('3', {'text' : 'First base analysis',
                     'return_module' : 'AnalyzePlayersDisplay' , 'return_function' : 'first_basemen'},),
              ('4', {'text' : 'Second base analysis',
                     'return_module' : 'AnalyzePlayersDisplay' , 'return_function' : 'second_basemen'},),
              ('5', {'text' : 'Third base analysis',
                     'return_module' : 'AnalyzePlayersDisplay' , 'return_function' : 'third_basemen'},),
              ('6', {'text' : 'Shortstop analysis',
                     'return_module' : 'AnalyzePlayersDisplay' , 'return_function' : 'shortstops'},),
              ('7', {'text' : 'Left field analysis',
                     'return_module' : 'AnalyzePlayersDisplay' , 'return_function' : 'left_fielders'},),
              ('8', {'text' : 'Center field analysis',
                     'return_module' : 'AnalyzePlayersDisplay' , 'return_function' : 'center_fielders'},),
              ('9', {'text' : 'Right field analysis',
                     'return_module' : 'AnalyzePlayersDisplay' , 'return_function' : 'right_fielders'},),
              ('10', {'text' : 'Overall analysis',
                      'return_module' : 'AnalyzePlayersDisplay' , 'return_function' : 'overall_simple',},),
              ('<br>',),
              ('B', {'text' : '-------- Search level 1 --------',
                     'return_module' : 'AnalysisMenu' , 'return_function' : 'main',},),
              ('11', {'text' : 'Overall analysis',
                     'return_module' : 'AnalyzePlayersDisplay' , 'return_function' : 'overall_search_1',},),
              ('<br>',),
              ('M', {'text' : 'Return to main menu',
                     'return_module' : 'MainMenu' , 'return_function' : 'main',},),
              ('q', {'text' : 'quit',},),
              )


def main():
    next_function_list = IOEngine.display(__intro_msg_, __select_msg_, __choices_, __path_)
    f = IOEngine.next(next_function_list)
    return f

