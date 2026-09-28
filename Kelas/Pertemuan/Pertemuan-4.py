# batas = 5
# for i in range(10):
#    print("Perulangan ke-", i)

# nilai = [75, 60, 80, 60, 50]
# for item in nilai:
#    if item >= 70:
#       print( item, "Lulus")
#    else:
#        print(item, "Tidak Lulus")

# for i in range(5, 0, -1):
#    print(i) 

# for i in range(1, 3):
#    for j in range(1, 4):
#        print(f'{i} x {j} = {i * j}')
#    print('') 

# jawab = "ya"
# hitung = 0
# while(jawab == "ya"):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total Perulangan : {hitung}")

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(10):
#     if i == 0:
#         continue
#     elif i == 5:
#         break
#     else:
#         print(i)

# for i in range(10):
#     if i == 0:
#         continue
#     elif i == 5:
#         break
#     else:
#         print(i, end=",")

# n = int(input("Masukkan batas perulangan: "))
# hitung = 0

# for i in range(n):
#     if i % 2 == 0:
#         continue
#     hitung += 1
#     print(i, end=",")

# print("\n")
# print(f"Jumlah bilangan ganjil: {hitung}")

UangSakuAwal = int(input("Masukkan uang saku awal: "))
UangDigunakan = int(input("Masukkan uang yang digunakan: "))
SisaUangSaku = UangSakuAwal - UangDigunakan
while SisaUangSaku > 0:
    SisaUangSaku = UangSakuAwal - UangDigunakan
    print(f"Sisa uang saku: {SisaUangSaku}")
    if SisaUangSaku <= 0:
        print("Uang saku habis.")
        break
    UangDigunakan = int(input("Masukkan uang yang digunakan: "))