# list 

# kumpulan data numbers
data_angka = [1,2,3]
print(data_angka)

# kumpulan data string
data_string = ["idham", "adi", "leksono"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, False, True]
print(data_boolean)

# kumpulan campuran 
data_campuran = [1, "idham", True]
print(data_campuran)

# cara alternatif membuat list
data_range = range(0,10,2) # range(start, stop, step)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
data_list = [i**2 for i in range(0,10)]
print(data_list)

# membuat list dengan for if
data_list = [i for i in range(0, 10) if i != 5]
print(data_list)

data_list = [i for i in range(0, 10) if i % 2 == 0]
print(data_list)

data_list = [i for i in range(0, 10) if i % 2 != 0]
print(data_list)