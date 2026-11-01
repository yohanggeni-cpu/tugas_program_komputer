# Exercise 6-8: Pets
pets = [
    {"animal": "kucing", "owner": "Alya", "name": "Milo"},
    {"animal": "anjing", "owner": "Bima", "name": "Bobby"},
    {"animal": "kelinci", "owner": "Citra", "name": "Snowy"},
]
for pet in pets:
    print("\nInformasi hewan peliharaan:")
    for key, value in pet.items():
        print(f"{key.title()}: {value}")
