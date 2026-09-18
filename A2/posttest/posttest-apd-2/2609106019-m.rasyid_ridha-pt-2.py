bagasi_1 = 12
bagasi_2 = 18
bagasi_3 = 7
bagasi_4 = 15
bagasi_5 = 20
bagasi_6 = 10

bagasi = [bagasi_1, bagasi_2, bagasi_3, bagasi_4, bagasi_5, bagasi_6]
total_berat = bagasi_1 + bagasi_2 + bagasi_3 + bagasi_4 + bagasi_5 + bagasi_6
total_berat_akhir = total_berat + (total_berat * 5 / 100)
rata_rata = total_berat_akhir / len(bagasi)

nim = 19
bolean = nim < rata_rata

data_tengah = bagasi[2:5]
total_berat_gram = total_berat_akhir * 1000

print("bagasi 1 =", bagasi_1)
print("bagasi 2 =", bagasi_2)
print("bagasi 3 =", bagasi_3)
print("bagasi 4 =", bagasi_4)
print("bagasi 5 =", bagasi_5)
print("bagasi 6 =", bagasi_6)
print("bagasi =", bagasi)
print("total berat =", total_berat)
print("total berat akhir =", total_berat_akhir)
print("rata-rata =", rata_rata)
print("nim =", nim)
print("bolean =", bolean)
print("data tengah =", data_tengah)
print("total berat gram =", total_berat_gram)