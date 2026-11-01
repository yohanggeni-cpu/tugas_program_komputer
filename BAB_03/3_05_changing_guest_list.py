# Exercise 3-5: Changing Guest List
guests = ["B.J. Habibie", "Marie Curie", "Leonardo da Vinci"]
unavailable_guest = guests[1]
print(f"{unavailable_guest} tidak dapat menghadiri makan malam.")

guests[1] = "Ki Hajar Dewantara"
for guest in guests:
    print(f"Yth. {guest}, Anda tetap diundang untuk makan malam.")
