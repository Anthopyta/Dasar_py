# tyoe hits pada fungsi 

# penggunaan type hints

def fungsi_dengan_hints(argument:int) -> int:
  output = 10**argument
  return output

hasil = fungsi_dengan_hints(2)
print(hasil)


import string

def display(argument:string) -> string:
  print(argument)
  
display(10)
