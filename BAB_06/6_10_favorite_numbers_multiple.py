# Exercise 6-10: Favorite Numbers
favorite_numbers = {
    "Alya": [7, 14],
    "Bima": [12, 24, 36],
    "Citra": [4],
    "Doni": [21, 42],
    "Eka": [8, 16, 32],
}
for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers: {', '.join(map(str, numbers))}")
