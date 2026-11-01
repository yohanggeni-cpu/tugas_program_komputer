# Exercise 7-5: Movie Tickets
print("Masukkan usia penonton. Ketik 'quit' untuk mengakhiri.")
while True:
    raw_age = input("Usia: ").strip()
    if raw_age.lower() == "quit":
        break
    try:
        age = int(raw_age)
    except ValueError:
        print("Masukkan usia berupa bilangan bulat atau 'quit'.")
        continue
    if age < 0:
        print("Usia tidak boleh negatif.")
    elif age < 3:
        print("Harga tiket: gratis.")
    elif age <= 12:
        print("Harga tiket: $10.")
    else:
        print("Harga tiket: $15.")
