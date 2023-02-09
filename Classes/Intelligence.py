import random


class Intelligence:
    def __init__(self, difficulty):
        self._difficulty = difficulty

    def easy(self) -> str:
        """Picks 50/50 between hold and roll and returns
        result"""
        computer_choices = ["h", "r"]
        choice = computer_choices[random.randrange(0, 2)]
        return choice

    def intermediate(self) -> str:
        """ca 66% chance that roll is returned"""
        computer_choices = ["h", "r", "r"]
        choice = computer_choices[random.randrange(0, 3)]

        return choice

    def difficult(self, current_score: int):
        """80% that computer picks roll, unless current score
        random number between 10, 50"""
        computer_choices = computer_choices = ["h", "r", "r", "r", "r"]
        choice = computer_choices[random.randrange(0, 5)]

        if current_score == random.randrange(10, 50):
            return "h"

        return choice
