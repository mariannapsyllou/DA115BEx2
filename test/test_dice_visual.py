"""Testing dice visual."""
import io
import unittest
from unittest.mock import patch
from dice import dice_visual


class TestDiceVisual(unittest.TestCase):
    """Will test the class dice_visual."""

    def setUp(self):
        """Will set up the class."""
        self.dice_visual = dice_visual.DiceVisual()

    def test_dice1(self):
        """Will match the expected output with dice 1."""
        expected_output = (
            " -----------\n"
            "|    |     |\n"
            "|    |     |\n"
            "|    |     |\n"
            " -----------\n"
        )
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            self.dice_visual.dice1()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_dice2(self):
        """Will match the expected output with dice 2."""
        expected_output = (
            " ----------\n"
            "|   ____  |\n"
            "|   ____| |\n"
            "|  |_____ |\n"
            " ----------\n"
        )
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            self.dice_visual.dice2()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_dice3(self):
        """Will match the expected output with dice 3."""
        expected_output = (
            " ----------\n"
            "|  ____   |\n"
            "|  ____|  |\n"
            "|  ____|  |\n"
            " ----------\n"
        )
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            self.dice_visual.dice3()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_dice4(self):
        """Will match the expected output with dice 4."""
        expected_output = (
            " ----------\n"
            "| |    |  |\n"
            "| |____|  |\n"
            "|      |  |\n"
            " ----------\n"
        )
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            self.dice_visual.dice4()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_dice5(self):
        """Will match the expected output with dice 5."""
        expected_output = (
            " ----------\n"
            "|  ____    |\n"
            "| |____    |\n"
            "|  ____|   |\n"
            " ----------\n"
        )
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            self.dice_visual.dice5()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_dice6(self):
        """Will match the expected output with dice 6."""
        expected_output = (
            " -----------\n"
            "|  ___     |\n"
            "| |___     |\n"
            "| |___|    |\n"
            " -----------\n"
        )
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            self.dice_visual.dice6()
            self.assertEqual(fake_out.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
