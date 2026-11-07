from pathlib import Path
path = Path(__file__).with_name("learning_python.txt")
for line in path.read_text(encoding="utf-8").splitlines():
    print(line.replace("Python", "C"))
