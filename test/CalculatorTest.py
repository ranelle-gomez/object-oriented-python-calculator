import unittest
import ModularCalculator
import RecursiveExponentCalculator


class MyTestCase(unittest.TestCase):
    def test_add(self):
        for a in range(-100, 100):
            for b in range(-100, 100):
                for c in range(-100, 100):
                    print(
                        'add_test', a, b, c, 'result: ',
                        ModularCalculator.ModularCalculator.add(
                            self, [a, b, c]))
                    self.assertAlmostEqual(
                        a + b + c,
                        ModularCalculator.ModularCalculator.add(
                            self, [a, b, c]))

    def test_subtract(self):
        for a in range(-100, 100):
            for b in range(-100, 100):
                for c in range(-100, 100):
                    print(
                        'subtract_test', a, b, c, 'result: ',
                        ModularCalculator.ModularCalculator.subtract(
                            self, [a, b, c]))
                    self.assertAlmostEqual(
                        a - b - c,
                        ModularCalculator.ModularCalculator.subtract(
                            self, [a, b, c]))

    def test_multiply(self):
        for x in range(-100, 100):
            for y in range(-100, 100):
                for z in range(-100, 100):
                    print(
                        'multiply_test', x, y, z, 'result: ',
                        ModularCalculator.ModularCalculator.multiply(
                            self, [x, y, z]))
                    self.assertAlmostEqual(
                        x * y * z,
                        ModularCalculator.ModularCalculator.multiply(
                            self, [x, y, z]))

    def test_exponentiate(self):
        for b in range(-10, 100):
            for p in range(-10, 100):
                self.assertEqual(
                    b**p,
                    RecursiveExponentCalculator.RecursiveExponentiation.
                    tail_recursive_exponentiate(self, b, p))
                self.assertEqual(
                    b**p,
                    RecursiveExponentCalculator.RecursiveExponentiation.
                    recursive_exponentiate(self, b, p))
                self.assertEqual(
                    b**p,
                    ModularCalculator.ModularCalculator.
                    two_integer_exponentiate(self, b, p))

    def test_divide(self):
        for a in range(-100, 100):
            for b in range(-100, 100):
                for c in range(-100, 100):
                    if b == 0 or c == 0:
                        self.assertEqual(
                            'Whoops. Cannot divide by zero. 😭',
                            ModularCalculator.ModularCalculator.divide(
                                self, [a, b, c]))
                    else:
                        print(
                            'divide_test', a, b, c, 'result: ',
                            ModularCalculator.ModularCalculator.divide(
                                self, [a, b, c]))
                        self.assertAlmostEqual(
                            a / b / c,
                            ModularCalculator.ModularCalculator.divide(
                                self, [a, b, c]))


if __name__ == '__main__':
    unittest.main()
