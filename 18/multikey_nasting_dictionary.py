import datetime

mahasiswa1 = {
  "nama" : "Ahmad",
  "nim" : "1112013092",
  "sks_lulus" : "144",
  "beasiswa" : False,
  "lahir" : datetime.datetime(2002,2,24)
}

mahasiswa2 = {
  "nama" : "Rahmat",
  "nim" : "111210918",
  "sks_lulus" : "145",
  "beasiswa" : False,
  "lahir" : datetime.datetime(2002,3,9)
}

mahasiswa3 = {
  "nama" : "Mamat",
  "nim" : "111209181",
  "sks_lulus" : "144",
  "beasiswa" : True,
  "lahir" : datetime.datetime(2002,2,1)
}

data_mahasiswa = {
  "maha1" : mahasiswa1,
  "maha2" : mahasiswa2,
  "maha3" : mahasiswa3 
}

print(f"{'KEY':<6} {'NAMA':<17} {'SKS':<3} {'Beasiswa':<9} {'lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
  KEY = mahasiswa
  
  NAMA = data_mahasiswa[KEY]['nama']
  NIM = data_mahasiswa[KEY]['nim']
  SKS = data_mahasiswa[KEY]['sks_lulus']
  BEASISWA  = data_mahasiswa[KEY]['beasiswa']
  LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')
  
  print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")
  