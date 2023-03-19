# fungsi argumen default

def say_hello(nama, panggil = "mas"):
  print(f"hallo {nama}, {panggil}")

say_hello("budi")

def hitung_pangkat(angka, pangkat = 2):
  hasil = angka ** pangkat
  return hasil

print(hitung_pangkat(2,4))

