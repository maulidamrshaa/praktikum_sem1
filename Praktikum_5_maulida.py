print("Latihan Perulangan dan Kontrol Alur")

#Latihan
# 1. Program bilangan ganjil dan genap dari 1 sampai 50 menggunakan perulangan 
print("\nBilangan Ganjil dan Genap 1-50\n")
for angka in range(1, 51):
    if angka % 2 == 0:
        print(f"Angka genap -> {angka}")
    else :
        print(f"Angka ganjil -> {angka}")

# 2. Program menampilkan bilangan Prima antara 1 sampai 100
print("\nBilangan Prima 1-100\n") 
for angka in range(2, 101):
    prima = True

    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            prima = False 
            break 

    if prima :
        print(f"Angka Prima -> {angka}")
