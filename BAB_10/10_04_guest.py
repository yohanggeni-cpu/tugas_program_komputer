from pathlib import Path
name = input("Nama: ").strip()
if name:
    Path(__file__).with_name("guest.txt").write_text(name + "\n", encoding="utf-8")
    print("Nama tersimpan.")
else:
    print("Nama tidak boleh kosong.")
