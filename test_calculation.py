import calculation
import unittest


class Testing(unittest.TestCase):
    #  test 1
    def test_add(self):
        assert calculation.calc.add(4, 5) == 9
        assert calculation.calc.add(-1, 1) == 0  # edge case testing
        assert calculation.calc.add(-1, -1) == -2  # edge case testing

    #  test 2
    def test_multiply(self):
        assert calculation.calc.multiply(5, 4) == 20
        assert calculation.calc.multiply(-1, 1) == -1  # edge case testing
        assert calculation.calc.multiply(-1, -1) == 1  # edge case testing

    #  test 3
    def test_subtract(self):
        assert calculation.calc.subtract(5, 4) == 1
        assert calculation.calc.subtract(-1, 1) == -2  # edge case testing
        assert calculation.calc.subtract(-1, -1) == 0  # edge case testing

    #  test 4
    def test_divide(self):
        assert calculation.calc.divide(3, 1) == 3
        assert calculation.calc.divide(-1, 1) == -1  # edge case testing
        assert calculation.calc.divide(-1, -1) == 1  # edge case testing

    #  test 5
    def test_result(self):
        b = f"""the result of a and b is = 5, the result of 4 * 5 = 20, the result of subtracting 2 from 3 is 1 
    and the result of dividing 2 / 3 is 0.6666666666666666"""
        self.assertEqual(calculation.calc.result(), b)

