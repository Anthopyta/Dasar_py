# width and multiline

#  data

data_nama = "Budi"
data_umur = 19
data_tinggi = 160.9
data_nomor_sepatu = 45

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor sepatu = {data_nomor_sepatu:d}"
print("Data String".center(20, '='))
print(data_string)

# string multiline
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor sepatu = {data_nomor_sepatu:d}"
print("\n"+"Data String".center(20, '='))
print(data_string)

# string multiline (kutip triplets)
data_string = f"""
nama = {data_nama:>5}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+"Data String".center(20, '='))
print(data_string)
