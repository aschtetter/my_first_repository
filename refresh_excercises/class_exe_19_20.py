# Combining two files? Station data and precipitaction data, EXCERCISE 19 and 20


def fileSummary (path, ifFieldName, avgFieldName):
    with open (path, "r") as file:
        lines = file.readlines()
    
    # just to have it defined somewhere, theoretically it could also just be defined in the for loop
    idIndex = None # we could also set it to any other value really
    analyzeIndex = None
    hSum = 0 # this will be incremented meaning we don't want to check if it already exists and can just work with
    count = 0
    uniqueIdsList = []
    
    for line in lines:
        line = line.strip()
        if line.startswith("#"): #we have the header (=fields)
            fields = line.strip("#").split(",") # here we strip the first line of # and then split it so we have the headers
            
            for index, field in enumerate(fields): # index is the postion
                field = field.strip()
                if field == ifFieldName:
                    idIndex = index
                elif field == avgFieldName:
                    analyzeIndex = index
                
            # print(idIndex, analyzeIndex)
            
        else:
            # HERE DATA STARTS
            lineSplit = line.split(",")
            value = float(lineSplit[analyzeIndex])
            if value != -9999: # just to rule out any missing data
                hSum += value
                count += 1
            
            idValue = lineSplit[idIndex]
            if idValue not in uniqueIdsList:
                uniqueIdsList.append(idValue)
                
    print(f" This is the list of all unique countries: {uniqueIdsList}")
    print(f"This sums up to {len(uniqueIdsList)} different countries.")
            
    avg = hSum/count
    
    print(f"File info: {path}")
    print("=====")
    print(f"Average value of field {avgFieldName}: {avg}")
    print("Fields:")
    for field in fields:
        print(f" --> {field.strip()}")
            
        
    
    
    

# This will overwrite the existing files /add to it

fileSummary("C:/users/aschw/OneDrive - Scientific Network South Tyrol/00_advanced_geomatics/station_data.txt","STAID", "RR")
print("********")
fileSummary("C:/users/aschw/OneDrive - Scientific Network South Tyrol/00_advanced_geomatics/stations.txt","CN", "HGHT")
