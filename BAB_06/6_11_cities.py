# Exercise 6-11: Cities
# Angka populasi berikut hanya contoh untuk latihan dictionary.
cities = {
    "Surakarta": {
        "country": "Indonesia",
        "population": "sekitar 0,5 juta (contoh)",
        "fact": "Dikenal sebagai Kota Bengawan.",
    },
    "Kyoto": {
        "country": "Jepang",
        "population": "sekitar 1,4 juta (contoh)",
        "fact": "Pernah menjadi ibu kota Jepang.",
    },
    "Paris": {
        "country": "Prancis",
        "population": "sekitar 2,1 juta (contoh kota administratif)",
        "fact": "Dilalui Sungai Seine.",
    },
}
for city, information in cities.items():
    print(f"\n{city}:")
    for key, value in information.items():
        print(f"  {key.title()}: {value}")
