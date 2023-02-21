import game


class Intelligence():

    def __init__(self, difficulty) -> None:
        self.player1 = None
        self.player2 = "Computer"
        self.game = game.Game(self.player1, self.player2)
        self.current_score = self.game.current_score
        self.difficulty = difficulty


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
