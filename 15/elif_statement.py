# elif = else if statement 

nama = input("nama kamu siapa? ")

if nama == "Budi":
  print(f"halo bank {nama}")
elif nama == "Bambang":
  print(f"halo mas {nama}")
elif nama == "Budi" or "Bambang":
  print("lu siapa cok?!")
else:
  print("eh maap salah orang")