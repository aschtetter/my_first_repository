from pyqgis_scripting_ext.core import *

folder = "C:/github/my_first_repository/"
# TMP FOLDER DEFINITION
tmp_folder = "C:/Users/aschw/OneDrive - Scientific Network South Tyrol/00_advanced_geomatics/tmp_folder"


geopackagePath = folder + "natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"
citiesName = "ne_50m_populated_places"
riversName = "ne_10m_rivers_lake_centerlines_scale_rank"

# cleanup
HMap.remove_layers_by_name(["OpenStreetMap", citiesName, countriesName, "rivers_italy"])

# load openstreetmap tiles layer
osm = HMap.get_osm_layer()
HMap.add_layer(osm)

# load the layer
# cities layer
citiesLayer = HVectorLayer.open(geopackagePath, citiesName)
citiesLayer.subset_filter("SOV0NAME='Italy'")

pointStyle = HMarker("square", 6, 45) + \
                HFill("red") + HStroke("black", 1)
field = "NAME"
#pointStyle += HLabel(field, yoffset=-8) + HHalo("white", 1)
field = "if(POP_MAX>1000000, concat(NAME, ' (', round(POP_MAX/1000000, 1), ')'), NAME)"

labelProperties = {
    "font": "Arial",
    "color": "black",
    "size": 20,
    "field": field,
    "xoffset": 0,
    "yoffset": -8
}
pointStyle += HLabel(**labelProperties) + HHalo("white", 2)
citiesLayer.set_style(pointStyle)

# polygon layer
countriesLayer = HVectorLayer.open(geopackagePath, countriesName)
countriesLayer.subset_filter("NAME='Italy'")
italyGeometry = countriesLayer.features()[0].geometry


#print(italyGeometry.centroid())

polygonStyle = HFill("0,255,0,128") + HStroke("green", 2)
countriesLayer.set_style(polygonStyle)

# lines layer
riversLayer = HVectorLayer.open(geopackagePath, riversName)
riversLayerItaly = riversLayer.sub_layer(italyGeometry, "rivers_italy", ['scalerank', 'name'])


# thematic styling
ranges = [
    [0, 0],
    [1, 5],
    [6, 7],
    [8, 9],
    [10, 11]
]
styles = [
    HStroke("blue", 7),
    HStroke("blue", 5),
    HStroke("blue", 3),
    HStroke("blue", 2),
    HStroke("blue", 1)
]
labelProperties = {
    "font": "Arial",
    "color": "blue",
    "size": 14,
    "field": 'name',
    "along_line": True,
    "bold": True,
    "italic": True
}
labelStyle = HLabel(**labelProperties) + HHalo("white", 1)
riversLayerItaly.set_graduated_style('scalerank', ranges, styles, labelStyle)

# riversStyle = HStroke("blue", 2)


# riversStyle += labelStyle
# riversLayerItaly.set_style(riversStyle)


HMap.add_layer(countriesLayer)
HMap.add_layer(riversLayerItaly)
HMap.add_layer(citiesLayer)

# PRINTING

printer = HPrinter(iface)

printer.add_map(**mapProperties) # Map has to be added before properties can be changed

mapProperties = { #A4 landscape by default
    "x": 5,
    "y": 25, # position of the paper from top left
    "width": 285,
    "height": 180,
    "frame": True,
    "extent": [7.141113,38.717783,14.633789,46.468684] # form of bounding box --> northern part of Italy
}

labelProperties = {
"x": 120,
"y": 10,
"text": "Such a nice map!",
"font_size": 28,
"bold": True,
"italic": False
}
printer.add_label(**labelProperties) # Add label to the map

legendProperties = {
"x": 215,
"y": 30,
"width": 150,
"height": 100,
"frame": True,
"max_symbol_size": 3
}
printer.add_legend(**legendProperties) # Add legend to the map

scalebarProperties = {
"x": 10,
"y": 190,
"units": "km",
"segments": 4,
"unit_per_segment": 100,
"style": "Single Box", # or 'Line Ticks Up'
"font_size": 12
}
printer.add_scalebar(**scalebarProperties) # Add scalebar

# IMPORT DATETIME TO STOP OVERWRITING

output_pdf = f"{tmp_folder}/test.pdf" # Print to PDF
printer.dump_to_pdf(output_pdf)

output_png = f"{tmp_folder}/test.png" # Print to png
printer.dump_to_pdf(output_png)

