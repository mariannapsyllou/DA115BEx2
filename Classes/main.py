from Menu.menu import main_menu, two_player_menu, \
    single_player_menu

import cmd, sys
import game
import Intelligence


class MainShell(cmd.Cmd):
    main_menu()
    prompt = ">>> "

    def __init__(self):
        super().__init__()
        self.player1 = None
        self.player2 = None
        self.difficulty = None
        self.highscore_name = None

    def do_main(self, args):
        main_menu()

    def do_two(self, args):
        self.player1, self.player2 = two_player_menu()

        game.Game(self.player1, self.player2)

    def do_single(self, args):
        self.player1, self.difficulty = single_player_menu()

        Intelligence.Intelligence(self.player1, self.difficulty)

    def do_highscore(self, args):
        self.highscore_name = highscore_getname()

    def do_exit(self, args):
        print("Thank you for playing")
        exit()


if __name__ == "__main__":
    MainShell().cmdloop()

