a = int(input("bilangan pertama: "))
b = int(input("bilangan kedua: "))
c = int(input("bilangan ketiga: "))

def terbesar(a, b, c):
    if a == b == c:
        print(f"Semuanya sama {a}")
    else:
        terbesar = max(a, b, c)
        print(f"bilangan terbesar adalah: {terbesar}")
        
terbesar(a, b, c)  