from Highscores import Highscores


class Player:

    def __init__(self, name, score, round_score):
        self.name = name
        self.score = 0
        self.round_score = 0
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
