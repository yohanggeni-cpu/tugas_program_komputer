# Exercise 3-11: Intentional Error
# IndexError dipicu dan ditangkap, lalu indeks diperbaiki agar
# program selesai normal.
colors = ["merah", "biru", "hijau"]
try:
    print(colors[3])  # Indeks 3 tidak tersedia: indeks valid 0, 1, dan 2.
except IndexError as error:
    print(f"IndexError berhasil diperagakan: {error}")

print("Perbaikan: elemen terakhir adalah", colors[-1])
