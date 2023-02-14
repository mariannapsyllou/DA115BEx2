import random
import cmd
import dice_visual
import two_player
import time

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
        """Picks 50/50 between hold and roll and returns
        result"""
        computer_choices = ["h", "r"]
        if self.current_score == 0:
            return "r"
        else:
            choice = computer_choices[random.randrange(0, 2)]
            return choice

    def intermediate(self) -> str:
        """ca 66% chance that roll is returned"""
        computer_choices = ["h", "r", "r"]
        if self.current_score == 0:
            return "r"
        else:
            choice = computer_choices[random.randrange(0, 3)]
            return choice

    def difficult(self, current_score: int):
        """80% that computer picks roll, unless current score
        random number between 10, 50"""
        difference = max(self.total_score.values()) - min(self.total_score.values())
        if max(self.total_score.values()) >= 71 or self.current_score == 0:
            return "r"
        else:
            if self.current_score >= \
                    21 + (difference//8):
                return "h"
            else:
                return "r"

    def display_dice_visual(self, roll):
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

    def do_hold(self, args):
        self.total_score[self.current_player] += self.current_score
        self.current_score = 0
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
        self.game_menu()

    def game_menu(self):
        while max(self.total_score.values()) < 100 and \
                max(self.total_score.values()) + self.current_score < 100:
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

    def game_pc(self):
        if self._difficulty == 1:
            computer_choice = self.easy()
        elif self._difficulty == 2:
            computer_choice = self.intermediate()
        else:
            computer_choice = self.difficult(self.current_score)
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
