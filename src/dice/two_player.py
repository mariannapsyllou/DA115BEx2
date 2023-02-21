import cmd
import random
import dice_visual
import main
import Highscores


class TwoPlayer(cmd.Cmd):
    """
    responsible for the main game functionality
    """
    prompt = ">>> "

    def __init__(self, player1, player2):
        super().__init__()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.total_score = {player1: 0, player2: 0}
        self.current_score = 0
        self.game_menu()

    def do_roll(self, _):
        roll = random.randint(1, 6)
        if roll == 1:
            dice_visual.dice1()
            self.current_score = 0
            if self.current_player == self.player1:
                self.current_player = self.player2
            else:
                self.current_player = self.player1
        elif roll == 2:
            dice_visual.dice2()
            self.current_score += 2
        elif roll == 3:
            dice_visual.dice3()
            self.current_score += 3
        elif roll == 4:
            dice_visual.dice4()
            self.current_score += 4
        elif roll == 5:
            dice_visual.dice5()
            self.current_score += 5
        else:
            dice_visual.dice6()
            self.current_score += 6
        self.game_menu()

    def do_hold(self, _):
        self.total_score[self.current_player] += self.current_score
        self.current_score = 0
        if self.current_player == self.player1:
            self.current_player = self.player2
            self.current_player = self.player1
        else:
            self.game_menu()

    def do_hack(self, _):
        self.current_score += 5

    def game_menu(self):
        while self.total_score[self.current_player] < 100 and \
                (self.total_score[self.current_player])\
                + self.current_score < 100:
            print(f"{self.current_player}'s turn")
            print(f"{self.current_player}'s total score:", end=' ')
            print(f"{self.total_score[self.current_player]}")
            print(f"Current round score: {self.current_score}")
            self.cmdloop()
        print(f"{max(self.total_score, key=self.total_score.get)} wins!")
        high = Highscores.Highscores()
        high.update(self.current_player)
        self.do_quit("")

    def do_new(self, _):
        self.total_score = {self.player1: 0, self.player2: 0}
        self.current_score = 0
        self.cmdloop()

    def do_quit(self, _):
        shell = main.MainShell()
        shell.cmdloop()