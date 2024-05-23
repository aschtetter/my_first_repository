# DICTIONARIES
## 12 Create, get, add, remove
townsProvinceMap = {"merano":"BZ", "bolzano":"BZ", "trento":"TN"}
print(townsProvinceMap["merano"])

townsProvinceMap["Potsdam"] = "BR"
print(townsProvinceMap)

townsProvinceMap.pop("Potsdam")
print(townsProvinceMap)

## 13 What if an item doesn't exist
if townsProvinceMap.get("Merano") is None:
    print("The key doesn't exist")
else:
    print("The key exists")

print( townsProvinceMap.get("merano", "unknown") )

## 14 Looping dictionaries
for key, value in townsProvinceMap.items():
    print( key + " is in province of " + value )
    
## 15 Keys and values
print( townsProvinceMap.keys() )
print( townsProvinceMap.values() )

# conversion of dictioniary (any iterable object; loopable) into list
towns = list(townsProvinceMap.keys())
towns.sort()

# for key in keys
for town in towns:
    print( town + " is in province of " + townsProvinceMap[town] )
    
## 16 A pattern you need to learn
myText = """
We would like to know how many times
every character appears in this text.
"""
charDictionary = {}
for character in myText.strip():
    count = charDictionary.get(character, 0)
    count += 1
    charDictionary[character] = count
for key, value in charDictionary.items():
    if key == " ":
        key = "The space"
    elif key == "\n":
        key = "The newline"
    print(key, "appears", value, "times.")