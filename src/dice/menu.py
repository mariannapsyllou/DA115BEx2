"""
This modules holds the main menus
"""


def main_menu() -> None:
    """prints main menu and returns choice"""
    print("Welcome! Enter help to see commands")
    print("1- Two players\n2- Single-Player"
          "\n3- Show highscore\n4- Exit")


def two_player_menu() -> tuple:
    """Prompts user to enter name of two players,
            returns names in a tuple"""
    player1 = str(input("Name of player1: "))
    player2 = str(input("Name of player2: "))
    return player1, player2


def single_player_menu() -> tuple:
    """Prompts user to enter name when in single-player,
            returns name, and calls lvl2_2_1"""
    player1 = str(input("Enter player-name: "))
    difficulty = set_difficulty()
    return player1, difficulty


def set_difficulty() -> str:
    """Allows user to pick a difficulty"""
    print("Pick a difficulty")
    print("1- Easy\n2- Intermediate\n3- Hard")
    print("(1, 2 or 3)")
    difficulty = int(input("Choice: "))

    while difficulty > 3:
        print("Pick a number between 1-3")
        difficulty = int(input("Choice: "))
    difficulty = "easy" if difficulty == 1 \
        else "intermediate" if difficulty == 2 else "hard"
    return difficulty

