"""Handles the methods of the Intelligence class."""


class Intelligence():
    """
    Class that handles the different levels.

    Thenprompts the Computer to
    act according to the modules.
    """

    def __init__(self) -> None:
        """Iniatialise."""
        self.player1 = None
        self.player2 = "Computer"
        self.score = 0
        self.max_score: dict = {}

    def easy(self) -> str:
        """Will roll till 20 points and then holds."""
        if self.score <= 20:
            return "r"
        return "h"

    def intermediate(self) -> str:
        """Will roll till 25 points and then holds."""
        if self.score <= 25:
            return "r"
        return "h"

    def difficult(self) -> str:
        """
        Difficult level.

        Will roll if either player has score of 71
        Otherwise hold on 21 plus the difference between scores
        divided by 8.
        """
        difference = max(
            self.max_score.values()) - min(self.max_score.values())
        if max(self.max_score.values()) >= 71:
            return "r"
        if self.score >= 21 + (difference / 8):
            return "h"
        return "r"
