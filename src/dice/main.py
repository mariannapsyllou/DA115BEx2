import cmd
import sys
import menu
import two_player
import single_player
import Highscores


class MainShell(cmd.Cmd):
    """
    This class takes care of the main menus,
    and the setup of games
    """
    prompt = ">>> "

    def __init__(self):
        super().__init__()
        self.player1 = None
        self.player2 = None
        self.difficulty = None
        self.highscore_name = None
        menu.main_menu()

    def do_main(self, _):
        """
        Prints the main menu
        """
        menu.main_menu()

    def do_two(self, _):
        """
        prompts user for two names,
        then starts two-player mode
        """
        self.player1, self.player2 = menu.two_player_menu()
        two_player.TwoPlayer(self.player1, self.player2)

    def do_single(self, _):
        """
        Prompts user for name and difficulty,
        then starts single-player mode
        """
        try:
            self.player1, self.difficulty = menu.single_player_menu()
            single_player.SinglePlayer(self.player1, self.difficulty)
        except ValueError:
            print("Please pick a number")

    def do_highscore(self, _):
        """
        Asks for name and prints highscore
        of entered name if registered
        """
        self.highscore_name = menu.highscore_getname()
        high = Highscores.Highscores()
        high.scores(self.highscore_name)

    def do_view(self, _):
        """
        Prints the instruction for the program
        """
        high = Highscores.Highscores()
        high.view_instructions()

    def do_exit(self, _):
        """
        Prints exit message and exits program
        """
        menu.exit_menu()
        sys.exit()


if __name__ == "__main__":
    MainShell().cmdloop()
