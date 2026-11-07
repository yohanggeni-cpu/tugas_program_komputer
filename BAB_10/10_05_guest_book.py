from pathlib import Path
path = Path(__file__).with_name("guest_book.txt")
print("Buku tamu. Ketik q untuk berhenti.")
while True:
    name = input("Nama: ").strip()
    if name.lower() == "q":
        break
    if name:
        with path.open("a", encoding="utf-8") as file:
            file.write(f"{name} mengunjungi buku tamu.\n")
        print(f"Selamat datang, {name}.")
