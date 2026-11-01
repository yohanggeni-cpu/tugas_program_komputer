# Exercise 6-6: Polling
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}
people_to_poll = ["jen", "edward", "wisang", "sarah", "maria"]
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Terima kasih, {person.title()}, sudah mengisi polling.")
    else:
        invitation = (
            f"{person.title()}, silakan ikut polling bahasa "
            "pemrograman favorit."
        )
        print(invitation)
