import datetime
import os 

mahasiswa_template = {
  "nama" : "nama",
  "nim" : "000000000",
  "sks_lulus" : "0",
  "lahir" : datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

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
print(mahasiswa)