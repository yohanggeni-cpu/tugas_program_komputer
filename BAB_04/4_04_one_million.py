# Exercise 4-4: One Million
# Menampilkan satu juta baris dapat memenuhi terminal.
# Ubah PRINT_ALL menjadi True untuk mencetak seluruh angka.
numbers = list(range(1, 1_000_001))
PRINT_ALL = False
if PRINT_ALL:
    for number in numbers:
        print(number)
else:
    print(f"Jumlah angka: {len(numbers):,}")
    print(f"Lima angka pertama: {numbers[:5]}")
    print(f"Lima angka terakhir: {numbers[-5:]}")
    print("Ubah PRINT_ALL = True untuk mencetak seluruh angka.")
