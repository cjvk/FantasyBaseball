# LOG(str, [loglevel])
# LOGCHAR(str, [loglevel])
# INFO(str)
# DEBUG(str)
# WARN(str)
# ERROR(str)
# ERROR2(str)
# RETURN_NO_ERROR():
# RETURN_ERROR():

# you will see all messages at or above this level
# set to 0 to set silent
__LOGLEVEL_ = 2
def LOG(str, log_level=2):
    if log_level >= __LOGLEVEL_:
        print str
        pass
    return
def LOGCHAR(char, log_level=2):
    if log_level >= __LOGLEVEL_:
        print char,
        pass
    return

def INFO(str):
    print """\
----------- INFO -------------"""
    print str
    return

__debug_ = False
def DEBUG(str):
    if __debug_:
        print str
        pass
    return

def WARN(str):
    print """
------------------------------
---------- WARNING! ----------
------------------------------"""
    print str
    return

def ERROR(str):
    print """\
 _________
/         \
|         |
|  ERROR  |
|         |
\_________/"""
    print str
    return

def ERROR2(str):
    print """\

          .-------,
        .'         '.
      .'  _ ___ _ __ '.
      |  (_' | / \|_) |
      |  ,_) | \_/|   |
      '.             .'
        '.         .'
  jgs     '-------'"""
    print str
    return

def RETURN_NO_ERROR():
    DEBUG('next function empty, returning...')
    return

def RETURN_ERROR():
    DEBUG('an error occurred')
    return

