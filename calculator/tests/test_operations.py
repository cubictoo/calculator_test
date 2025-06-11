import unittest
import math
from calculator_logic.operations import (
    add, subtract, multiply, divide,
    square_root, power, log_natural, log_base10,
    sin_degrees, cos_degrees, tan_degrees
)

class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    def test_subtract(self):
        # This test will initially fail due to the intentional error
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(1, -1), 2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(-1, 2), -2)
        self.assertEqual(multiply(-1, -2), 2)
        self.assertEqual(multiply(0, 5), 0)
        self.assertAlmostEqual(multiply(0.5, 0.5), 0.25)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-6, 3), -2)
        self.assertEqual(divide(6, -3), -2)
        self.assertAlmostEqual(divide(1, 3), 0.3333333333333333)
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_square_root(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(2), 1.4142135623730951)
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 5), 0) # 0^0 is 1 by math.pow, but 0 to any positive power is 0
        self.assertEqual(power(2, -2), 0.25)
        self.assertAlmostEqual(power(4, 0.5), 2)

    def test_log_natural(self):
        self.assertAlmostEqual(log_natural(math.e), 1)
        self.assertAlmostEqual(log_natural(1), 0)
        self.assertAlmostEqual(log_natural(10), 2.302585092994046)
        with self.assertRaises(ValueError):
            log_natural(0)
        with self.assertRaises(ValueError):
            log_natural(-1)

    def test_log_base10(self):
        self.assertAlmostEqual(log_base10(100), 2)
        self.assertAlmostEqual(log_base10(1), 0)
        self.assertAlmostEqual(log_base10(50), 1.6989700043360187)
        with self.assertRaises(ValueError):
            log_base10(0)
        with self.assertRaises(ValueError):
            log_base10(-1)

    def test_sin_degrees(self):
        self.assertAlmostEqual(sin_degrees(0), 0)
        self.assertAlmostEqual(sin_degrees(90), 1)
        self.assertAlmostEqual(sin_degrees(180), 0)
        self.assertAlmostEqual(sin_degrees(270), -1)
        self.assertAlmostEqual(sin_degrees(30), 0.5)
        self.assertAlmostEqual(sin_degrees(45), math.sqrt(2)/2)

    def test_cos_degrees(self):
        self.assertAlmostEqual(cos_degrees(0), 1)
        self.assertAlmostEqual(cos_degrees(90), 0)
        self.assertAlmostEqual(cos_degrees(180), -1)
        self.assertAlmostEqual(cos_degrees(270), 0)
        self.assertAlmostEqual(cos_degrees(60), 0.5)
        self.assertAlmostEqual(cos_degrees(45), math.sqrt(2)/2)

    def test_tan_degrees(self):
        self.assertAlmostEqual(tan_degrees(0), 0)
        self.assertAlmostEqual(tan_degrees(45), 1)
        # For tan(90), math.tan returns a very large number, not infinity.
        # Depending on precise requirements, might need specific handling for undefined cases.
        self.assertTrue(tan_degrees(90) > 1e15) # Check for a very large number
        self.assertAlmostEqual(tan_degrees(180), 0)
        self.assertAlmostEqual(tan_degrees(30), 1/math.sqrt(3))


if __name__ == "__main__":
    unittest.main()
