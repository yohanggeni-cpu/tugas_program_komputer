# Exercise 7-2: Restaurant Seating
try:
    group_size = int(input("Berapa orang dalam kelompok makan malam Anda? "))
    if group_size < 1:
        print("Jumlah orang harus minimal 1.")
    elif group_size > 8:
        print("Anda harus menunggu meja.")
    else:
        print("Meja Anda sudah siap.")
except ValueError:
    print("Masukkan jumlah orang dalam bentuk bilangan bulat.")
