# perulangan (for loop)
# for <nama_var> in <data>:
#     <pernyataan>
#     <pernyataan>
#     ...
#     <pernyataan>

angka = [1, 2, 3, 4, 5] # ini adalah list
print(angka)

for i in angka:
  print(f"i => {i}")
print("akhir dari program 1\n")

# range
angka_range = range(1,5)

for i in angka_range:
  print(f"i => {i}")
print("akhir dari program 2\n")

# mengguanakan string
for huruf in "Python":
  print(f"huruf => {huruf}")
print("akhir dari program 3\n")

