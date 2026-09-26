nama_terdaftar = "Rasyid"
nim_terdaftar = "19"

print("LOGIN SISTEM SPBU")

nama = input("Masukkan nama panggilan Anda: ")
nim = input("Masukkan 2 digit terakhir kode anggota anda (NIM): ")

if nama == nama_terdaftar and nim == nim_terdaftar:

    print("Hallooo Welcome back sirrr", nama)

    print("\n")

    print("Opsi BBM yang tersedia:")
    print("1. Pertalite        Rp 10000/Liter")
    print("2. Pertamax         Rp 12500/Liter")
    print("3. Pertamax Turbo   Rp 15000/Liter")
    print("\n")

    pilihan = input("Pilih jenis BBM yang anda mau (1-3): ")

    if pilihan == "1":
        jenis_bbm = "Pertalite"
        harga_per_liter = 10000
    elif pilihan == "2":
        jenis_bbm = "Pertamax"
        harga_per_liter = 12500
    elif pilihan == "3":
        jenis_bbm = "Pertamax Turbo"
        harga_per_liter = 15000
    else:
        jenis_bbm = "tidak valid"
        harga_per_liter = 0

    if pilihan == "1" or pilihan == "2" or pilihan == "3":

        jumlah_liter = float(input("mau beli berapa liter srr: "))
        total_harga = harga_per_liter * jumlah_liter

        if jumlah_liter >= 10:
            diskon = 10
        elif jumlah_liter >= 5:
            diskon = 5
        else:
            diskon = 0

        diskon_liter = (diskon / 100) * total_harga

        member = input("ada member nyaa? (ada/tidak): ")

        if member == "ada":
            diskon_member = 0.02 * total_harga
            keterangan_member = "terdaftaar sebagai member"
        else:
            diskon_member = 0
            keterangan_member = "belum terdaftar sebagai member"

        total_diskon = diskon_liter + diskon_member
        total_bayar = total_harga - total_diskon

        print("\n")
        print("====================================")
        print("------------------------------------")
        print("        STRUK TRANSAKSI SPBU")
        print("------------------------------------")
        print("====================================")
        print("Nama Pembeli      :", nama)
        print("NIM               :", nim)
        print("====================================")
        print("Jenis BBM         :", jenis_bbm)
        print("Jumlah Liter      :", jumlah_liter, "Liter")
        print("Total Harga       : Rp", total_harga)
        print("Diskon Pembelian  :", diskon, "% (Rp", diskon_liter, ")")
        print("Status Member     :", keterangan_member)
        print("Diskon Member     : Rp", diskon_member)
        print("TOTAL BAYAR       : Rp", total_bayar)
        print("====================================")
        print("====================================")

    else:
        print("Pilihan BBM tidak valid. Program selesai.")

else:
    print("Sorrry nama atau kode anggota anda belum terdaftar.")
    print("Program selesai.")