# operator yang dapat dilakukan dengan penyingkatan dengan menggunakan operator assingment
# operator assingment ini dapat digabungkan dengan operator aritmatika
# 

# operator assingment yang ada
# =, +=, -=, *=, /=, %=, **=, //=

# contoh operator assingment
a = 5
print('nilai a =', a)

a += 1 # a = a + 1
print('nilai a += 1, nilai a menjadi', a)

a -= 2 # a = a - 2
print('nilai a -= 2, nilai a menjadi', a)

a *= 5 # a = a * 5
print('nilai a *= 5, nilai a menjadi', a)

a /= 2 # a = a / 2
print('nilai a /= 2, nilai a menjadi', a)

a %= 2 # a = a % 2
print('nilai a %= 2, nilai a menjadi', a)

a **= 5 # a = a ** 5
print('nilai a **= 5, nilai a menjadi', a)

a //= 2 # a = a // 2
print('nilai a //= 2, nilai a menjadi', a)

print('--------------------------------')

# operator bitwise pada assigment
# &=
# |=
# ^=
# >>=
# <<=

b = 10
print('nilai b =', b)

b &= 2 # b = b & 2
print('nilai b &= 2, nilai b menjadi', b)

b |= 8 # b = b | 8
print('nilai b |= 8, nilai b menjadi', b)

b ^= 3 # b = b ^ 3
print('nilai b ^= 3, nilai b menjadi', b)

b >>= 3 # b = b >> 3
print('nilai b >>= 3, nilai b menjadi', b)

b <<= 3 # b = b << 3
print('nilai b <<= 3, nilai b menjadi', b)

print('--------------------------------')

# operator bitewise left shift right shift
# <<, >>

c = 0b0100
print('nilai c =', format(c, '04b'))

c = c << 2 # c = c << 2
print('nilai c << 2, nilai c menjadi', format(c, '04b'))

c = c >> 1 # c = c >> 1
print('nilai c >> 1, nilai c menjadi', format(c, '04b'))