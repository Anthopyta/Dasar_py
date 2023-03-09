# looping dictionary

data_dict = {
    "nama": "Budi",
    "umur": 20,
    "hobi": "membaca",
    "nilai" : 100,
}

# operator untuk mengambil item / iterables
keys = data_dict.keys()
print(keys)

for key in data_dict.keys():
  print(data_dict.get(key))
  
values = data_dict.values()
print(values)

for value in data_dict.values():
  print(value)

items = data_dict.items()
print(items)

for item in data_dict.items():
  print(item)
  

for key, value in data_dict.items():
  print(f"key : {key} , value : {value}")