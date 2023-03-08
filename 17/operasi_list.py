data_angka = [1, 3, 1, 5, 12, 5, 16, 9, 4, 0, 3, 9, 2, 7, 2]
print(f"data angka : \n{data_angka}")

# count data
jumlah_data_3 = data_angka.count(3)
jumlah_data_1 = data_angka.count(1)
print(f"junlah data 3 ada {jumlah_data_3} buah")
print(f"junlah data 1 ada {jumlah_data_1} buah")

# ambil posisi data
data = ["Ahmad", "Mahendra", "Indra", "Rendra"]
print(f"data : \n{data}")

index_Mahendra = data.index("Mahendra")
print(f"index_Mahendra : \n{index_Mahendra}")

# mengurutkan list 
print(f"data seblum di sorting : \n{data}")
data_angka.sort()
print(f"data angka sort : \n{data_angka}")

print(f"data : \n{data}")
data.sort()
print(f"data sort : \n{data}")

# balik listnya
data_angka.reverse()
data.reverse()

print(f"data dibalik : \n{data_angka}")
print(f"data dibalik : \n{data}")

