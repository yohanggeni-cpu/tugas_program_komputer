from pathlib import Path
path = Path(__file__).with_name("learning_python.txt")
contents = path.read_text(encoding="utf-8")
print("Seluruh isi file:")
print(contents)
print("Isi melalui list dan loop:")
for line in contents.splitlines():
    print(line)
