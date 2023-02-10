from Menu.menu import *
from game import Game
from Player import Player
import cmd, sys
class MainShell(cmd.Cmd):
    main_menu()
    prompt = ">>> "
# run the program and type the command two.
    # this will bring up the two player menu
    def do_two(self, args):
        player1, player2 = two_player_menu()
        return player1, player2



if __name__ == "__main__":
    MainShell().cmdloop()