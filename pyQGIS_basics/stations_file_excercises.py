from pyqgis_scripting_ext.core import*


## EXCERCISE 02: Plot stations file
path = "C:/users/aschw/OneDrive - Scientific Network South Tyrol/00_advanced_geomatics/stations.txt"

with open(path, "r") as file:
    lines = file.readlines()
    
points=[] #list
country_counts={} #dictionary
names = []

for line in lines:
    if len(line) == 0 or line.startswith('#'): # general parsing, empty lines and # can be ignored
            continue
    
    line = line.strip().split(",") # remove whitespaces and split lines
    
    lat = line[3].split(":") #lat is split in 3 by the delimeter :
    lon = line[4].split(":")
    
    LAT = float(lat[0])+float(lat[1])/60+float(lat[2])/3600
    LON = float(lon[0])+float(lon[1])/60+float(lon[2])/3600
    
    point = HPoint(LON, LAT)
    points.append(point)
    
    ## Country count
    country = line[2]
    
    if country in country_counts:
        country_counts[country] += 1
    
    # If the country is not in the dictionary, initialize its count to 1
    else:
        country_counts[country] = 1
        
    ## Name of the station
    name = line[1].strip()
    names.append(name)

# Just checking
#for point in points[:10]:
    #print(point.asWkt()) # as well known text

# Define transformmation
crsHelper = HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(3857)

points_transformed = []

for point in points:
    point_transform = crsHelper.transform(point)
    # print(f"{point} in EPSG:4326 transforms to {point_transform} in EPSG:3857.")
    points_transformed.append(point_transform)


# ## EXCERCISE 02.1: Print station count
# for country, count in sorted(country_counts.items()):
#     print(country + ": " + str(count))


# ## EXCERCISE 03: Find nearest station to university
# ref_point = HPoint(11.34999, 46.49809)
# ref_point_transform = crsHelper.transform(ref_point)

# ## With the help of CHATGPT
# # Calculate distances between reference point and all stations
# nearest_station_name = None
# min_distance = float('inf')  # Initialize with infinity

# for point, name in zip(points_transformed, names):  #zip to combine
#     distance = ref_point_transform.distance(point)
#     if distance < min_distance:
#         min_distance = distance
#         nearest_station_name = name

# print(f" Nearest station: {nearest_station_name} with the coordinates: {nearest_station}")  # This will print the nearest station object


## EXCERCISE 4: Find stations within a radius (buffer)

radius_km = 50
radius_m = radius_km*1000

buffer = ref_point_transform.buffer(radius_m)

for point, name in zip(points_transformed, names):  #zip to combine
    if buffer.contains(point):
        print(f"This station is within a {radius_km} km radius of the university: {name} ({point}). The exact distance are {float(((ref_point_transform.distance(point))/1000)):.1f} km.")
        

'''
## CANVAS
canvas = HMapCanvas.new()
# Load osm base map
osm = HMap.get_osm_layer()
canvas.set_layers([osm])

# Add transformed points
for point in points_transformed:
    canvas.add_geometry(point, "magenta", 1) # add_geometry only takes single geometry as parameter --> pass each point (alternative creat MultiPoint)

# Add ref point
canvas.add_geometry(ref_point_transform,"blue", 2)

# Add radius
canvas.add_geometry(buffer,"yellow", 1)


# Calculate the extent of the points
min_lon = min(point.x for point in points_transformed)
max_lon = max(point.x for point in points_transformed)
min_lat = min(point.y for point in points_transformed)
max_lat = max(point.y for point in points_transformed)

canvas.set_extent([min_lon, min_lat, max_lon, max_lat])

canvas.show()
'''