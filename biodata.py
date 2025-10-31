print ("====================================")
print ("\tBIODATA\tSISWA")
print ("====================================")
print ("Nama       :\tZabarill\tAzrifath\nNis        :\t47394566\nJurusan    :\tRPL\nUmur       :\t15\nHobi       :\tMain game")
print ("====================================")


data = None
print (data)

nama = "Zabaril"
if nama is None:
    print("Nama belum diisi")
else:
    print("Nama kamu adalah:", nama)    


list_1=[2,3,8,16]
print(list_1[0])

list_2 = ["grayson","jason","tim","damian"]
print(list_2[2])

list_3 = [24,False,"hello python"]
print(list_3[1])

buah = ["apel","jeruk"]
buah.append("mangga")
print(buah)

buah = ["jeruk","durian"]
buah.extend(["mangga","pisang"])
print(buah)

angka = [1,2,3]
angka.insert(3,4)
print(angka)

buah = ["mangga", "pisang","apel","anggur","melon"]
buah.pop(3)
print(buah)

angka = [5,2,9,1]
angka.sort()
print(angka)

buah = ["apel","jeruk", "manggga"]
buah.remove("apel")
print(buah)

angka = [5,2,9,1,4,7,3]
angka.sort(reverse=True)
print(angka)

data = [1,2,3]
data.clear()
print(data)

nama = ["zabaril","azrifath"]
print(nama.index("zabaril"))

warna = ["merah","kuning","hijau"]
warna.reverse()
print(warna)

angka = [1,2,2,3,2,2,2,2,2]
print(angka.count(2))


