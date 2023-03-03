"""Test game."""
import unittest
from unittest.mock import patch, MagicMock
from dice import game


class TestGame(unittest.TestCase):
    """Class testgame."""

    def setUp(self):
        """Will set up method."""
        self.player1 = "Alice"
        self.player2 = "Bob"
        self.difficulty = "hard"
        self.game = game.Game(self.player1, self.player2, self.difficulty)

    def test_roll(self):
        """Will test roll."""
        with patch('random.randint', return_value=4):
            with patch('dice.dice_visual.DiceVisual.dice4'):
                with patch('dice.game.Game.game_menu'):
                    self.game.roll()
                    self.assertEqual(self.game.current_score, 4)
                    self.assertEqual(self.game.current_player, self.player1)

        with patch('random.randint', return_value=5):
            with patch('dice.dice_visual.DiceVisual.dice5'):
                with patch('dice.game.Game.game_menu'):
                    self.game.roll()
                    self.assertEqual(self.game.current_score, 9)
                    self.assertEqual(self.game.current_player, self.player1)

        with patch('random.randint', return_value=6):
            with patch('dice.dice_visual.DiceVisual.dice6'):
                with patch('dice.game.Game.game_menu'):
                    self.game.roll()
                    self.assertEqual(self.game.current_score, 15)
                    self.assertEqual(self.game.current_player, self.player1)

        with patch('random.randint', return_value=2):
            with patch('dice.dice_visual.DiceVisual.dice2'):
                with patch('dice.game.Game.game_menu'):
                    self.game.roll()
                    self.assertEqual(self.game.current_score, 17)
                    self.assertEqual(self.game.current_player, self.player1)

        with patch('random.randint', return_value=3):
            with patch('dice.dice_visual.DiceVisual.dice3'):
                with patch('dice.game.Game.game_menu'):
                    self.game.roll()
                    self.assertEqual(self.game.current_score, 20)
                    self.assertEqual(self.game.current_player, self.player1)

        with patch('random.randint', return_value=1):
            with patch('dice.dice_visual.DiceVisual.dice1'):
                with patch('dice.game.Game.game_menu'):
                    self.game.roll()
                    self.assertEqual(self.game.current_score, 0)
                    self.assertEqual(self.game.current_player, self.player2)

    def test_init(self):
        """Will check the init."""
        self.assertEqual(self.game.player1, self.player1)
        self.assertEqual(self.game.player2, self.player2)
        self.assertEqual(self.game.difficulty, self.difficulty)
        self.assertEqual(self.game.current_player, self.player1)
        self.assertEqual(self.game.total_score[self.player1], 0)
        self.assertEqual(self.game.total_score[self.player2], 0)
        self.assertEqual(self.game.current_score, 0)

    def test_hold(self):
        """Will test the hold."""
        self.game.current_player = self.game.player1
        self.game.total_score[self.game.current_player] = 10
        self.game.current_score = 10
        with patch('dice.game.Game.game_menu'):
            self.game.hold()
            self.assertEqual(self.game.total_score[self.game.player1], 20)
            self.assertEqual(self.game.current_score, 0)
            self.assertEqual(self.game.current_player, self.game.player2)

    def test_hold2(self):
        """Will test the hold."""
        self.game.current_player = self.game.player2
        self.game.total_score[self.game.current_player] = 40
        self.game.current_score = 20
        with patch('dice.game.Game.game_menu'):
            self.game.hold()
            self.assertEqual(self.game.total_score[self.game.player2], 60)
            self.assertEqual(self.game.current_score, 0)
            self.assertEqual(self.game.current_player, self.game.player1)

    def test_game_pc_easy(self):
        """Will test the game_pc method with level easy."""
        self.game.difficulty = "easy"
        self.game.intelligence.easy = MagicMock(return_value="r")
        self.game.roll = MagicMock()
        self.game.hold = MagicMock()
        self.game.game_pc()
        self.game.intelligence.easy.assert_called_once()
        self.game.roll.assert_called_once()
        self.game.hold.assert_not_called()

    def test_game_pc_intermediate(self):
        """Will test the game_pc with level intermediate."""
        self.game.difficulty = "intermediate"
        self.game.intelligence.intermediate = MagicMock(return_value="h")
        self.game.roll = MagicMock()
        self.game.hold = MagicMock()
        self.game.game_pc()
        self.game.intelligence.intermediate.assert_called_once()
        self.game.roll.assert_not_called()
        self.game.hold.assert_called_once()

    def test_game_pc_difficult(self):
        """Will test the game_pc with level difficult."""
        self.game.difficulty = "difficult"
        self.game.intelligence.difficult = MagicMock(return_value="h")
        self.game.roll = MagicMock()
        self.game.hold = MagicMock()
        self.game.game_pc()
        self.game.intelligence.difficult.assert_called_once()
        self.game.roll.assert_not_called()
        self.game.hold.assert_called_once()

    def test_hack(self):
        """Will test the hack method."""
        expected_score = self.game.total_score[self.game.current_player] + 50
        self.game.hack()
        self.assertEqual(self.game.total_score[self.game.current_player],
                         expected_score)


if __name__ == "__main__":
    unittest.main()
