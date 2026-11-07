print("Kalkulator. Ketik q untuk keluar.")
while True:
    a = input("Angka pertama: ")
    if a.lower() == "q":
        break
    b = input("Angka kedua: ")
    if b.lower() == "q":
        break
    try:
        print("Hasil:", int(a) + int(b))
    except ValueError:
        print("Input harus berupa bilangan bulat.")
