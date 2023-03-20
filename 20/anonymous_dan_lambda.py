# lambda function

# fungsi biasa
def f_kuadrat(angka):
    return angka ** 2


print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

""" 
syntax:
output = lambda aegument: expression 
"""


def kuadrat(angka): return angka**2


print(f"hasil lambda kuadrat = {kuadrat(3)}")


def pangkat(num, pow): return num**pow


print(f"hasil lambda pangkat = {pangkat(3, 2)}")

# sorting untuk list biasa
data_list = ["mamat", "rahmat", "rahman"]
data_list.sort()
print(f"sorted list = {data_list}")


# sorting menggunakan len
def panjang_nama(nama):
    return len(nama)


data_list.sort(key=panjang_nama)
print(f"sorted list by len = {data_list}")


# sorting dengan lambda
data_list = ["mamat", "rahmat", "rahman"]
data_list.sort(key=lambda nama: len(nama))
print(f"sorted list by lambda  = {data_list}")


# filter
data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def kurang_dari_lima(angka):
    return angka < 5


data_angka_baru = list(filter(kurang_dari_lima, data_angka))
data_angka_baru = list(filter(lambda x: x < 7, data_angka))
print(data_angka_baru)

# kasus genap
data_genap = list(filter(lambda x: (x % 2 == 0), data_angka))
print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x: (x % 2 != 0), data_angka))
print(data_ganjil)


# anonymouse function

def pangkat(angka, n):
    hasil = angka**n
    return hasil


data_hasil = pangkat(5, 2)
print(f"fungsi biasa = {data_hasil}")

# data dengan currying menjadi


def pangkat(n):
    return lambda angka: angka**n


pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")

pangkat2 = pangkat(3)
print(f"pangkat 3 = {pangkat2(3)}")

print(f"pangkat bebas = {pangkat(5)(5)}")
