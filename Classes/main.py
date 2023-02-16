import menu
import cmd
import two_player
import single_player
import Highscores
import Player

class MainShell(cmd.Cmd):
    prompt = ">>> "

    def __init__(self):
        super().__init__()
        self.player1 = Player.Player(None)
        self.player2 = Player.Player(None)
        self.difficulty = None
        self.highscore_name = None
        menu.main_menu()

    def do_main(self, args):
        menu.main_menu()

    def do_two(self, args):
        self.player1, self.player2 = menu.two_player_menu()
        # create players
        two_player.TwoPlayer(self.player1, self.player2)

    def do_single(self, args):
        self.player1, self.difficulty = menu.single_player_menu()

        single_player.SinglePlayer(self.player1, self.difficulty)

    def do_highscore(self, args):
        self.highscore_name = menu.highscore_getname()
        high = Highscores.Highscores()
        high.scores(self.highscore_name)

    def do_change(self, args):
        pass
    
    def do_view(self, args):
        high = Highscores.Highscores()
        high.view_instructions()

    def do_exit(self, args):
        print("Thank you for playing")
        exit()


if __name__ == "__main__":
    MainShell().cmdloop()

