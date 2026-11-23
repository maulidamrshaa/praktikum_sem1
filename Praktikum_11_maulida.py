# --- PRAKTIKUM 11 (Multi keys & Nesting Dictionary) --- #

# membuat program sistem manajemen perpustakaan (menambahkan dan menampilkan buku baru ke dalam sistem) 
# menggunakan konsep multi_keys dan nesting dictionary 
# format = KEYS, JUDUL BUKU, PENULIS, TAHUN TERBIT, TANGGAL TERAKHIR PINJAM, STATUS (TERSEDIA/TIDAK)

import datetime
import string
import random 
import os

#dictionary utama
buku_template = {
    'judul' : 'judul',
    'penulis' : 'penulis',
    'tahunterbit' : 0000,
    'tanggalpinjam' : datetime.datetime(1111, 1, 11),
    'status' : 'TERSEDIA'
}
#dictionary kosong 
data_buku = {}

while True :
    os.system("cls")
    print(f"{'SELAMAT DATANG' : ^20}")
    print(f"{'MANAJEMEN PERPUSTAKAAN' : ^20}")
    print("="*25)

    buku = dict.fromkeys(buku_template.keys())

    #mengambil input
    buku['judul'] = input("Judul Buku : ")
    buku['penulis'] = input("Penulis : ")
    buku['tahunterbit'] = int(input("Tahun Terbit : "))

    print("\n--- Tanggal Terakhir Pinjam ---")
    tahun = int(input(f"{'Tahun (YYYY)' : <28}: "))
    bulan = int(input(f"{'Bulan (1-12)' : <28}: "))
    tanggal = int(input(f"{'Tanggal (1-31)' : <28}: "))
    buku['tanggalpinjam'] = datetime.datetime(tahun, bulan, tanggal)

    buku['status'] = input(f"{'Status (TERSEDIA / TIDAK)' : <28}: ").upper()

    #membuat KEY acak yang unik sebanyak 6 karakter
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6))) 
    data_buku.update({KEY: buku})

    #menampilkan header tabel 
    print(f"\n {'KEY':<8} {'JUDUL':<25} {'PENULIS':<18} {'TAHUN':<7} {'TANGGALPINJAM':<12} {'STATUS':<10}")
    print('-'*85)

    #menampilkan seluruh data buku 
    for KEY in data_buku : 
        JUDUL = data_buku[KEY]['judul']
        PENULIS = data_buku[KEY]['penulis']
        TAHUN = data_buku[KEY]['tahunterbit']
        TANGGALPINJAM = data_buku[KEY]['tanggalpinjam'].strftime("%d-%m-%Y")
        STATUS = data_buku[KEY]['status']

        print(f"\n {KEY:<8} {JUDUL:<25} {PENULIS:<18} {TAHUN:<7} {TANGGALPINJAM:<12} {STATUS:<10}")

    #membuat pilihan program berhenti atau dijalankan lagi
    print("\n")
    is_done = input("Mau tambah buku lagi? (y/n) : ").lower()
    if is_done == "n" :
        break
print("\n Akhir dari program, terima kasih")
