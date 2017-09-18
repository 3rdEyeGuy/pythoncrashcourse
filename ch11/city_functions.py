def city_format(city, country, population = ''):
    """Formats the city and country in a single string"""
    if population:
        cityCountry = city + ', ' + country + ' - ' + 'population' + population
    else:
        cityCountry = city + ', ' + country
    return cityCountry.title()
