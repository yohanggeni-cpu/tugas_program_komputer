import csv
FILE_NAME = 'files/nilaiKuliah.csv'
listNilai = []
kolom = []
with open(FILE_NAME, mode='r')as file:
    csv_reader = csv.reader(file,delimiter=',')
    bariske = 0
    for row in csv_reader:
        if bariske == 0:
            kolom = row
            bariske += 1
            continue
        listNilai.append(row)

print(kolom)
print(listNilai)