# program list buku

list_buku = []

while True:
  print("Masukan data buku")
  judul = input("Judul buku \t : ")
  penulis = input("Nama penulis\t : ")

  buku_baru = [judul, penulis]
  print(buku_baru)
  list_buku.append(buku_baru)
  print(list_buku)
  
  
  print("\n\n","="*10, "Data Buku", "="*10)
  for index, buku in enumerate(list_buku):
    print(f"{index+1} | {buku[0]}| {buku[1]}")
  
  print("\n\n","="*20)
  keluar = input("Apakah dilanjutkan? (y/n): ")
  
  if keluar == "n" :
    break
print("program selesai")
