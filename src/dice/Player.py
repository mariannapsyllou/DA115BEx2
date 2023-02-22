"""
Handles the methods of the Highscore class
"""


class Player:
    """
    Class Player is responsible for creating
    Player objects that holds the name of user.
    """

    def __init__(self, name):
        self.name = name

    def name(self):
        """
        Setter for the attribute name. In case
        the user wishes to change his name.
        """
        return self.name

    def __str__(self):
        """
        To string method for printing
        the Player objects.
        """
        return f"{self.name}"
