import unittest
from unittest.mock import patch
from src.dice import menu


class TestMenus(unittest.TestCase):

    def test_main_menu(self) -> None:
        output = ""
        output += "Welcome! Enter help to see commands\n"
        output += "1- Two players\n2- Single-Player\n"
        output += "3- Show highscore\n4- Exit"
        self.assertEqual(menu.main_menu(), output)

    @patch('builtins.input', side_effect=['name1', 'name2'])
    def test_two_player_names(self, mock_input) -> None:
        player1, player2 = menu.two_player_menu()
        self.assertEqual(player1, 'name1')
        self.assertEqual(player2, 'name2')

    @patch('builtins.input', side_effect=['player1', '1'])
    @patch('src.dice.menu.set_difficulty', return_value='easy')
    def test_single_player_name_and_difficulty(self, mock_set_difficulty, mock_input) -> None:
        player1, difficulty = menu.single_player_menu()
        self.assertEqual(player1, 'player1')
        self.assertEqual(difficulty, 'easy')


if __name__ == "__main__":
    unittest.main()
