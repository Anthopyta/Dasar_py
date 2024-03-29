import datetime
import os 
import string
import random

mahasiswa_template = {
  "nama" : "nama",
  "nim" : "000000000",
  "sks_lulus" : "0",
  "lahir" : datetime.datetime(1111,1,11)
}

data_mahasiswa = {}


while True:
  os.system("cls")
  print(f"{'SELAMAT DATANG':^20}")
  print(f"{'DATA MAHASISWA':^20}")
  print("-"*20)

  mahasiswa = dict.fromkeys(mahasiswa_template.keys())
  print(mahasiswa)
  mahasiswa['nama'] = input('Nama Mahasiswa: ')
  mahasiswa['nim'] = input('NIM Mahasiswa: ')
  mahasiswa['sks_lulus'] = int(input('SKS Lulus: '))
  Tahun_lahir = int(input('Tahun lahir (YYYY): '))
  Bulan_lahir = int(input('Bulan lahir (1-12): '))
  Tanggal_lahir = int(input('Tanggal lahir (1-31): '))
  mahasiswa['lahir'] = datetime.datetime(Tahun_lahir, Bulan_lahir, Tanggal_lahir)
  
  KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
  data_mahasiswa.update({KEY: mahasiswa})
  
  print(f"{'KEY':<6} {'NAMA':<17} {'SKS':^3} {'LAHIR':^10}")
  print("-"*20)
  
  for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')
    
    print(f"{KEY:<6} {NAMA:<17} {SKS:^3} {LAHIR:^10}")
    
  print("\n")
  is_done = input('\nAre you done? (y/n): ')
  if is_done == "y":
    break
print("program selesai")
    