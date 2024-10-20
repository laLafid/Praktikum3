terbesar = None

while True:
    n = int(input("Masukan Bilangan mu: "))
    if n == 0:
        break
    if terbesar is None or n > terbesar:
        terbesar = n

print("Bilangan Terbesar adalah:", terbesar)