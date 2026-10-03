print("Halloo selamaat dataaangg, silahkaaan masukan ussername dan password andaa tuaan")

username_benar = "Rasyid"
password_benar = "019"
kesalahan = 0
login_berhasil = False

while kesalahan < 3:
    username = input("Username: ")
    password = input("Password: ")

    if username == username_benar and password == password_benar:
        login_berhasil = True
        break
    else:
        kesalahan += 1
        print(f"Username atau password muu salah srr! sisa kesempatan: {3 - kesalahan}")

if login_berhasil == False:
    print("Salaaah 3 kali akun anda kami freez, program kmai hentikan")

if login_berhasil:
    print("Login berhasil!")

    
    daftar_nama = []
    daftar_kelas_siswa = []
    daftar_ikut = []
    daftar_nilai = []
    daftar_kategori = []
    daftar_kelas = []   
    jumlah = 0

    lanjut = "ya"

    while lanjut == "ya":
       
        print("\n--- Input Data Siswa ---")
        nama = input("Nama siswa: ")
        kelas = input("Kelas siswa: ")
        ikut = input("siswa ikutt  ujian? (ya/tidak): ")

        while ikut != "ya" and ikut != "tidak":
            print("Jawab dengan 'ya' atau 'tidak'!")
            ikut = input("siswa ikut ujian? (ya/tidak): ")

        if ikut == "tidak":
            nilai = 0
            kategori = "-"
        else:
    
            while True:
                benar = int(input("Jumlah soal benar: "))
                salah = int(input("Jumlah soal salah: "))

                if benar >= 0 and salah >= 0 and benar + salah == 20:
                    break
                else:
                    print("jumlah soal harus 20, tolong lebih teliti.")

            nilai = benar * 5

            if nilai >= 80:
                kategori = "Sangat Baik"
            elif nilai >= 60:
                kategori = "Baik"
            elif nilai >= 40:
                kategori = "Cukup"
            else:
                kategori = "Perlu belajar lagi"

        daftar_nama += [nama]
        daftar_kelas_siswa += [kelas]
        daftar_ikut += [ikut]
        daftar_nilai += [nilai]
        daftar_kategori += [kategori]
        jumlah += 1

        if kelas not in daftar_kelas:
            daftar_kelas += [kelas]

        lanjut = input("masih mau input data? (ya/tidak): ")

    
    print("\n========== DATA NILAI SISWA ==========")
    for kelas in daftar_kelas:
        print(f"\n=== Kelas {kelas} ===")
        for i in range(jumlah):
            if daftar_kelas_siswa[i] == kelas:
                print(f"Nama siswa   : {daftar_nama[i]}")
                print(f"Kelas        : {daftar_kelas_siswa[i]}")
                print(f"Ikut ujian   : {daftar_ikut[i]}")
                print(f"Nilai        : {daftar_nilai[i]}")
                print(f"Kategori     : {daftar_kategori[i]}")
                print("")