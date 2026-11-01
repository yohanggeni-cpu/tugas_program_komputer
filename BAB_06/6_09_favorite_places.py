# Exercise 6-9: Favorite Places
favorite_places = {
    "Alya": ["Raja Ampat", "Bali"],
    "Bima": ["Gunung Bromo"],
    "Citra": ["Kyoto", "Paris", "Istanbul"],
}
for person, places in favorite_places.items():
    print(f"\nTempat favorit {person}:")
    for place in places:
        print(f"- {place}")
