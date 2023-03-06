#  format string

# contoh generic
# string
nama = "Budi"
format_str = f"hello {nama}"
print(format_str)

# boolean
bool = True
format_str = f"boolean = {bool}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat 
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan ribuan 
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.51312
format_str = f"angka = {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 2005.51312
format_str = f"angka = {angka:09.3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.1241
format_minus = f"angka minus = {angka_minus:+d}"
format_plus = f"angka plus = {angka_plus:+.2f}"
print(format_minus)
print(format_plus)

# memformat persen
presentase = 0.045
format_persen = f"persen = {presentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam plecholder
harga = 10000
jumlah = 5

format_str = f"harga total = Rp.{harga*jumlah:,}"
print(format_str)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)