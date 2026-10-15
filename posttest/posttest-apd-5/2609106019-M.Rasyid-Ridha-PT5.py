import os

perintah_clear = "cls" if os.name == "nt" else "clear"

data_admin = [["Hobarrt", "Hobarrt270326", "Administrator"]]
data_teknisi = [["Worker", "1234", "Koordinator Worker"]]
data_customer = [["Rasyid", "270326", "Rasyid Ridha"]]
data_layanan = [
    ["L1", "Ganti Layar", 500000],
    ["L2", "Ganti Baterai", 250000],
    ["L3", "Servis Software", 100000],
    ["L4", "Ganti Keyboard", 200000],
    ["L5", "Ganti Touchpad", 500000],
    ["L6", "Ganti Speaker", 1000000],
    ["L7", "Ganti Kamera", 750000],
    ["L8", "Servis Engsel", 2000000],
    ["L9", "Servis port USB & HDMI", 5000000],
    ["L10", "Servis Motherboard", 10000000],
    ["L11", "Ganti RAM", 1500000]
]
data_servis = []
jam_operasional = ["08:00", "17:00"]

nomor_servis = 1
nomor_layanan = 12

program_jalan = True

while program_jalan == True:
    os.system(perintah_clear)
    print("=====================================")
    print("      SISTEM SERVIS PERANGKAT")
    print("=====================================")
    print("Jam operasional:", jam_operasional[0], "-", jam_operasional[1])
    print("")
    print("1. Login")
    print("2. Daftar sebagai Customer")
    print("0. Keluar")
    pilihan_awal = input("Pilih menu: ")

    if pilihan_awal == "2":
        os.system(perintah_clear)
        print("=== DAFTAR CUSTOMER ===")
        username_baru = input("Username : ")
        while username_baru == "":
            print("Username tidak boleh kosong!")
            username_baru = input("Username : ")

        terpakai = False
        for akun in data_admin:
            if akun[0] == username_baru:
                terpakai = True
        for akun in data_teknisi:
            if akun[0] == username_baru:
                terpakai = True
        for akun in data_customer:
            if akun[0] == username_baru:
                terpakai = True

        if terpakai == True:
            print("Username sudah dipakai!")
        else:
            password_baru = input("Password : ")
            while password_baru == "":
                print("Password tidak boleh kosong!")
                password_baru = input("Password : ")
            nama_baru = input("Nama lengkap : ")
            while nama_baru == "":
                print("Nama tidak boleh kosong!")
                nama_baru = input("Nama lengkap : ")
            data_customer.append([username_baru, password_baru, nama_baru])
            print("Pendaftaran berhasil, silakan login.")
        input("Tekan Enter untuk melanjutkan...")

    elif pilihan_awal == "1":
        os.system(perintah_clear)
        print("=== LOGIN ===")
        username_input = input("Username : ")
        password_input = input("Password : ")

        role = ""
        nama_login = ""
        username_login = ""

        for akun in data_admin:
            if akun[0] == username_input and akun[1] == password_input:
                role = "admin"
                nama_login = akun[2]
                username_login = akun[0]
        for akun in data_teknisi:
            if akun[0] == username_input and akun[1] == password_input:
                role = "teknisi"
                nama_login = akun[2]
                username_login = akun[0]
        for akun in data_customer:
            if akun[0] == username_input and akun[1] == password_input:
                role = "customer"
                nama_login = akun[2]
                username_login = akun[0]

        if role == "":
            print("Username atau password salah!")
            input("Tekan Enter untuk melanjutkan...")
        else:
            login_aktif = True

            while login_aktif == True:
                os.system(perintah_clear)

                if role == "admin":
                    print("=== MENU ADMIN ===")
                    print("Selamat datang,", nama_login)
                    print("1. Lihat semua customer")
                    print("2. Lihat semua teknisi")
                    print("3. Lihat semua data servis")
                    print("4. Kelola teknisi (tambah/ubah/hapus)")
                    print("5. Kelola layanan (tambah/ubah/hapus)")
                    print("6. Ubah jam operasional")
                    print("7. Penugasan servis")
                    print("0. Logout")
                    pilihan = input("Pilih menu: ")

                    if pilihan == "1":
                        os.system(perintah_clear)
                        print("=== DAFTAR CUSTOMER ===")
                        if data_customer == []:
                            print("Data customer masih kosong.")
                        else:
                            for customer in data_customer:
                                print("-------------------------------------")
                                print(f"Username : {customer[0]}")
                                print(f"Nama     : {customer[2]}")
                        input("Tekan Enter untuk melanjutkan...")
                    elif pilihan == "2":
                        os.system(perintah_clear)
                        print("=== DAFTAR TEKNISI ===")
                        if data_teknisi == []:
                            print("Data teknisi masih kosong.")
                        else:
                            for teknisi in data_teknisi:
                                print("-------------------------------------")
                                print(f"Username : {teknisi[0]}")
                                print(f"Nama     : {teknisi[2]}")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "3":
                        os.system(perintah_clear)
                        print("=== SEMUA DATA SERVIS ===")
                        if data_servis == []:
                            print("Data servis masih kosong.")
                        else:
                            for servis in data_servis:
                                print("-------------------------------------")
                                print(f"ID Servis : {servis[0]}")
                                print(f"Customer  : {servis[1]}")
                                print(f"Perangkat : {servis[2]}")
                                print(f"Keluhan   : {servis[3]}")
                                print(f"Layanan   : {servis[6]}")
                                print(f"Status    : {servis[4]}")
                                print(f"Teknisi   : {servis[5]}")
                                print(f"Biaya     : Rp{servis[7]}")
                                print(f"Catatan   : {servis[8]}")
                                print(f"Alasan batal: {servis[9]}")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "4":
                        os.system(perintah_clear)
                        print("=== KELOLA TEKNISI ===")
                        print("1. Tambah teknisi")
                        print("2. Ubah data teknisi")
                        print("3. Hapus teknisi")
                        print("0. Kembali")
                        sub = input("Pilih menu: ")

                        if sub == "1":
                            username_baru = input("Username teknisi : ")
                            while username_baru == "":
                                print("Username tidak boleh kosong!")
                                username_baru = input("Username teknisi : ")

                            terpakai = False
                            for akun in data_admin:
                                if akun[0] == username_baru:
                                    terpakai = True
                            for akun in data_teknisi:
                                if akun[0] == username_baru:
                                    terpakai = True
                            for akun in data_customer:
                                if akun[0] == username_baru:
                                    terpakai = True

                            if terpakai == True:
                                print("Username sudah dipakai!")
                            else:
                                password_baru = input("Password : ")
                                while password_baru == "":
                                    print("Password tidak boleh kosong!")
                                    password_baru = input("Password : ")
                                nama_baru = input("Nama teknisi : ")
                                while nama_baru == "":
                                    print("Nama tidak boleh kosong!")
                                    nama_baru = input("Nama teknisi : ")
                                data_teknisi.append([username_baru, password_baru, nama_baru])
                                print("Teknisi berhasil ditambahkan.")
                            input("Tekan Enter untuk melanjutkan...")

                        elif sub == "2":
                            username_cari = input("Masukkan username teknisi: ")
                            ditemukan = False
                            for teknisi in data_teknisi:
                                if teknisi[0] == username_cari:
                                    ditemukan = True
                                    print("1. Ubah nama")
                                    print("2. Ubah password")
                                    pilihan_ubah = input("Pilih data yang diubah: ")

                                    if pilihan_ubah == "1":
                                        nama_baru = input("Nama baru : ")
                                        while nama_baru == "":
                                            print("Nama tidak boleh kosong!")
                                            nama_baru = input("Nama baru : ")
                                        nama_lama = teknisi[2]
                                        teknisi[2] = nama_baru
                                        for servis in data_servis:
                                            if servis[5] == nama_lama:
                                                servis[5] = nama_baru
                                        print("Nama teknisi berhasil diubah.")
                                    elif pilihan_ubah == "2":
                                        password_baru = input("Password baru : ")
                                        while password_baru == "":
                                            print("Password tidak boleh kosong!")
                                            password_baru = input("Password baru : ")
                                        teknisi[1] = password_baru
                                        print("Password teknisi berhasil diubah.")
                                    else:
                                        print("Pilihan tidak valid!")
                            if ditemukan == False:
                                print("Teknisi tidak ditemukan.")
                            input("Tekan Enter untuk melanjutkan...")

                        elif sub == "3":
                            username_cari = input("Masukkan username teknisi yang dihapus: ")
                            ditemukan = False
                            indeks_hapus = -1
                            indeks = 0
                            for teknisi in data_teknisi:
                                if teknisi[0] == username_cari:
                                    ditemukan = True
                                    indeks_hapus = indeks
                                    nama_hapus = teknisi[2]
                                indeks += 1

                            if ditemukan == False:
                                print("Teknisi tidak ditemukan.")
                            else:
                                masih_bertugas = False
                                for servis in data_servis:
                                    if servis[5] == nama_hapus and (servis[4] == "Diambil" or servis[4] == "Diproses"):
                                        masih_bertugas = True
                                if masih_bertugas == True:
                                    print("Teknisi masih memiliki job aktif, tidak bisa dihapus!")
                                else:
                                    del data_teknisi[indeks_hapus]
                                    print("Teknisi berhasil dihapus.")
                            input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "5":
                        os.system(perintah_clear)
                        print("=== KELOLA LAYANAN ===")
                        if data_layanan == []:
                            print("(Belum ada layanan)")
                        else:
                            for layanan in data_layanan:
                                print(f"{layanan[0]} | {layanan[1]} | Rp{layanan[2]}")
                        print("")
                        print("1. Tambah layanan")
                        print("2. Ubah layanan")
                        print("3. Hapus layanan")
                        print("0. Kembali")
                        sub = input("Pilih menu: ")

                        if sub == "1":
                            nama_baru = input("Nama layanan : ")
                            while nama_baru == "":
                                print("Nama layanan tidak boleh kosong!")
                                nama_baru = input("Nama layanan : ")

                            teks = input("Harga layanan (angka) : ")
                            valid = False
                            while valid == False:
                                valid = True
                                if teks == "":
                                    valid = False
                                for karakter in teks:
                                    if karakter < "0" or karakter > "9":
                                        valid = False
                                if valid == False:
                                    print("Harga harus berupa angka (tanpa titik/koma/spasi)!")
                                    teks = input("Harga layanan (angka) : ")
                            harga_baru = int(teks)

                            id_baru = "L" + str(nomor_layanan)
                            nomor_layanan += 1
                            data_layanan.append([id_baru, nama_baru, harga_baru])
                            print("Layanan berhasil ditambahkan dengan ID", id_baru)
                            input("Tekan Enter untuk melanjutkan...")

                        elif sub == "2":
                            id_cari = input("Masukkan ID layanan: ")
                            ditemukan = False
                            for layanan in data_layanan:
                                if layanan[0] == id_cari:
                                    ditemukan = True
                                    print("1. Ubah nama layanan")
                                    print("2. Ubah harga layanan")
                                    pilihan_ubah = input("Pilih data yang diubah: ")

                                    if pilihan_ubah == "1":
                                        nama_baru = input("Nama baru : ")
                                        while nama_baru == "":
                                            print("Nama tidak boleh kosong!")
                                            nama_baru = input("Nama baru : ")
                                        nama_lama = layanan[1]
                                        layanan[1] = nama_baru
                                        for servis in data_servis:
                                            if servis[6] == nama_lama:
                                                servis[6] = nama_baru
                                        print("Nama layanan berhasil diubah.")
                                    elif pilihan_ubah == "2":
                                        teks = input("Harga baru (angka) : ")
                                        valid = False
                                        while valid == False:
                                            valid = True
                                            if teks == "":
                                                valid = False
                                            for karakter in teks:
                                                if karakter < "0" or karakter > "9":
                                                    valid = False
                                            if valid == False:
                                                print("Harga harus berupa angka (tanpa titik/koma/spasi)!")
                                                teks = input("Harga baru (angka) : ")
                                        layanan[2] = int(teks)
                                        print("Harga layanan berhasil diubah.")
                                    else:
                                        print("Pilihan tidak valid!")
                            if ditemukan == False:
                                print("Layanan tidak ditemukan.")
                            input("Tekan Enter untuk melanjutkan...")

                        elif sub == "3":
                            id_cari = input("Masukkan ID layanan yang dihapus: ")
                            ditemukan = False
                            indeks_hapus = -1
                            indeks = 0
                            for layanan in data_layanan:
                                if layanan[0] == id_cari:
                                    ditemukan = True
                                    indeks_hapus = indeks
                                    nama_hapus = layanan[1]
                                indeks += 1

                            if ditemukan == False:
                                print("Layanan tidak ditemukan.")
                            else:
                                sedang_dipakai = False
                                for servis in data_servis:
                                    if servis[6] == nama_hapus and (servis[4] == "Menunggu" or servis[4] == "Diambil" or servis[4] == "Diproses"):
                                        sedang_dipakai = True
                                if sedang_dipakai == True:
                                    print("Layanan masih dipakai oleh servis yang berjalan, tidak bisa dihapus!")
                                else:
                                    del data_layanan[indeks_hapus]
                                    print("Layanan berhasil dihapus.")
                            input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "6":
                        os.system(perintah_clear)
                        print("=== UBAH JAM OPERASIONAL ===")
                        print("Jam saat ini:", jam_operasional[0], "-", jam_operasional[1])
                        print("Format jam: HH:MM (contoh 08:00)")

                        jam_buka = input("Jam buka baru  : ")
                        valid = False
                        while valid == False:
                            valid = True
                            if jam_buka[2:3] != ":" or jam_buka[0:2] == "" or jam_buka[3:5] == "" or jam_buka[5:] != "":
                                valid = False
                            for karakter in jam_buka[0:2] + jam_buka[3:5]:
                                if karakter < "0" or karakter > "9":
                                    valid = False
                            if valid == False:
                                print("Format jam salah! Gunakan HH:MM")
                                jam_buka = input("Jam buka baru  : ")

                        jam_tutup = input("Jam tutup baru : ")
                        valid = False
                        while valid == False:
                            valid = True
                            if jam_tutup[2:3] != ":" or jam_tutup[0:2] == "" or jam_tutup[3:5] == "" or jam_tutup[5:] != "":
                                valid = False
                            for karakter in jam_tutup[0:2] + jam_tutup[3:5]:
                                if karakter < "0" or karakter > "9":
                                    valid = False
                            if valid == False:
                                print("Format jam salah! Gunakan HH:MM")
                                jam_tutup = input("Jam tutup baru : ")

                        jam_operasional[0] = jam_buka
                        jam_operasional[1] = jam_tutup
                        print("Jam operasional berhasil diubah.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "7":
                        os.system(perintah_clear)
                        print("=== PENUGASAN SERVIS ===")
                        if data_servis == []:
                            print("Data servis masih kosong.")
                        else:
                            for servis in data_servis:
                                if servis[4] == "Menunggu" or servis[4] == "Diambil":
                                    print(f"{servis[0]} | {servis[2]} | {servis[4]} | Teknisi: {servis[5]}")
                            print("")
                            id_servis = input("Masukkan ID servis: ")
                            ditemukan = False
                            for servis in data_servis:
                                if servis[0] == id_servis:
                                    ditemukan = True
                                    if servis[4] == "Menunggu" or servis[4] == "Diambil":
                                        print("")
                                        print("Daftar teknisi:")
                                        for teknisi in data_teknisi:
                                            print(f"{teknisi[0]} | {teknisi[2]}")
                                        username_cari = input("Masukkan username teknisi: ")
                                        teknisi_ada = False
                                        for teknisi in data_teknisi:
                                            if teknisi[0] == username_cari:
                                                teknisi_ada = True
                                                servis[5] = teknisi[2]
                                                servis[4] = "Diambil"
                                                print("Servis berhasil ditugaskan ke", teknisi[2])
                                        if teknisi_ada == False:
                                            print("Teknisi tidak ditemukan.")
                                    else:
                                        print("Servis sudah berjalan/selesai, tidak bisa ditugaskan ulang.")
                            if ditemukan == False:
                                print("ID servis tidak ditemukan.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "0":
                        login_aktif = False

                    else:
                        print("Pilihan tidak valid!")
                        input("Tekan Enter untuk melanjutkan...")

                elif role == "teknisi":
                    print("=== MENU TEKNISI ===")
                    print("Selamat datang,", nama_login)
                    print("1. Lihat job tersedia")
                    print("2. Lihat job saya")
                    print("3. Ambil job")
                    print("4. Ubah status job")
                    print("5. Isi biaya & catatan servis")
                    print("6. Batalkan pengerjaan")
                    print("0. Logout")
                    pilihan = input("Pilih menu: ")

                    if pilihan == "1":
                        os.system(perintah_clear)
                        print("=== JOB TERSEDIA ===")
                        ditemukan = False
                        for servis in data_servis:
                            if servis[4] == "Menunggu":
                                ditemukan = True
                                print("-------------------------------------")
                                print(f"ID Servis : {servis[0]}")
                                print(f"Perangkat : {servis[2]}")
                                print(f"Keluhan   : {servis[3]}")
                                print(f"Layanan   : {servis[6]}")
                                print(f"Alasan batal sebelumnya: {servis[9]}")
                        if ditemukan == False:
                            print("Belum ada job yang tersedia.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "2":
                        os.system(perintah_clear)
                        print("=== JOB SAYA ===")
                        ditemukan = False
                        for servis in data_servis:
                            if servis[5] == nama_login:
                                ditemukan = True
                                print("-------------------------------------")
                                print(f"ID Servis : {servis[0]}")
                                print(f"Perangkat : {servis[2]}")
                                print(f"Keluhan   : {servis[3]}")
                                print(f"Layanan   : {servis[6]}")
                                print(f"Status    : {servis[4]}")
                                print(f"Biaya     : Rp{servis[7]}")
                                print(f"Catatan   : {servis[8]}")
                        if ditemukan == False:
                            print("Kamu belum memiliki job.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "3":
                        os.system(perintah_clear)
                        print("=== AMBIL JOB ===")
                        id_servis = input("Masukkan ID servis: ")
                        ditemukan = False

                        for servis in data_servis:
                            if servis[0] == id_servis:
                                ditemukan = True

                                if servis[4] == "Menunggu":
                                    servis[4] = "Diambil"
                                    servis[5] = nama_login
                                    print("Job berhasil diambil")
                                else:
                                    print("Job tidak tersedia")

                        if ditemukan == False:
                            print("ID servis tidak ditemukan")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "4":
                        os.system(perintah_clear)
                        print("=== UBAH STATUS JOB ===")
                        id_servis = input("Masukkan ID servis: ")
                        ditemukan = False

                        for servis in data_servis:
                            if servis[0] == id_servis and servis[5] == nama_login:
                                ditemukan = True
                                print("Status saat ini:", servis[4])

                                if servis[4] == "Diambil":
                                    servis[4] = "Diproses"
                                    print("Status diubah menjadi Diproses")
                                elif servis[4] == "Diproses":
                                    if servis[7] == 0:
                                        print("Isi biaya servis dulu (menu 5) sebelum menyelesaikan job!")
                                    else:
                                        servis[4] = "Selesai"
                                        print("Status diubah menjadi Selesai")
                                else:
                                    print("Status job ini tidak dapat diubah lagi.")

                        if ditemukan == False:
                            print("Job tidak ditemukan atau bukan milik kamu.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "5":
                        os.system(perintah_clear)
                        print("=== ISI BIAYA & CATATAN ===")
                        id_servis = input("Masukkan ID servis: ")
                        ditemukan = False

                        for servis in data_servis:
                            if servis[0] == id_servis and servis[5] == nama_login:
                                ditemukan = True

                                if servis[4] == "Diambil" or servis[4] == "Diproses":
                                    teks = input("Biaya servis (angka) : ")
                                    valid = False
                                    while valid == False:
                                        valid = True
                                        if teks == "":
                                            valid = False
                                        for karakter in teks:
                                            if karakter < "0" or karakter > "9":
                                                valid = False
                                        if valid == False:
                                            print("Biaya harus berupa angka (tanpa titik/koma/spasi)!")
                                            teks = input("Biaya servis (angka) : ")

                                    catatan_baru = input("Catatan servis : ")
                                    while catatan_baru == "":
                                        print("Catatan tidak boleh kosong!")
                                        catatan_baru = input("Catatan servis : ")

                                    servis[7] = int(teks)
                                    servis[8] = catatan_baru
                                    print("Biaya dan catatan berhasil disimpan.")
                                else:
                                    print("Biaya/catatan hanya bisa diisi saat status Diambil atau Diproses.")

                        if ditemukan == False:
                            print("Job tidak ditemukan atau bukan milik kamu.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "6":
                        os.system(perintah_clear)
                        print("=== BATALKAN PENGERJAAN ===")
                        id_servis = input("Masukkan ID servis: ")
                        ditemukan = False

                        for servis in data_servis:
                            if servis[0] == id_servis and servis[5] == nama_login:
                                ditemukan = True

                                if servis[4] == "Diambil" or servis[4] == "Diproses":
                                    alasan = input("Alasan pembatalan : ")
                                    while alasan == "":
                                        print("Alasan tidak boleh kosong!")
                                        alasan = input("Alasan pembatalan : ")

                                    servis[4] = "Menunggu"
                                    servis[5] = "-"
                                    servis[7] = 0
                                    servis[8] = "-"
                                    servis[9] = alasan
                                    print("Pengerjaan dibatalkan, job kembali ke daftar tersedia.")
                                else:
                                    print("Job ini tidak dapat dibatalkan.")

                        if ditemukan == False:
                            print("Job tidak ditemukan atau bukan milik kamu.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "0":
                        login_aktif = False

                    else:
                        print("Pilihan tidak valid!")
                        input("Tekan Enter untuk melanjutkan...")


                else:
                    print("=== MENU CUSTOMER ===")
                    print("Selamat datang,", nama_login)
                    print("Jam operasional:", jam_operasional[0], "-", jam_operasional[1])
                    print("1. Ajukan servis")
                    print("2. Lihat servis saya")
                    print("3. Ubah pengajuan servis")
                    print("4. Hapus pengajuan servis")
                    print("0. Logout")
                    pilihan = input("Pilih menu: ")

                    if pilihan == "1":
                        os.system(perintah_clear)
                        print("=== AJUKAN SERVIS ===")
                        if data_layanan == []:
                            print("Belum ada layanan tersedia, hubungi admin.")
                        else:
                            perangkat = input("Nama perangkat : ")
                            while perangkat == "":
                                print("Perangkat tidak boleh kosong!")
                                perangkat = input("Nama perangkat : ")

                            keluhan = input("Keluhan        : ")
                            while keluhan == "":
                                print("Keluhan tidak boleh kosong!")
                                keluhan = input("Keluhan        : ")

                            print("")
                            print("Daftar layanan:")
                            for layanan in data_layanan:
                                print(f"{layanan[0]} | {layanan[1]} | Rp{layanan[2]}")

                            nama_layanan = ""
                            while nama_layanan == "":
                                id_layanan = input("Masukkan ID layanan (0 = batal): ")
                                if id_layanan == "0":
                                    break
                                for layanan in data_layanan:
                                    if layanan[0] == id_layanan:
                                        nama_layanan = layanan[1]
                                if nama_layanan == "":
                                    print("ID layanan tidak ditemukan!")

                            if nama_layanan != "":
                                id_baru = "SRV" + str(nomor_servis)
                                nomor_servis += 1
                                data_servis.append([id_baru, username_login, perangkat, keluhan, "Menunggu", "-", nama_layanan, 0, "-", "-"])
                                print("Pengajuan berhasil! ID servis kamu:", id_baru)
                            else:
                                print("Pengajuan dibatalkan.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "2":
                        os.system(perintah_clear)
                        print("=== SERVIS SAYA ===")
                        ditemukan = False
                        for servis in data_servis:
                            if servis[1] == username_login:
                                ditemukan = True
                                print("-------------------------------------")
                                print(f"ID Servis : {servis[0]}")
                                print(f"Perangkat : {servis[2]}")
                                print(f"Keluhan   : {servis[3]}")
                                print(f"Layanan   : {servis[6]}")
                                print(f"Status    : {servis[4]}")
                                print(f"Teknisi   : {servis[5]}")
                                print(f"Biaya     : Rp{servis[7]}")
                                print(f"Catatan   : {servis[8]}")
                        if ditemukan == False:
                            print("Data servis masih kosong.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "3":
                        os.system(perintah_clear)
                        print("=== UBAH PENGAJUAN SERVIS ===")
                        id_servis = input("Masukkan ID servis: ")
                        ditemukan = False

                        for servis in data_servis:
                            if servis[0] == id_servis and servis[1] == username_login:
                                ditemukan = True

                                if servis[4] == "Menunggu":
                                    print("1. Ubah perangkat")
                                    print("2. Ubah keluhan")
                                    print("3. Ubah layanan")
                                    pilihan_ubah = input("Pilih data yang diubah: ")

                                    if pilihan_ubah == "1":
                                        perangkat_baru = input("Perangkat baru : ")
                                        while perangkat_baru == "":
                                            print("Perangkat tidak boleh kosong!")
                                            perangkat_baru = input("Perangkat baru : ")
                                        servis[2] = perangkat_baru
                                        print("Perangkat berhasil diubah.")
                                    elif pilihan_ubah == "2":
                                        keluhan_baru = input("Keluhan baru : ")
                                        while keluhan_baru == "":
                                            print("Keluhan tidak boleh kosong!")
                                            keluhan_baru = input("Keluhan baru : ")
                                        servis[3] = keluhan_baru
                                        print("Keluhan berhasil diubah.")
                                    elif pilihan_ubah == "3":
                                        for layanan in data_layanan:
                                            print(f"{layanan[0]} | {layanan[1]} | Rp{layanan[2]}")
                                        id_layanan = input("Masukkan ID layanan baru: ")
                                        layanan_ada = False
                                        for layanan in data_layanan:
                                            if layanan[0] == id_layanan:
                                                layanan_ada = True
                                                servis[6] = layanan[1]
                                                print("Layanan berhasil diubah.")
                                        if layanan_ada == False:
                                            print("ID layanan tidak ditemukan.")
                                    else:
                                        print("Pilihan tidak valid!")
                                else:
                                    print("Pengajuan sudah diproses, tidak bisa diubah.")

                        if ditemukan == False:
                            print("ID servis tidak ditemukan.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "4":
                        os.system(perintah_clear)
                        print("=== HAPUS PENGAJUAN SERVIS ===")
                        id_servis = input("Masukkan ID servis yang ingin dihapus: ")
                        ditemukan = False
                        indeks_hapus = -1
                        status_hapus = ""
                        indeks = 0

                        for servis in data_servis:
                            if servis[0] == id_servis and servis[1] == username_login:
                                ditemukan = True
                                indeks_hapus = indeks
                                status_hapus = servis[4]
                            indeks += 1

                        if ditemukan == False:
                            print("ID servis tidak ditemukan.")
                        elif status_hapus == "Menunggu":
                            del data_servis[indeks_hapus]
                            print("Pengajuan servis berhasil dihapus.")
                        else:
                            print("Pengajuan sudah diproses, tidak bisa dihapus.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "0":
                        login_aktif = False

                    else:
                        print("Pilihan tidak valid!")
                        input("Tekan Enter untuk melanjutkan...")

    
    elif pilihan_awal == "0":
        program_jalan = False
        print("Terima kasih, program selesai.")

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk melanjutkan...")