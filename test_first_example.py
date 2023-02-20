import first_example
import unittest

class TestingFile(unittest.TestCase):

    def test_answer1(self):
        assert first_example.func(6) == 12


    def test_answer2(self):
        assert first_example.func(5) == 10


    def test_answer3(self):
        assert first_example.func(2) == 4


    def test_answer4(self):
        assert first_example.func(3) == 6
