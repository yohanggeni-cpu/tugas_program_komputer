#matriks berukuran 2x2
listA = [3,4,6]
matriksA = [[11,    12],[13,    14]]
print (matriksA)
print (matriksA[0][0])
print (matriksA[1][1])

# Menampilkan elemen matrik menggunakan pengulangan
for baris in range(len(matriksA)):
    for kolom in range(len(matriksA[baris])):
        print(matriksA[baris][kolom],'\t', end = '')
    print()