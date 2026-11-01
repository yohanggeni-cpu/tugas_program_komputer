# Exercise 8-17: Styling Functions
# Tiga contoh fungsi ditulis dengan nama deskriptif, docstring, dan PEP 8.

def greet_user(username: str) -> None:
    """Tampilkan sapaan untuk seorang pengguna."""
    print(f"Halo, {username.title()}!")


def make_sandwich(*ingredients: str) -> None:
    """Tampilkan daftar bahan sandwich."""
    print("Isi sandwich:")
    for ingredient in ingredients:
        print(f"- {ingredient}")


def build_profile(first_name: str, last_name: str, **details: str) -> dict:
    """Bangun profil sederhana dari nama dan detail tambahan."""
    profile = {"first_name": first_name, "last_name": last_name}
    profile.update(details)
    return profile


greet_user("Wisang")
make_sandwich("ayam", "keju", "selada")
print(build_profile("Yohanes", "Wisanggeni", major="Teknik Industri"))
