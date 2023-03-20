# global dan local scope

nama_global = "adi"  # ini adalah variabel global

# akses variabel blobal dalam fungsi


def fungsi1():
    print(f"fungsi menampilkan {nama_global}")


fungsi1()

# akses variabel global dalam loop
for i in range(0, 5):
    print(f"loop {i} - {nama_global}")

# percabangan
if True:
    print(f"if manampilkan {nama_global}")

# variabel local scope
def fungsi2():
  nama_local = "rahmat"
  
fungsi2()
# print(nama_local) # tidak bisa diakses


# contoh 1: penggunaan akses variabel
def say_hello():
  print(f"hello {nama}")

nama = "rahman"
say_hello()

# contoh 2: merubah variabel global 
angka = 0
nama = "dio"

def ubah(nilai_baru, nama_baru):
  global angka # ini untuk mendapat akses merubah nilai  
  global nama
  angka = nilai_baru
  nama = nama_baru
  
print(f"sebelum {angka,nama}")
ubah(10, "mamat")
print(f"sesudah {angka,nama}")

