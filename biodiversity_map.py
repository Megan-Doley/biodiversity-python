# Biodiversity analysis with Simpson's Index and GIS mapping

import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
import contextily as ctx

# Example species data with coordinates
data = [
    ("Frog",   -1.2921, 36.8219),
    ("Bird",   -1.2900, 36.8200),
    ("Snake",  -1.2950, 36.8250),
    ("Frog",   -1.2930, 36.8225),
    ("Lizard", -1.2910, 36.8190),
    ("Bird",   -1.2895, 36.8230),
    ("Bird",   -1.2945, 36.8260),
    ("Ant",    -1.2925, 36.8205)
]

# Convert to GeoDataFrame
df = gpd.GeoDataFrame(
    data,
    columns=["Species", "Latitude", "Longitude"],
    geometry=[Point(lon, lat) for _, lat, lon in data],
    crs="EPSG:4326"
)

# --------
# Simpson's Index
# --------
counts = df["Species"].value_counts()
N = counts.sum()

D = sum((count / N) ** 2 for count in counts)
simpsons_index = 1 - D

print("Biodiversity Summary")
print("-------------------")
print(f"Total records: {N}")
print(f"Species richness: {len(counts)}")
print(f"Simpson's Index of Diversity: {simpsons_index:.3f}")

# --------
# Map plot
# --------
fig, ax = plt.subplots(figsize=(8, 8))

df = df.to_crs(epsg=3857)
df.plot(ax=ax, column="Species", legend=True, markersize=60)

ctx.add_basemap(ax)

ax.set_title("Species Observation Map")
ax.set_axis_off()

plt.show()


