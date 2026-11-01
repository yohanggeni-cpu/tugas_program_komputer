# Exercise 3-10: Every Function
mountains = ["Semeru", "Merbabu", "Rinjani"]
print("Daftar awal:", mountains)
print("Elemen pertama:", mountains[0])
mountains[1] = "Merapi"                 # Mengubah elemen
mountains.append("Lawu")                # Menambah di akhir
mountains.insert(1, "Sindoro")          # Menambah di posisi tertentu
print("Setelah append/insert:", mountains)
removed = mountains.pop(0)               # Menghapus berdasarkan posisi pertama
print("Hasil pop:", removed)
mountains.remove("Merapi")              # Menghapus berdasarkan nilai
print("Setelah remove:", mountains)
print("Panjang:", len(mountains))
print("Urutan alfabetis sementara:", sorted(mountains))
mountains.sort()                         # Mengurutkan permanen
print("Setelah sort:", mountains)
mountains.reverse()                      # Membalik urutan
print("Setelah reverse:", mountains)
print("Salinan:", mountains.copy())
print("Indeks Lawu:", mountains.index("Lawu"))
print("Jumlah Lawu:", mountains.count("Lawu"))
