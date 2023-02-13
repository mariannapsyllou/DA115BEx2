import menu
import cmd
import game
import Intelligence


class MainShell(cmd.Cmd):
    menu.main_menu()
    prompt = ">>> "

    def __init__(self):
        super().__init__()
        self.player1 = None
        self.player2 = None
        self.difficulty = None
        self.highscore_name = None

    def do_main(self, args):
        menu.main_menu()

    def do_two(self, args):
        self.player1, self.player2 = menu.two_player_menu()
        # create players
        game.Game(self.player1, self.player2)

    def do_single(self, args):
        self.player1, self.difficulty = menu.single_player_menu()

        Intelligence.Intelligence(self.player1, self.difficulty)

    def do_highscore(self, args):
        self.highscore_name = menu.highscore_getname()

    def do_change(self, args):
        pass

    def do_exit(self, args):
        print("Thank you for playing")
        exit()


if __name__ == "__main__":
    MainShell().cmdloop()

