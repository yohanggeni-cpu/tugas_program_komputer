from pathlib import Path
contents = Path(__file__).with_name("learning_python.txt").read_text(encoding="utf-8")
for line in contents.splitlines():
    print(line)
