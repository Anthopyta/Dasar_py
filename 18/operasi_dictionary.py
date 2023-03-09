# operator dictionary

data_dict = {
    "nama": "Budi",
    "umur": 20,
    "hobi": "membaca",
    "nilai" : 100
}

# panjang dictionary
lenDict = len(data_dict)
print(f"panjang dictionary : {lenDict}")

# mengecek key exist atau tidak 
key = 'nama'
check_key = key in data_dict
print(f"apakah {key} ada di data_dict : {check_key}")


# mengakses value (read) dengan get
print(data_dict['nama'])
print(data_dict.get('nama'))
print(data_dict.get('nama' ,'key tidak ditemukan')) # cek key dengan message tidak ditemukan 


# mengupdate data
data_dict['nama'] = "Budi D Luffy"
print(data_dict)

data_dict.update({"nama": "Budi D Luffy"})
print(data_dict)
data_dict.update({"kebiasaan": "balapan"}) # kalo ga ada di add
print(data_dict)

# mendelete data pada dictionary
del data_dict['kebiasaan']
print(data_dict)

