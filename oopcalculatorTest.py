import unittest
import ModularCalculator
import RecursiveExponentCalculator


class MyTestCase(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(45+44, ModularCalculator.ModularCalculator.add(self, [45, 44]))
        self.assertEqual(100+(-100), ModularCalculator.ModularCalculator.add(self, [100, -100]))
        self.assertEqual(999999+1, ModularCalculator.ModularCalculator.add(self, [999999, 1]))
        self.assertEqual(3.1415926+85, ModularCalculator.ModularCalculator.add(self, [3.1415926, 85]))
        self.assertEqual(3.1415926+85-85-3.1415926, ModularCalculator.ModularCalculator.add(self, [3.1415926, 85, -85, -3.1415926]))

    def testMultiply(self):
        self.assertEqual(16*0.25, ModularCalculator.ModularCalculator.multiply(self, [16, 0.25]))
        self.assertEqual(6*1, ModularCalculator.ModularCalculator.multiply(self, [6, 1]))
        self.assertEqual(6*0.5*2, ModularCalculator.ModularCalculator.multiply(self, [6, 0.5, 2]))
        self.assertEqual(6.6*-6.6*3, ModularCalculator.ModularCalculator.multiply(self, [6.6, -6.6, 3]))
        self.assertEqual(6.6*-6.6*-3, ModularCalculator.ModularCalculator.multiply(self, [6.6, -6.6, -3]))

    def testDivide(self):
        self.assertEqual("Whoops. Can't divide by zero.", ModularCalculator.ModularCalculator.divide(self, [4, 0, 2]))
        self.assertEqual(8, ModularCalculator.ModularCalculator.divide(self, [64, 8]))
        self.assertEqual(8, ModularCalculator.ModularCalculator.divide(self, [128, 2, 8]))
        self.assertEqual(-8, ModularCalculator.ModularCalculator.divide(self, [128, -2, 8]))

    def testExponentiate(self):
        self.assertEqual(19**5, ModularCalculator.ModularCalculator.two_integer_exponentiate(self, 19, 5))
        self.assertEqual(3**999999, ModularCalculator.ModularCalculator.two_integer_exponentiate(self, 3, 999999))
        self.assertEqual(8**2, ModularCalculator.ModularCalculator.two_integer_exponentiate(self, 8, 2))


if __name__ == '__main__':
    unittest.main()
