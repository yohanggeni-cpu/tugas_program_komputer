import json
from pathlib import Path
path = Path(__file__).with_name("favorite_number.json")
if path.exists():
    print("Angka favoritmu:", json.loads(path.read_text(encoding="utf-8")))
else:
    print("Data belum ada. Jalankan 10_11 terlebih dahulu.")
