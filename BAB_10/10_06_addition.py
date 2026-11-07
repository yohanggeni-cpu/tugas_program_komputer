try:
    a = int(input("Angka pertama: "))
    b = int(input("Angka kedua: "))
except ValueError:
    print("Masukkan bilangan bulat.")
else:
    print("Hasil:", a + b)
