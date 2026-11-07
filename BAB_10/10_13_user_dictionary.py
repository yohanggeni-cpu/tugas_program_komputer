import json
from pathlib import Path
path = Path(__file__).with_name("user_profile.json")
profile = {
    "first_name": input("Nama depan: "),
    "last_name": input("Nama belakang: "),
    "age": input("Usia: "),
    "city": input("Kota: "),
}
path.write_text(json.dumps(profile, indent=4), encoding="utf-8")
print("Profil disimpan:", profile)
