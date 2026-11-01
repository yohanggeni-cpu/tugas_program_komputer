# Exercise 6-4: Glossary 2
glossary = {
    "variable": "Nama yang merujuk pada suatu nilai.",
    "string": "Tipe data untuk teks.",
    "integer": "Bilangan bulat.",
    "float": "Bilangan pecahan desimal.",
    "list": "Kumpulan elemen berurutan yang dapat diubah.",
    "tuple": "Kumpulan elemen berurutan yang tidak dapat diubah.",
    "dictionary": "Kumpulan pasangan kunci dan nilai.",
    "loop": "Struktur untuk menjalankan instruksi berulang.",
    "function": "Blok kode yang dapat dipanggil kembali.",
    "boolean": "Tipe nilai True atau False.",
}
for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}\n")
