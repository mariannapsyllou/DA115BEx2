import unittest
import random
from Classes import single_player


class Test_single_player(unittest.TestCase):
    def setUp(self):
        self.single_player = single_player
        self.single_player.player1 = "player 1"
        self.single_player.player2 = "Computer"
        self.single_player.current_player = self.single_player.player1
        self.single_player.current_score = 0

    def test_do_roll_one(self):
        random.seed(1)
        self.single_player.do_roll("")
        self.assertEqual(self.single_player.current_score, 0)
        self.assertEqual(
            self.single_player.current_player,
            self.single_player.player2)
