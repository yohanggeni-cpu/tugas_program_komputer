# Exercise 8-13: User Profile

def build_profile(first: str, last: str, **user_info: str) -> dict:
    """Kumpulkan nama dan informasi tambahan dalam sebuah dictionary."""
    profile = {"first_name": first, "last_name": last}
    profile.update(user_info)
    return profile


my_profile = build_profile(
    "Yohanes",
    "Wisanggeni",
    major="Teknik Industri",
    university="Universitas Sebelas Maret",
    hobby="belajar Python",
)
print(my_profile)
