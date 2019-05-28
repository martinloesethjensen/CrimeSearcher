import unittest

from app import get_input


class TestUserInput(unittest.TestCase):
    def test_user_input_should_be_int(self):
        # User input should be of type int
        self.assertEqual(type(get_input("Enter any number: ")), int)

    def test_user_input_should_return_zero(self):
        # Should return 0 if user enters anything except a number
        self.assertEqual(get_input("Enter any except a number: "), 0)
