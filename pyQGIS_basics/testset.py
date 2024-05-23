from pyqgis_scripting_ext.core import *

## Define geometriees
g1 = HPolygon.fromCoords([[0, 0], [0, 5], [5, 5], [5, 0], [0, 0]])
g2 = HPolygon.fromCoords([[5, 0], [5, 2], [7, 2], [7, 0], [5, 0]])
g3 = HPoint(4, 1)
g4 = HPoint(5, 4)
g5 = HLineString.fromCoords([[1, 0], [1, 6]])
g6 = HPolygon.fromCoords([[3, 3], [3, 6], [6, 6], [6, 3], [3, 3]])


## The envelope of a geometry
print("polygon bbox:", g1.bbox())

## Length, area and distance
print("polygon length:", g1.length())
print("polygon area:", g1.area())

print("line length:", g5.length())
print("line area:", g5.area())

print("point length:", g3.length())
print("point area:", g3.area())

print("distance between line and point:", g5.distance(g4))

## PREDICATES
## Intersect
print("Intersects")
print(g1.intersects(g2)) # true
print(g1.intersects(g3)) # true
print(g1.intersects(g4)) # true
print(g1.intersects(g5)) # true
print(g1.intersects(g6)) # true

## touches
print("touches")
print(g1.touches(g2)) # true
print(g1.touches(g3)) # false
print(g1.touches(g4)) # true
print(g1.touches(g5)) # false
print(g1.touches(g6)) # false

## contains
print("contains")
print(g1.contains(g2)) # false
print(g1.contains(g3)) # true
print(g1.contains(g4)) # false
print(g1.contains(g5)) # false
print(g1.contains(g6)) # false


## FUNCTIONS
print("intersection")
print(g1.intersection(g6))
print(g1.intersection(g2)) # touching polygons -> line
print(g1.intersection(g3)) # polygon and point -> point
print(g1.intersection(g5)) # polygon and line -> line

newGeom = g1.intersection(g6)

print("symdifference")
print(g1.symdifference(g6))
print(g1.symdifference(g2)) # touching polygons -> line
print(g1.symdifference(g3)) # polygon and point -> point
print(g1.symdifference(g5)) # polygon and line -> line

newGeom = g1.symdifference(g6)

print("union")
print(g1.union(g6))
print(g1.union(g2)) # touching polygons -> line
print(g1.union(g3)) # polygon and point -> point
print(g1.union(g5)) # polygon and line -> line

newGeom = g1.union(g6)

print("difference")
print(g6.difference(g1))
print(g6.difference(g5))

newGeom = g1.difference(g6)

print("buffers")
b1 = g3.buffer(1.0) # the buffer of a point, automatically assumes a buffer (sphere) with 8 corners
b2 = g3.buffer(1.0, 1) # the buffer of a point with few quandrant segments
b3 = g5.buffer(1.0) # line buffer
b4 = g5.buffer(1.0, 2) # line buffer with few points
# square end cap style (flat, square, round)
b5 = g5.buffer(1.0, -1, JOINSTYLE_ROUND, ENDCAPSTYLE_SQUARE)

print("convexhull") # useful to define the bounding box!!!
collection = HGeometryCollection([g1, g2, g3, g4, g5, g6])
hull = collection.convex_hull()



## CANVAS
canvas = HMapCanvas.new()

canvas.add_geometry(g1, 'black', 3)
canvas.add_geometry(g2, 'black', 3)
canvas.add_geometry(g6, 'black', 3)
canvas.add_geometry(g5, 'black', 3)
canvas.add_geometry(g3, 'black', 10)
canvas.add_geometry(g4, 'black', 10)

#canvas.add_geometry(newGeom, 'yellow', 2)

# canvas.add_geometry(b1, 'yellow', 2)
# canvas.add_geometry(b2, 'blue', 2)
# canvas.add_geometry(b3, 'red', 2)
# canvas.add_geometry(b4, 'green', 2)
# canvas.add_geometry(b5, 'purple', 2)

canvas.add_geometry(hull, 'orange', 3)

#canvas.set_extent(hull.bbox)
canvas.show()