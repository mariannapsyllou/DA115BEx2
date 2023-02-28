"""Shell."""
import cmd
import sys
import intelligence
import highscores
import player
import game
import menu


class Shell(cmd.Cmd):
    """Handles all the cmd/shell commands of the game."""

    prompt = ">>>"

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.highscore = highscores.Highscores()
        self.game = game.Game(None, None, None)
        self.player1 = None
        self.player2 = None
        self.intelligence = intelligence.Intelligence()
        self.game_started = False
        print(menu.main_menu())

    def do_main(self, _) -> None:
        """Will print the main menu."""
        print(menu.main_menu())

    def do_double(self, _) -> None:
        """Will start two_player mode with given player-names."""
        name1, name2 = menu.two_player_menu()
        self.player1 = player.Player(name1)
        self.player2 = player.Player(name2)
        self.game_started = True
        self.game = game.Game(self.player1, self.player2, None)
        self.game.game_menu()

    def do_roll(self, _) -> None:
        """
        Will allor user to roll the dice.

        Calls the roll function of the game-class
        """
        if not self.game_started:
            print("Please start a game first (type 'double' or 'single')")
            return
        self.game.roll()

    def do_hold(self, _) -> None:
        """
        Will allow the user to hold during the game.

        Calls the hold function of the game-class
        """
        if not self.game_started:
            print("Please start a game first (type 'double' or 'single')")
            return
        self.game.hold()
        self.game.game_menu()

    def do_single(self, _) -> None:
        """Will start single-player mode with given name."""
        name1, difficulty = menu.single_player_menu()
        self.game_started = True
        player1 = player.Player(name1)
        self.game = game.Game(player1, "Computer", difficulty)
        self.game.game_menu()

    def do_view(self, _) -> None:
        """Will print the instructions for the program."""
        high = highscores.Highscores()
        high.view_instructions()

    def do_exit(self, _) -> None:
        """Will print the exit message and exits program."""
        print("Thank you for playing")
        sys.exit()

    def do_hack(self, _) -> None:
        """
        Will allow current player to hack the game.

        Calls the hack function of the game-class
        """
        if not self.game_started:
            print("Please start a game first (type 'double' or 'single')")
            return
        self.game.hack()

    def do_new(self, _) -> None:
        """
        Will allow user to restart the game.

        Sets all the scores to 0
        """
        if not self.game_started:
            print("Please start a game first (type 'double' or 'single')")
            return
        print("Your game is now restarted! Roll or hold!!")
        self.game.total_score = {self.game.player1: 0, self.game.player2: 0}
        self.game.current_score = 0

    def do_highscore(self, _) -> None:
        """
        Will prompt user for a player-name.

        Returns how many times given player has won
        or if name is not found prints error-message
        """
        name = menu.highscore()
        self.highscore.scores(name)


if __name__ == "__main__":
    Shell().cmdloop()
