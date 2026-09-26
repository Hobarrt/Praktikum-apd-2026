angka = 6 
if  angka < 10:
    print ("Angka kurang dari 10")


umur = int(input("Masukkan umur Anda: "))
if umur >= 17:
    print ("kamu sudah bisa membuat KTP")
else:
    print ("kamu belum bisa membuat KTP")


kendaraan = input("Masukkan jenis kendaraan anda: ").lower()
if kendaraan == "mobil":
    tarif_parkir = 10000
elif kendaraan == "motor":
    tarif_parkir = 5000
else:
    tarif_parkir = 15000
print("Tarif parkir yang harus dibayar:", tarif_parkir)

nilai = int(input("Masukkan nilai : "))

if nilai >= 10:
    if nilai >= 20:
        if nilai >= 30:
            print("Angka Besar")
        print("Angka Sedang")
    print("Angka Kecil")

umur = int(input("Masukkan umur Anda: "))
izin = "Boleh masuk" if umur >= 16 else "Tidak boleh masuk"
print(izin)

pembelian = int(input("Masukkan total pembelian: "))
if pembelian > 200000:
    diskon = 0.3 * pembelian
    hasil = pembelian - diskon
elif pembelian > 100000:
    diskon = 0.1 * pembelian
    hasil = pembelian - diskon
else: 
    diskon = 0
    hasil = pembelian
print("Diskon yang diterima:", diskon)
print("Total yang harus dibayar:", hasil)
