## Late start

from pyqgis_scripting_ext.core import*

## EXCERCISE 2
extent = 6 # define widht of stripes
polygons = []
##Range function can take from 1 to 3 arguments: the third argument define the interval between items

for lon in range(-100, 100, extent):
    minX = lon
    maxX = lon + extent
    minY = -84 #UTM coordinates extent from -84 to 84 degrees of latitude
    maxY = 84
    
    coords = [[minX, minY], [minX, maxY], [maxX, maxY], [maxX, minY], [minX, minY]]
    polygon = HPolygon.fromCoords(coords)
    polygons.append(polygon)

canvas = HMapCanvas.new()

osm = HMap.get_osm_layer()
canvas.set_layers([osm])

for polygon in polygons:
    canvas.add_geometry(polygon)
    
canvas.set_extent([-100, -84, 100, 84])
canvas.show()