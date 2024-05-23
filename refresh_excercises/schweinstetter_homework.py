'''
How to hand it in:
for file paths: 
Ordner mit eigenem Namen (gezzipt): Data + Skripts

folder: path

path = f"{folder}/01_exe_rain_data_1year.txt"

'''

folder = "C:/users/aschw/OneDrive - Scientific Network South Tyrol/"

# Excercise 1

age = 25
name = "Mario Rossi"
activity = "skating"
job = "engineer"

print(f"Hei, I am {name}. I am {age} years old and I love {activity}. I work as an {job}.")


# Excercise 2

csvPath = f"{folder}/01_exe2_data.csv"

## Step by step (done in jupyterLab first)

with open(csvPath, "r") as file:
    lines = file.readlines()

for line in lines:
    print(line)

for line in lines:
    lineSplit = line.split(";")
    print(lineSplit)
    
# \n indicates the empty line so the line break respectively

for line in lines:
    line = line.strip()
    lineSplit_2 = line.split(";")    
    print(lineSplit_2)

for line in lines:
    analogString = lineSplit[0]
    analogSplit = analogString.split(":")
    x1 = float(analogSplit[1])
    print(x1)

for line in lines:
    maxvoltageString = lineSplit[1]
    y2 = float(maxvoltageString[11:])
    print(x1, y2)

for line in lines:
    maxanalogString = lineSplit[2]
    x2 = float(maxanalogString.split(":")[1])
    print(x1, x2, y2)
    

# Excercise 3

string = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s"

modified_string = string.replace(",", ";")

print(string)
print(modified_string)


# Excercise 4

list = [ 1, 2, 3, 4, 5]

for i in list:
    print(i)


# Excercise 5

list = [ 1, 2, 3, 4, 5]

for i in list:
    print(f"Number {i}")


# Excercise 6

list = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]

for i in list:
    if i <= 50:
        print(f"Number {i}")
        

# Excercise 7

list1 = [1, 2, 3, 4, 5]
list2 = ["first", "second", "third", "fourth", "fifth"]

for i, value in enumerate(list1):
    print(f"{list2[i]} is {value}")


# Excercise 8

