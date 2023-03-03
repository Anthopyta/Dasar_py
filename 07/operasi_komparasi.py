# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

a = 4
b = 2

# (>)
hasil = a > 3
print(a, '>', 3, '=', hasil) # true

hasil = b > 3
print(b, '>', 3, '=', hasil) # false

# (<)
hasil = a < 3
print(a, '<', 3, '=', hasil) # false

hasil = b < 3
print(b, '<', 3, '=', hasil) # true

# (>=)
hasil = a >= 3
print(a, '>=', 3, '=', hasil) # true

hasil = b >= 3
print(b, '>=', 3, '=', hasil) # false

# (<=)
hasil = a <= 3
print(a, '<=', 3, '=', hasil) # false

hasil = b <= 3
print(b, '<=', 3, '=', hasil) # true

# (==)
hasil = a == 3
print(a, '==', 3, '=', hasil) # false

hasil = b == 3
print(b, '==', 3, '=', hasil) # false

# (!=)
hasil = a != 3
print(a, '!=', 3, '=', hasil) # true

hasil = b != 3
print(b, '!=', 3, '=', hasil) # true

# is : sebagai komparasi object identity
x = 5 # ini adalah assigment membuat object
y = 5 

print('nilai x = ', x, 'id = ', hex(id(x)))
print('nilai y = ', y, 'id = ', hex(id(y)))

hasil = x is y
print(hasil) # true

x = 5 # ini adalah assigment membuat object
y = 6

print('nilai x = ', x, 'id = ', hex(id(x)))
print('nilai y = ', y, 'id = ', hex(id(y)))

hasil = x is y
print(hasil) # false
# hasil = x is 5 (false)

# is not
x = 5
y = 5

print('nilai x = ', x, 'id = ', hex(id(x)))
print('nilai y = ', y, 'id = ', hex(id(y)))

hasil = x is not y
print(hasil) # false

x = 5
y = 6

print('nilai x = ', x, 'id = ', hex(id(x)))
print('nilai y = ', y, 'id = ', hex(id(y)))

hasil = x is not y
print(hasil) # true


