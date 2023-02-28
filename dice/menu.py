"""Menu."""
import re


def main_menu() -> str:
    """Will print main menu and returns choice."""
    output = ""
    output += "Welcome! Enter help to see commands\n"
    output += "1- Two players\n2- Single-Player\n"
    output += "3- Show highscore\n4- Exit"
    return output


def two_player_menu() -> tuple:
    """
    Prompts user to enter name of two players.

    Returns names in a tuple
    """
    player1 = str(input("Name of player1: "))
    player2 = str(input("Name of player2: "))
    while True:
        if not re.match("[a-zA-Z]", (player1 and player2)):
            print("Enter valid names!")
            player1 = str(input("Name of player1: "))
            player2 = str(input("Name of player2: "))
        else:
            break
    return player1, player2


def single_player_menu() -> tuple:
    """
    Prompts user to enter name when in single-player.

    Returns name, and calls set_difficulty
    """
    player1 = str(input("Enter player-name: "))
    difficulty = set_difficulty()
    return player1, difficulty


def set_difficulty() -> str:
    """Will allow user to pick a difficulty."""
    print("Pick a difficulty")
    print("1- Easy\n2- Intermediate\n3- Hard")
    print("(1, 2 or 3)")
    difficulty = int(input("Choice: "))

    while difficulty > 3:
        print("Pick a number between 1-3")
        difficulty = int(input("Choice: "))
    difficulty = (
        "easy" if difficulty == 1 else "intermediate" if difficulty == 2
        else "hard")
    return difficulty


def highscore() -> str:
    """
    Prompts the user to input a name.

    Returns the highscore of the player with name
    """
    return str(input("Enter a name to view highscore: "))
