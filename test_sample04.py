import unittest


def add(number1, number2):
    return number1 + number2


class TestCalculation(unittest.TestCase):
    def test_二つの整数の和を計算できる_3タス4は7(self):
        self.assertEqual(7, add(3, 4))

    def test_二つの整数の和を計算できる_2タス3は5(self):
        self.assertEqual(5,add(2,3))


if __name__ == "__main__":
    unittest.main()

