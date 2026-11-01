# Exercise 3-7: Shrinking Guest List
guests = [
    "R.A. Kartini", "B.J. Habibie", "Albert Einstein",
    "Ki Hajar Dewantara", "Leonardo da Vinci", "Nelson Mandela",
]
print("Maaf, meja baru belum datang. Saya hanya dapat mengundang dua orang.")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Maaf {removed_guest}, undangan makan malam dibatalkan.")
for guest in guests:
    print(f"{guest}, Anda tetap diundang.")
del guests[:]
print("Daftar tamu setelah dikosongkan:", guests)
