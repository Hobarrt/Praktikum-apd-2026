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


def bersihkan_layar():
    os.system(perintah_clear)


def jeda():
    input("Tekan Enter untuk melanjutkan...")


def tampilkan_judul(teks):
    bersihkan_layar()
    print(f"=== {teks} ===")


# =====================================================
# FUNGSI TANPA PARAMETER (dengan return)
# =====================================================
def buat_id_servis():
    """FUNGSI TANPA PARAMETER 1: membuat ID servis baru (SRV1, SRV2, ...)."""
    global nomor_servis
    id_baru = "SRV" + str(nomor_servis)
    nomor_servis += 1
    return id_baru


def buat_id_layanan():
    """FUNGSI TANPA PARAMETER 2: membuat ID layanan baru (L12, L13, ...)."""
    global nomor_layanan
    id_baru = "L" + str(nomor_layanan)
    nomor_layanan += 1
    return id_baru


def input_tidak_kosong(label):
    while True:
        try:
            nilai = input(label)
            if nilai.strip() == "":
                raise ValueError("Input tidak boleh kosong!")
        except ValueError as e:
            print(e)
        else:
            return nilai


def input_angka_positif(label):
    while True:
        try:
            teks = input(label)
            if not teks.isdigit():
                raise ValueError("Harus berupa angka (tanpa titik/koma/spasi)!")
            angka = int(teks)
            if angka <= 0:
                raise ValueError("Angka harus lebih dari 0!")
        except ValueError as e:
            print(e)
        else:
            return angka


def input_jam(label):
    while True:
        try:
            teks = input(label)
            bagian = teks.split(":")
            if len(bagian) != 2 or len(bagian[0]) != 2 or len(bagian[1]) != 2 \
                    or not bagian[0].isdigit() or not bagian[1].isdigit():
                raise ValueError("Format jam salah! Gunakan HH:MM (contoh 08:00)")
            if int(bagian[0]) > 23 or int(bagian[1]) > 59:
                raise ValueError("Jam harus di antara 00:00 - 23:59")
        except ValueError as e:
            print(e)
        else:
            return teks


def cek_login(username, password):
    akun = data_akun.get(username)
    if akun is not None and akun["password"] == password:
        return akun
    return None


def cari_akun_role(username, role):
    akun = data_akun.get(username)
    if akun is not None and akun["role"] == role:
        return akun
    return None


def ambil_biaya_selesai(username_customer=None):
    daftar = []
    for servis in data_servis.values():
        if servis["status"] == "Selesai":
            if username_customer is None or servis["customer"] == username_customer:
                daftar.append(servis["biaya"])
    return daftar

def total_biaya_rekursif(daftar_biaya, indeks=0):
    if indeks >= len(daftar_biaya):
        return 0
    return daftar_biaya[indeks] + total_biaya_rekursif(daftar_biaya, indeks + 1)

def tampilkan_layanan():
    for id_layanan, layanan in data_layanan.items():
        print(f"{id_layanan} | {layanan['nama']} | Rp{layanan['harga']}")


def tampilkan_user(role, judul):
    tampilkan_judul(judul)
    jumlah = 0
    for username, akun in data_akun.items():
        if akun["role"] == role:
            jumlah += 1
            print("-------------------------------------")
            print(f"Username : {username}")
            print(f"Nama     : {akun['nama']}")
    if jumlah == 0:
        print(f"Data {role} masih kosong.")
    else:
        print("-------------------------------------")
        print(f"Total {role}:", jumlah)
    jeda()


def tampilkan_semua_servis():
    tampilkan_judul("SEMUA DATA SERVIS")
    if hitung_total_servis() == 0:
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
        print("Total servis:", hitung_total_servis())
    jeda()


def hitung_total_servis():
    return len(data_servis)

