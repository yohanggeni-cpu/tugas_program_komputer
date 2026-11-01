# Exercise 5-9: No Users


def greet_users(usernames: list[str]) -> None:
    """Tampilkan pesan khusus saat tidak ada pengguna."""
    if usernames:
        for username in usernames:
            if username == "admin":
                print("Hello admin, would you like to see a status report?")
            else:
                greeting = (
                    f"Hello {username.title()}, thank you for "
                    "logging in again."
                )
                print(greeting)
    else:
        print("We need to find some users!")


greet_users(["admin", "sarah", "mike"])
print("\nSetelah semua pengguna dihapus:")
greet_users([])
