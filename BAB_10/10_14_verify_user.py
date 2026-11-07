import json
from pathlib import Path
path = Path(__file__).with_name("user_profile.json")
if not path.exists():
    print("Profil belum ada. Jalankan 10_13 terlebih dahulu.")
else:
    profile = json.loads(path.read_text(encoding="utf-8"))
    print(f"Apakah kamu {profile['first_name']} {profile['last_name']}?")
    if input("Benar? (y/n): ").strip().lower() == "y":
        print("Pengguna berhasil diverifikasi.")
    else:
        print("Silakan perbarui profil.")