def kelola_teknisi():
    tampilkan_judul("KELOLA TEKNISI")
    print("1. Tambah teknisi")
    print("2. Ubah data teknisi")
    print("3. Hapus teknisi")
    print("0. Kembali")
    sub = input("Pilih menu: ")

    if sub == "1":
        username_baru = input_tidak_kosong("Username teknisi : ")
        if username_baru in data_akun:
            print("Username sudah dipakai!")
        else:
            password_baru = input_tidak_kosong("Password : ")
            nama_baru = input_tidak_kosong("Nama teknisi : ")
            data_akun[username_baru] = {"password": password_baru, "nama": nama_baru, "role": "teknisi"}
            print("Teknisi berhasil ditambahkan.")
        jeda()

    elif sub == "2":
        username_cari = input("Masukkan username teknisi: ")
        teknisi = cari_akun_role(username_cari, "teknisi")
        if teknisi is None:
            print("Teknisi tidak ditemukan.")
        else:
            print("1. Ubah nama")
            print("2. Ubah password")
            pilihan_ubah = input("Pilih data yang diubah: ")
            if pilihan_ubah == "1":
                teknisi["nama"] = input_tidak_kosong("Nama baru : ")
                print("Nama teknisi berhasil diubah.")
            elif pilihan_ubah == "2":
                teknisi["password"] = input_tidak_kosong("Password baru : ")
                print("Password teknisi berhasil diubah.")
            else:
                print("Pilihan tidak valid!")
        jeda()

    elif sub == "3":
        username_cari = input("Masukkan username teknisi yang dihapus: ")
        teknisi = cari_akun_role(username_cari, "teknisi")
        if teknisi is None:
            print("Teknisi tidak ditemukan.")
        else:
            masih_bertugas = False
            for servis in data_servis.values():
                if servis["teknisi"] == username_cari and servis["status"] in ("Diambil", "Diproses"):
                    masih_bertugas = True
            if masih_bertugas:
                print("Teknisi masih memiliki job aktif, tidak bisa dihapus!")
            else:
                del data_akun[username_cari]
                print("Teknisi berhasil dihapus.")
        jeda()


def kelola_layanan():
    tampilkan_judul("KELOLA LAYANAN")
    if len(data_layanan) == 0:
        print("(Belum ada layanan)")
    else:
        tampilkan_layanan()
    print("")
    print("1. Tambah layanan")
    print("2. Ubah layanan")
    print("3. Hapus layanan")
    print("0. Kembali")
    sub = input("Pilih menu: ")

    if sub == "1":
        nama_baru = input_tidak_kosong("Nama layanan : ")
        harga_baru = input_angka_positif("Harga layanan (angka) : ")
        id_baru = buat_id_layanan()
        data_layanan[id_baru] = {"nama": nama_baru, "harga": harga_baru}
        print("Layanan berhasil ditambahkan dengan ID", id_baru)
        jeda()

    elif sub == "2":
        id_cari = input("Masukkan ID layanan: ")
        layanan = data_layanan.get(id_cari)
        if layanan is None:
            print("Layanan tidak ditemukan.")
        else:
            print("1. Ubah nama layanan")
            print("2. Ubah harga layanan")
            pilihan_ubah = input("Pilih data yang diubah: ")
            if pilihan_ubah == "1":
                nama_baru = input_tidak_kosong("Nama baru : ")
                nama_lama = layanan["nama"]
                layanan["nama"] = nama_baru
                for servis in data_servis.values():
                    if servis["layanan"] == nama_lama:
                        servis["layanan"] = nama_baru
                print("Nama layanan berhasil diubah.")
            elif pilihan_ubah == "2":
                layanan["harga"] = input_angka_positif("Harga baru (angka) : ")
                print("Harga layanan berhasil diubah.")
            else:
                print("Pilihan tidak valid!")
        jeda()

    elif sub == "3":
        id_cari = input("Masukkan ID layanan yang dihapus: ")
        layanan = data_layanan.get(id_cari)
        if layanan is None:
            print("Layanan tidak ditemukan.")
        else:
            sedang_dipakai = False
            for servis in data_servis.values():
                if servis["layanan"] == layanan["nama"] and servis["status"] in ("Menunggu", "Diambil", "Diproses"):
                    sedang_dipakai = True
            if sedang_dipakai:
                print("Layanan masih dipakai oleh servis yang berjalan, tidak bisa dihapus!")
            else:
                del data_layanan[id_cari]
                print("Layanan berhasil dihapus.")
        jeda()


