import os

# program menghitung luas dan keliling panjang

# os.system("clear")

# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # input user
# lebar = int(input("Masukan nilai lebar: "))
# panjang = int(input("Masukan nilai panjang: "))

# # program menghitung luas
# luas = panjang * lebar
# keliling = 2*(panjang + lebar)

# # menampilkan hasil
# print(f"hasil perhitungan luas {luas}")
# print(f"hasil perhitungan keliling {keliling}")


""" menggunakan fungsi """

def header():
  os.system("clear")
  # os.system("cls")
  print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
  print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
  print(f"{'-'*40:^40}")

#* input user
def input_angka():
  lebar = int(input("Masukan nilai lebar: "))
  panjang = int(input("Masukan nilai panjang: "))
  return lebar, panjang

# program luas
def hitung_luas(lebar, panjang):
  return lebar* panjang

def hitung_keliling(lebar, panjang):
  return 2*(panjang + lebar)

def hasil(message, value):
  print(f"hasil perhitungan {message} = {value}")

# menu program
while True:
  header()
  lebar, panjang = input_angka()
  luas = hitung_luas(lebar, panjang)
  keliling = hitung_keliling(lebar, panjang)
  
  hasil("luas", luas)
  hasil("keliling", keliling)
  
  isContine = input("apakah lanjut (y/n)?")
  if isContine == "y":
    break

print("proram selesai")