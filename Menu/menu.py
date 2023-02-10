import cmd, sys

def main_menu() -> str:
    """prints main menu and returns choice"""
    print("1- Two players\n2- Single-Player"
          "\n3- Show highscore\n4- Exit")
    return input("choice: ")


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
    difficulty = str(input("Choice: "))

    difficulty = "easy" if difficulty == "1" \
        else "intermediate" if difficulty == "2" else "hard"
    return difficulty


def highscore_getname() -> str:
    """Allows user to enter name of a player to view highscore"""
    name_highscore = str(
        input("Enter the name of a player to view highscore: "))
    return name_highscore


def game_choice(player):
    """Allows user to choose either roll or hold in game"""
    print(f"{player}s turn")
    print("1- Roll\n2- Hold\n3- Exit game")
    choice_game = str(
        input('Enter R to roll, or H to hold: ')).lower()[0]
    return choice_game

