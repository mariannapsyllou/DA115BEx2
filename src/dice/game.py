import random
import time
import dice_visual
import Highscores
import Intelligence


class Game():
    """
    responsible for the main game functionality
    """

    def __init__(self, player1, player2):
        super().__init__()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.total_score = {player1: 0, player2: 0}
        self.current_score = 0
        self.game_menu()

    def roll(self):
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

    def hold(self):
        self.total_score[self.current_player] += self.current_score
        self.current_score = 0
        if self.current_player == self.player1:
            self.current_player = self.player2
        elif self.current_player == self.player2:
            self.current_player = self.player1
        else:
            self.game_menu()

    def do_hack(self):
        self.current_score += 5

    def game_menu(self):
        if self.total_score[self.current_player] < 100 and \
                (self.total_score[self.current_player])\
                + self.current_score < 100:
            print(f"{self.current_player}'s turn")
            print(f"{self.current_player}'s total score:", end=' ')
            print(f"{self.total_score[self.current_player]}")
            print(f"Current round score: {self.current_score}")
            # if self.current_player == self.player2:
            #     time.sleep(2.0)
            #     self.game_pc()
        else:
            print(f"{max(self.total_score, key=self.total_score.get)} wins!")
            high = Highscores.Highscores()
            high.update(self.current_player)

    # def game_pc(self):
    #     if difficulty == 1:
    #         computer_choice = self.intelligence.easy()
    #     elif difficulty == 2:
    #         computer_choice = self.intelligence.intermediate()
    #     else:
    #         computer_choice = self.intelligence.difficult()
    #     if self.current_player == self.player2:
    #         if computer_choice == "r":
    #             roll_pc = random.randint(1, 6)
    #             dice_visual(roll_pc)
    #             if roll_pc == 1:
    #                 self.current_score = 0
    #                 self.current_player = self.player1
    #             else:
    #                 self.current_score += roll_pc
    #         else:
    #             self.hold()
