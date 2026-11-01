# Exercise 4-15: Code Review
# Pemeriksa sederhana untuk tiga file Python pilihan.
# Alat ini bukan pengganti linter PEP 8.
from pathlib import Path

MAX_LINE_LENGTH = 79


def review_file(file_path: Path) -> list[str]:
    """Kembalikan temuan dasar gaya kode pada satu file Python."""
    findings = []
    lines = file_path.read_text(encoding="utf-8").splitlines()
    for line_number, line in enumerate(lines, start=1):
        if len(line) > MAX_LINE_LENGTH:
            findings.append(
                f"Baris {line_number}: {len(line)} karakter (maks. 79)."
            )
        if "\t" in line:
            findings.append(f"Baris {line_number}: ditemukan karakter tab.")
        if line.rstrip() != line:
            findings.append(f"Baris {line_number}: whitespace di akhir baris.")
    for index in range(2, len(lines)):
        if lines[index] == lines[index - 1] == lines[index - 2] == "":
            findings.append(
                f"Baris {index + 1}: lebih dari satu baris kosong berurutan."
            )
    return findings


def main() -> None:
    """Minta tiga file, lalu tampilkan hasil pemeriksaan."""
    for _ in range(3):
        raw_path = input("Path file .py (Enter untuk selesai): ").strip()
        if not raw_path:
            break
        path = Path(raw_path)
        if not path.is_file() or path.suffix != ".py":
            print("File .py tidak ditemukan.\n")
            continue
        findings = review_file(path)
        print(f"\nHasil {path}:")
        if findings:
            print("\n".join(findings))
        else:
            print("Tidak ditemukan masalah dasar yang diperiksa.")
        print()


if __name__ == "__main__":
    main()
