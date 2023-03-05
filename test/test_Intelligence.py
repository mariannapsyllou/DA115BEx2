"""Test for Intelligence class."""
import unittest
from dice import intelligence


class TestIntelligence(unittest.TestCase):
    """
    TestIntelligence class will handle the functions.

    for checking the Intelligence.
    """

    def setUp(self):
        """Will set up the class."""
        self.intelligence = intelligence.Intelligence()

    def test_init(self):
        """Will check the init."""
        self.assertIsNone(self.intelligence.player1)
        self.assertEqual(self.intelligence.player2, "Computer")
        self.assertEqual(self.intelligence.score, 0)
        self.assertEqual(self.intelligence.max_score, {})

    def test_easy(self):
        """Will check for the easy function with return roll."""
        self.intelligence.score = 10
        self.assertEqual(self.intelligence.easy(), "r")

    def test_easy2(self):
        """Will check for the easy function with return hold."""
        self.intelligence.score = 25
        self.assertEqual(self.intelligence.easy(), "h")

    def test_intermediate(self):
        """Will check for the intermediate function with return roll."""
        self.intelligence.score = 15
        self.assertEqual(self.intelligence.intermediate(), "r")

    def test_intemediate2(self):
        """Will check for the intermediate function with return hold."""
        self.intelligence.score = 26
        self.assertEqual(self.intelligence.intermediate(), "h")

    def test_difficult(self):
        """Will check for the difficult function with return roll."""
        self.intelligence.max_score = {"Player1": 60, "Computer": 60}
        self.intelligence.score = 10
        self.assertEqual(self.intelligence.difficult(), "r")

    def test_difficult2(self):
        """Will check for the difficult function with return hold."""
        self.intelligence.max_score = {"Player1": 40, "Computer": 60}
        self.intelligence.score = 30
        self.assertEqual(self.intelligence.difficult(), "h")


if __name__ == "__main__":
    unittest.main()
