import first_example
import unittest

class TestingFile(unittest.TestCase):

    def test_five_by_two_is_ten(self):
        assert first_example.func(5) == 10


    def test_two_by_two_is_four(self):
        assert first_example.func(2) == 4


    def test_three_by_two_is_six(self):
        assert first_example.func(3) == 6

    def test_edges(self):
        self.assertEqual(first_example.func(2), 2 * 2)
        self.assertEqual(first_example.func(124), 124 * 2)
        self.assertEqual(first_example.func(124), 2 * 124)
        self.assertEqual(first_example.func(65535), 65535 * 2)
        self.assertEqual(first_example.func(65535), 2 * 65535)
        self.assertEqual(first_example.func(1), 1 * 2)
        self.assertEqual(first_example.func(-1), (-1) * 2)

    def test_invalid_type(self):
        self.assertRaises(TypeError, first_example.func("Hello World!"))
        self.assertRaises(TypeError, first_example.func(True))
        self.assertRaises(TypeError, first_example.func([1, 2, 3, 4, 5]))