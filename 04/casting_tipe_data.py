# merbah dari satu tipe ke tipe lain 

# integer
print("===INTEGER===")
data_int = 9

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai int = 0
print("data : ", data_int, ",type =", type(data_int))
print("data : ", data_str, ",type =", type(data_int))
print("data : ", data_bool, ",type =", type(data_int))

# float
print("===FLOAT===")
data_float = 1.0

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) 
print("data : ", data_int, ",type =", type(data_float))
print("data : ", data_str, ",type =", type(data_float))
print("data : ", data_bool, ",type =", type(data_float))

# boolean
print("===BOOLEAN==")
data_bool = True

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool) 
print("data : ", data_int, ",type =", type(data_bool))
print("data : ", data_str, ",type =", type(data_bool))
print("data : ", data_float, ",type =", type(data_bool))


# string
print("===STRING===")
data_str = '10'

data_int = int(data_str)
data_float = str(data_str)
data_bool = bool(data_str) 
print("data : ", data_int, ",type =", type(data_str))
print("data : ", data_float, ",type =", type(data_str))
print("data : ", data_bool, ",type =", type(data_str))