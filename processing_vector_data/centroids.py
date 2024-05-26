from pyqgis_scripting_ext.core import*

# remove life saver map
HMap.remove_layers_by_name(["OpenStreetMap", "ne_50m_admin_0_countries"])

#Define paths
folder = "C:/github/my_first_repository/"
naturalEarth_path = folder + "natural_earth_vector.gpkg" #geopackage to be found at path
gpkg_path = folder + "pyQGIS_basics/centroids.gpkg"

# Define the layers within the gpkg that we want to use
countries = "ne_50m_admin_0_countries"

# reading an excisitng gpkg layer for france
countries_layer = HVectorLayer.open(naturalEarth_path, countries)

# add the life saver map
osm = HMap.get_osm_layer()
HMap.add_layer(osm)

# add the country and city layer
HMap.add_layer(countries_layer)

for feature in countries_layer.features(): # --> name is at index 4
    attributes = feature.attributes #attributes of this feature
    #print(attributes)

# Calculate centroids of countries
centroids = []

for feature in countries_layer.features():
    country_name = attributes[4]  # Index 4 contains the country name
    centroid = feature.geometry.centroid()
    centroids.append({'country': country_name, 'centroid': centroid})

### THIS IS NOT WORKING YET

for centroid in centroids:
    # Create a point geometry
    point = HPoint(lon,lat)
    
    # Add the feature to the layer
    dump_layer.add_feature(point, [])


error = dump_layer.dump_to_gpkg(gpkg_path, overwrite=True)

if(error): #error is NONE if there is no error
    print(error)
