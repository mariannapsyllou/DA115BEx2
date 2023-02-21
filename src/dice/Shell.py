import cmd
import sys
import Intelligence
import game
import menu
import Player
import Highscores


class shell(cmd.Cmd):
    """
    Handles all the cmd/shell commands of the game
    """

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
        """
        Outputs the menu for 2 player game
        and creates Players with their names
        """
        name1, name2 = menu.two_player_menu()
        self.player1 = Player.Player(name1)
        self.player2 = Player.Player(name2)
        self.game = game.Game(self.player1, self.player2, None)

    def do_roll(self, _):
        """
        Handles the rolling of the dice
        by calling the function roll from
        game class
        """
        self.game.roll()

    def do_hold(self, _):
        """
        Handles the holding of the game when
        player decides to save his score. It
        does that by calling the hold function from
        game class
        """
        self.game.hold()
        self.game.game_menu()

    def do_single(self, _):
        """
        Outputs the menu when player is playing against
        the  computer and create a Player with his name
         """
        name1, difficulty = menu.single_player_menu()
        player1 = Player.Player(name1)
        self.game = game.Game(player1, "Computer", difficulty)

    def do_view(self, _):
        """
        Prints the instructions for the program
        """
        high = Highscores.Highscores()
        high.view_instructions()

    def do_exit(self, _):
        """
        Prints exit message and exits program
        """
        print("Thank you for playing")
        sys.exit()

    def do_hack(self, _):
        """
        Allows current player to hack the game by
        adding 50 points to his total score.
        """
        self.game.hack()

    def do_new(self, _):
        """
        Sets the total and current scores to zero
        So the game restarts.
        """
        print("Your game is now restarted! Roll or hold!!")
        self.game.total_score = {self.game.player1: 0, self.game.player2: 0}
        self.game.current_score = 0

    def do_highscore(self, _):
        """
        The function asks from the user to input a name and returns
        how many times the have won the game!
        """
        name = menu.highscore()
        self.highscore.scores(name)


if __name__ == "__main__":
    shell().cmdloop()
