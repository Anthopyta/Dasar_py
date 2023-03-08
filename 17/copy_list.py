# menduplikat lsit dengan copy

a = ["Ahmad", "Mahendra", "Indra", "Rendra"]

b = a.copy()
print(f"address a : {hex(id(a))}")
print(f"address b : {hex(id(b))}")

# sehingga
b.append("Oji")
print(f"data tambah : {a}")
print(f"data tambah : {b}")
