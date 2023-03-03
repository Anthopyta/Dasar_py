# operasi logika atau boolean

# not, or, and, xor

# NOT
a = True # jika False maka out: False
b = not a
print('data a =', a)
print('===NOT===')
print('data b =', b)

# OR
print('===OR===')
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)

# AND
print('===AND===')
a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, '=', c)
a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)

# XOR : salah satu true, maka out: true
print('===XOR===')
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
