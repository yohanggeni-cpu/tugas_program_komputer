# Exercise 6-5: Rivers
rivers = {
    "Nil": "Mesir",
    "Amazon": "Brasil dan beberapa negara Amerika Selatan",
    "Gangga": "India dan Bangladesh",
}
for river, country in rivers.items():
    print(f"Sungai {river} mengalir melalui {country}.")
print("\nNama sungai:")
for river in rivers:
    print(river)
print("\nNegara/wilayah:")
for country in rivers.values():
    print(country)
