# Exercise 3-6: More Guests
guests = ["B.J. Habibie", "Ki Hajar Dewantara", "Leonardo da Vinci"]
print("Saya menemukan meja makan yang lebih besar!")
guests.insert(0, "R.A. Kartini")
guests.insert(len(guests) // 2, "Albert Einstein")
guests.append("Nelson Mandela")
for guest in guests:
    print(f"Yth. {guest}, Anda diundang untuk makan malam.")
