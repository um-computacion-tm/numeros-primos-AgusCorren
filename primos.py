import unittest
def is_primo(value):
    # valor % div -> resto
    div = 2
    while div < value:
        if value % div == 0:

            return False
        div += 1
    return True
        
class TestPrimos(unittest.TestCase):
    def test_1(self):
        result = is_primo(1)
        self.assertEqual(result, True)
    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result, True)
    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result, True)
    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result, False)
    def test_5(self):
        result = is_primo(5)
        self.assertEqual(result, True)
    def test_6(self):
        result = is_primo(6)
        self.assertEqual(result, False)
    def test_19(self):
       result = is_primo(19)
       self.assertEqual(result, True)
        
if __name__ == "__main__":
    unittest.main()