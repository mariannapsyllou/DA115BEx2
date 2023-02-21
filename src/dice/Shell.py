import cmd
import sys
import Intelligence
import game
import menu
import Player
import Highscores


class shell(cmd.Cmd):

    prompt = ">>>"

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.highscore = Highscores.Highscores()
        self.game = game.Game(None, None, None)
        self.player1 = None
        self.player2 = None
        self.intelligence = Intelligence.Intelligence()
        print(menu.main_menu())

    def do_main(self, _):
        """
        Prints the main menu
        """
        print(menu.main_menu())

    def do_double(self, _):
        name1, name2 = menu.two_player_menu()
        self.player1 = Player.Player(name1)
        self.player2 = Player.Player(name2)
        self.game = game.Game(self.player1, self.player2, None)

    def do_roll(self, _):
        self.game.roll()

    def do_hold(self, _):
        self.game.hold()
        self.game.game_menu()

    def do_single(self, _):
        name1, difficulty = menu.single_player_menu()
        player1 = Player.Player(name1)
        self.game = game.Game(player1, "Computer", difficulty)


    def do_exit(self, _):
        """
        Prints exit message and exits program
        """
        print("Thank you for playing")
        sys.exit()





if __name__ == "__main__":
    shell().cmdloop()