def ubah_jam_operasional():
    tampilkan_judul("UBAH JAM OPERASIONAL")
    print("Jam saat ini:", jam_operasional["buka"], "-", jam_operasional["tutup"])
    print("Format jam: HH:MM (contoh 08:00)")
    jam_buka = input_jam("Jam buka baru  : ")
    jam_tutup = input_jam("Jam tutup baru : ")

    if jam_tutup <= jam_buka:
        print("Jam tutup harus lebih besar dari jam buka! Perubahan dibatalkan.")
    else:
        jam_operasional["buka"] = jam_buka
        jam_operasional["tutup"] = jam_tutup
        print("Jam operasional berhasil diubah.")
    jeda()


def penugasan_servis():
    tampilkan_judul("PENUGASAN SERVIS")
    if hitung_total_servis() == 0:
        print("Data servis masih kosong.")
    else:
        for id_servis, servis in data_servis.items():
            if servis["status"] in ("Menunggu", "Diambil"):
                print(f"{id_servis} | {servis['perangkat']} | {servis['status']} | Teknisi: {servis['teknisi']}")
        print("")
        id_servis = input("Masukkan ID servis: ")
        servis = data_servis.get(id_servis)

        if servis is None:
            print("ID servis tidak ditemukan.")
        elif servis["status"] not in ("Menunggu", "Diambil"):
            print("Servis sudah berjalan/selesai, tidak bisa ditugaskan ulang.")
        else:
            print("")
            print("Daftar teknisi:")
            for username, akun in data_akun.items():
                if akun["role"] == "teknisi":
                    print(f"{username} | {akun['nama']}")
            username_cari = input("Masukkan username teknisi: ")
            teknisi = cari_akun_role(username_cari, "teknisi")
            if teknisi is None:
                print("Teknisi tidak ditemukan.")
            else:
                servis["teknisi"] = username_cari
                servis["status"] = "Diambil"
                print("Servis berhasil ditugaskan ke", teknisi["nama"])
    jeda()


def tampilkan_total_pendapatan():
    tampilkan_judul("TOTAL PENDAPATAN (SERVIS SELESAI)")
    daftar_biaya = ambil_biaya_selesai()
    total = total_biaya_rekursif(daftar_biaya)  
    print("Jumlah servis selesai :", len(daftar_biaya))
    print(f"Total pendapatan      : Rp{total}")
    jeda()


def lihat_job_tersedia():
    tampilkan_judul("JOB TERSEDIA")
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
    jeda()


def lihat_job_saya(username_login):
    tampilkan_judul("JOB SAYA")
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
    jeda()


def ambil_job(username_login):
    tampilkan_judul("AMBIL JOB")
    id_servis = input("Masukkan ID servis: ")
    servis = data_servis.get(id_servis)
    if servis is None:
        print("ID servis tidak ditemukan")
    elif servis["status"] == "Menunggu":
        servis["status"] = "Diambil"
        servis["teknisi"] = username_login
        print("Job berhasil diambil")
    else:
        print("Job tidak tersedia")
    jeda()


def ubah_status_job(username_login):
    tampilkan_judul("UBAH STATUS JOB")
    id_servis = input("Masukkan ID servis: ")
    servis = data_servis.get(id_servis)

    if servis is None:
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
    jeda()


def isi_biaya_catatan(username_login):
    tampilkan_judul("ISI BIAYA & CATATAN")
    id_servis = input("Masukkan ID servis: ")
    servis = data_servis.get(id_servis)

    if servis is None:
        print("ID servis tidak ditemukan.")
    elif servis["teknisi"] != username_login:
        print("Job ini bukan milik kamu.")
    elif servis["status"] not in ("Diambil", "Diproses"):
        print("Biaya/catatan hanya bisa diisi saat status Diambil atau Diproses.")
    else:
        biaya_baru = input_angka_positif("Biaya servis (angka) : ")
        catatan_baru = input_tidak_kosong("Catatan servis : ")
        servis["biaya"] = biaya_baru
        servis["catatan"] = catatan_baru
        print("Biaya dan catatan berhasil disimpan.")
    jeda()


