"""Test Player."""
import unittest
from dice import player


class TestPlayer(unittest.TestCase):
    """Testing the player class."""

    def test_player_name(self):
        """Testing the to sting method."""
        player1 = player.Player("Anna")
        self.assertEqual(str(player1), "Anna")


if __name__ == '__main__':
    unittest.main()
