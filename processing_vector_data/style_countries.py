import geopandas as gpd
import matplotlib.pyplot as plt

# Define paths
folder = "C:/github/my_first_repository/"
naturalEarth_path = folder + "natural_earth_vector.gpkg"

# Define the layers within the gpkg that we want to use
countries = "ne_50m_admin_0_countries"

# Load the world shapefile from Natural Earth
world = gpd.read_file(naturalEarth_path, countries)

print(world.columns)

'''
# Define the population thresholds and corresponding colors
colors = {'red': world['pop_est'] > 80000000,
          'blue': (world['pop_est'] > 1000000) & (world['pop_est'] <= 80000000),
          'green': world['pop_est'] < 1000000}

# Plot the map
fig, ax = plt.subplots(figsize=(10, 5))
for color, condition in colors.items():
    world[condition].plot(ax=ax, color=color)

# Set title and remove axis
plt.title('World Population by Country')
plt.axis('off')

# Save as PDF
# plt.savefig('world_population_map.pdf', bbox_inches='tight')
plt.show()
'''