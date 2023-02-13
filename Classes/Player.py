from Highscores import Highscores


class Player:

    def __init__(self, name):
        self.name = name
        self.cls = Highscores()

    def name(self):
        return self.name

    def __str__(self):
        return f"{self.name}"
