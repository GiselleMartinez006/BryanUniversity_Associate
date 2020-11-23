import unittest  
from fizzbuzz import calcTest, callFizzStr, numToStr

print(calcTest(5,6))
print(callFizzStr("I can call FizzBuzz"))
print(numToStr(1))
print(numToStr(2))


class ShoppingBasketTest(unittest.TestCase):
    def test_empty_basket_total(self):
        string = "I can call FizzBuzz"
        numStr1 = 1
        numStr2 = 2
        self.assertEqual(callFizzStr(string), string)
        self.assertEqual(numToStr(numStr1),str(numStr1))
        self.assertEqual(numToStr(numStr2),str(numStr2))

if __name__ == '__main__':
    pass