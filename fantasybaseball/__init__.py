import Presentation
import Utils

def play():
    Utils.DEBUG('FantasyBaseball.play()')
    f = Presentation.WelcomeMessage.main()
    while not f is None:
        f = f()
        pass
    return

