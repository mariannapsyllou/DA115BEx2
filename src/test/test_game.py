import unittest
from unittest.mock import patch, MagicMock
from src.dice.Intelligence import Intelligence
from src.dice.game import Game
from src.dice.dice_visual import dice1, dice4


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = "Anna"
        self.player2 = "Kalle"
        self.difficulty = "easy"
        self.current_score = 5
        self.game = Game(self.player1, self.player2, self.difficulty)

    def test_roll(self):
        with patch("builtins.print"), patch("random.randint", return_value=4), patch(
            "src.dice.dice_visual.dice4"
        ):
            self.game.roll()
            self.assertEqual(self.game.current_score, 4)
            self.assertEqual(self.game.current_player, self.player1)

        with patch("builtins.print"), patch("random.randint", return_value=1), patch(
            "src.dice.dice_visual.dice1"
        ):
            self.game.roll()
            self.assertEqual(self.game.current_score, 0)
            self.assertEqual(self.game.current_player, self.player2)

    def test_hold(self):
        self.game.total_score[self.game.player1] = 10
        self.game.current_score = 5
        self.game.current_player = self.player1

        self.game.hold()

        self.assertEqual(self.game.total_score[self.game.player1], 15)

        self.assertEqual(self.game.current_score, 0)
        self.assertEqual(self.game.current_player, self.game.player2)

    def test_init(self):
        self.assertEqual(self.game.player1, self.player1)
        self.assertEqual(self.game.player2, self.player2)
        self.assertEqual(self.game.difficulty, self.difficulty)
        self.assertEqual(self.game.current_player, self.player1)
        self.assertEqual(self.game.total_score[self.player1], 0)
        self.assertEqual(self.game.total_score[self.player2], 0)
        self.assertEqual(self.game.current_score, 0)
        self.assertIsInstance(self.game.intelligence, Intelligence)


if __name__ == "__main__":
    unittest.main()
