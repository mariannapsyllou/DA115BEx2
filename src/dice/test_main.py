import unittest
from io import StringIO
import main
import menu

class TestMain(unittest.TestCase()):

    def setUp(self):
        self.object = main.MainShell()

    def test_do_main(self):

        # Redirect stdout to a StringIO object
        with StringIO() as output:
            with patch('sys.stdout', new=output):
                # Call the method that prints the menu
                my_object.do_main(None)

                # Get the actual output from the StringIO object
                actual_output = output.getvalue()

        # Split the actual output into separate lines
        actual_lines = actual_output.split('\n')

        # Get the expected output from the menu module
        expected_lines = []
        menu.main_menu(lambda line: expected_lines.append(line))

        # Remove any blank lines from the expected output
        expected_lines = [line for line in expected_lines if line]

        # Assert that the expected output matches the actual output
        self.assertEqual(expected_lines, actual_lines)
