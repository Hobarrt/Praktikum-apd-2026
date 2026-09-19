bagasi_1 = 12
bagasi_2 = 18
bagasi_3 = 7
bagasi_4 = 15
bagasi_5 = 20
bagasi_6 = 10
nim = 19

bagasi = [bagasi_1, bagasi_2, bagasi_3, bagasi_4, bagasi_5, bagasi_6]
total_berat = bagasi_1 + bagasi_2 + bagasi_3 + bagasi_4 + bagasi_5 + bagasi_6
total_bayar = total_berat + (total_berat * 5 / 100)
rata_rata = total_berat / len(bagasi)

bolean = nim < rata_rata

pemumpang_tengah = bagasi[2:5]
total_berat_gram = total_berat * 1000

print("berat bagasi 1 =", bagasi_1)
print("berat bagasi 2 =", bagasi_2)
print("berat bagasi 3 =", bagasi_3)
print("berat bagasi 4 =", bagasi_4)
print("berat bagasi 5 =", bagasi_5)
print("berat bagasi 6 =", bagasi_6)
print("total berat bagasi =", total_berat)
print("total bayar setelah mempertimbangkan biaya kompensasi =", total_bayar)
print("rata-rata berat setiap =", rata_rata)
print("nim =", nim)
print("bolean =", bolean)
print("Berat bagasi penumpang tengah =", pemumpang_tengah)
print("total berat dalam gram =", total_berat_gram)