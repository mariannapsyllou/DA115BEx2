import unittest
from unittest.mock import mock_open, patch
from io import StringIO
from src.dice.Highscores import Highscores
from src.dice.Player import Player


class TestHighscores(unittest.TestCase):

    def setUp(self) -> None:
        self.highscores = Highscores()

    def test_dict_results(self):
        mock_file_data = "Anna,10\nKalle,20\nAlex,30\n"
        with patch("builtins.open", mock_open(read_data=mock_file_data)) \
                as mock_file:
            result_dict = self.highscores.dict_results()
            expected_output = {"Anna": 10, "Kalle": 20, "Alex": 30}
        self.assertEqual(result_dict, expected_output)

    def test_scores(self):
        with patch.object(self.highscores, "dict_results", \
                          return_value={"Anna": 10, "Kalle": 20}):
            expected_output = "Anna you have won the game 10 times!!\n"
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.highscores.scores("Anna")
                self.assertEqual(fake_output.getvalue(), expected_output)

            expected_output = "This user has not been registered\n"
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.highscores.scores("Alex")
                self.assertEqual(fake_output.getvalue(), expected_output)

    def test_view(self):
        expected_output = "This is a test file"
        with patch("builtins.open", return_value=StringIO(expected_output)):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.highscores.view_instructions()
                self.assertEqual(fake_output.getvalue().strip(),
                                 expected_output)

    def test_update(self):
        mock_file_data = "Anna,10\nKalle,20\nAlex,30\n"
        with patch("builtins.open", mock_open(read_data=mock_file_data)) \
                as mock_file:
            player = Player("Anna")
            self.highscores.update(player)

        expected_output = "Anna,11\nKalle,20\nAlex,30\n"
        handle = mock_file
        handle.write.assert_called_once_with(expected_output)

        with patch("builtins.open", mock_open(read_data=mock_file_data)) \
                as mock_file:
            player = Player("Samy")
            self.highscores.update(player)
        expected_output = "Anna,10\nKalle,20\nAlex,30\nSamy,1\n"
        handle = mock_file()
        handle.write.assert_called_once_with(expected_output)


if __name__ == "__main__":
    unittest.main()
