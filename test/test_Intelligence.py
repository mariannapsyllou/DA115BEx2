"""Test for Intelligence class."""
import unittest
from dice import Intelligence


class TestIntelligence(unittest.TestCase):
    """
    The TestIntelligence class handles the functions
    for checking the Intelligence
    """

    def setUp(self):
        """Setting up the class"""
        self.intelligence = Intelligence.Intelligence()

    def test_init(self):
        """Cheking the init"""
        self.assertIsNone(self.intelligence.player1)
        self.assertEqual(self.intelligence.player2, "Computer")
        self.assertEqual(self.intelligence.score, 0)
        self.assertEqual(self.intelligence.max_score, {})

    def test_easy(self):
        """"Checks for the easy function with return roll"""
        self.intelligence.score = 10
        self.assertEqual(self.intelligence.easy(), 'r')

    def test_easy2(self):
        """Checks for the easy function with return hold"""
        self.intelligence.score = 25
        self.assertEqual(self.intelligence.easy(), 'h')

    def test_intermediate(self):
        """"Checks for the intermediate function with return roll"""
        self.intelligence.score = 15
        self.assertEqual(self.intelligence.intermediate(), "r")

    def test_intemediate2(self):
        """"Checks for the intermediate function with return hold"""
        self.intelligence.score = 26
        self.assertEqual(self.intelligence.intermediate(), "h")

    def test_difficult(self):
        """"Checks for the difficult function with return roll"""
        self.intelligence.max_score = {"Player1": 60, "Computer": 60}
        self.intelligence.score = 10
        self.assertEqual(self.intelligence.difficult(), "r")

    def test_difficult2(self):
        """"Checks for the difficult function with return hold"""
        self.intelligence.max_score = {"Player1": 40, "Computer": 60}
        self.intelligence.score = 30
        self.assertEqual(self.intelligence.difficult(), "h")


if __name__ == '__main__':
    unittest.main()
