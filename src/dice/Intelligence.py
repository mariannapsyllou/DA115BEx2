import game


class Intelligence():

    def __init__(self) -> None:
        self.player1 = None
        self.player2 = "Computer"
        self.score = 0

    def easy(self) -> str:
        """
        Computer rolls till 20 points and then holds
        """
        if self.score <= 10:
            return "r"
        return "h"


    def intermediate(self) -> str:
        """
        Computer rolls till 25 points and then holds
        """
        if self.score <= 25:
            return "r"
        return "h"


    # def difficult(self):
    #     """
    #     Computer will roll if either player has score of 71
    #     Otherwise hold on 21 plus the difference between scores
    #     divided by 8
    #     """
    #     difference = max(self.game.total_score.values())\
    #         - min(self.game.total_score.values())
    #     if max(self.game.total_score.values()) >= 71 or \
    #             self.game.current_score == 0:
    #         self.game.roll()

    #     if self.game.current_score >= \
    #             21 + (difference//8):
    #         self.game.hold()
    #     self.game.roll()
