from pyqgis_scripting_ext.core import *

folder = "C:/users/aschw/OneDrive - Scientific Network South Tyrol/00_advanced_geomatics/"

geopackagePath = folder + "natural_earth_vector.gpkg" #naming convention Anna!!!!
countriesName = "ne_50m_admin_0_countries"
citiesName = "ne_50m_populated_places"
riversName = "ne_10m_rivers_lake_centerlines_scale_rank"

# cleanup
HMap.remove_layers_by_name(["OpenStreetMap", countriesName, citiesName, riversName, "riversItaly"]) #removes lyers if they're already loaded; useful wehn running the script multiple times

# load osm tiles layer
osm = HMap.get_osm_layer()
HMap.add_layer(osm)

# CITIES LAYER AS POINT LAYER
# load the layer
citiesLayer = HVectorLayer.open(geopackagePath, citiesName)

# Apply filter for only cities in Italy
citiesLayer.subset_filter("SOV0NAME='Italy'")

# STYLING (#Red, Green, blue, opacity)
pointStyle = HMarker("square", 6, 45) + \
                        HFill("70, 130, 130, 128")+\
                        HStroke("green", 1)
field = "NAME"
# Add more options to an existing style
# pointStyle += HLabel(field, yoffset=-8) + HHalo("white", 1)

# field overwritten by expression
field = "if(POP_MAX>1000000, concat(NAME, ' (', round(POP_MAX/1000000, 1), ')'), NAME)"

# Dictionary to define the label properties
labelProperties = {
    "font": "Times New Roman",
    "color": "black",
    "size": 12,
    "field": field,
    "xoffset": 0,
    "yoffset": -8
}

# calling the dictionary defined above with two *; for a list you call with one *
pointStyle += HLabel(**labelProperties) + HHalo("white", 1)

#Assign style to the cities layer
citiesLayer.set_style(pointStyle)



# COUTNRIES LAYER AS (MULTI)POLYGON
countriesLayer = HVectorLayer.open(geopackagePath, countriesName)
countriesLayer.subset_filter("NAME='Italy'") #applied alphanumeric filter internally --> same layer
italyGeometry = countriesLayer.features()[0].geometry #0 for extracting the first

polygonStyle = HFill("0, 255, 0, 128") + HStroke("green", 2)
countriesLayer.set_style(polygonStyle)

# LINES LAYER
# RIVERS
riversLayer = HVectorLayer.open(geopackagePath, riversName)

# create a subset of the river
riversLayerItaly = riversLayer.sub_layer(italyGeometry, "riversItaly", ['scalerank', 'name']) #new layer

lineStyle = HStroke("blue", 2)

labelProperties = {
    "font": "Times New Roman",
    "color": "blue",
    "size": 8,
    "field": 'name',
    "along_line": True, #label follows direction of the lineStyle
    "bold": True,
    "italic": True
}

labelStyle = HLabel(**labelProperties) + HHalo("white", 1)
# lineStyle += labelStyle
riversLayerItaly.set_style(lineStyle+labelStyle)

#Thematic styling
ranges = [
    [0, 0],
    [1, 5],
    [6, 8],
    [8, 9],
    [10, 11]
]

style = [
    HStroke("blue", 7),
    HStroke("blue", 5),
    HStroke("blue", 3),
    HStroke("blue", 2),
    HStroke("blue", 1)
]

#riversLayerItaly.set_graduated_style('scalerank', ranges, styles, lineStyle)



# Add layer to map
HMap.add_layer(countriesLayer)
HMap.add_layer(citiesLayer)
HMap.add_layer(riversLayerItaly)