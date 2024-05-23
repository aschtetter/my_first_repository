# Define path
filepath = r"C:\Users\aschw\OneDrive - Scientific Network South Tyrol\00_advanced_geomatics\02_exe_rain_data_1year.txt"

## read the data into a lines list
with open(filepath, "r") as file:
    lines = file.readlines()

## print out first 5 lines (my solution)
#print(lines[:4])

## print out first 5 lines
#for line in lines[:5]:
    #print(line)

date2ValuesListMap = {}

## print out first 5 lines
for line in lines:
    line = line.strip() #removes empty spaces, cleans up (\n for instance)
    if line.startswith("#") or len(line) == 0: # we don't want to evaluate lines that start with # or 0
        continue #starting over from where we left off
        
    ## parse each line to extract the date (str) and value(num)
    lineSplit = line.split(",")
    date = lineSplit[0]
    value = float(lineSplit[1])
    
    ## extract the year-month from the date
    month = date[:-2]
    # print(month, ":", value)

    ## aggreagte the values by month, i.e. collect all values
    ## for each date in a list
    values = date2ValuesListMap.get(month, [])
    values.append(value)
    date2ValuesListMap[month] = values
    
for month, values in date2ValuesListMap.items():
    #print(date2ValuesListMap)
    cumRain = sum(values)
    print(f"Cumulated rain for month {month} is {cumRain}.")
