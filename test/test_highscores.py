"""Test high_scores."""
import unittest
from unittest.mock import mock_open, patch
from io import StringIO
from dice import highscores
from dice import player


class TestHighscores(unittest.TestCase):
    """
    Test Highscores class is
    responsible for testing Highscore class
    """

    def setUp(self) -> None:
        """
        Setting up the class
        """
        self.highscores = highscores.Highscores()

    def test_dict_results(self):
        """
        The test checks the dict_results function
        Reads a file and checks that the expected
        output is a dictionary with names and scores
        """
        mock_file_data = "Anna,10\nKalle,20\nAlex,30\n"
        with patch("builtins.open", mock_open(read_data=mock_file_data)) \
                as mock_file:
            result_dict = self.highscores.dict_results()
            expected_output = {"Anna": 10, "Kalle": 20, "Alex": 30}
        self.assertEqual(result_dict, expected_output)

    def test_scores(self):
        """
        Thes test checks inside the dictionary if the user played the game
        and prints the expected outputs
        """
        with patch.object(
            self.highscores, "dict_results",
             return_value={"Anna": 10, "Kalle": 20}):
            expected_output = "Anna you have won the game 10 times!!\n"
            with patch("sys.stdout", new=StringIO()) as fake_output:
                self.highscores.scores("Anna")
                self.assertEqual(fake_output.getvalue(), expected_output)

            expected_output = "This user has not been registered\n"
            with patch("sys.stdout", new=StringIO()) as fake_output:
                self.highscores.scores("Alex")
                self.assertEqual(fake_output.getvalue(), expected_output)

    def test_view(self):
        """
        Checks if the game instructions are printed correct
        """
        expected_output = "This is a test file"
        with patch("builtins.open", return_value=StringIO(expected_output)):
            with patch("sys.stdout", new=StringIO()) as fake_output:
                self.highscores.view_instructions()
                self.assertEqual(fake_output.getvalue().strip(),
                                 expected_output)

    def test_update(self):
        """
        Checks if the results when the player has won a game
        are updated correctly
        """
        mock_file_data = "Anna,10\nKalle,20\nAlex,30\n"
        with patch("builtins.open", mock_open(read_data=mock_file_data)) \
             as mock_file:
            player1 = player.Player("Anna")
            self.highscores.update(player1)

        expected_output = "Anna,11\nKalle,20\nAlex,30\n"
        handle = mock_file
        # handle.write.assert_called_once_with(expected_output)

        with patch("builtins.open", mock_open(read_data=mock_file_data)) \
             as mock_file:
            player2 = player.Player("Samy")
            self.highscores.update(player2)
        expected_output = "Anna,10\nKalle,20\nAlex,30\nSamy,1\n"
        handle = mock_file()
        handle.write.assert_called_once_with(expected_output)


if __name__ == "__main__":
    unittest.main()
