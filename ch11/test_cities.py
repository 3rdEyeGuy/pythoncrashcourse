import unittest

from city_functions import city_format

class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""
    def test_city_country(self):
        """Do names like "Santiago, Chile" work?"""
        formatted_city = city_format('santiago','chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

unittest.main()