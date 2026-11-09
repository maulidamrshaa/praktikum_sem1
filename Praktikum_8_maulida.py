# --- Praktikum (Tuple, Set, Dictionary) ---
# 1. Tuple
#   a. Tuple yg berisi data diri
print("1. Tuple")
print("a. membuat Tuple yang berisikan data diri") #Nama, NIM, Prodi
mahasiswa = ("Maulida Marsha Shahada", 2605060048, "Teknologi Informasi")
print(f"Nama, NIM, Prodi    = {mahasiswa}")

#   b. Menampilkan data NIM dan Prodi menggunakan indeksnya
print("b. menampilkan data NIM dan Prodi menggunakan indeksnya")
print(f"NIM     = {mahasiswa[1]}")
print(f"Prodi   = {mahasiswa[2]}")

#   c. menjalankan kode mahasiswa[2] = Teknologi Informasi dan amati pesan yg error
mahasiswa[2] = "Teknologi Informasi"
print(mahasiswa)

#   d. buat Set (nilai_angka) = 10, 4, 3, 2, 4, 10, 7, 5
print("d. buat Set nilai_angka dan jelaskan mengapa angka 10 dan 4 tertulis dua kali")
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)

#2. Manipulasi Dictionary 
#   a. buat data_mahasiswa 
print("\n2. Manipulasi Dictionary")
print("a. membuat Dictionary")
data_mahasiswa = {
    'nim' : '240101',
    'nama' : 'Budi Santoso',
    'prodi' : 'Teknologi informasi',
}
print(data_mahasiswa)
#   b. mengubah nilai "prodi" menjadi "Sastra Mesin" & tambahkan key baru 'angkatan' : "2026"
print("b. ubah nilai 'prodi' menjadi 'sastra mesin' & tambahkan nilai 'angkatan' : '2026'")
#data awal
print(data_mahasiswa)
# mengubah nilai pada key "prodi"
data_mahasiswa.update({"prodi":"Sastra Mesin"})
# menambahkan key "angkatan" : 2026
data_mahasiswa["angkatan"] = 2026
print(data_mahasiswa)
#   c. menghapus data 'nim'
print("c. menghapus data 'nim'")
print(data_mahasiswa)
del data_mahasiswa['nim']
print(data_mahasiswa)

#3. Perulangan pada Dictionary 
#   a. membuat Dictionary keranjang 
print("\n3. Perulangan pada Dictionary")
print("a. membuat Dictionary bernama keranjang")
keranjang = {
    'apel' : 5000,
    'pisang' : 3000,
    'jeruk' : 7000,
    'anggur' : 15000,
}
print(keranjang)
#   b. gunakan perulangan untuk menampilkan barang
print("b. menggunakan perulangan untuk menampilkan data")
for key,value in keranjang.items() :
    print(f"Harga {key} = Rp{value}")
#   c. menampilkan total belanja
print("c. menampilkan total belanja")
total = sum(keranjang.values())
print("apel(Rp5000) + pisang(Rp3000) + jeruk(Rp7000) + anggur(Rp15000)")
print(f"Total harga = {total}")