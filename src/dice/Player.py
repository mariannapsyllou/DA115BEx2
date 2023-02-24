"""
Handles the methods of the Highscore class
"""


class Player:
    """Class Player is responsible for creating Player objects."""

    def __init__(self, name):
        """Will set the name of the player on instantiation."""
        self.name = name

    def __str__(self) -> str:
        """To string method for printing the Player objects."""
        return f"{self.name}"
