import unittest

from city_functions import city_format

class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""
    def test_city_country(self):
        """Do names like "Santiago, Chile" work?"""
        formatted_city = city_format('santiago','chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        format_cityCtryPop = city_format('santiago','chile','5000000')
        self.assertEqual(format_cityCtryPop, 'Santiago, Chile - population 5000000')

unittest.main()