string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum."""

## Character count with spaces
character_count = len(string)
print(f"The character count is: {character_count}.")

## Character count without spaces
string_without_spaces = string.replace(" ","")
print(f"The character count without spaces is: {len(string_without_spaces)}.")

## Word count

print(f"The word count is: {len(string.split())}.")


# Excercise 9

## Define the path
csvPath = f"{folder}/01_exe9_data.csv"

with open(csvPath, "r") as file:
    for line in file:
        ## remove whitespaces and comments that start with #
        if line.strip() and not line.startswith('#'):
            ## print the results
            print(line.strip())
            

# Excercise 10
## Path
csvPath = f"{folder}/01_exe9_data.csv"

with open(csvPath, "r") as file:
    for line in file:
        ## remove whitespaces and comments that start with #
        if line.strip() and not line.startswith('#'):
            ## Split the line into parts (delimeter = ",")
            parts = line.split(',')
            ## Extract the measurement part at pos 1 after the split
            measurement_str = parts[1].strip()
            ## Convert the measurement to a float and check if it's within the valid range
            if 0 < float(measurement_str) < 1000:
                ## Print valid data
                print(line.strip())
                

# Excercise 11

## Path
csvPath = f"{folder}/01_exe11_data.csv"

## Open the file
with open(csvPath, "r") as file:
    for line in file:
        ## Remove whitespaces
        line = line.strip()
        ## Split  line into two parts (delimiter = ";")
        parts = line.split(';')
        ## Define base and height by poistion in parts and then split again and only keep the 2nd part after the split + remove unit
        base_str = parts[0].split('=')[1].strip('cm')
        height_str = parts[1].split('=')[1]
        ## Convert base and height strings to floats for calculations
        base, height = float(base_str), float(height_str)
        ## Print
        print(f"base * height / 2 = {base} * {height} = {(base * height) / 2}cm2")


# Excercise 12

## data
who = {
"Daisy": 11,
"Joe": 201,
"Will": 23,
"Hanna": 44
}

what = {
44: "runs",
11: "dreams",
201: "plays",
23: "walks"
}

where = {
44: "to town.",
11: "in her bed.",
201: "in the livingroom.",
23: "up the mountain."
}

## who as a dictionary of tuples --> first part as defined in persion and 2nd in id that then assings the other values
sentences = [f"{person} {what[person_id]} {where[person_id]}" for person, person_id in who.items()]

## Print  sentences
for sentence in sentences:
    print(sentence)

# Excercise 12/2
##Daat
who = {
"Daisy": 11,
"Joe": 201,
"Will": 23,
"Hanna": 44
}

what = {
44: "runs",
11: "dreams",
201: "plays",
23: "walks"
}

where = {
"runs": "to town.",
"dreams": "in her bed.",
"plays": "in the livingroom.",
"walks": "up the mountain."
}

## Iterate over the IDs in the 'who' dictionary as above in the fstring
for person, person_id in who.items():
    # Get the action (what) corresponding to the ID
    action = what.get(person_id)
    
    # Get the location corresponding to the action ()
    location = where.get(action)
    
    # Print
    print(f"{person} {action} {location}")
 
 
# Excercise 13

## Data
list1 = ["a", "b", "c", "d", "e", "f"]
list2 = ["c", "d", "e", "f", "g", "h", "a"]
list3 = ["c", "d", "e", "f", "g"]
list4 = ["c", "d", "e", "h", "a"]

## Empty dictionary to store data
letter_counts = {}

## Iterate over each list
for list in [list1, list2, list3, list4]:
    ## Each letter in the lists
    for letter in list:
        ## Increment the count of the letter in letter_counts
        letter_counts.setdefault(letter, 0)
        letter_counts[letter] += 1

#print(letter_counts)

## Print count of each letter (sorted ensures alphabetical order)
for letter, count in sorted(letter_counts.items()):
    print(f"count of {letter} = {count}")
    
### for letter, count in sorted(letter_counts.items()):. In this loop, count is automatically assigned the value of the second element of each tuple returned by letter_counts.items()    


# Excercise 14

## Path
csvPath = f"{folder}/stations.txt"

with open(csvPath, "r") as file:
    for i in range(20):
        line = file.readline().strip()
        print(line)
        

# Excercise 15

## Path
csvPath = f"{folder}/stations.txt"

## Count of stations
station_count = 0

with open(csvPath, "r") as file:
    # Read the file line by line
    for line in file:
        station_count += 1

print(f"Number of stations: {station_count}")


# Excercise 16
## Path
csvPath = f"{folder}/stations.txt"

with open(csvPath, "r") as file:
    ## Read the first line of the file as a basis for the column count
    first_line = file.readline().strip()
    
    ## Split first line
    columns = first_line.split(',')
    
## Print the count of columns
print(f"Number of stations: {len(columns)}")


# Excercise 17

## Path
filePath = f"{folder}/stations.txt"

with open(filePath, "r") as file:
    ## Initialize count
    line_count = 0
    
    for line in file:
        ## Start line count
        line_count += 1
        
        ## Strip leading/trailing whitespace and split the line by comma
        parts = line.strip().split(',')
        
        ## Extract station ID and name from parts
        station_id = parts[0]
        station_name = parts[1]
        
        ## Print station ID and name
        print(f"Station ID: {station_id}, Station Name: {station_name}")
        
        ## Break  loop once 20 lines are printed
        if line_count >= 20:
            break
            

#Excercise 18

## Path
filePath = f"{folder}/stations.txt"

## Initialize variables
total_height = 0
station_count = 0

## Open the file in read mode
with open(filePath, "r") as file:
    
    ## Skip the header line
    next(file)
    
    ## Read the file line by line
    for line in file:
        ## Split the line and remove whitepspaces
        parts = line.strip().split(',')
        
        ## Extract the height (last column)
        height_str = parts[-1].strip()
        
        ## Convert height to float
        height = float(height_str)
            
        ## Add height to the total
        total_height += height
            
        ## Increment the station count
        station_count += 1

## Print
print(f"Average height of stations: {(total_height / station_count):.2f}")


#Excercise 19
## done wtih CHATGPT

## Path
filePath = "C:/users/aschw/OneDrive - Scientific Network South Tyrol/00_advanced_geomatics/stations.txt"

# Initialize variables
station_count = 0
total_height = 0
fields = set()
first_data_lines = []

# Open the file in read mode
with open(filePath, "r") as file:
    # Read the file line by line
    for line in file:
        # Increment station count for each line
        station_count += 1
        
        # Extract fields from the header line
        if station_count == 1:
            header_fields = line.strip().split(',')
            for field in header_fields:
                fields.add(field.strip())
        
        # Extract height from data lines
        if station_count <= 5:  # Consider first 5 data lines for summary
            first_data_lines.append(line.strip())

        # Extract height from each line (assuming it's the last column)
        parts = line.strip().split(',')
        height_str = parts[-1].strip()
        if height_str.isdigit() or (height_str[0] == '-' and height_str[1:].isdigit()):
            total_height += float(height_str)

# Calculate average height
average_height = total_height / station_count

# Print summary
print(f"File info: {filePath}")
print("-" * len(f"File info: {filePath}"))
print(f"Stations count: {station_count}")
print(f"Average value: {average_height:.0f}")
print("Available fields:")
for field in sorted(fields):
    print(f"-> {field}")
print("First data lines:")
for line in first_data_lines:
    print(line)

# Excercise 20

# Excercise 21

n = 10
m = 5

for x in range(n):
    print("*" * m)

# Excercise 22

n = 10
i=0

for x in range(n):
    print("*" * i)
    i += 1

#Excercise 23

n = 10
i=10

for x in range(n):
    print("*" * i)
    i -= 1

    
#Excercise 24

a = 10
sum = 0

for x in range(a):
    if x % 2 == 0:
        print(x)
        sum = sum + x

print(sum)


#Excercise 25

numbers = [123, 345, 5, 3, 8, 87, 64, 95, 9, 10, 24, 54, 66]

sum = 0

for num in numbers:
    if num % 2 == 0:
        print(num)
        sum = sum + num

print(f"The total sum is: {sum}")

#Excercise 26
## chatGPT

import csv

# Define the paths to the datasets
dataset1_path = f"{folder}/01_exe26_dataset1.csv"
dataset2_path = f"{folder}/01_exe26_dataset2.csv"

# Initialize dictionaries to store the data from each dataset
dataset1_data = {}
dataset2_data = {}

# Read and store data from dataset 1
with open(dataset1_path, "r") as file1:
    reader1 = csv.DictReader(file1)
    for row in reader1:
        dataset1_data[row["#id"]] = (row["x"], row["y"])

# Read and store data from dataset 2
with open(dataset2_path, "r") as file2:
    reader2 = csv.DictReader(file2)
    for row in reader2:
        dataset2_data[row["#id"]] = row["value"]

# Join the datasets based on the common id
for id_value in dataset1_data:
    if id_value in dataset2_data:
        print(f"id: {id_value}, value: {dataset1_data[id_value]}, x: {dataset2_data[id_value][0]}, y: {dataset2_data[id_value][1]}")