def batalkan_pengerjaan(username_login):
    tampilkan_judul("BATALKAN PENGERJAAN")
    id_servis = input("Masukkan ID servis: ")
    servis = data_servis.get(id_servis)

    if servis is None:
        print("ID servis tidak ditemukan.")
    elif servis["teknisi"] != username_login:
        print("Job ini bukan milik kamu.")
    elif servis["status"] not in ("Diambil", "Diproses"):
        print("Job ini tidak dapat dibatalkan.")
    else:
        alasan = input_tidak_kosong("Alasan pembatalan : ")
        servis.update({
            "status": "Menunggu",
            "teknisi": "-",
            "biaya": 0,
            "catatan": "-",
            "alasan_batal": alasan
        })
        print("Pengerjaan dibatalkan, job kembali ke daftar tersedia.")
    jeda()


def ajukan_servis(username_login):
    tampilkan_judul("AJUKAN SERVIS")
    if len(data_layanan) == 0:
        print("Belum ada layanan tersedia, hubungi admin.")
        jeda()
        return

    perangkat = input_tidak_kosong("Nama perangkat : ")
    keluhan = input_tidak_kosong("Keluhan        : ")
    print("")
    print("Daftar layanan:")
    tampilkan_layanan()

    nama_layanan = ""
    while nama_layanan == "":
        id_layanan = input("Masukkan ID layanan (0 = batal): ")
        if id_layanan == "0":
            break
        layanan = data_layanan.get(id_layanan)
        if layanan is None:
            print("ID layanan tidak ditemukan!")
        else:
            nama_layanan = layanan["nama"]

    if nama_layanan != "":
        id_baru = buat_id_servis()
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
    jeda()


def lihat_servis_saya(username_login):
    tampilkan_judul("SERVIS SAYA")
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
    jeda()


def ubah_pengajuan(username_login):
    tampilkan_judul("UBAH PENGAJUAN SERVIS")
    id_servis = input("Masukkan ID servis: ")
    servis = data_servis.get(id_servis)

    if servis is None or servis["customer"] != username_login:
        print("ID servis tidak ditemukan.")
    elif servis["status"] != "Menunggu":
        print("Pengajuan sudah diproses, tidak bisa diubah.")
    else:
        print("1. Ubah perangkat")
        print("2. Ubah keluhan")
        print("3. Ubah layanan")
        pilihan_ubah = input("Pilih data yang diubah: ")

        if pilihan_ubah == "1":
            servis["perangkat"] = input_tidak_kosong("Perangkat baru : ")
            print("Perangkat berhasil diubah.")
        elif pilihan_ubah == "2":
            servis["keluhan"] = input_tidak_kosong("Keluhan baru : ")
            print("Keluhan berhasil diubah.")
        elif pilihan_ubah == "3":
            tampilkan_layanan()
            id_layanan = input("Masukkan ID layanan baru: ")
            layanan = data_layanan.get(id_layanan)
            if layanan is None:
                print("ID layanan tidak ditemukan.")
            else:
                servis["layanan"] = layanan["nama"]
                print("Layanan berhasil diubah.")
        else:
            print("Pilihan tidak valid!")
    jeda()


def hapus_pengajuan(username_login):
    tampilkan_judul("HAPUS PENGAJUAN SERVIS")
    id_servis = input("Masukkan ID servis yang ingin dihapus: ")
    servis = data_servis.get(id_servis)

    if servis is None or servis["customer"] != username_login:
        print("ID servis tidak ditemukan.")
    elif servis["status"] != "Menunggu":
        print("Pengajuan sudah diproses, tidak bisa dihapus.")
    else:
        del data_servis[id_servis]
        print("Pengajuan servis berhasil dihapus.")
    jeda()


def tampilkan_total_biaya_saya(username_login):
    tampilkan_judul("TOTAL BIAYA SERVIS SAYA")
    daftar_biaya = ambil_biaya_selesai(username_login)
    total = total_biaya_rekursif(daftar_biaya)  # pemanggilan fungsi rekursif
    print("Jumlah servis selesai :", len(daftar_biaya))
    print(f"Total biaya           : Rp{total}")
    jeda()


