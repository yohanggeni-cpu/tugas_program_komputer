# Exercise 5-10: Checking Usernames
current_users = ["John", "sarah", "mike", "admin", "Nayla"]
new_users = ["JOHN", "wisang", "Tika", "ADMIN", "raihan"]
current_users_lower = [username.lower() for username in current_users]

for new_username in new_users:
    if new_username.lower() in current_users_lower:
        print(
            f"{new_username}: nama sudah digunakan; silakan pilih nama lain."
        )
    else:
        print(f"{new_username}: nama tersedia.")
