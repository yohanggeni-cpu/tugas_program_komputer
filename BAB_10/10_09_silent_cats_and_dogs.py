from pathlib import Path
folder = Path(__file__).parent
for name in ("cats.txt", "dogs.txt"):
    try:
        contents = (folder / name).read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        print(f"\n{name}:\n{contents}")
