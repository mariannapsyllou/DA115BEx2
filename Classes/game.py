import cmd
import random


class Game():

    def __init__(self):
        self.dice = [1, 2, 3, 4, 5, 6]
        self.round_score = 0
        self.score = 0

    def roll_dice(self, player):
        throw = random.choice(self.dice)
        if throw == 1:
            self.round_score = 0
            print(f"Oh no!, {player} You are losing your round points")
        else:
            print(f"{player},You rolled {throw}")
            self.round_score += throw
            print(f"{player} Your round score is : {self.round_score}")
        return self.round_score

    def hold(self, player):
        self.score += self.round_score
        print(f"Your round score {player} is : {self.round_score} and your total score is : {self.score}")
        return self.score

    def find_winner(self, player):
        if self.score >= 100:
            return f"{player} YOU WONN"

    def get_round_score(self):
        return self.round_score

    def reset_scores(self):
        """Setting the scores back to 0 in case he quits the game"""
        self.round_score = 0
        self.score = 0

