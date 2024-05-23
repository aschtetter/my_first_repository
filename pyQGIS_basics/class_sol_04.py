## EXCERCISE 04: find all stations within a buffer

from pyqgis_scripting_ext.core import*

# define necessary functions (on top because py is a interpreted language not a compiling language)

def fromLatString(latString):
    sign = latString[0]
    latDegrees = float(latString[0:3])
    latMinutes = float(latString[4:6])
    latSeconds = float(latString[7:9])
    lat = latDegrees + latMinutes/60 + latSeconds/3600
    if sign == "-":
        lat = lat * -1
    return lat
 
def fromLonString(lonString):
    sign = latString[0]
    lonDegrees = float(lonString[1:4])
    lonMinutes = float(lonString[5:7])
    lonSeconds = float(lonString[8:10])
    lon = lonDegrees + lonMinutes/60 + lonSeconds/3600
    if sign == "-":
        lon = lon * -1
    return lon


# Here the actual script begins

lon = 11.34999
lat = 46.49809

centerPoint = HPoint(lon,lat)

stationsfile = "C:/users/aschw/OneDrive - Scientific Network South Tyrol/00_advanced_geomatics/stations.txt"

with open(stationsfile, "r") as file:
    lines = file.readlines()
    
crsHelper = HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(32632)

centerPoint32632 = crsHelper.transform(centerPoint)

radiusKm = 20

buffer = centerPoint32632.buffer(radiusKm*1000)

for line in lines[1:]:
    line = line.strip()
    
    lineSplit = line.split(",")
    name = lineSplit[1].strip()
    latString = lineSplit[3]
    lonString = lineSplit[4]
    
    latDec = fromLatString(latString)
    lonDec = fromLonString(lonString)
    
    point = HPoint(lonDec,latDec)
    point_32632 = crsHelper.transform(point)
    
    if buffer.intersects(point_32632):
        distance = point_32632.distance(centerPoint32632)
        print(name, distance/1000, point)