# Exercise 6-3: Glossary
glossary = {
    "variable": "Nama yang merujuk pada suatu nilai.",
    "string": "Tipe data untuk rangkaian karakter atau teks.",
    "list": "Kumpulan elemen berurutan yang dapat diubah.",
    "loop": "Struktur untuk menjalankan instruksi berulang.",
    "condition": "Ekspresi yang menghasilkan True atau False.",
}
for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")
