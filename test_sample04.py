import unittest


def add(number1, number2):
    return number1 + number2


class TestCalculation(unittest.TestCase):
    def test_二つの整数の和を計算できる(self):
        self.assertEqual(7, add(3, 4))


if __name__ == "__main__":
    unittest.main()

