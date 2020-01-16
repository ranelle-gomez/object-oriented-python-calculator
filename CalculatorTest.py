import unittest
import ModularCalculator
import math
import time
import RecursiveExponentCalculator


class MyTestCase(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(45+44, ModularCalculator.ModularCalculator.add(self, [45, 44]))
        self.assertEqual(100+(-100), ModularCalculator.ModularCalculator.add(self, [100, -100]))
        self.assertEqual(999999+1, ModularCalculator.ModularCalculator.add(self, [999999, 1]))
        self.assertEqual(3.1415926+85, ModularCalculator.ModularCalculator.add(self, [3.1415926, 85]))
        self.assertEqual(3.1415926+85-85-3.1415926, ModularCalculator.ModularCalculator.add(self, [3.1415926, 85, -85, -3.1415926]))

        for a in range(-100, 100):
            for b in range(-100, 100):
                for c in range(-100, 100):
                    print(a, b, c, ModularCalculator.ModularCalculator.add(self, [a, b, c]))
                    self.assertAlmostEqual(a+b+c, ModularCalculator.ModularCalculator.add(self, [a, b, c]))
    """
    def testMultiply(self):

        self.assertEqual(16*0.25, ModularCalculator.ModularCalculator.multiply(self, [16, 0.25]))
        self.assertEqual(6*1, ModularCalculator.ModularCalculator.multiply(self, [6, 1]))
        self.assertEqual(6*0.5*2, ModularCalculator.ModularCalculator.multiply(self, [6, 0.5, 2]))
        self.assertEqual(6.6*-6.6*3, ModularCalculator.ModularCalculator.multiply(self, [6.6, -6.6, 3]))
        self.assertEqual(6.6*-6.6*-3, ModularCalculator.ModularCalculator.multiply(self, [6.6, -6.6, -3]))

        for x in range(-100, 100):
            for y in range(-100, 100):
                for z in range(-100, 100): # naming this c gave the other for loop downstairs a run lol.
                    print(x, y, z, ModularCalculator.ModularCalculator.multiply(self, [x, y, z]))
                    self.assertAlmostEqual(x*y*z, ModularCalculator.ModularCalculator.multiply(self, [x, y, z]))

    def testDivide(self):
        self.assertEqual("Whoops. Can't divide by zero. 😭", ModularCalculator.ModularCalculator.divide(self, [4, 0, 2]))
        self.assertEqual(8, ModularCalculator.ModularCalculator.divide(self, [64, 8]))
        self.assertEqual(8, ModularCalculator.ModularCalculator.divide(self, [128, 2, 8]))
        self.assertEqual(-8, ModularCalculator.ModularCalculator.divide(self, [128, -2, 8]))
        for a in range(-100, 100):
            for b in range(-100, 100):
                for c in range(-100, 100):
                    if a == 0 or b == 0 or c == 0:
                        self.assertEqual("Whoops. Can't divide by zero. 😭", ModularCalculator.ModularCalculator.divide(self, [a, b, c]))
                    else:
                        print(a, b, c, ModularCalculator.ModularCalculator.divide(self, [a, b, c]))
                        self.assertAlmostEqual(a / b / c, ModularCalculator.ModularCalculator.divide(self, [a, b, c])) 


    def testExponentiate(self):
        for b in range(0, 101):
            for p in range(0, 101):
                self.assertEqual(b**p, RecursiveExponentCalculator.RecursiveExponentiation.tail_recursive_exponentiate(self, b, p))
                self.assertEqual(b**p, RecursiveExponentCalculator.RecursiveExponentiation.recursive_exponentiate(self, b, p))
                self.assertEqual(b**p, RecursiveExponentCalculator.RecursiveExponentiation.two_integer_exponentiate(self, b, p))



"""





if __name__ == '__main__':
    unittest.main()
