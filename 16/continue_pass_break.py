# pernyataan continue

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

""" 
Contoh di atas akan mencetak angka dari 1 hingga 10, 
namun akan mengabaikan angka genap dan hanya mencetak angka ganjil. 
Hal ini dilakukan dengan menggunakan pernyataan continue. Ketika program menemukan angka genap,
maka pernyataan continue akan dilewati, dan program akan melanjutkan ke iterasi berikutnya tanpa mencetak angka tersebut.

"""

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

# pernyataan break

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

""" 
Contoh di atas menunjukkan penggunaan pernyataan break pada pernyataan perulangan for.
Program akan mengecek setiap elemen dalam list fruits dan mencetak setiap elemen sampai 
program menemukan elemen "banana". Setelah menemukan elemen "banana", program akan keluar
dari perulangan dengan menggunakan pernyataan break dan tidak akan mencetak elemen selanjutnya.

"""