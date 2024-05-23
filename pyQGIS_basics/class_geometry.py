from pyqgis_scripting_ext.core import *

point = HPoint(30.0, 10.0)

## print as well known text for presentation
# print(point)
print(point.asWkt())

coords = [[31,11], [10,30], [20,40], [40,40]]
line = HLineString.fromCoords(coords)
print(line.asWkt())

##a polygon is created using a closed linestring. This will be the exterior ring of the polygon.

coords = [[32,12], [10,20], [20,39], [40,39], [32, 12]]
polygon = HPolygon.fromCoords(coords)
print(polygon)


## DONUT --> erster und letzter Punkt gleich damit Polygon geschlossen wird!
exteriorPoints = [[35,10],[10,20],[15,40],[45,45],[35,10]]
holePoints = [[20,30],[35,35],[30,20],[20,30]]

## Create the polygon using the exterior ring.
polygonWithHole = HPolygon.fromCoords(exteriorPoints)

## Create the whole ring
holeRing = HLineString.fromCoords(holePoints)

## Add the hole ring to the polygon
polygonWithHole.add_interior_ring(holeRing)
print(polygonWithHole.asWkt())

'''
## Get the bound of a polygon
# the external bound of a polygon can be retrieved as an HLineString through the exteriorRing attribute
print(polygonWithHole.exterior_ring().asWkt())
# since the interior rings can be several, their count can be
obtained…
print("hole count:", polygonWithHole.interior_rings_count())
# and through the index of the ring, the line of the hole
print(polygonWithHole.interior_ring(0).asWkt())
'''

# Multis
## Multipoints --> Mehrere Punkte z. B. Städte
coords = [[10,40],[40,30],[20,20],[30,10]]
multiPoints = HMultiPoint.fromCoords(coords)

## MultiLineAlignment --> z. B. Straßennetz
coords1 = [[10,10],[20,20],[10,40]]
coords2 = [[40,40],[30,30],[40,20],[30,10]]
multiLine = HMultiLineString.fromCoords([coords1, coords2])

## Multi polygon from coords
coords3 = [[30,20], [10,40], [45,40], [30,20]]
coords4 = [[15,5], [40,10], [10,20], [5,10], [15,5]]
multiPolygon_coord = HMultiPolygon.fromCoords([coords3, coords4])


## Multipolygon from two polygons!
polygon1 = HPolygon.fromCoords(coords3)
#polygon1.add_interior_ring(holeRing)
polygon2 = HPolygon.fromCoords(coords4)
multiPolygon = HMultiPolygon([polygon1, polygon2])

## subGeometries
subGeometries = multiPolygon_coord.geometries()
colorsList = {'red', 'blue', 'green'}

subGeometries = multiPolygon.geometries()
for i in range(len(subGeometries)):
    child = subGeometries[i]
    print(f"polygon at position {i} = {child.asWkt()}")


'''
## Coordinate
for i, coordinate in enumerate(polygon.coordinates()):
    print(f"coord {i}) x={coordinate[0]}, y={coordinate[1]}")
for i, coordinate in enumerate(line.coordinates()):
    print(f"coord {i}) x={coordinate[0]}, y={coordinate[1]}")
'''




## CANVAS
canvas = HMapCanvas.new()
#canvas.add_geometry(point, "red", 2)
#canvas.add_geometry(line, "blue", 2)
#canvas.add_geometry(polygon, "green", 2)
#canvas.add_geometry(polygonWithHole, "purple", 0.5)

#canvas.add_geometry(multiPoints, "lightblue", 100)
#canvas.add_geometry(multiLine, "yellow", 20)
canvas.add_geometry(multiPolygon_coord, "orange", 3)
canvas.add_geometry(multiPolygon, "black", 4)

## zoom to layer
canvas.set_extent([0, 0, 50, 50])
canvas.show()

