# kalkulator sederhana

print("kalkulator Sederhana".center(10))
print(20*"=")

angka_1 = float(input("masukan angka 1: "))
operator = input("masukan operator (+, -, *, /): ")
angka_2 = float(input("masukan angka 2: "))

if operator == "+":
  print(f"{angka_1} {operator} {angka_2} = {angka_1 + angka_2}")
elif operator == "-":
  print(f"{angka_1} {operator} {angka_2} = {angka_1 - angka_2}")
elif operator == "*":
  print(f"{angka_1} {operator} {angka_2} = {angka_1 * angka_2}")
elif operator == "/":
  print(f"{angka_1} {operator} {angka_2} = {angka_1 / angka_2}")
else:
  print("Invalid operator")
