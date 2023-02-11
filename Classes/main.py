from Menu.menu import *
from game import Game
from Player import Player
import cmd, sys
class MainShell(cmd.Cmd):
    main_menu()
    prompt = ">>> "
    player1 = None
    player2 = None
# run the program and type the command two.
    # this will bring up the two player menu
    def do_main(self, args):
        main_menu()
    def do_two(self, args):
        player1, player2 = two_player_menu()

    def do_single(self, args):
        player1 = single_player_menu()
        print(player1)
        return player1

    def do_highscore(self, args):
        name = highscore_getname()
    def do_exit(self, args):
        print("Thank you for playing")
        exit()

if __name__ == "__main__":
    MainShell().cmdloop()
