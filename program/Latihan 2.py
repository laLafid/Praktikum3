# Latihan 2

a = input("masukan nilai a: ")
b = input("masukan nilai b: ")

print("variable a =", a)
print("variable b =", b)
print("hasil penggabungan variable {}&{}={}".format(a, b, a+b))

# konversi nilai variable 
a = int(a)
b = int(b)

print("hasil penjumlahan {}+{}={}".format(a, b, a+b))
print("hasil pembagian {}/{}={}".format(a, b, a/b if a != 0 else "undefined"))
