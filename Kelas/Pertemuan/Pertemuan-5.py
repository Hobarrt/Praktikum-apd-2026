nama1 = "Rasyid"
nama2 = "Bambang"
nama3 = "Irul"

print(nama1, nama2, nama3)

list_nama = ["Rasyid", "Jamal", "Bambang"]
print(list_nama)
for i in(list_nama):
    print(i)

list_nama.append("Irul")
print(list_nama)

list_nama.extend(["Naya"])
print(list_nama)

list_nama.insert(1, "Jaya")
print(list_nama)

list_nama[1:2] = ["Farhan", "Sahiraa"]
print(list_nama)

del list_nama[1:3]
print(list_nama)

list_nama.remove("Jamal")
print(list_nama)

# poin = [1, 2, 3, 4, 5, 6, 7]
# print(poin)

# poin[4:7] = [11, 12, 13]
# print(poin)

ambil_nama = list_nama.pop(1)
print(ambil_nama)


poin1 = [1, 2, 3, 4, 5, 6, 7]
point2 = [8, 9, 10, 11, 12, 13, 14]
point = poin1 + point2
print(point)

line_up = [
    ["BMW", "X5", "2020"],
    ["Toyota", "Camry", "2021"],
    ["Honda", "Civic", "2022"]
]
print(line_up[1][0])  

nama = "Rasyid, Jago, Mtk, fisika"
print(nama)
hapus = int(input("Masukkan index yang ingin dihapus: "))
nama_list = nama.split(", ")
del nama_list[hapus]
print(nama_list)

buah = ("apel", "jeruk", "mangga", "pisang")
print(buah[int(input("Masukkan index buah yang ingin ditampilkan: "))])

game = ("Mobile Legends", "PUBG", "Free Fire", "Valorant")
(moba, fps, battle_royale, shooter) = game
print(moba)
print(fps)
print(battle_royale)