import pandas as pd

FILE_NAME = 'files/nilaiKuliah.csv'
dfNilai = pd.read_csv(FILE_NAME, delimiter=',', encoding='Latin1')
print(type(dfNilai))
print(dfNilai)

# save csv pandas
dfNilai.to_csv('files/nilaiKuliah_pd.csv', sep=';', index=False)

nilaiKelasA = pd.read_excel('files/Nilai_KelasA.xlsx', sheet_name='Nilai_A')
print (nilaiKelasA)