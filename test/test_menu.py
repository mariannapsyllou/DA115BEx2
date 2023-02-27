import unittest
from unittest.mock import patch
from dice import menu


class TestMenus(unittest.TestCase):
    """This class handles tests for menu functions."""

    def test_main_menu(self) -> None:
        """Will test the output of the main menu."""
        output = ""
        output += "Welcome! Enter help to see commands\n"
        output += "1- Two players\n2- Single-Player\n"
        output += "3- Show highscore\n4- Exit"
        self.assertEqual(menu.main_menu(), output)

    @patch("builtins.input", side_effect=["name1", "name2"])
    def test_two_player_names(self, mock_input) -> None:
        """Will test the two-player menu with good input."""
        player1, player2 = menu.two_player_menu()
        self.assertEqual(player1, "name1")
        self.assertEqual(player2, "name2")

    @patch("builtins.input", side_effect=["player1", "1"])
    @patch("dice.menu.set_difficulty", return_value="easy")
    def test_single_player_name_and_difficulty(
        self, mock_set_difficulty, mock_input
    ) -> None:
        """Tests singelplayer and difficulty with good inpout."""
        player1, difficulty = menu.single_player_menu()
        self.assertEqual(player1, "player1")
        self.assertEqual(difficulty, "easy")

    @patch("builtins.input", side_effect=["name1"])
    def test_highscore_menu(self, mock_input):
        """Tests highscore menu with good input."""
        name1 = menu.highscore()
        self.assertEqual(name1, "name1")


if __name__ == "__main__":
    unittest.main()
