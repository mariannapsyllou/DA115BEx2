import random


class Game:
    dice = [1, 2, 3, 4, 5, 6]

    def roll_dice(self, round_score):
        throw = random.choice(self.dice)
        if throw == 1:
            round_score = 0
        else:
            round_score += throw
        return round_score

    def hold(self, round_score, score):
        score += round_score
        return score
