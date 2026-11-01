# Exercise 8-7: Album


def make_album(
    artist: str, title: str, number_of_songs: int | None = None
) -> dict:
    """Buat dictionary informasi album; jumlah lagu bersifat opsional."""
    album = {"artist": artist, "title": title}
    if number_of_songs is not None:
        if number_of_songs < 0:
            raise ValueError("Jumlah lagu tidak boleh negatif.")
        album["number_of_songs"] = number_of_songs
    return album


print(make_album("Coldplay", "Parachutes"))
print(make_album("Tulus", "Manusia"))
print(make_album("Taylor Swift", "1989", 13))