def menu_admin(nama_login):
    login_aktif = True
    while login_aktif:
        bersihkan_layar()
        print("=== MENU ADMIN ===")
        print("Selamat datang,", nama_login)
        print("1. Lihat semua customer")
        print("2. Lihat semua teknisi")
        print("3. Lihat semua data servis")
        print("4. Kelola teknisi (tambah/ubah/hapus)")
        print("5. Kelola layanan (tambah/ubah/hapus)")
        print("6. Ubah jam operasional")
        print("7. Penugasan servis")
        print("8. Total pendapatan")
        print("0. Logout")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_user("customer", "DAFTAR CUSTOMER")
        elif pilihan == "2":
            tampilkan_user("teknisi", "DAFTAR TEKNISI")
        elif pilihan == "3":
            tampilkan_semua_servis()
        elif pilihan == "4":
            kelola_teknisi()
        elif pilihan == "5":
            kelola_layanan()
        elif pilihan == "6":
            ubah_jam_operasional()
        elif pilihan == "7":
            penugasan_servis()
        elif pilihan == "8":
            tampilkan_total_pendapatan()
        elif pilihan == "0":
            login_aktif = False
        else:
            print("Pilihan tidak valid!")
            jeda()


def menu_teknisi(nama_login, username_login):
    login_aktif = True
    while login_aktif:
        bersihkan_layar()
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
            lihat_job_tersedia()
        elif pilihan == "2":
            lihat_job_saya(username_login)
        elif pilihan == "3":
            ambil_job(username_login)
        elif pilihan == "4":
            ubah_status_job(username_login)
        elif pilihan == "5":
            isi_biaya_catatan(username_login)
        elif pilihan == "6":
            batalkan_pengerjaan(username_login)
        elif pilihan == "0":
            login_aktif = False
        else:
            print("Pilihan tidak valid!")
            jeda()


def menu_customer(nama_login, username_login):
    login_aktif = True
    while login_aktif:
        bersihkan_layar()
        print("=== MENU CUSTOMER ===")
        print("Selamat datang,", nama_login)
        print("Jam operasional:", jam_operasional["buka"], "-", jam_operasional["tutup"])
        print("1. Ajukan servis")
        print("2. Lihat servis saya")
        print("3. Ubah pengajuan servis")
        print("4. Hapus pengajuan servis")
        print("5. Total biaya servis saya")
        print("0. Logout")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            ajukan_servis(username_login)
        elif pilihan == "2":
            lihat_servis_saya(username_login)
        elif pilihan == "3":
            ubah_pengajuan(username_login)
        elif pilihan == "4":
            hapus_pengajuan(username_login)
        elif pilihan == "5":
            tampilkan_total_biaya_saya(username_login)
        elif pilihan == "0":
            login_aktif = False
        else:
            print("Pilihan tidak valid!")
            jeda()


def daftar_customer():
    tampilkan_judul("DAFTAR CUSTOMER")
    username_baru = input_tidak_kosong("Username : ")
    if username_baru in data_akun:
        print("Username sudah dipakai!")
    else:
        password_baru = input_tidak_kosong("Password : ")
        nama_baru = input_tidak_kosong("Nama lengkap : ")
        data_akun[username_baru] = {"password": password_baru, "nama": nama_baru, "role": "customer"}
        print("Pendaftaran berhasil, silakan login.")
    jeda()


def proses_login():
    tampilkan_judul("LOGIN")
    username_input = input("Username : ")
    password_input = input("Password : ")
    akun_login = cek_login(username_input, password_input)

    if akun_login is None:
        print("Username atau password salah!")
        jeda()
        return

    role = akun_login["role"]
    nama_login = akun_login["nama"]
    if role == "admin":
        menu_admin(nama_login)
    elif role == "teknisi":
        menu_teknisi(nama_login, username_input)
    else:
        menu_customer(nama_login, username_input)


def main():
    program_jalan = True
    while program_jalan:
        bersihkan_layar()
        print("=====================================")
        print("      SISTEM SERVIS PERANGKAT")
        print("=====================================")
        print("Jam operasional:", jam_operasional["buka"], "-", jam_operasional["tutup"])
        print("")
        print("1. Login")
        print("2. Daftar sebagai Customer")
        print("0. Keluar")
        pilihan_awal = input("Pilih menu: ")

        if pilihan_awal == "1":
            proses_login()
        elif pilihan_awal == "2":
            daftar_customer()
        elif pilihan_awal == "0":
            program_jalan = False
        else:
            print("Pilihan tidak valid!")
            jeda()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram dihentikan paksa oleh pengguna.")
    finally:
        print("Terima kasih, program selesai.")