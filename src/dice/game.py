import random
import time
import dice_visual
import Highscores
import Intelligence


class Game():
    """
    responsible for the main game functionality
    """

    def __init__(self, player1, player2, difficulty):
        super().__init__()
        self.player1 = player1
        self.player2 = player2
        self.difficulty = difficulty
        self.current_player = player1
        self.total_score = {player1: 0, player2: 0}
        self.current_score = 0
        self.intelligence = Intelligence.Intelligence()

    def roll(self) -> None:
        """
        Method that handles the rolling of the dice!
        and switch players when roll is equal to 1
        """
        roll = random.randint(1, 6)
        if roll == 1:
            dice_visual.dice1()
            self.current_score = 0
            if self.current_player == self.player1:
                self.current_player = self.player2
            else:
                self.current_player = self.player1
        elif roll == 2:
            dice_visual.dice2()
            self.current_score += 2
        elif roll == 3:
            dice_visual.dice3()
            self.current_score += 3
        elif roll == 4:
            dice_visual.dice4()
            self.current_score += 4
        elif roll == 5:
            dice_visual.dice5()
            self.current_score += 5
        else:
            dice_visual.dice6()
            self.current_score += 6
        self.game_menu()

    def hold(self) -> None:
        """
        Method that handles the holding, in case the player wants
        to stop rolling and save his current score to his total
        score. After holding is pressed the method switch players.
        """
        self.total_score[self.current_player] += self.current_score
        self.current_score = 0
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
            self.game_menu()

    def hack(self) -> None:
        """
        Increase the current player total score by 50 points
        so he can win faster.
        """
        self.total_score[self.current_player] += 50

    def game_menu(self) -> None:
        """
        he method finds and prints the winner.
        If winner was not found prints the menu of whose player
        turn is.
        """
        if self.total_score[self.current_player] < 100 and \
                (self.total_score[self.current_player])\
                + self.current_score < 100:
            print(f"{self.current_player}'s turn")
            print(f"{self.current_player}'s total score:", end=' ')
            print(f"{self.total_score[self.current_player]}")
            print(f"Current round score: {self.current_score}")
            if self.current_player == "Computer":
                time.sleep(2.0)
                self.intelligence.score = self.current_score
                self.intelligence.max_score = self.total_score
                self.game_pc()
        else:
            print(f"{max(self.total_score, key=self.total_score.get)} wins!")
            high = Highscores.Highscores()
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
