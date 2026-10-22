import os
perintah_clear = "cls" if os.name == "nt" else "clear"

data_akun = {
    "Hobarrt": {"password": "Hobarrt270326", "nama": "Administrator", "role": "admin"},
    "Worker": {"password": "1234", "nama": "Koordinator Worker", "role": "teknisi"},
    "Rasyid": {"password": "270326", "nama": "Rasyid Ridha", "role": "customer"}
}

data_layanan = {
    "L1": {"nama": "Ganti Layar", "harga": 500000},
    "L2": {"nama": "Ganti Baterai", "harga": 250000},
    "L3": {"nama": "Servis Software", "harga": 100000},
    "L4": {"nama": "Ganti Keyboard", "harga": 200000},
    "L5": {"nama": "Ganti Touchpad", "harga": 500000},
    "L6": {"nama": "Ganti Speaker", "harga": 1000000},
    "L7": {"nama": "Ganti Kamera", "harga": 750000},
    "L8": {"nama": "Servis Engsel", "harga": 2000000},
    "L9": {"nama": "Servis port USB & HDMI", "harga": 5000000},
    "L10": {"nama": "Servis Motherboard", "harga": 10000000},
    "L11": {"nama": "Ganti RAM", "harga": 1500000}
}

data_servis = {}

jam_operasional = {"buka": "08:00", "tutup": "17:00"}

nomor_servis = 1
nomor_layanan = 12

program_jalan = True

