# Exercise 8-5: Cities

def describe_city(city: str, country: str = "Indonesia") -> None:
    """Tampilkan kota dan negara tempat kota tersebut berada."""
    print(f"{city.title()} is in {country.title()}.")


describe_city("Surakarta")
describe_city("Yogyakarta")
describe_city("Kyoto", "Japan")
