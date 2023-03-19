import os

# program menghitung luas dan keliling panjang

os.system("clear")

print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
print(f"{'-'*40:^40}")

# input user
lebar = int(input("Masukan nilai lebar: "))
panjang = int(input("Masukan nilai panjang: "))

# program menghitung luas
luas = panjang * lebar
keliling = 2*(panjang + lebar)

# menampilkan hasil
print(f"hasil perhitungan luas {luas}")
print(f"hasil perhitungan keliling {keliling}")
