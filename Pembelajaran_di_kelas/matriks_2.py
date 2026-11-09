MatA = [
    [8, 2],
    [4, 6],
]
MatB = [
    [3, 5],
    [1, 3],
]

MATC = []

for i in range(0, len(MatA)):
    hasiljumlah = 0
    row =[]
    for j in range(0, len(MatA[0])):
#         print (MatA[i][j] + MatB[i][j], end=' ')
        hasiljumlah = MatA[i][j] + MatB[i][j]
        row.append(hasiljumlah)
#         MATC[i][j] = hasiljumlah            
    # print(row)
    MATC.append(row)

print(MATC)

print(len(MatA))
