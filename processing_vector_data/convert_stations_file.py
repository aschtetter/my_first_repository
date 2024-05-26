from pyqgis_scripting_ext.core import*

# Define paths
folder = "C:/github/my_first_repository/"
filepath = folder + "pyQGIS_basics/stations.txt"
gpkg_path = folder + "pyQGIS_basics/stations.gpkg"

dump_layer = HVectorLayer.new("stations", "Point", "EPSG:4326", fields) # Name of the layer, geometry type and projection   

fields = {
    "STAID": "Integer",
    "STANAME": "String",
    "CN": "String",
    "LAT": "Float",
    "LON": "Float",
    "HGHT": "Float"
}

# Read the file and parse the data
with open(filepath, "r") as file:
    lines = file.readlines()

for line in lines[1:10]:
    line = line.strip().split(",")
    
    sta_id = line[0]
    sta_name = line[1]
    cn = line[2]
    hght = line[5]
    
    # Split the latitude and longitude strings and remove any "+" symbols
    lat = line[3].strip("+")
    lon = line[4].strip("+")

    # Split the latitude and longitude strings into degrees, minutes, and seconds parts
    lat = lat.split(":")
    lon = lon.split(":")

    # Convert minutes and seconds to fractions of degrees
    lat_min = float(lat[1]) / 60
    lon_min = float(lon[1]) / 60
    lat_sec = float(lat[2]) / 3600
    lon_sec = float(lon[2]) / 3600

    # Calculate the final latitude and longitude in decimal degrees
    lat = float(lat[0]) + lat_min + lat_sec
    lon = float(lon[0]) + lon_min + lon_sec
    
    # Create a point geometry
    point = HPoint(lon,lat)
    
    # Add the feature to the layer
    dump_layer.add_feature(point, [sta_id, sta_name, cn, lat, lon, hght])


error = dump_layer.dump_to_gpkg(gpkg_path, overwrite=True)

if(error): #error is NONE if there is no error
    print(error)