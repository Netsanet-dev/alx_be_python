from simple_calculator import SimpleCalculator
import unittest

class Test_simple_calculator(unittest.TestCase):
    def test_addition(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(1, 0), 1)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(2, -3), -1)
    def test_subtraction(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.subtract(1,1), 0)
        self.assertEqual(self.calc.subtract(-1,-1), 0)
        self.assertEqual(self.calc.subtract(9,-1), 10)
        self.assertEqual(self.calc.subtract(-1,1), -2)
        # if num minus string
        # if negative number
        pass
    def test_multiplication(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.multiply(2, 4), 8)
        self.assertEqual(self.calc.multiply(1, 0), 0)
        self.assertEqual(self.calc.multiply(1, 1), 1)
        
    def test_division(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.divide(1, 0),None)
        self.assertEqual(self.calc.divide(1, 1),1)
        self.assertEqual(self.calc.divide(4, 2),2)
        self.assertEqual(self.calc.divide(5, 2),2.5)
        #if num and str
        # test if the denominator is zero