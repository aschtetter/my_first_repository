# Polar system so it will go round and round and round

from math import cos, sin, radians
from pyqgis_scripting_ext.core import*

n = 7
d = 8

iterations = max(n,d)

# Define an angle in rad (0-2pi bzw. vielfache davon)
maxAngle = 360*iterations

coords = []
for angle in range(0, maxAngle, 1):
    radAngle = radians(angle)
    k = n/d
    r = cos(k*radAngle)
    x = r*cos(radAngle)
    y = r*sin(radAngle)

    coords.append([x,y])
    
line = HLineString.fromCoords(coords)

## CANVAS
canvas = HMapCanvas.new()
canvas.add_geometry(line, "magenta", 1)
canvas.set_extent(line.bbox())

canvas.show()

