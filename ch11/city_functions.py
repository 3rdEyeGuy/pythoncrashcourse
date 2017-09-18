def city_format(city, country, population):
    """Formats the city and country in a single string"""
    cityCountry = city + ', ' + country + ' - ' + 'population' + population
    return cityCountry.title()
