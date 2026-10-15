# kartu = {"merah", "kuning", "hijau", "merah"}
# kartu.add("biru")

# print(kartu)


# aslab1 = {"fina", "shasha", "risma"}
# aslab2 = {"larry", "attar", "haekal"}
# gabung = aslab1.union(aslab2)
# print(gabung)
# print(aslab1)
# print(aslab2)

# Biodata = {
# "Nama" : "Siti Julpa", 
# "NIM" : 25091060,
# "KRS" : ["Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Instagram" : "julpatarr"
# }
# print(Biodata["Instagram"])
# print(Biodata["KRS"][0])

# game = {
#     "pou" : "chill",
#     "genshin impact" : "action",
#     "valorant" : "fps",
#     "minecraft" : "sandbox",
#     "mobile legend" : "moba"
# }

# game["genshin impact"] = "adventure"
# game["free fire"] = "battle royale"




# # for i in game:
# #     print(i)

# for i in game.keys():
#     print(i)

# print("===================================")
# for i in game.values():
#     print(i)

# print("===================================")
# for keys, values in game.items():
#     print(f"{keys} adalah jenis game {values}")


# aset = {
#     "jenis" : "rumah",
#     "harga" : 120000000,
#     "alamat" : "Jl. Raya No. 1",
#     "berpenghuni" : True,
#     "luas" : "120m x 80m"
# }

# print(aset)
# del aset["luas"]
# print(aset)
# print(aset.get("luas"))

# print(aset)
# cache = aset.pop("luas")
# print(aset)
# print(aset.get("luas"))
# print(cache)

# print(aset)
# aset.clear()
# print(aset)

# print("Panjang dictionary :", len(aset))
# print(len(aset))


# gamebaru = game.copy()
# print(game)
# print(gamebaru)

# key = "ayam geprek", "ayam goreng", "ayam bakar",
# value = 12000, 14000

# menu = dict.fromkeys(key, value)
# print(menu)

# menu = {
#     "ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
#     "nasi" : ["nasi goreng", "nasi uduk"],
#     "mie" : ["mie goreng rendang", "mie goreng aceh"],
#     "kuah" : ["soto", "rawon", "sop iga"]
# }

# for i, j in menu.items():
#     print(f"Kategori {i} memiliki menu :")
#     for kategori in j:
#             print(kategori)
#     print("")



poli_umum = {"Andi", "Budi", "Citra", "Doni"}
poli_gigi = {"Citra", "Doni", "Eka", "Fani"}

semua_pasien = poli_umum | poli_gigi

print("Daftar seluruh pasien:")
for keys, values in enumerate(sorted(semua_pasien), start=1):
    print(f"{keys}. {values}")

print("\nTotal pasien:", len(semua_pasien))


data_siswa = {
    "siswa1": {
        "nama": "Johan",
        "kelas": "A2",
        "nilai": 85,
    },
 
    "siswa2": {
        "nama" : "Niyah",
        "kelas" : "A2",
        "nilai" : 95,
    },

}