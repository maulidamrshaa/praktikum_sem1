print("\nLatihan Logical, Komparasi Logical dan ELIF\n")

#program untuk meminta user memasukkan usia seseorang, lalu kategorikan usia tersebut berdasar kriteria :
# 0-12 tahun : anak anak
# 13-17 tahun : remaja
# 18-59 tahun : dewasa
#60 tahun ke atas : lansia

usiaUser = int(input("Masukkan usia anda :"))
# membuat input untuk user memasukkan data usia dengan konversi tipe data integer


if usiaUser >= 0 and usiaUser <= 12:            # 0-12 tahun : anak-anak
    print("Anak-anak")                          # -------0++++++12------
elif usiaUser >= 13 and usiaUser <= 17:         # 13-17 tahun : remaja
    print("Remaja")                             # -------13+++++17------
elif usiaUser >= 18 and usiaUser <= 59:         # 18-59 tahun : dewasa
    print("Dewasa")                             # -------18+++++59------
elif usiaUser >= 60:                            # >=60 tahun : lansia
    print("Lansia")                             # -------60+++++++
else :
    print ("Usia tidak valid")  #jika input lainnya, maka akan menampilkan usia tidak valid

print("\nProgram selesai\n")