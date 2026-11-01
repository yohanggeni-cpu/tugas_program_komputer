# Exercise 4-13: Buffet
menu = ("nasi goreng", "sate ayam", "gado-gado", "soto", "es cendol")
print("Menu awal:")
for food in menu:
    print(food)

try:
    menu[0] = "mie goreng"  # Tuple tidak dapat diubah.
except TypeError as error:
    print("Perubahan tuple ditolak:", error)

menu = ("mie goreng", "sate kambing", "gado-gado", "soto", "es cendol")
print("\nMenu baru:")
for food in menu:
    print(food)
