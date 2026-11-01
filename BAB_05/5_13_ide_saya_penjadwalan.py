
# PENCATATAN JADWAL MAHASISWA
# Pengelola Jadwal Kuliah dan Tenggat Tugas

# BAB 2: VARIABLES
nama_mahasiswa = "Yohanes Wisanggeni Dwi Putra"

# BAB 3: LIST
jadwal_kuliah = []
daftar_tugas = []


# BAB 8: FUNCTIONS
def tambah_jadwal():
    print("\n--- TAMBAH JADWAL KULIAH ---")

    mata_kuliah = input("Nama mata kuliah: ")
    hari = input("Hari: ")
    jam = input("Jam: ")
    ruangan = input("Ruangan: ")

    # BAB 6: DICTIONARY
    jadwal = {
        "mata_kuliah": mata_kuliah,
        "hari": hari,
        "jam": jam,
        "ruangan": ruangan
    }

    jadwal_kuliah.append(jadwal)

    print("Jadwal berhasil ditambahkan!")


def lihat_jadwal():
    print("\n--- DAFTAR JADWAL KULIAH ---")

    # BAB 5: CONDITIONAL
    if not jadwal_kuliah:
        print("Belum ada jadwal kuliah.")
    else:
        # BAB 4: FOR LOOP
        for nomor, jadwal in enumerate(jadwal_kuliah, start=1):
            print(f"\nJadwal {nomor}")
            print(f"Mata Kuliah : {jadwal['mata_kuliah']}")
            print(f"Hari        : {jadwal['hari']}")
            print(f"Jam         : {jadwal['jam']}")
            print(f"Ruangan     : {jadwal['ruangan']}")


def tambah_tugas():
    print("\n--- TAMBAH TUGAS ---")

    nama_tugas = input("Nama tugas: ")
    mata_kuliah = input("Mata kuliah: ")
    tenggat = input("Tenggat (DD-MM-YYYY): ")

    tugas = {
        "nama": nama_tugas,
        "mata_kuliah": mata_kuliah,
        "tenggat": tenggat,
        "status": "Belum selesai"
    }

    daftar_tugas.append(tugas)

    print("Tugas berhasil ditambahkan!")


def lihat_tugas():
    print("\n--- DAFTAR TUGAS ---")

    if not daftar_tugas:
        print("Belum ada tugas.")
    else:
        for nomor, tugas in enumerate(daftar_tugas, start=1):
            print(f"\nTugas {nomor}")
            print(f"Nama       : {tugas['nama']}")
            print(f"Mata Kuliah: {tugas['mata_kuliah']}")
            print(f"Tenggat    : {tugas['tenggat']}")
            print(f"Status     : {tugas['status']}")


def selesaikan_tugas():
    lihat_tugas()

    if not daftar_tugas:
        return

    try:
        nomor = int(input("\nNomor tugas yang selesai: "))

        if 1 <= nomor <= len(daftar_tugas):
            daftar_tugas[nomor - 1]["status"] = "Selesai"
            print("Status tugas berhasil diperbarui!")
        else:
            print("Nomor tugas tidak ditemukan.")

    except ValueError:
        print("Masukkan nomor berupa angka.")


# BAB 7: INPUT DAN WHILE LOOP
while True:

    print("\n====================================")
    print("       STUDENT ACADEMIC PLANNER")
    print("====================================")
    print(f"Mahasiswa: {nama_mahasiswa}")

    print("\n1. Tambah Jadwal Kuliah")
    print("2. Lihat Jadwal Kuliah")
    print("3. Tambah Tugas")
    print("4. Lihat Daftar Tugas")
    print("5. Tandai Tugas Selesai")
    print("6. Keluar")

    pilihan = input("\nPilih menu (1-6): ")

    # BAB 5: CONDITIONAL
    if pilihan == "1":
        tambah_jadwal()

    elif pilihan == "2":
        lihat_jadwal()

    elif pilihan == "3":
        tambah_tugas()

    elif pilihan == "4":
        lihat_tugas()

    elif pilihan == "5":
        selesaikan_tugas()

    elif pilihan == "6":
        print("\nTerima kasih telah menggunakan aplikasi!")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
