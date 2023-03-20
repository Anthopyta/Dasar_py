# *args

def fungsi(nama, tinggi, berat):
  print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
  
fungsi("adi", 180, 80)

def fungsi(data_list):
  data = data_list.copy()
  nama = data[0]
  tinggi = data[1]
  berat = data[2]
  print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["rahmat", 140, 50])

# penggunaan *args

def fungsi(*args):
  nama = args[0]
  tinggi = args[1]
  berat = args[2]
  print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
  
fungsi("mamat", 150, 69)


# contoh kasus
def tambah(*data):
  # data tipenya adalah tuple, dia bisa diiterasi
  output = 0
  for angka in data:
    output += angka
  
  return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil}")


