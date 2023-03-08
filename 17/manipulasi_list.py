# operasi

# index  0(-3)    2(-2)    3(-1)
data = ["idham", "adi", "leksono"]

# mangambil data dari list 
data_0 = data[0]
print(f"data index 0: {data_0}")

data_terakhir = data[-1]
print(f"data index 1: {data_terakhir}")

# mengambil jumlah data dalam list
panjang_data = len(data)
print(f"panjang data: {panjang_data}")

# memanipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah : \n{data}")

data.insert(1, "Ahmad")
print(f"data setelah ditambah : \n{data}")

# menambah di akhir list
data.append("Oji")
print(f"data setelah ditambah : \n{data}")

# manambahkan list dengan list
data_baru = ["Ahmad", "Rendra", "Mahendra", "Ilham"]
data.extend(data_baru)
print(f"data setelah digabung : \n{data}")

# merubah data
data[3] = "D"
print(f"data berubah : \n{data}")

# menghapus data
data.remove("D") # akan error ketika data nama tidak sesuai 
print(f"data setelah dihapus : \n{data}")

# menghapus data paling belakang
data_terakhir = data.pop()
print(f"data akhir : \n{data_terakhir}")




