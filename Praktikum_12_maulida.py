# ---PRAKTIKUM 12--- #
# --- FUNGSI --- #

# membuat program dengan input dan fungsi untuk menghitung 
#   a. Luas persegi panjang
#   b. Volume persegi panjang
#   c. Luas lingkaran
#   d. Volume bola

# a. Luas persegi panjang
print("=== LUAS PERSEGI PANJANG ===")
def LuasPersegiPanjang (panjang, lebar):
    luas = panjang * lebar
    return luas

p = float(input("Masukkan panjang = "))
l = float(input("Masukkan lebar = "))

luas = LuasPersegiPanjang (p, l)
print (f"Hasil luas persegi panjang = {luas}")


# b. Volume persegi panjang 
print("\n=== VOLUME PERSEGI PANJANG ===")
def VolumePersegiPanjang (panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi 
    return volume 

p = float(input("Masukkan panjang = "))
l = float(input("Masukkan lebar = "))
t = float(input("Masukkan tinggi = "))

volume = VolumePersegiPanjang(p, l, t)
print(f"Hasil Volume persegi panjang = {volume}")


# c. Luas lingkaran 
print("\n=== LUAS LINGKARAN ===")

def LuasLingkaran (jari_jari) :
    phi = 3.14
    luas = phi * jari_jari**2
    return luas

jari_jari = float(input("Masukkan jari-jari lingkaran = "))

luas = LuasLingkaran(jari_jari)
print (f"Hasil Luas Lingkaran = {luas}")


# d. Volume bola 
print("\n=== VOLUME BOLA ===")

def VolumeBola (jari_jari) :
    phi = 3.14
    volume = 4/3 * phi * jari_jari**3
    return volume

jari_jari = float(input("Masukkan jari-jari Bola = "))

volume = VolumeBola(jari_jari)
print(f"Hasil Volume Bola = {volume}") 