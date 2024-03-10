capitals = {"Kenya":"Nairobi","USA":"Washigton D.C","China":"Beijing"} # {"key":"value"}making a dictionary
print(capitals.get("Kenya"))# to get a given value
update = capitals.update({"Rwanda":"Kigali"})
print(capitals)
remove = capitals.pop("China")
print(capitals)
keys = capitals.keys() #Get all keys in a dictionary
print(keys)
for key in capitals.keys():
    print(key)
values = capitals.values()
print(values)