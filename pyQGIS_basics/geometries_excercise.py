'''
## Colors are assigned based on last column



Colors Romina solution
if formline == "point":
        for x,y in coordsList:
            form = HPoint(x,y)
            


from pyqgis_scripting_ext.core import *
import csv


## colors --> thcikness und colors einfach random as einer LIstee


data_geometries = "C:/users/aschw/OneDrive - Scientific Network South Tyrol/00_advanced_geomatics/02_exe0_geometries.csv"

# list of tuples with geometry types and their respective color
geometries = []

# Read geometries from the CSV file
with open(data_geometries, "r") as file_handle:
    reader = csv.reader(file_handle, delimiter=';') ## this way I can define the delimeter
    for row in reader:
        geom_type = row[0] ## row[0], row[1], and row[2] correspond to the first, second, and third columns of the CSV file, respectively.
        coords_str = row[1]
        color_value = int(row[2])  # Convert color value to integer
        
        # Process coordinates
        coords = []
        for coord_str in coords_str.split():
            x, y = map(float, coord_str.split(','))
            coords.append([x, y])
        
        # Create geometry based on type
        if geom_type == 'point':
            geometry = HPoint(coords[0][0], coords[0][1])
        elif geom_type == 'line':
            geometry = HLineString.fromCoords(coords)
        elif geom_type == 'polygon':
            geometry = HPolygon.fromCoords(coords)
        
        # Map color value to specific colors
        if color_value == 1:
            color = 'pink'
        elif color_value == 2:
            color = 'blue'
        
        geometries.append((geometry, color))

## CANVAS

# Initialize the map
canvas = HMapCanvas()

# Add geometries to the map
for geometry, color in geometries:
    canvas.add_geometry(geometry, color, 2)

# Set the extent for the canvas
canvas.set_extent([0, 0, 50, 50])

# Show the map
canvas.show()


'''
### OTHER SOLUTIon


from pyqgis_scripting_ext.core import *
import csv
import random

data_geometries = "C:/users/aschw/OneDrive - Scientific Network South Tyrol/00_advanced_geomatics/02_exe0_geometries.csv"

# list of tuples with geometry types, their respective thickness, and colors
'''
as compared to lists tuples cannot be changed!
Tuples vs Lists
The key difference between tuples and lists is that, while tuples are immutable
objects, lists are mutable. This means that tuples cannot be changed while the
lists can be modified. Tuples are more memory efficient than the lists
'''

geometries = []

# Read geometries from the CSV file
with open(data_geometries, "r") as file_handle:
    reader = csv.reader(file_handle, delimiter=';')
    for row in reader:
        geom_type = row[0]
        coords_str = row[1]
        thickness = float(row[2])  # Convert thickness value to float
        
        # Process coordinates
        coords = []
        for coord_str in coords_str.split():
            x, y = map(float, coord_str.split(','))
            coords.append([x, y])
        
        # Create geometry based on type
        if geom_type == 'point':
            geometry = HPoint(coords[0][0], coords[0][1])
        elif geom_type == 'line':
            geometry = HLineString.fromCoords(coords)
        elif geom_type == 'polygon':
            geometry = HPolygon.fromCoords(coords)
        
        # Generate a random color for each geometry
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        
        geometries.append((geometry, thickness, color))


## CANVAS

# Initialize the map
canvas = HMapCanvas()

# Add geometries to the map
for geometry, thickness, color in geometries:
    canvas.add_geometry(geometry, color, thickness)

# Set the extent for the canvas
canvas.set_extent([0, 0, 50, 50])

# Show the map
canvas.show()




    