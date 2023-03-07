# latihan perulangan membuat segitiga

sisi = 10
# menggunakan for

print("-"*10)
# dummy variable
count = 1
for i in range(sisi):
  print("*"*count)
  count += 1


print("-"*10)
# menggunakan while
count = 1
while True:
  print("*"*count)
  count += 1
  
  if count > sisi:
    break
  
print("-"*10)
# hanya ganjil saja
count = 1
while True:
  if (count % 2):
    print("*"*count)
    count += 1
  else:
    count += 1
    continue
  
  if count > sisi:
    break
  
print("-"*10)
count = 1
spasi = int(sisi/2)
while True:
  if (count % 2):
    print(" "*spasi,"*"*count)
    spasi -= 1
    count += 1
  else:
    count += 1
    continue
  
  if count > sisi:
    break

