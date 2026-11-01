# Solusi Exercise Python Crash Course (Bab 2-8)

Paket ini berisi solusi latihan mandiri berdasarkan *Python Crash Course*, edisi ke-3, karya Eric Matthes (No Starch Press, 2023). Setiap exercise bernomor memiliki file Python tersendiri. Contoh data, nama, dan nilai dipilih sebagai ilustrasi dan dapat diganti.

## Struktur folder

- `BAB_02/` - variabel, string, angka, komentar.
- `BAB_03/` - list dan operasi dasar.
- `BAB_04/` - perulangan, range, slicing, tuple, dan gaya kode.
- `BAB_05/` - conditional tests dan if statements.
- `BAB_06/` - dictionary dan nesting.
- `BAB_07/` - input pengguna dan while loops.
- `BAB_08/` - functions, arguments, return values, dan modules.

Terdapat **90 exercise bernomor** (2-1 sampai 8-17). Exercise yang bersifat reflektif atau meninjau gaya kode diberi file contoh/alat bantu, dengan keterbatasannya dijelaskan pada komentar.

## Menjalankan program di Windows / VS Code

1. Gunakan Python 3.10 atau lebih baru. Beberapa file memakai type hints modern.
2. Ekstrak ZIP ke sebuah folder.
3. Buka folder hasil ekstraksi melalui VS Code: **File → Open Folder**.
4. Buka terminal VS Code (**Terminal → New Terminal**).
5. Jalankan file yang dipilih, misalnya:

```powershell
python .\BAB_02\2_01_simple_message.py
```

Latihan interaktif Bab 7 dan Exercise 8-8 akan meminta input melalui terminal.

### Catatan khusus

- `BAB_04/4_04_one_million.py`: daftar satu juta angka dibuat. Untuk menghindari keluaran satu juta baris secara tidak sengaja, ubah `PRINT_ALL = False` menjadi `True` jika ingin mencetak semuanya.
- `BAB_07/7_07_infinity.py`: versi latihan dapat dihentikan dengan mengetik `quit` atau menekan `Ctrl+C`.
- `BAB_08/ex_8_15/`: file utama mengimpor fungsi dari `printing_functions.py`. Jalankan dengan `python .\BAB_08\ex_8_15\printing_models.py` dari root proyek.
- `BAB_08/ex_8_16/`: terdapat lima file demo untuk lima pola import. Jalankan masing-masing dari terminal yang berada di folder `BAB_08\ex_8_16`.
- `BAB_04/4_14_pep8_style_guide.py`, `BAB_04/4_15_code_review.py`, `BAB_05/5_12_styling_if_statements.py`, dan `BAB_05/5_13_your_ideas.py` merupakan latihan pengamatan/refleksi. Solusi yang disertakan berupa contoh atau alat bantu, bukan satu-satunya jawaban.

## Pemeriksaan seluruh file

Dari root folder proyek, jalankan:

```powershell
python -m compileall -q .
```

Perintah tersebut memeriksa sintaks semua file Python tanpa menjalankan program interaktifnya.

## Memasukkan solusi ke repository GitHub milikmu

Repository tujuan yang terakhir dibahas adalah:

`https://github.com/yohanggeni-cpu/tugas_program_komputer.git`

**Gunakan clone baru yang bersih.** Ini menghindari konflik merge yang sempat terjadi di folder lokal sebelumnya. Buka terminal PowerShell VS Code, lalu jalankan:

```powershell
cd C:\
git clone https://github.com/yohanggeni-cpu/tugas_program_komputer.git C:\repo_tugas_program_komputer
cd C:\repo_tugas_program_komputer
```

Jika folder `C:\repo_tugas_program_komputer` sudah ada, pilih nama folder tujuan lain yang belum digunakan. Jangan menjalankan `git init` atau `git remote add` lagi pada folder hasil clone; koneksi `origin` sudah dibuat otomatis oleh `git clone`.

Selanjutnya:

1. Ekstrak ZIP ini ke folder sementara, misalnya `C:\solusi_pcc`.
2. Dari terminal yang berada di `C:\repo_tugas_program_komputer`, salin folder dan dokumen dengan perintah berikut:

```powershell
Copy-Item C:\solusi_pcc\BAB_02 -Destination . -Recurse
Copy-Item C:\solusi_pcc\BAB_03 -Destination . -Recurse
Copy-Item C:\solusi_pcc\BAB_04 -Destination . -Recurse
Copy-Item C:\solusi_pcc\BAB_05 -Destination . -Recurse
Copy-Item C:\solusi_pcc\BAB_06 -Destination . -Recurse
Copy-Item C:\solusi_pcc\BAB_07 -Destination . -Recurse
Copy-Item C:\solusi_pcc\BAB_08 -Destination . -Recurse
Copy-Item C:\solusi_pcc\INDEKS_SOLUSI.md -Destination .
Copy-Item C:\solusi_pcc\PETUNJUK.md -Destination .

if (Test-Path .gitignore) {
    Get-Content C:\solusi_pcc\.gitignore | Add-Content .gitignore
} else {
    Copy-Item C:\solusi_pcc\.gitignore -Destination .
}
```

3. **Jangan mengganti `README.md` yang sudah ada di GitHub.** Paket ini memakai nama `PETUNJUK.md` agar README repository-mu tetap aman. Aturan `.gitignore` ditambahkan ke file yang sudah ada, atau disalin bila belum ada.
4. Periksa perubahan dan unggah:

```powershell
git status
git add BAB_02 BAB_03 BAB_04 BAB_05 BAB_06 BAB_07 BAB_08
git add INDEKS_SOLUSI.md PETUNJUK.md
git commit -m "Add Python Crash Course exercises chapters 2-8"
git push origin main
```

Jika Git menyatakan `nothing to commit`, periksa `git status` dan pastikan folder bab sudah disalin ke dalam folder clone, bukan ke folder lain.

## Identitas commit

Jika identitas Git belum diatur, jalankan sekali:

```powershell
git config --global user.name "Yohanes Wisanggeni Dwi Putra"
git config --global user.email "yohanggeni@student.uns.ac"
```

Identitas tersebut hanya dicantumkan pada commit; hak akses push ditentukan oleh akun GitHub yang diautentikasi.

## Sumber acuan

Matthes, E. (2023). *Python Crash Course* (3rd ed.). No Starch Press. Exercise Bab 2-8.
