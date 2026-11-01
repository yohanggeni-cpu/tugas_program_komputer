# Exercise 7-6: Three Exits
# Tiga cara menghentikan loop, masing-masing ditunjukkan secara terpisah.

print("Versi 1: kondisi pada while. Ketik selain 'lanjut' untuk berhenti.")
answer = "lanjut"
while answer == "lanjut":
    answer = input("Ketik 'lanjut' untuk mengulang: ").strip().lower()

print("\nVersi 2: active variable. Ketik 'berhenti' untuk mengakhiri.")
active = True
while active:
    answer = input("Perintah: ").strip().lower()
    if answer == "berhenti":
        active = False

print("\nVersi 3: break. Ketik 'quit' untuk mengakhiri.")
while True:
    answer = input("Perintah: ").strip().lower()
    if answer == "quit":
        break
print("Semua demonstrasi loop selesai.")
