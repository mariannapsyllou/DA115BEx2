import unittest
from Classes.Intelligence import Intelligence

class TestIntelligence(unittest.TestCase):
    _p = Intelligence("wa")

    def test_easy(self):
        result = self._p.easy()
        if result == "r":
            self.assertEqual(result, "r")
        else:
            self.assertEqual(result, "h")

    def test_intermediate(self):
        rolls = 0
        iterations = 10000
        for i in range(iterations):
            ans = self._p.intermediate()
            if ans == "r":
                rolls += 1

        result = (rolls/iterations) * 100
        final = True
        if result < 55 or result > 77:
            final = False
        print(result)
        self.assertEqual(final, True)


