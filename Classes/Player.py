from Highscores import Highscores


class Player:

    def __init__(self, name):
        self.name = name
        self.cls = Highscores()

    def retrieve_player(self, name):
        list = self.cls.list_results()
        for item in list:
            name, *rest = item.split(',')
            if name == self.name:
                highscore, times_played = [int(num) for num in rest]
                return self.name, highscore, times_played
            else:
                return self.name, 0, 0
