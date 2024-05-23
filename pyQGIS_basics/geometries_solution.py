from pyqgis_scripting_ext.core import*

#Exercise 1
path = "C:/users/aschw/OneDrive - Scientific Network South Tyrol/00_advanced_geomatics/02_exe0_geometries.csv"

with open(path, 'r') as file:
    readLines = file.readlines()

points = [] #It collects already defined points
lines = [] #It collects a list of coordinates
polygons = []
for line in readLines:
    line = line.strip()
    split = line.split(";")
    gtype = split[0]
    coords = split[1]
    num = split[2]
    
    if gtype == "point":
        cSplit = coords.split(",")
        lon = float(cSplit[0])
        lat = float(cSplit[1])
        point = HPoint(lon, lat)
        points.append(point)
    elif gtype == "line":
        cSplit = coords.split(" ")
        pointList = []
        for cStr in cSplit:
            split = cStr.split(",")
            lon = float(split[0])
            lat = float (split[1])
            pointList.append([lon, lat])
        line = HLineString.fromCoords(pointList)
        lines.append(line)
    elif gtype == "polygon":
        cSplit = coords.split(" ")
        pointList = []
        for cStr in cSplit:
            split = cStr.split(",")
            lon = float(split[0])
            lat = float (split[1])
            pointList.append([lon, lat])
        polygon = HPolygon.fromCoords(pointList)
        polygons.append(polygon)


canvas = HMapCanvas()

for point in points:
    canvas.add_geometry(point, "magenta", 50)

for line in lines:
    canvas.add_geometry(line, "blue", 3)
    
for polygon in polygons:
    canvas.add_geometry(polygon, "red", 1)
    
bounds = [0, 0, 50, 50]
canvas.set_extent(bounds)
canvas.show()