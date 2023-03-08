# looping dari list

# for loop 
kumpulan_list = [2, 1,5,6, 3, 8,0]

for angka in kumpulan_list:
  print(f"angka : {angka}")
  
peserta = ['Ahmad', 'Rendra', 'Mahendra', 'Indra']

for nama in peserta:
  print(f"nama : {nama}")
  
# for loop dan range
# kumpulan_angka = [2, 1,5,6, 3, 8]
# panjang = len(kumpulan_angka)

# for i in range(panjang):
#   print(f"i : {kumpulan_angka[i]}") 

# while
print("\n")
kumpulan_angka = [2, 1,5,6, 3, 8]
panjang = len(kumpulan_angka)

i = 0
while i < panjang:
  print(f"angka : {kumpulan_angka[i]}")
  i += 1

# list comprehension
print("\n")
data = ["Ahmad", 1, "Rahmat"]
[print(f"data : {i}") for i in data]

# enumerate
print("\n")
data_list = ["Ahmad", 1,2,3, "Rahmad",]

for index, data in enumerate(data_list):
  print(f"data : {data} index : {index}")

print("\n")
angka = [2, 1,5,6, 3, 8]
angka_kuadrat = [i**2 for i in angka]
print(f"angka : {angka}")