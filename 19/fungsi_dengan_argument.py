# fungsi dengna argument (input

def hello_world(nama):
  print(f"hallo bank {nama}")
  
hello_world("mamat")

# program tambah

def tambah(angka1, angka2):
  hasil = angka1 + angka2
  print(f"hasil penjumlahan {angka1} + {angka2} = {hasil}")

tambah(1, 5)
tambah(1001, 291)

def say_hi(list_peserta):
  data_peserta = list_peserta.copy()
  for peserta in data_peserta:
    print(f"yang terhormat {peserta}")

anggota_boyband = ["mamat", "rahmat", "fikri"]
say_hi(anggota_boyband)

