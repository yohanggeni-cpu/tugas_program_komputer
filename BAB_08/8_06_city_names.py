# Exercise 8-6: City Names

def city_country(city: str, country: str) -> str:
    """Kembalikan pasangan kota dan negara dalam format yang diminta."""
    return f"{city.title()}, {country.title()}"


print(city_country("santiago", "chile"))
print(city_country("jakarta", "indonesia"))
print(city_country("tokyo", "japan"))
