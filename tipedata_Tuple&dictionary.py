#Tipe data Tuple

tuple_1 = (2,3,4)
tuple_2 = ("gino", "tari")
tuple_3 = (24, False, "Hello")
print(tuple_1,tuple_2,tuple_3)

#fungsi tuple

#string ke tuple
alphabets = tuple("abcdefgh")
print(alphabets)


#list ke tuple

number = tuple([1,2,3,4])
print(number)

#range ke tuple

r = range(0,200)
rtuple = tuple(r)
print(rtuple)


#tipe data dictionary
biodata_1 ={
    "nama" : "zabaril",
    "umur" : "15",
    "hobi" : "main game"
}
print("nama: %s" %(biodata_1["nama"]))
print("umur: %s" %(biodata_1["umur"]))
print("umur: %s" %(biodata_1["hobi"]))

