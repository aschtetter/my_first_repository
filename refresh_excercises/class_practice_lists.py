# LISTS
## 1 Operations on lists
mylist = ["Merano", "Bolzano", "Trento"]
print(mylist)

print("The elements start at position 0:" + mylist[0])

mylist.append("Potsdam")
print(mylist)

mylist.remove("Potsdam")
print(mylist)

mylist.pop(0)
print(mylist)

## 2 Check if an argument is in a list
mylist = ["Merano", "Bolzano", "Trento"]

doIHaveBolzano = "Bolzano" in mylist
print(doIHaveBolzano)

# doIHavePotsdam = "Potsdam" in mylist
# print(doIHavePotsdam)

## 3 looping over lists
for item in mylist:
    print(item)
    
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]

for index in range(len(colors)):
    ratio = ratios[index]
    color = colors[index]
    print(f"{color} -> {ratio}")

## 4 Break and continue 
for i in range(10):
    if i == 5:
        break
    print(f"A) {i}")
    
for i in range(10):
    if i == 5:
        continue
    print(f"B) {i}")


## 5 Ranges
for i in range(0,10):
    print(f"A) {i}")

for i in range(10):
    print(f"B) {i}")
    
for i in range(0,10,2):
    print(f"C) {i}")
    
for i in range(10,0,-2):
    print(f"D) {i}")

## 6 Sorting
mylist = ["Merano", "Bolzano", "Trento"]
print( f"This is the original mylist: {mylist}" )

mylist.sort()
print( f"This is the sorted mylist: {mylist}" )

mylist.sort(reverse = True)
print( f"This is the reverse mylist: {mylist}" )

mylist = ["banana", "Orange", "Kiwi", "cherry"]

# in this case the asci order is followed; upper case alphabetically and then lower case alphabetically
mylist.sort()
print(f"A mixed case mylist, sorted: {mylist}")

# Before the sorting happens lowercase is applied to the list but only during the sorting process! Og list is not changed
mylist.sort(key = str.lower)
print(f"A mixed case mylist, properly sorted: {mylist}")

numlist = ["002", "01", "3", "004"]
def toInt(string):
    return int(string)

numlist.sort(key = toInt)
print(f"A formatted list of nums, properly sorted: {mylist}")

# Add on about numerical; passing on our own function for the conversion from str to int and then using it as key
numlist_1= ["002", "01", "3", "004"]

numlist_1.sort()
print(f"list_1 is: {numlist_1}")

numlist_2 = ["002", "01", "3", "004"]

def toInt(string):
    return int(string)
    
numlist_2.sort(key = toInt)
print(f"list_2 is: {numlist_2}")

## 7 Last about lists

abc = ["a", "b", "c"]
cde = ["c", "d", "e"]
newabcde = abc + cde
print( newabcde )

print( ";".join(newabcde) )
print( " | ".join(newabcde) )

nums = [1.0, 2, 3.5, 6, 11, 34, 12]
print( max(nums) )
print( min(nums) )
print( sum(nums) )

#excercise
avg = sum(nums)/len(nums)
print(avg)

# calculate the average in a loop
total_sum = 0
count = 0
for num in nums:
    total_sum += num
    count += 1
print(f"The average is: {total_sum/count:.2f}")

# extra excercise variance


    
    