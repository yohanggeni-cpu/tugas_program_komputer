from pathlib import Path
folder = Path(__file__).parent
for name in ("cats.txt", "dogs.txt"):
    print(f"\n{name}:")
    try:
        print((folder / name).read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"File {name} tidak ditemukan.")
