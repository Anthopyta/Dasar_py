data = "ini adalah string"
# print(data)
# print(type(data))

# cara membuat string
'''
1. dengan menggunakan single quote '...'
2. dengan menggunakan double quote "..."
'''
data = 'Menggunakan single quote'
# print(data)

data = "Menggunakan double quote"
# print(data)

print('"Halo apa kabar?"')
print("'Halo apa kabar?'")

# menggunakan tanda \
# membuat tanda ' menjadi string
print('\'Halo apa kabar?\'')
print('ini adalah hari jum\'at')

# blackslah
print('C:\\user\\namauser')

# tab
print("panjang\t\tsekali!!")

# backspace
print("pendek  \b\bsekali!!")

# newline 
print("baris pertama.\nbaris kedua") # LF -> line feed
print("baris pertama.\rbaris kedua") # CR -> carriage return
print("baris pertama.\r\nbaris kedua") # CRLF -> carriage return line feed

# string literal atau raw
print(r'C:\new') # tidak akan dianggap sebagai escape sequence

# multiline literal string
print("""
Nama: Andi
Umur: 21
""")
print('''
Nama: Andi
Umur: 21
''')

# multiline literal string dan raw
print(r'''
Nama: Andi
Umur: 21
''')


