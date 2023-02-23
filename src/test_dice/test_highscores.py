import unittest
from unittest.mock import mock_open, patch
from src.dice.Highscores import Highscores


class TestHighscores(unittest.TestCase):
    def setUp(self) -> None:
        self.highscores = Highscores()

    def test_dict_results(self):
        mock_file = "Alex,10\nKalle,2\n"
        with patch("builtins.open", mock_open(read_data=mock_file)) \
                as mock_file:
            result_dict = self.highscores.dict_results()
        expected_out = {"Alex": 10, "Kalle": 2}
        self.assertEqual(result_dict, expected_out)

    def test_dict_fileNotFound(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            result_dict = self.highscores.dict_results()
        expected_out = {}
        self.assertEqual(result_dict, expected_out)


if __name__ == "__main__":
    unittest.main()
