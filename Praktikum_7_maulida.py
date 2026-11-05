# --- Praktikum (Operasi dan Manipulasi LIST) ---

# 1. diberikan list -> kendaraan = ['motor', 'mobil', 'sepeda', 'bus']
kendaraan = ['motor', 'mobil', 'sepeda', 'bus']
print(f"1. List data = {kendaraan}")
#   a. tambahkan 'truck' diakhir list 
kendaraan.append("truck")
print(f"a. menambahkan 'truck' diakhir list = \n\t{kendaraan}")

#   b. sisipkan "becak" pada index ke 1
kendaraan.insert(1, "becak")
print(f"b. sisipkan 'becak' pada index ke-1 = \n\t {kendaraan} ")

#   c. hapus data yang ada di paling belakang dari list
kendaraan.pop ()
print(f"c. menghapus data paling belakang = \n\t {kendaraan}")

#   d. ubah elemen "sepeda" menjadi "skuter"
kendaraan[3] = "skuter"
print(f"d. merubah data 'sepeda' menjadi 'skuter' = \n\t {kendaraan}")

#   e. menampilkan informasi jumlah total data di dalam list
data_kendaraan = len(kendaraan)
print(f"e. jumlah total data = \n\t {data_kendaraan}")

print( )

# 2. diberikan list -> angka = [75, 80, 90, 75, 85, 100, 65]
angka = [75, 80, 90, 75, 85, 100, 65]
print(f"2. List data = {angka}")
#   a. mencari indeks ke berapa skor 100 berada
index_100 = angka.index (100)
print(f"a. indeks skor 100 berada pada indeks = {index_100}")

#   b. hitung banyak siswa yang mendapat skor 75
jumlahskor_75 = angka.count(75)
print(f"b. jumlah siswa yang mendapat skor 75 = {jumlahskor_75}")

#   c. urutkan list skor_ujian dari nilai terkecil - terbesar
angka.sort()
print(f"c. mengurutkan data (terkecil ke terbesar) = \n\t{angka}")

#   d. balikkan urutan list (terbesar- terkecil)
angka.reverse()
print(f"d. membalikkan urutan list (terbesar ke terkecil) = \n\t{angka}")

print()

# 3. menu_utama = ["Nasi Goreng", "Mie Ayam"]   ;   menu_tambahan = ["Kerupuk", "Es Teh"]
#   menggabungkan menu_tambahan ke dalam menu_utama menggunakan fungsi, kemudian tampilkan hasil dari data gabungan
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]
print("3. Menggabungkan data")
print(f"\tdata sebelum digabungkan = \n{menu_utama} dan {menu_tambahan}")
menu_utama.extend(menu_tambahan)
print(f"\tdata setelah digabungkan = \n{menu_utama}")

print()

# 4. data nested list -> data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]
print (f"4. data barang = \n{data_barang}")
#   a. menampilkan harga "Pensil" (2000) dengan memanggil indeks baris dan kolom dari list 
# ["Buku", 5000],       Baris indeks 0
# ["Pensil", 2000]      Baris indeks 1
# ["Penggaris", 3000]   Baris indeks 2
barang_harga = data_barang [1][0], data_barang[1][1]
#[1][0] -> pensil   = [1] utk memanggil baris pensil, [0] utk memanggil kolom pensil
#[1][1] -> 2000     = [1] utk memanggil baris 2000, [1] utk memanggil kolom 2000
print(f"a. menampilkan harga pensil dengan memanggil indeks baris dan kolom")
print(f"Nama Barang & Harga    : {barang_harga}")

#   b. menggunakan perulangan untuk membaca data satu persatu,
#       format output = "Nama : [nama barang], Harga : [harga]" utk setiap elemen 
print("b. program perulangn untuk membaca data")
for i in data_barang :
    print(f"Nama    : {i[0]}")
    print(f"Harga   : {i[1]}")
          