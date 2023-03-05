# operasi dan manipulasi pada string

# 1. penambahan string
namaDepan = "John"
namaBelakang = "Doe"
nama = namaDepan + " " + namaBelakang
print(nama)

# menghitung panjang string
panjang = len(nama)
print(panjang)

# operator untuk string

# untuk mengecek apakah ada komponen char atau string di dalam string

d = "d" 
status = d in nama
print("Status " + d + " ada di " + nama + " = " + str(status))

d = "D" 
status = d in nama
print("Status " + d + " ada di " + nama + " = " + str(status))

d = "d" 
status = d not in nama
print("Status " + d + " tidak ada di " + nama + " = " + str(status))

# menghitung string
print("hwhwh"*5)
print(5*"hwhwh")

# indexing
print("index ke-0 : " + nama[0])
print("index ke-6 : " + nama[6])
print("index ke-(-1) : " + nama[-1])
print("index ke-(-2) : " + nama[-2])
print("index ke-[0:4] : " + nama[0:4])
print("index ke-[0:4:2] : " + nama[0:4:2])

# item paling kecil 
print("paling kecil : " + min(nama))
# item paling besar
print("paling besar : " + max(nama))

asscii_coed = ord(" ")
print("ASCII code untuk spasi adalah " + str(asscii_coed))
data = 117
print("char untuk ASCII code 117 adalah " + chr(data))

# operator dalam bentuk method

data = "huruf kecil"
jumlah = data.count("u")
print("jumlah huruf u pada " + data + " adalah " + str(jumlah))

## merubah case dari string

# merubah ke upper case
salam = "halo"
print("halo -> " + salam.upper())

# merubah ke lower case
bro = "BRO"
print("BRO -> " + bro.lower())

## pengecekan dengan isX method

# contoh pengecekan lower case
salam = "halo"
apakahLower = salam.islower() # hasilnya boolean
print("apakah " + salam + " lower case? : " + str(apakahLower))
apakahUpper = salam.isupper() # hasilnya boolean
print("apakah " + salam + " upper case? : " + str(apakahUpper))

# isalpha() -> mengembalikan true jika string hanya terdiri dari huruf
# isnumeric() -> mengembalikan true jika string hanya terdiri dari angka
# isdecimal() -> mengembalikan true jika string hanya terdiri dari angka dan tanda desimal
# isspace() -> mengembalikan true jika string hanya terdiri dari spasi, tab, atau newline
# istitle() -> mengembalikan true jika string berupa judul, yaitu setiap kata dimulai dengan huruf kapital

## mengecek komponen startswith() dan endswith()
cek_start = "belajar python"
cek_akhir = "python"
print(cek_start.startswith("belajar"))
print(cek_akhir.endswith("python"))

## penggabungan komponen join() dan split()
data = ["belajar", "python", "di", "dunia ilkom"]
gabung = " ".join(data)
print(gabung)
pecah = gabung.split(" ")
print(pecah)

# alokasi karakter rjust(), ljust(), dan center()
kata = "halo"
print("kata : " + kata)
print("rjust : " + kata.rjust(10))
print("ljust : " + kata.ljust(10))
print("center : " + kata.center(10))

print()
# kebalikan dari strip() adalah rstrip() dan lstrip()
kata = "  halo  "
print("kata : " + kata)
print("strip : " + kata.strip())
print("rstrip : " + kata.rstrip())
print("lstrip : " + kata.lstrip())

