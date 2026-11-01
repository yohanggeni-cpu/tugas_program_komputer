# Exercise 6-12: Extensions
# Pengembangan contoh Exercise 6-9: menambah negara dan kategori tempat.
favorite_places = {
    "Alya": [
        {"name": "Raja Ampat", "country": "Indonesia", "category": "alam"},
        {"name": "Bali", "country": "Indonesia", "category": "pantai"},
    ],
    "Bima": [
        {
            "name": "Gunung Bromo",
            "country": "Indonesia",
            "category": "pegunungan",
        },
    ],
    "Citra": [
        {"name": "Kyoto", "country": "Jepang", "category": "budaya"},
    ],
}
for person, places in favorite_places.items():
    print(f"\nTempat favorit {person}:")
    for place in places:
        print(f"- {place['name']} ({place['country']}; {place['category']})")
