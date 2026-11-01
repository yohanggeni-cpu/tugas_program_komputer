# Exercise 7-7: Infinity
# Loop ini berlangsung berulang sampai pengguna mengetik 'quit'.
# Ctrl+C juga dapat digunakan untuk menghentikan program.
while True:
    command = input("Loop aktif. Ketik 'quit' untuk keluar: ").strip().lower()
    if command == "quit":
        print("Loop dihentikan dengan aman.")
        break
    print("Program terus berjalan...")
