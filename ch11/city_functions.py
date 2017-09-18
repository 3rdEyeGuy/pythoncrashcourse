def city_format(city, country, population = ''):
    """Formats the city and country in a single string"""
    if population:
        cityCountry = city.title() + ', ' + country.title() + ' - ' + 'population ' + population
    else:
        cityCountry = city.title() + ', ' + country.title()
    return cityCountry
