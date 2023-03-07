# pernyataan continue
# menggunakan for
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

    
print("=====================================")
# menggunakan while
angka = 0
print(f"agnaka sekarang -> {angka}")

while angka < 5:
  angka += 1
  print(f"angka sekarang -> {angka}") # aksi 1
  
  if angka == 3:
    print("Check!!")
    continue # akan membuat loop meloncat ke step selanjutnya
  print("Pass") # aksi 2

""" 
Contoh di atas akan mencetak angka dari 1 hingga 10, 
namun akan mengabaikan angka genap dan hanya mencetak angka ganjil. 
Hal ini dilakukan dengan menggunakan pernyataan continue. Ketika program menemukan angka genap,
maka pernyataan continue akan dilewati, dan program akan melanjutkan ke iterasi berikutnya tanpa mencetak angka tersebut.

"""
print("=====================================")
# pernyataan pass

for i in range(1, 6):
    if i == 3:
        pass  # placeholder for implementing other actions in the future
    else:
        print(i)

""" 
Dengan menggunakan pernyataan pass, 
kita dapat membuat kerangka program atau blok kode pada loop,
tanpa harus mengisi seluruh implementasi kode dalam satu waktu.
Hal ini memungkinkan kita untuk mengembangkan kode secara bertahap dan
memudahkan proses debugging ketika terjadi kesalahan.

"""

print("=====================================")
# pernyataan break

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

print("=====================================")
angka = 0

while angka < 5:
  angka += 1
  print(f"angka sekarang -> {angka}")
  
  if angka == 3:
    print("break")
    break
  print("Check!!")

""" 
Contoh di atas menunjukkan penggunaan pernyataan break pada pernyataan perulangan for.
Program akan mengecek setiap elemen dalam list fruits dan mencetak setiap elemen sampai 
program menemukan elemen "banana". Setelah menemukan elemen "banana", program akan keluar
dari perulangan dengan menggunakan pernyataan break dan tidak akan mencetak elemen selanjutnya.

"""