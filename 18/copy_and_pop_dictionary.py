# copy dictionary 

teman_teman = {
  "mad" : "ahmad",
  "mat" : "rahmat",
  "sep" : "asep"
}

friends = teman_teman.copy()
print(f"teman-teman : {teman_teman}\n")
print(f"friends : {friends}\n")

teman_teman["mad"] = "mamad"
print(f"teman-teman : {teman_teman}\n")
print(f"friends : {friends}\n")

# pop dictionary
dataAsep = friends.pop("sep")
print(f"dataAsep : {dataAsep}\n")
print(f"friends : {friends}\n")

# ppoitem dictionary
dataTerakhir = friends.popitem()
print(f"dataTerkhir : {dataTerakhir}\n")
print(f"friends : {friends}\n")
