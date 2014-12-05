from FantasyBaseball.Utils import *
DEBUG("./Presentation/ScoreboardHelper.py")

from FantasyBaseball import Midtier

def custom_1():
    raw_scores = Midtier.Scorer.get_raw_scores()

    visitor = raw_scores['VIS']
    home = raw_scores['HOME']
    plus = raw_scores['+']

    # visitor
    m22 = visitor['H']['18OPS']
    m23 = visitor['H']['PA']
    m24 = m22 + m23

    # home
    m32 = home['H']['18OPS']
    m33 = home['H']['PA']
    m34 = m32 + m33

    # "plus score"
    m42 = plus['H']['18OPS']
    m43 = plus['H']['PA']
    m44 = m42 + m43

    return_tuple = (m22, m23, m24,
                    m32, m33, m34,
                    m42, m43, m44,
                    )
    return return_tuple

def custom_2():
    raw_scores = Midtier.Scorer.get_raw_scores()

    visitor = raw_scores['VIS']
    home = raw_scores['HOME']
    plus = raw_scores['+']

    # visitor
    m22 = visitor['SP']['18OPS']
    m23 = visitor['SP']['IP']
    m24 = visitor['SP']['K/9']
    m25 = m22 + m23 + m24

    # home
    m32 = home['SP']['18OPS']
    m33 = home['SP']['IP']
    m34 = home['SP']['K/9']
    m35 = m32 + m33 + m34

    # "plus score"
    m42 = plus['SP']['18OPS']
    m43 = plus['SP']['IP']
    m44 = plus['SP']['K/9']
    m45 = m42 + m43 + m44

    return_tuple = (m22, m23, m24, m25,
                    m32, m33, m34, m35,
                    m42, m43, m44, m45,
                    )
    return return_tuple

def custom_3():
    raw_scores = Midtier.Scorer.get_raw_scores()

    visitor = raw_scores['VIS']
    home = raw_scores['HOME']
    plus = raw_scores['+']

    # visitor
    m22 = visitor['CL']['18OPS']
    m23 = visitor['CL']['G']
    m24 = visitor['CL']['SV%']
    m25 = visitor['CL']['K/9']
    m26 = m22 + m23 + m24 + m25

    # home
    m32 = home['CL']['18OPS']
    m33 = home['CL']['G']
    m34 = home['CL']['SV%']
    m35 = home['CL']['K/9']
    m36 = m32 + m33 + m34 + m35

    # "plus score"
    m42 = plus['CL']['18OPS']
    m43 = plus['CL']['G']
    m44 = plus['CL']['SV%']
    m45 = plus['CL']['K/9']
    m46 = m42 + m43 + m44 + m45

    return_tuple = (m22, m23, m24, m25, m26,
                    m32, m33, m34, m35, m36,
                    m42, m43, m44, m45, m46,
                    )
    return return_tuple

def custom_4():
    raw_scores = Midtier.Scorer.get_raw_scores()

    visitor = raw_scores['VIS']
    home = raw_scores['HOME']
    plus = raw_scores['+']

    # visitor
    m22 = visitor['H']['18OPS'] + visitor['H']['PA']
    m23 = visitor['SP']['18OPS'] + visitor['SP']['IP'] + visitor['SP']['K/9']
    m24 = visitor['CL']['18OPS'] + visitor['CL']['G'] + visitor['CL']['SV%'] + visitor['CL']['K/9']
    m25 = m22 + m23 + m24

    # home
    m32 = home['H']['18OPS'] + home['H']['PA']
    m33 = home['SP']['18OPS'] + home['SP']['IP'] + home['SP']['K/9']
    m34 = home['CL']['18OPS'] + home['CL']['G'] + home['CL']['SV%'] + home['CL']['K/9']
    m35 = m32 + m33 + m34

    # "plus score"
    m42 = plus['H']['18OPS'] + plus['H']['PA']
    m43 = plus['SP']['18OPS'] + plus['SP']['IP'] + plus['SP']['K/9']
    m44 = plus['CL']['18OPS'] + plus['CL']['G'] + plus['CL']['SV%'] + plus['CL']['K/9']
    m45 = m42 + m43 + m44

    return_tuple = (m22, m23, m24, m25,
                    m32, m33, m34, m35,
                    m42, m43, m44, m45,
                    )
    return return_tuple

