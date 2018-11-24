import unittest

class TestSample01(unittest.TestCase):

    def test_初めてのテスト(self):
        self.assertEqual(7 , 3+4)

    def test_引き算(self):
        self.assertEqual(3 , 5-2)

    def test_失敗するテスト(self):
        self.assertEqual(1 , 3)

    def test_やっぱり失敗するテスト(self):
        self.assertEqual(99,50)

    def test_成功するテスト(self):
        self.assertEqual(100,10*10)

    def test_失敗(self):
        self.assertEqual(10,100)





if __name__ == "__main__":
    unittest.main()



