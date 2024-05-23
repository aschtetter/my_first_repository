from pyqgis_scripting_ext.core import *

# cleanup
HMap.remove_layers_by_name(["OpenStreetMap"]) #removes lyers if they're already loaded; useful wehn running the script multiple times
HMap.remove_layers_by_name(["ne_50m_populated_places"])
HMap.remove_layers_by_name(["test"])

folder = "C:/users/aschw/OneDrive - Scientific Network South Tyrol/00_advanced_geomatics/"


geopackagePath = folder + "natural_earth_vector.gpkg" #naming convention Anna!!!!
countriesName = "ne_50m_admin_0_countries"
citiesName = "ne_50m_populated_places"

# load osm tiles layer
osm = HMap.get_osm_layer()
HMap.add_layer(osm)

# load the countries layer
countriesLayer = HVectorLayer.open(geopackagePath, countriesName)


print("Schema (first 4 fields):")

counter = 0
for name, type in countriesLayer.fields.items():
    counter += 1
    if counter < 5:
        print("\t", name, "of type", type)

crs = countriesLayer.prjcode
print("Projection: ", crs)
print("Spatial extent:", countriesLayer.bbox()) # whole world
print("Feature count:", countriesLayer.size()) #number of countries in the world


## This is where we picked up
print("Attributes for Italy:")
nameIndex = countriesLayer.field_index("NAME")
#print(nameIndex)
countriesFeatures = countriesLayer.features()
for feature in countriesFeatures:
    if feature.attributes[nameIndex] == 'Italy':
        geometry = feature.geometry
        print("Geom:", geometry.asWkt()[:50] + "...")

'''
print("Attributes for Italy:")
countriesFeatures = countriesLayer.features()
nameIndex = countriesLayer.field_index("NAME")
fieldNames = countriesLayer.field_names
for feature in countriesFeatures:
    if feature.attributes[nameIndex] == 'Italy':
        geom = feature.geometry # get the geometry
        print("GEOM:", geom.asWkt()[:50] + "...")
        count = 0
        for index, attribute in enumerate(feature.attributes):
            print(fieldNames[index] + ":", attribute)
            count += 1
            if count > 5:
                print("...")
                break
'''



        
# Filters using expressions
## 

expressions = "NAME like 'I% AND POP_EST > 300000" #name --> column in attrbiute table; I% --> if name matches anything with an uppercase I and anything after that AND population größer
filteredCountriesFeatures = countriesLayer.features(expressions)
count = 0
for feature in filteredCountriesFeatures:
    print(feature.attributes[nameIndex])
    count +=1
print("Feature count with filter", count)

lon = 11.119982
lat = 46.080428
point = HPoint(lon,lat)
buffer = point.buffer(2) #2 degrees

citiesLayer = HVectorLayer.open(geopackagePath, citiesName) # load the cities layer
HMap.add_layer(citiesLayer)

citiesNameIndex = citiesLayer.field_index("NAME")
aoi = buffer.bbox()

count = 0
for feature in citiesLayer.features(bbox=aoi):
    print(feature.attributes[citiesNameIndex])
    count+=1
print("Cities features listed:", count)

count = 0
for feature in citiesLayer.features(geometryfilter=buffer):
    print(feature.attributes[citiesNameIndex])
    count+=1
print("Cities features listed with geometry filter:", count)


# CREATE DATA
## create a schema
fields = {
    "id": "Integer",
    "name": "String"
}
just2citiesLayer = HVectorLayer.new("test", "Point", "EPSG:4326", fields)
just2citiesLayer.add_feature(HPoint(-122.42, 37.78), [1, "San Francisco"])
just2citiesLayer.add_feature(HPoint(-73.98, 40.47), [2, "New York"])

path = folder + "test.gpkg"
error = just2citiesLayer.dump_to_gpkg(path, overwrite=True) #at first overwrite \True, later false so that geopackage databse still contains previous files
if error:
    print(error)

testLayer = HVectorLayer.open(path, "test")
#HMap.add_layer(testLayer)


'''
path = folder + "test.shp"
error = just2citiesLayer.dump_to_shp(path, overwrite=True)
'''

HMap.add_layer(just2citiesLayer)

# Create a new schema
fields = { #bewusster overwrite, weil wir es von davor nicht mehr brauchen
    "name": "String",
    "population": "Integer",
    "lat": "double",
    "lon": "double"
}

oneCityMoreAttributes = HVectorLayer.new("test2", "Point", "EPSG:4326", fields)
oneCityMoreAttributes.add_feature(HPoint(-73.98, 40.47), \
                            ["New York", 19040000, 40.47, -73.98])

error = oneCityMoreAttributes.dump_to_gpkg(path, overwrite=False)
if(error):
    print(error)