while program_jalan == True:
    os.system(perintah_clear)
    print("=====================================")
    print("      SISTEM SERVIS PERANGKAT")
    print("=====================================")
    print("Jam operasional:", jam_operasional["buka"], "-", jam_operasional["tutup"])
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

        if data_akun.get(username_baru) != None:
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

            data_akun[username_baru] = {"password": password_baru, "nama": nama_baru, "role": "customer"}
            print("Pendaftaran berhasil, silakan login.")
        input("Tekan Enter untuk melanjutkan...")

    elif pilihan_awal == "1":
        os.system(perintah_clear)
        print("=== LOGIN ===")
        username_input = input("Username : ")
        password_input = input("Password : ")

        akun_login = data_akun.get(username_input)
        login_berhasil = False
        if akun_login != None:
            if akun_login["password"] == password_input:
                login_berhasil = True

        if login_berhasil == False:
            print("Username atau password salah!")
            input("Tekan Enter untuk melanjutkan...")
        else:
            role = akun_login["role"]
            nama_login = akun_login["nama"]
            username_login = username_input
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
                        jumlah = 0
                        for username, akun in data_akun.items():
                            if akun["role"] == "customer":
                                jumlah += 1
                                print("-------------------------------------")
                                print(f"Username : {username}")
                                print(f"Nama     : {akun['nama']}")
                        if jumlah == 0:
                            print("Data customer masih kosong.")
                        else:
                            print("-------------------------------------")
                            print("Total customer:", jumlah)
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "2":
                        os.system(perintah_clear)
                        print("=== DAFTAR TEKNISI ===")
                        jumlah = 0
                        for username, akun in data_akun.items():
                            if akun["role"] == "teknisi":
                                jumlah += 1
                                print("-------------------------------------")
                                print(f"Username : {username}")
                                print(f"Nama     : {akun['nama']}")
                        if jumlah == 0:
                            print("Data teknisi masih kosong.")
                        else:
                            print("-------------------------------------")
                            print("Total teknisi:", jumlah)
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "3":
                        os.system(perintah_clear)
                        print("=== SEMUA DATA SERVIS ===")
                        if len(data_servis) == 0:
                            print("Data servis masih kosong.")
                        else:
                            for id_servis, servis in data_servis.items():
                                print("-------------------------------------")
                                print(f"ID Servis    : {id_servis}")
                                print(f"Customer     : {servis['customer']}")
                                print(f"Perangkat    : {servis['perangkat']}")
                                print(f"Keluhan      : {servis['keluhan']}")
                                print(f"Layanan      : {servis['layanan']}")
                                print(f"Status       : {servis['status']}")
                                print(f"Teknisi      : {servis['teknisi']}")
                                print(f"Biaya        : Rp{servis['biaya']}")
                                print(f"Catatan      : {servis['catatan']}")
                                print(f"Alasan batal : {servis['alasan_batal']}")
                            print("-------------------------------------")
                            print("Total servis:", len(data_servis))
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

                            if data_akun.get(username_baru) != None:
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

                                data_akun[username_baru] = {"password": password_baru, "nama": nama_baru, "role": "teknisi"}
                                print("Teknisi berhasil ditambahkan.")
                            input("Tekan Enter untuk melanjutkan...")

                        elif sub == "2":
                            username_cari = input("Masukkan username teknisi: ")
                            teknisi = data_akun.get(username_cari)

                            if teknisi == None:
                                print("Teknisi tidak ditemukan.")
                            elif teknisi["role"] != "teknisi":
                                print("Teknisi tidak ditemukan.")
                            else:
                                print("1. Ubah nama")
                                print("2. Ubah password")
                                pilihan_ubah = input("Pilih data yang diubah: ")

                                if pilihan_ubah == "1":
                                    nama_baru = input("Nama baru : ")
                                    while nama_baru == "":
                                        print("Nama tidak boleh kosong!")
                                        nama_baru = input("Nama baru : ")
                                    teknisi["nama"] = nama_baru
                                    print("Nama teknisi berhasil diubah.")
                                elif pilihan_ubah == "2":
                                    password_baru = input("Password baru : ")
                                    while password_baru == "":
                                        print("Password tidak boleh kosong!")
                                        password_baru = input("Password baru : ")
                                    teknisi["password"] = password_baru
                                    print("Password teknisi berhasil diubah.")
                                else:
                                    print("Pilihan tidak valid!")
                            input("Tekan Enter untuk melanjutkan...")

                        elif sub == "3":
                            username_cari = input("Masukkan username teknisi yang dihapus: ")
                            teknisi = data_akun.get(username_cari)

                            if teknisi == None:
                                print("Teknisi tidak ditemukan.")
                            elif teknisi["role"] != "teknisi":
                                print("Teknisi tidak ditemukan.")
                            else:
                                masih_bertugas = False
                                for servis in data_servis.values():
                                    if servis["teknisi"] == username_cari and (servis["status"] == "Diambil" or servis["status"] == "Diproses"):
                                        masih_bertugas = True

                                if masih_bertugas == True:
                                    print("Teknisi masih memiliki job aktif, tidak bisa dihapus!")
                                else:
                                    del data_akun[username_cari]
                                    print("Teknisi berhasil dihapus.")
                            input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "5":
                        os.system(perintah_clear)
                        print("=== KELOLA LAYANAN ===")
                        if len(data_layanan) == 0:
                            print("(Belum ada layanan)")
                        else:
                            for id_layanan, layanan in data_layanan.items():
                                print(f"{id_layanan} | {layanan['nama']} | Rp{layanan['harga']}")
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
                                if valid == True:
                                    if int(teks) == 0:
                                        valid = False
                                if valid == False:
                                    print("Harga harus angka lebih dari 0 (tanpa titik/koma/spasi)!")
                                    teks = input("Harga layanan (angka) : ")

                            id_baru = "L" + str(nomor_layanan)
                            nomor_layanan += 1
                            data_layanan[id_baru] = {"nama": nama_baru, "harga": int(teks)}
                            print("Layanan berhasil ditambahkan dengan ID", id_baru)
                            input("Tekan Enter untuk melanjutkan...")

                        elif sub == "2":
                            id_cari = input("Masukkan ID layanan: ")
                            layanan = data_layanan.get(id_cari)

                            if layanan == None:
                                print("Layanan tidak ditemukan.")
                            else:
                                print("1. Ubah nama layanan")
                                print("2. Ubah harga layanan")
                                pilihan_ubah = input("Pilih data yang diubah: ")

                                if pilihan_ubah == "1":
                                    nama_baru = input("Nama baru : ")
                                    while nama_baru == "":
                                        print("Nama tidak boleh kosong!")
                                        nama_baru = input("Nama baru : ")
                                    nama_lama = layanan["nama"]
                                    layanan["nama"] = nama_baru
                                    for servis in data_servis.values():
                                        if servis["layanan"] == nama_lama:
                                            servis["layanan"] = nama_baru
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
                                        if valid == True:
                                            if int(teks) == 0:
                                                valid = False
                                        if valid == False:
                                            print("Harga harus angka lebih dari 0 (tanpa titik/koma/spasi)!")
                                            teks = input("Harga baru (angka) : ")
                                    layanan["harga"] = int(teks)
                                    print("Harga layanan berhasil diubah.")
                                else:
                                    print("Pilihan tidak valid!")
                            input("Tekan Enter untuk melanjutkan...")

                        elif sub == "3":
                            id_cari = input("Masukkan ID layanan yang dihapus: ")
                            layanan = data_layanan.get(id_cari)

                            if layanan == None:
                                print("Layanan tidak ditemukan.")
                            else:
                                sedang_dipakai = False
                                for servis in data_servis.values():
                                    if servis["layanan"] == layanan["nama"] and (servis["status"] == "Menunggu" or servis["status"] == "Diambil" or servis["status"] == "Diproses"):
                                        sedang_dipakai = True

                                if sedang_dipakai == True:
                                    print("Layanan masih dipakai oleh servis yang berjalan, tidak bisa dihapus!")
                                else:
                                    del data_layanan[id_cari]
                                    print("Layanan berhasil dihapus.")
                            input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "6":
                        os.system(perintah_clear)
                        print("=== UBAH JAM OPERASIONAL ===")
                        print("Jam saat ini:", jam_operasional["buka"], "-", jam_operasional["tutup"])
                        print("Format jam: HH:MM (contoh 08:00)")

                        jam_buka = input("Jam buka baru  : ")
                        valid = False
                        while valid == False:
                            valid = True
                            if len(jam_buka) != 5:
                                valid = False
                            else:
                                if jam_buka[2] != ":":
                                    valid = False
                                for karakter in jam_buka[0:2] + jam_buka[3:5]:
                                    if karakter < "0" or karakter > "9":
                                        valid = False
                                if valid == True:
                                    if int(jam_buka[0:2]) > 23 or int(jam_buka[3:5]) > 59:
                                        valid = False
                            if valid == False:
                                print("Format jam salah! Gunakan HH:MM (00:00 - 23:59)")
                                jam_buka = input("Jam buka baru  : ")

                        jam_tutup = input("Jam tutup baru : ")
                        valid = False
                        while valid == False:
                            valid = True
                            if len(jam_tutup) != 5:
                                valid = False
                            else:
                                if jam_tutup[2] != ":":
                                    valid = False
                                for karakter in jam_tutup[0:2] + jam_tutup[3:5]:
                                    if karakter < "0" or karakter > "9":
                                        valid = False
                                if valid == True:
                                    if int(jam_tutup[0:2]) > 23 or int(jam_tutup[3:5]) > 59:
                                        valid = False
                            if valid == False:
                                print("Format jam salah! Gunakan HH:MM (00:00 - 23:59)")
                                jam_tutup = input("Jam tutup baru : ")

                        if jam_tutup <= jam_buka:
                            print("Jam tutup harus lebih besar dari jam buka! Perubahan dibatalkan.")
                        else:
                            jam_operasional["buka"] = jam_buka
                            jam_operasional["tutup"] = jam_tutup
                            print("Jam operasional berhasil diubah.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "7":
                        os.system(perintah_clear)
                        print("=== PENUGASAN SERVIS ===")
                        if len(data_servis) == 0:
                            print("Data servis masih kosong.")
                        else:
                            for id_servis, servis in data_servis.items():
                                if servis["status"] == "Menunggu" or servis["status"] == "Diambil":
                                    print(f"{id_servis} | {servis['perangkat']} | {servis['status']} | Teknisi: {servis['teknisi']}")
                            print("")
                            id_servis = input("Masukkan ID servis: ")
                            servis = data_servis.get(id_servis)

                            if servis == None:
                                print("ID servis tidak ditemukan.")
                            elif servis["status"] != "Menunggu" and servis["status"] != "Diambil":
                                print("Servis sudah berjalan/selesai, tidak bisa ditugaskan ulang.")
                            else:
                                print("")
                                print("Daftar teknisi:")
                                for username, akun in data_akun.items():
                                    if akun["role"] == "teknisi":
                                        print(f"{username} | {akun['nama']}")
                                username_cari = input("Masukkan username teknisi: ")
                                teknisi = data_akun.get(username_cari)

                                if teknisi == None:
                                    print("Teknisi tidak ditemukan.")
                                elif teknisi["role"] != "teknisi":
                                    print("Teknisi tidak ditemukan.")
                                else:
                                    servis["teknisi"] = username_cari
                                    servis["status"] = "Diambil"
                                    print("Servis berhasil ditugaskan ke", teknisi["nama"])
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
                        jumlah = 0
                        for id_servis, servis in data_servis.items():
                            if servis["status"] == "Menunggu":
                                jumlah += 1
                                print("-------------------------------------")
                                print(f"ID Servis : {id_servis}")
                                print(f"Perangkat : {servis['perangkat']}")
                                print(f"Keluhan   : {servis['keluhan']}")
                                print(f"Layanan   : {servis['layanan']}")
                                print(f"Alasan batal sebelumnya: {servis['alasan_batal']}")
                        if jumlah == 0:
                            print("Belum ada job yang tersedia.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "2":
                        os.system(perintah_clear)
                        print("=== JOB SAYA ===")
                        jumlah = 0
                        for id_servis, servis in data_servis.items():
                            if servis["teknisi"] == username_login:
                                jumlah += 1
                                print("-------------------------------------")
                                print(f"ID Servis : {id_servis}")
                                print(f"Perangkat : {servis['perangkat']}")
                                print(f"Keluhan   : {servis['keluhan']}")
                                print(f"Layanan   : {servis['layanan']}")
                                print(f"Status    : {servis['status']}")
                                print(f"Biaya     : Rp{servis['biaya']}")
                                print(f"Catatan   : {servis['catatan']}")
                        if jumlah == 0:
                            print("Kamu belum memiliki job.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "3":
                        os.system(perintah_clear)
                        print("=== AMBIL JOB ===")
                        id_servis = input("Masukkan ID servis: ")
                        servis = data_servis.get(id_servis)

                        if servis == None:
                            print("ID servis tidak ditemukan")
                        elif servis["status"] == "Menunggu":
                            servis["status"] = "Diambil"
                            servis["teknisi"] = username_login
                            print("Job berhasil diambil")
                        else:
                            print("Job tidak tersedia")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "4":
                        os.system(perintah_clear)
                        print("=== UBAH STATUS JOB ===")
                        id_servis = input("Masukkan ID servis: ")
                        servis = data_servis.get(id_servis)

                        if servis == None:
                            print("ID servis tidak ditemukan.")
                        elif servis["teknisi"] != username_login:
                            print("Job ini bukan milik kamu.")
                        else:
                            print("Status saat ini:", servis["status"])

                            if servis["status"] == "Diambil":
                                servis["status"] = "Diproses"
                                print("Status diubah menjadi Diproses")
                            elif servis["status"] == "Diproses":
                                if servis["biaya"] == 0:
                                    print("Isi biaya servis dulu (menu 5) sebelum menyelesaikan job!")
                                else:
                                    servis["status"] = "Selesai"
                                    print("Status diubah menjadi Selesai")
                            else:
                                print("Status job ini tidak dapat diubah lagi.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "5":
                        os.system(perintah_clear)
                        print("=== ISI BIAYA & CATATAN ===")
                        id_servis = input("Masukkan ID servis: ")
                        servis = data_servis.get(id_servis)

                        if servis == None:
                            print("ID servis tidak ditemukan.")
                        elif servis["teknisi"] != username_login:
                            print("Job ini bukan milik kamu.")
                        elif servis["status"] != "Diambil" and servis["status"] != "Diproses":
                            print("Biaya/catatan hanya bisa diisi saat status Diambil atau Diproses.")
                        else:
                            teks = input("Biaya servis (angka) : ")
                            valid = False
                            while valid == False:
                                valid = True
                                if teks == "":
                                    valid = False
                                for karakter in teks:
                                    if karakter < "0" or karakter > "9":
                                        valid = False
                                if valid == True:
                                    if int(teks) == 0:
                                        valid = False
                                if valid == False:
                                    print("Biaya harus angka lebih dari 0 (tanpa titik/koma/spasi)!")
                                    teks = input("Biaya servis (angka) : ")

                            catatan_baru = input("Catatan servis : ")
                            while catatan_baru == "":
                                print("Catatan tidak boleh kosong!")
                                catatan_baru = input("Catatan servis : ")

                            servis["biaya"] = int(teks)
                            servis["catatan"] = catatan_baru
                            print("Biaya dan catatan berhasil disimpan.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "6":
                        os.system(perintah_clear)
                        print("=== BATALKAN PENGERJAAN ===")
                        id_servis = input("Masukkan ID servis: ")
                        servis = data_servis.get(id_servis)

                        if servis == None:
                            print("ID servis tidak ditemukan.")
                        elif servis["teknisi"] != username_login:
                            print("Job ini bukan milik kamu.")
                        elif servis["status"] != "Diambil" and servis["status"] != "Diproses":
                            print("Job ini tidak dapat dibatalkan.")
                        else:
                            alasan = input("Alasan pembatalan : ")
                            while alasan == "":
                                print("Alasan tidak boleh kosong!")
                                alasan = input("Alasan pembatalan : ")

                            servis.update({
                                "status": "Menunggu",
                                "teknisi": "-",
                                "biaya": 0,
                                "catatan": "-",
                                "alasan_batal": alasan
                            })
                            print("Pengerjaan dibatalkan, job kembali ke daftar tersedia.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "0":
                        login_aktif = False

                    else:
                        print("Pilihan tidak valid!")
                        input("Tekan Enter untuk melanjutkan...")


                else:
                    print("=== MENU CUSTOMER ===")
                    print("Selamat datang,", nama_login)
                    print("Jam operasional:", jam_operasional["buka"], "-", jam_operasional["tutup"])
                    print("1. Ajukan servis")
                    print("2. Lihat servis saya")
                    print("3. Ubah pengajuan servis")
                    print("4. Hapus pengajuan servis")
                    print("0. Logout")
                    pilihan = input("Pilih menu: ")

                    if pilihan == "1":
                        os.system(perintah_clear)
                        print("=== AJUKAN SERVIS ===")
                        if len(data_layanan) == 0:
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
                            for id_layanan, layanan in data_layanan.items():
                                print(f"{id_layanan} | {layanan['nama']} | Rp{layanan['harga']}")

                            nama_layanan = ""
                            while nama_layanan == "":
                                id_layanan = input("Masukkan ID layanan (0 = batal): ")
                                if id_layanan == "0":
                                    break
                                layanan = data_layanan.get(id_layanan)
                                if layanan == None:
                                    print("ID layanan tidak ditemukan!")
                                else:
                                    nama_layanan = layanan["nama"]

                            if nama_layanan != "":
                                id_baru = "SRV" + str(nomor_servis)
                                nomor_servis += 1
                                data_servis[id_baru] = {
                                    "customer": username_login,
                                    "perangkat": perangkat,
                                    "keluhan": keluhan,
                                    "layanan": nama_layanan,
                                    "status": "Menunggu",
                                    "teknisi": "-",
                                    "biaya": 0,
                                    "catatan": "-",
                                    "alasan_batal": "-"
                                }
                                print("Pengajuan berhasil! ID servis kamu:", id_baru)
                            else:
                                print("Pengajuan dibatalkan.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "2":
                        os.system(perintah_clear)
                        print("=== SERVIS SAYA ===")
                        jumlah = 0
                        for id_servis, servis in data_servis.items():
                            if servis["customer"] == username_login:
                                jumlah += 1
                                print("-------------------------------------")
                                print(f"ID Servis : {id_servis}")
                                print(f"Perangkat : {servis['perangkat']}")
                                print(f"Keluhan   : {servis['keluhan']}")
                                print(f"Layanan   : {servis['layanan']}")
                                print(f"Status    : {servis['status']}")
                                print(f"Teknisi   : {servis['teknisi']}")
                                print(f"Biaya     : Rp{servis['biaya']}")
                                print(f"Catatan   : {servis['catatan']}")
                        if jumlah == 0:
                            print("Data servis masih kosong.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == "3":
                        os.system(perintah_clear)
                        print("=== UBAH PENGAJUAN SERVIS ===")
                        id_servis = input("Masukkan ID servis: ")
                        servis = data_servis.get(id_servis)

                        if servis == None:
                            print("ID servis tidak ditemukan.")
                        elif servis["customer"] != username_login:
                            print("ID servis tidak ditemukan.")
                        elif servis["status"] != "Menunggu":
                            print("Pengajuan sudah diproses, tidak bisa diubah.")
                        else:
                            print("1. Ubah perangkat")
                            print("2. Ubah keluhan")
                            print("3. Ubah layanan")
                            pilihan_ubah = input("Pilih data yang diubah: ")

                            if pilihan_ubah == "1":
                                perangkat_baru = input("Perangkat baru : ")
                                while perangkat_baru == "":
                                    print("Perangkat tidak boleh kosong!")
                                    perangkat_baru = input("Perangkat baru : ")
                                servis["perangkat"] = perangkat_baru
                                print("Perangkat berhasil diubah.")
                            elif pilihan_ubah == "2":
                                keluhan_baru = input("Keluhan baru : ")
                                while keluhan_baru == "":
                                    print("Keluhan tidak boleh kosong!")
                                    keluhan_baru = input("Keluhan baru : ")
                                servis["keluhan"] = keluhan_baru
                                print("Keluhan berhasil diubah.")
                            elif pilihan_ubah == "3":
                                for id_layanan, layanan in data_layanan.items():
                                    print(f"{id_layanan} | {layanan['nama']} | Rp{layanan['harga']}")
                                id_layanan = input("Masukkan ID layanan baru: ")
                                layanan = data_layanan.get(id_layanan)
                                if layanan == None:
                                    print("ID layanan tidak ditemukan.")
                                else:
                                    servis["layanan"] = layanan["nama"]
                                    print("Layanan berhasil diubah.")
                            else:
                                print("Pilihan tidak valid!")
                        input("Tekan Enter untuk melanjutkan...")
    
                    elif pilihan == "4":
                        os.system(perintah_clear)
                        print("=== HAPUS PENGAJUAN SERVIS ===")
                        id_servis = input("Masukkan ID servis yang ingin dihapus: ")
                        servis = data_servis.get(id_servis)

                        if servis == None:
                            print("ID servis tidak ditemukan.")
                        elif servis["customer"] != username_login:
                            print("ID servis tidak ditemukan.")
                        elif servis["status"] != "Menunggu":
                            print("Pengajuan sudah diproses, tidak bisa dihapus.")
                        else:
                            del data_servis[id_servis]
                            print("Pengajuan servis berhasil dihapus.")
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