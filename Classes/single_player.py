import random
import cmd
import dice_visual
import time
import Highscores
import main


class SinglePlayer(cmd.Cmd):
    prompt = ">>>"

    def __init__(self, player1, difficulty):
        super().__init__()
        self.player1 = player1
        self.player2 = "Computer"
        self.current_player = player1
        self.total_score = {player1: 0, self.player2: 0}
        self._difficulty = difficulty
        self.current_score = 0
        self.game_menu()

    def easy(self) -> str:
        """
        Computer rolls till 20 points and then holds
        """
        if self.current_score <= 20:
            choice = "r"
        else:
            choice = "h"
        return choice

    def intermediate(self) -> str:
        """
        Computer rolls till 25 points and then holds
        """
        if self.current_score <= 25:
            choice = "r"
        else:
            choice = "h"
        return choice

    def difficult(self):
        """
        Computer will roll if either player has score of 71
        Otherwise hold on 21 plus the difference between scores
        divided by 8
        """
        difference = max(self.total_score.values())\
            - min(self.total_score.values())
        if max(self.total_score.values()) >= 71 or self.current_score == 0:
            return "r"
        if self.current_score >= \
                21 + (difference//8):
            return "h"
        return "r"

    def display_dice_visual(self, roll):
        """
        Prints out the visualisation of dices
        """
        if roll == 1:
            dice_visual.dice1()
        elif roll == 2:
            dice_visual.dice2()
        elif roll == 3:
            dice_visual.dice3()
        elif roll == 4:
            dice_visual.dice4()
        elif roll == 5:
            dice_visual.dice5()
        else:
            dice_visual.dice6()

    def do_roll(self, args):
        """
        Method that handles the game rolling when
        a user is playing against the Computer
        """
        roll = random.randint(1, 6)
        self.display_dice_visual(roll)
        if roll == 1:
            self.current_score = 0
            if self.current_player == self.player1:
                self.current_player = self.player2
                if self.current_player == self.player2:
                    self.game_menu()
            else:
                self.current_player = self.player1
        else:
            self.current_score += roll
            self.game_menu()

    def do_hold(self, _):
        """
        Adds the current score the players total score
        and switches the players.

        """
        self.total_score[self.current_player] += self.current_score
        self.current_score = 0
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
        self.game_menu()

    def game_menu(self):
        while self.total_score[self.current_player] < 100 and \
                (self.total_score[self.current_player])\
                + self.current_score < 100:

            print(f"{self.current_player}'s turn")
            print(f"{self.current_player}'s total score:", end=' ')
            print(f"{self.total_score[self.current_player]}")
            print(f"Current round score: {self.current_score}")
            if self.current_player == self.player2:
                time.sleep(2.0)
                self.game_pc()
            else:
                self.cmdloop()
        print(f"{max(self.total_score, key=self.total_score.get)} wins!")
        high = Highscores.Highscores()
        high.update(self.current_player)
        self.do_quit("")

    def game_pc(self):
        if self._difficulty == 1:
            computer_choice = self.easy()
        elif self._difficulty == 2:
            computer_choice = self.intermediate()
        else:
            computer_choice = self.difficult()
        if self.current_player == self.player2:
            if computer_choice == "r":
                roll_pc = random.randint(1, 6)
                self.display_dice_visual(roll_pc)
                if roll_pc == 1:
                    self.current_score = 0
                    self.current_player = self.player1
                else:
                    self.current_score += roll_pc
            else:
                self.do_hold("")

    def do_hack(self, _):
        """
        If the users uses the command hack
        60 points are gonna be added to his
        total score
        """
        self.total_score[self.current_player] += 90

    def do_new(self, _):
        """
        Sets the total and current scores to zero
        So the game restarts.
        """
        self.total_score = {self.player1: 0, self.player2: 0}
        self.current_score = 0
        self.cmdloop()

    def do_quit(self, _):
        """
        Quits the current game and go back to main menu
        """
        shell = main.MainShell()
        shell.cmdloop()
