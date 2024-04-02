"""
-------Pig Game instructions.------.

The game can be played with two player or with one against the computer.
The goal is to collect 100 points in order to winn!
You have 2 options to roll or hold
If you roll you collect points until you hold
When  you hold your current points are added to your total score
If you roll 1 you lose all your round points
The commands you can use are:
help: To see all comands available
single: Start a game with one player vs the computer
double : Start a game with two players
main : You go back to the main menu
view : You can see the instructions of the game at anytime
new : You restart your current game
highscore : You can see the highscores of a given player
exit : You exit the game
roll : You roll the dice
hold : You hold
hack : You are hacking the game
"""
#Hello from test-branch
import shell


def main():
    """Execute the main program."""
    print(__doc__)
    shell.Shell().cmdloop()


if __name__ == "__main__":
    main()
