import unittest

from service.value_checker import check_search_value


class TestValue(unittest.TestCase):
    def test_should_go_back(self):
        # User should go back to previous menu
        self.assertEqual(check_search_value(-1), "-1")

    def test_should_return_type_str(self):
        # Return should be of type str
        self.assertEqual(type(check_search_value(5)), str)

    def test_should_return_crimedescr(self):
        # User selects category 'crimedescr'
        self.assertEqual(check_search_value(5), 'crimedescr')
