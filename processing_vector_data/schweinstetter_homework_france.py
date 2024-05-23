from pyqgis_scripting_ext.core import*

# remove life saver map
HMap.remove_layers_by_name(["OpenStreetMap", "other map"])

HMap.remove_layers_by_name(['ne_50m_populated_places'])
HMap.remove_layers_by_name(['ne_50m_admin_0_countries'])

#Define paths
folder = "C:/users/aschw/OneDrive - Scientific Network South Tyrol/00_advanced_geomatics/"
geopackagePath = folder + "00_natural_earth_vector.gpkg" #geopackage to be found at path

# Define the layers within the gpkg that we want to use
countries = "ne_50m_admin_0_countries"
cities = "ne_50m_populated_places" #cultural

# add the life saver map
osm = HMap.get_osm_layer()
HMap.add_layer(osm)

# reading an excisitng gpkg layer for france
countries_layer = HVectorLayer.open(geopackagePath, countries)
cities_layer = HVectorLayer.open(geopackagePath, cities)

# add the country and city layer
HMap.add_layer(countries_layer)
HMap.add_layer(cities_layer)

# Identifying the France polygon and saving it as a geometry
#country_polygon = None

country_nameIndex = countries_layer.field_index("ADMIN")
countries_features = countries_layer.features()
# print(country_nameIndex) # --> 10. Spalte



for feature in countries_features:
    country_name = feature.attributes[country_nameIndex]
    # print(country_name) #only returns Zimbabwe
    if country_name == "France":
        country_polygon = feature.geometry
        break # exit loop once country is found
    #else:
        #print("Country not found.")
        

# Iterate through cities to see whcih ones intersect with France
print("Cities:")

city_nameIndex = cities_layer.field_index("NAME")
cities_features = cities_layer.features()
# print(city_nameIndex) #--> 5. Spalte


cities = []

for feature in cities_features:
    city_geometry = feature.geometry
    city_name = feature.attributes[city_nameIndex]
    
    if country_polygon.intersects(city_geometry):
        print(city_name)
        cities.append(city_name)
    #else:
        #print("No cities found.")
print(f"There are {len(cities)} in France.")