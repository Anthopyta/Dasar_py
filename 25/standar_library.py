import datetime

data_waktu = datetime.datetime.now()
print(f"datetime now : {data_waktu}")
print(f"year : {data_waktu.year}")
print(f"hari : {data_waktu.strftime('%A')}")

from collections import Counter

data = ["a", "b", "c", "d", "a", "d", "a"]

data_count = Counter(data)
print(f"data count = {data_count}")
print(f"jumlah a = {data_count['a']}")
print(f"jumlah a = {data_count['d']}")


import io

file = io.open("25\\file_text.txt", "r") # 25 itu file folder berada
print(file.read())
