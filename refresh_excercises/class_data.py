# Handling txt files
## r in front of file path so that slashes will be interpreted as string and not as special character
filepath = r"C:\Users\aschw\OneDrive - Scientific Network South Tyrol\00_advanced_geomatics\02_data.txt"

data = """# station id, datetime, temperature
1, 2023-01-01 00:00, 12.3
2, 2023-01-01 00:00, 11.3
3, 2023-01-01 00:00, 10.3"""

with open(filepath, "w") as file:
    file.write(data)
    
# "w" write data into file: "a" append to the existing file
with open(filepath, "a") as file:
    file.write("\n1, 2023-01-02 00:00, 9.3")
    file.write("\n2, 2023-01-02 00:00, 8.3")
    
## Reading files
with open(filepath, "r") as file:
    lines = file.readlines()

stationCount = {}

for line in lines:
    line = line.strip() #removes empty spaces, cleans up (\n for instance)
    if line.startswith("#") or len(line) == 0: # we don't want to evaluate lines that start with # or 0
        continue
    stationId = line.split(",")[0] #extract station ID
    count = stationCount.get(stationId, 0) #station count as key --> station ID
    count += 1
    stationCount[stationId] = count
    
    print(stationCount)

for key, value in stationCount.items():
    print(f"Station {key} appears {value} times.")