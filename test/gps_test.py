import unittest

from service.gps import __get_lon_lat as gll
from service.gps import calculate_distance


class TestValue(unittest.TestCase):

    def test_return_coords__tuple(self):
        # Should return the coordinates as a tuple
        self.assertEqual(type(gll()), tuple)

    def test_return_distance_km(self):
        # Should calculate the difference in KM between København - Sacramento to be above 8000
        self.assertGreaterEqual(calculate_distance((55.676098, 12.568337), (38.575764, -121.478851)), 8000)
