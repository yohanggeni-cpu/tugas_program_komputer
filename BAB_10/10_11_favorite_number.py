import json
from pathlib import Path
path = Path(__file__).with_name("favorite_number.json")
number = input("Angka favorit: ")
path.write_text(json.dumps(number), encoding="utf-8")
print("Angka disimpan.")
