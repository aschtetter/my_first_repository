from pyqgis_scripting_ext.core import *

# Remove existing layers by name
HMap.remove_layers_by_name(["OpenStreetMap", "ne_50m_admin_0_countries"])

# Define paths
folder = "C:/github/my_first_repository/"
geopackagePath = folder + "natural_earth_vector.gpkg"  # GeoPackage to be found at path

# Define the layer name within the GeoPackage
countries = "ne_50m_admin_0_countries"

# Add the OpenStreetMap base layer
osm = HMap.get_osm_layer()
HMap.add_layer(osm)

# Load the countries layer from the GeoPackage
countries_layer = HVectorLayer.open(geopackagePath, countries)

# Add the countries layer to the map
# HMap.add_layer(countries_layer)

# Get the features and the population index
features = countries_layer.features()
population_index = countries_layer.field_index("POP_EST")

# Function to determine the color based on population
def get_population_color(population):
    if population > 80000000:
        return 'red'
    elif 1000000 < population <= 80000000:
        return 'blue'
    else:
        return 'green'

# Apply colors to features
for feature in features[:10]:
    population = feature.attributes[population_index]
    print(population)
    color = get_population_color(population)
    print(color)
    
    # Create the style for the feature
    country_pop_style = HFill(color) + HStroke('0,0,0,255', 0.5)
    
    # Apply the style to the feature
    feature.set_style(country_pop_style)

# Add to map
HMap.add_layer(countries_layer)

