print("\n Latihan Operasi Aritmatika dan Komperasi\n")

panjang = 12
lebar = 5
tinggi = 8

print("a. Hitunglah luas, volume, dan keliling dari bangunan tersebut")

# Menghitung Luas
Luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
print("\tLuas bangunan adalah", 2, '*', '(', '(', panjang, '*', lebar,')', '+', '(', panjang, '*', tinggi, ')', '+', '(', lebar, '*', tinggi, ')', ')', '=', Luas )

# Menghitung Volume 
Volume = panjang * lebar * tinggi
print("\tVolume bangunan adalah", panjang, '*', lebar, '*', tinggi, '=', Volume)

# Menghitung Keliling
Keliling = 4 * (panjang + lebar + tinggi)
print("\tKeliling bangunan adalah", 4, '*', '(', panjang, '+', lebar, '+', tinggi, ')', '=', Keliling)

# b. luas bangunan lebih dari (> 50)
print("b. Apakah luas bangunan tersebut lebih luas dari 50?")

# hasil luas 
Luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
print("\tLuas bangunan adalah", 2, '*', '(', '(', panjang, '*', lebar,')', '+', '(', panjang, '*', tinggi, ')', '+', '(', lebar, '*', tinggi, ')', ')', '=', Luas )

# lebih besar dari >
hasil = Luas > 50
print("\t Luas bangunan tersebut lebih luas dari 50 =", hasil)

print("c. Apakah volume tersebut bernilai 480")
Volume = panjang * lebar * tinggi
print("\tVolume bangunan adalah", panjang, '*', lebar, '*', tinggi, '=', Volume) 
print("\tVolume bangunan tersebut bernilai 480 =", Volume == 480)
