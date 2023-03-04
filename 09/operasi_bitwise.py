# operator bitwise 

# Operator Bitwise AND
a = 10  # 1010 dalam biner
b = 3   # 0011 dalam biner
c = a & b # 0010 dalam biner
print(c) # Output: 2

# Operator Bitwise OR
a = 10  # 1010 dalam biner
b = 3   # 0011 dalam biner
c = a | b # 1011 dalam biner
print(c) # Output: 11

# Operator Bitwise XOR
a = 10  # 1010 dalam biner
b = 3   # 0011 dalam biner
c = a ^ b # 1001 dalam biner
print(c) # Output: 9

# Operator Bitwise NOT
a = 10  # 1010 dalam biner
c = ~a  # -11 dalam desimal (menggunakan representasi 2's complement)
print(c) # Output: -11

# Operator Bitwise Shift Left
a = 10  # 1010 dalam biner
c = a << 2 # 101000 dalam biner
print(c) # Output: 40

# Operator Bitwise Shift Right
a = 10  # 1010 dalam biner
c = a >> 2 # 0010 dalam biner
print(c) # Output: 2
