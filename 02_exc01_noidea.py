from pyqgis_scripting_ext.core import *
import csv

def degrees_to_utm(latitude_deg, longitude_deg):
    zone_number = int((longitude_deg + 180) / 6) + 1

    if 56.0 <= latitude_deg < 64.0 and 3.0 <= longitude_deg < 12.0:
        zone_number = 32

    if 72.0 <= latitude_deg < 84.0:
        if 0.0 <= longitude_deg < 9.0:
            zone_number = 31
        elif 9.0 <= longitude_deg < 21.0:
            zone_number = 33
        elif 21.0 <= longitude_deg < 33.0:
            zone_number = 35
        elif 33.0 <= longitude_deg < 42.0:
            zone_number = 37

    # Latitude band determination
    lat_band = 'S' if latitude_deg < 0 else 'N'

    utm_zone = str(zone_number) + lat_band
    return utm_zone

# Initialize the map canvas
canvas = HMapCanvas()

# Create the grid and add coordinates on top
for lon_deg in range(-180, 180, 6):
    lon_utm_zone = degrees_to_utm(0, lon_deg)
    lon_point = HPoint(lon_deg, 0)
    canvas.add_geometry(lon_point, 'black')  # Add longitude line
    lon_label = f'{lon_utm_zone}'
    canvas.add_annotation(lon_label, lon_point, color='black')

for lat_deg in range(-90, 90, 6):
    lat_point = HPoint(0, lat_deg)
    canvas.add_geometry(lat_point, 'black')  # Add latitude line
    lat_label = f'{lat_deg}'
    canvas.add_annotation(lat_label, lat_point, color='black')

# Show the map
canvas.set_extent([-180, -90, 180, 90])  # Set extent to cover the whole world
canvas.show()
