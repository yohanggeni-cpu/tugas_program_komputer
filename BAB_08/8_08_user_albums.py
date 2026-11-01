# Exercise 8-8: User Albums


def make_album(
    artist: str, title: str, number_of_songs: int | None = None
) -> dict:
    """Buat dictionary album dari data yang diterima."""
    album = {"artist": artist, "title": title}
    if number_of_songs is not None:
        album["number_of_songs"] = number_of_songs
    return album


print("Masukkan data album. Ketik 'quit' pada nama artis untuk keluar.")
while True:
    artist = input("Nama artis: ").strip()
    if artist.lower() == "quit":
        break
    title = input("Judul album: ").strip()
    if not artist or not title:
        print("Artis dan judul album wajib diisi.")
        continue
    raw_count = input("Jumlah lagu (boleh kosong): ").strip()
    if raw_count:
        try:
            count = int(raw_count)
            if count < 0:
                raise ValueError
        except ValueError:
            print("Jumlah lagu harus bilangan bulat nonnegatif.")
            continue
        print(make_album(artist, title, count))
    else:
        print(make_album(artist, title))
