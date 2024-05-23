from pyqgis_scripting_ext.core import *


file = "C:/users/aschw/OneDrive - Scientific Network South Tyrol/00_advanced_geomatics/22yr_T10MN"
folder = "C:/users/aschw/OneDrive - Scientific Network South Tyrol/00_advanced_geomatics/"

geopackagePath = folder + "natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"
countriesLayer = HVectorLayer.open(geopackagePath, countriesName)

#------------
#Definitions

countries = ["Germany", "Austria", "Italy", "Switzerland", "Poland"]
colors = ["purple", "darkblue", "blue", "lightblue", "turquoise", "lightgreen", "green", "yellow", "orange" ,"red", "brown"]


def conversion_test(line):
    try:
        float(line)
        return True
    except ValueError:
        return False

#-------------

crsHelper = HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(3857)


with open (file, 'r') as file:
    lines = file.readlines()
     
canvas = HMapCanvas.new() 
osm = HMap.get_osm_layer()
canvas.set_layers([osm])

segments = {}
segment_list = []

for country in countries:

    nameIndex = countriesLayer.field_index("NAME")
    countriesFeatures = countriesLayer.features()
    for feature in countriesFeatures:
        name = feature.attributes[nameIndex]
        if name == country:
            countryGeom = feature.geometry
            countryGeom = crsHelper.transform(countryGeom)
            break
                

    for line in lines:
        lineStrip = line.strip()
        lineSplit = lineStrip.split(' ')
        annualAverage = lineSplit[-1]
        
        if conversion_test(lineSplit[0]) == False or conversion_test(lineSplit[1]) == False:
            continue
        elif annualAverage == "":
            continue
        annualAverage = float(annualAverage)
        
        Lon = float(lineSplit[0])
        Lat = float(lineSplit[1])
        
        coords = [[Lat, Lon],[Lat+1, Lon],[Lat+1, Lon+1],[Lat, Lon+1],[Lat, Lon]]
        polygon = HPolygon.fromCoords(coords)
        polygon = crsHelper.transform(polygon)
        
        if polygon.intersects(countryGeom):
            polygon = polygon.intersection(countryGeom)
            segments[polygon] = annualAverage
            segment_list.append(polygon)


#segmentation of the segments

steps = (max(segments.values()) - min(segments.values()))/ len(colors)


count = min(segments.values())+ steps

color_range = {}

for color in colors:
    color_range[color] = count
    count += steps
    

for key, value in segments.items():
    for color, threshold in color_range.items():
        if value <= threshold:
            assigned_color = color
            break
    
    canvas.add_geometry(key, assigned_color)
    
    
#bounding box
hull = HGeometryCollection(segment_list).convex_hull()

canvas.set_extent(hull.bbox())
canvas.show()
