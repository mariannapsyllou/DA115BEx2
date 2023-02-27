import unittest
from unittest.mock import patch
from dice import Intelligence
from dice import game
from dice import dice_visual

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = "Alice"
        self.player2 = "Bob"
        self.difficulty = "hard"
        self.game = game.Game(self.player1, self.player2, self.difficulty)




    def test_roll(self):
        with patch('random.randint', return_value=4):
            with patch('dice.dice_visual.dice4'):
                self.game.roll()
                self.assertEqual(self.game.current_score, 4)
                self.assertEqual(self.game.current_player, self.player1)

        with patch('random.randint', return_value=1):
            with patch('dice.dice_visual.dice1'):
                self.game.roll()
                self.assertEqual(self.game.current_score, 0)
                self.assertEqual(self.game.current_player, self.player2)


    def test_init(self):
        self.assertEqual(self.game.player1, self.player1)
        self.assertEqual(self.game.player2, self.player2)
        self.assertEqual(self.game.difficulty, self.difficulty)
        self.assertEqual(self.game.current_player, self.player1)
        self.assertEqual(self.game.total_score[self.player1], 0)
        self.assertEqual(self.game.total_score[self.player2], 0)
        self.assertEqual(self.game.current_score, 0)
       

    def test_hold(self):
        self.game.current_player = self.game.player1
        self.game.total_score[self.game.current_player] = 10
        self.game.current_score = 10
        self.game.hold()
        self.assertEqual(self.game.total_score[self.game.player1], 20)
        self.assertEqual(self.game.current_score, 0)
        self.assertEqual(self.game.current_player, self.game.player2)

    def test_hold2(self):
        self.game.current_player = self.game.player2
        self.game.total_score[self.game.current_player] = 40
        self.game.current_score = 20
        self.game.hold()
        self.assertEqual(self.game.total_score[self.game.player2], 60)
        self.assertEqual(self.game.current_score, 0)
        self.assertEqual(self.game.current_player, self.game.player1)



if __name__ == "__main__":
    unittest.main()
