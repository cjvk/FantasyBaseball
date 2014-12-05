from FantasyBaseball.Utils import *
DEBUG("./Presentation/LoadExistingLeague.py")

import IOEngine
from FantasyBaseball import Midtier

__main_menu_ = ['MainMenu', 'main']
__admin_menu_ = ['AdminMenu', 'main']

def main():
    DEBUG('LoadExistingLeague.main()')
    Midtier.League.load_existing()
    return IOEngine.next(__main_menu_)

def create_players():
    DEBUG('LoadExistingLeague.create_players()')
    Midtier.League.create_players()
    return IOEngine.next(__admin_menu_)

def save_player_stats():
    DEBUG('LoadExistingLeague.save_player_stats()')
    Midtier.League.save_player_stats()
    return IOEngine.next(__admin_menu_)

