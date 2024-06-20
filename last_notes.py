'''

provincesLayer.subset_filter("iso_a2='IT'") # defining a string inside a notstring

regionIndex = provincesLayer.field_index("region") # we ask the provinces layer for the index of the column where region is

pass in if loop --> just pass and continure in the next line 
vs.
continure in if loop --> jumps to the beginning of the loop (if embedded in a for loop)



if regionGeometry:
    regionGeometry...

=

if regionGeometry != None:
    regionGeometry = regionGeometry.union(geometry) # if there's nothin in it the union doesn't happen
    

for name, geom in regionName2GeometryMap.items():
    print(name, geom.asWkt()[:20]) -> prints name and geometry (as coordinates) of the regions


CSV

totalCases = int(lineSplit[17]) --> everything you read from a csv file will first be a string


day2featuresMap = {} --> day as key that then opens a list with geometry, total cases and name of the region





for day, featureslist in day2featuresMap.items():
    if day != "2020-04-01": #this line ensures that we only work with that one day for now
        continue
    
    print("Generating day:", day)
    newLayerName = "covid_italy"
    HMap.remove_layer_by_name([newLayerName])



for geometry, attributes in featuresList:   # since this is a list with tuples

  
mapProperties = {

}

printer.add_map(**mapProperties) #this just accesses the map properties so we don't have to define it in the ()


png better than jpg for vector data; jpg better for images and photgraphy

'''