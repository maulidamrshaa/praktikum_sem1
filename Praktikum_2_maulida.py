print("Tugas Praktikum 2")
print("1. Nama Variabel ")

nama = "Maulida Marsha Shahada"
print("Nama     :", nama)
#Menyimpan nama dalam tipe data string 

umur = 18
print("Umur     :", umur, "tahun")
#Menyimpan data umur dalam tipe data integer 

berat = 49.5
print("Berat    :", berat, "kg")
#Menyimpan data berat badan dalam tipe data float

print("\n 2. Mengubah Tipe Data ")
angka_str = "123" 
angka_float = 45.67 
angka_integer = 89
print("\t 1) Konverensi angka_string menjadi Integer")
data_int = int(angka_str) #menyimpan data string menjadi tipe data Integer
print("\t data = ", data_int, ",type = ", type(data_int))
# Mengubah data string menjadi tipe data integer

print("\t 2) Konverensi angka_float menjadi Integer")
data_int = int(angka_float) #menyimpan data float menjadi tipe data integer
print("\t data = ", data_int, ",type = ", type(data_int))
# Mengubah data float menjadi tipe data integer

print("\t 3) Konverensi angka_integer menjadi Float ")
data_float = float(angka_integer) #menyimpan data integer menjadi tipe data float
print("\t data = ", data_float, ",type = ", type(data_float))
# Mengubah data integer menjadi tipe data float

print("\t 4) Konverensi angka_integer menjadi string ") 
data_str = str(angka_integer) #menyimpan data integer menjadi tipe data float
print("\t data = ", data_str, ",type = ", type(data_str))
#mengubah data integer menjadi tipe data string

print("\n 3. Membuat Program")
print("a. Meminta input Usia") # Meminta input usia dalam tipe data integer
angka = int(input ("Masukkan data Usia = "))
print("data ", angka,",type=", type(angka))

print("b. Meminta input tinggi badan") # Meminta input tb dalam tipe data float
angka = float(input("Masukkan data Tinggi badan ="))
print("data ", angka,",type=", type(angka))

print("c. Meminta input Nama")
data = input("Masukkan data Nama =")
print("data ", data,",type=", type(data))

