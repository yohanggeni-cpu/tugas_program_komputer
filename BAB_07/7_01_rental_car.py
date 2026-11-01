# Exercise 7-1: Rental Car
car = input("Mobil rental apa yang ingin Anda gunakan? ").strip()
if car:
    print(f"Let me see if I can find you a {car.title()}.")
else:
    print("Anda belum memasukkan jenis mobil.")
