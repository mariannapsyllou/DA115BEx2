"""Class Game."""
import random
import time
from dice import intelligence
from dice import highscores
from dice import dice_visual


class Game:
    """Class is responsible for the main game functionality."""

    def __init__(self, player1, player2, difficulty):
        """Will initialize game-object."""
        super().__init__()
        self.player1 = player1
        self.player2 = player2
        self.difficulty = difficulty
        self.current_player = player1
        self.total_score = {player1: 0, player2: 0}
        self.current_score = 0
        self.intelligence = intelligence.Intelligence()

    def roll(self) -> None:
        """
        Will handle the rolling of the dice.

        Also calls dice_visual functions
        """
        roll = random.randint(1, 6)
        dice = dice_visual.DiceVisual()
        if roll == 1:
            dice.dice1()
            self.current_score = 0
            if self.current_player == self.player1:
                self.current_player = self.player2
            else:
                self.current_player = self.player1
        elif roll == 2:
            dice.dice2()
            self.current_score += 2
        elif roll == 3:
            dice.dice3()
            self.current_score += 3
        elif roll == 4:
            dice.dice4()
            self.current_score += 4
        elif roll == 5:
            dice.dice5()
            self.current_score += 5
        else:
            dice.dice6()
            self.current_score += 6
        self.game_menu()

    def hold(self) -> None:
        """Will allow user to hold, and changes whose turn it is."""
        self.total_score[self.current_player] += self.current_score
        self.current_score = 0
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
            self.game_menu()

    def hack(self) -> None:
        """Will increase the current player total score by 50 points."""
        self.total_score[self.current_player] += 50

    def game_menu(self) -> None:
        """
        Will print the in-game menu.

        if total score > 100 will print the winner and call update highscore
        """
        if (
            self.total_score[self.current_player] < 100
            and (self.total_score[self.current_player]) +
                self.current_score < 100):
            print(f"{self.current_player}'s turn")
            print(f"{self.current_player}'s total score:", end=" ")
            print(f"{self.total_score[self.current_player]}")
            print(f"Current round score: {self.current_score}")
            if self.current_player == "Computer":
                time.sleep(2.0)
                self.intelligence.score = self.current_score
                self.intelligence.max_score = self.total_score
                self.game_pc()
        else:
            print(f"{max(self.total_score, key=self.total_score.get)} wins!")
            high = highscores.Highscores()
            high.update(self.current_player)

    def game_pc(self) -> None:
        """
        The method handles the game when the second player is
        the Computer. Checks the difficulty level and act
        appropriate according to that.
        """
        if self.difficulty == "easy":
            choice = self.intelligence.easy()
        elif self.difficulty == "intermediate":
            choice = self.intelligence.intermediate()
        else:
            choice = self.intelligence.difficult()

        if choice == "r":
            self.roll()
        else:
            self.hold()
