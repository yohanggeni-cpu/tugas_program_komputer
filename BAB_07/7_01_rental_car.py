# Exercise 7-1: Rental Car
car = input("Mobil rental apa yang ingin Anda gunakan? ").strip()
if car:
    print(f"Coba kulihat, apakah aku bisa mencarikan {car.title()} untukmu.")
else:
    print("Anda belum memasukkan jenis mobil.")
