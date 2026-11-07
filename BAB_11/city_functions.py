def city_country(city, country, population=None):
    result = f"{city.title()}, {country.title()}"
    if population is not None:
        result += f" - population {population}"
    return result
