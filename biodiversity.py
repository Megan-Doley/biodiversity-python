# Biodiversity analysis with Simpson's Index and bar plot

import matplotlib.pyplot as plt

species = [
    "Frog", "Bird", "Snake", "Frog",
    "Lizard", "Bird", "Bird", "Ant"
]

# Count each species
counts = {}
for s in species:
    counts[s] = counts.get(s, 0) + 1

# Total organisms
N = sum(counts.values())

# Simpson's Index
D = 0
for count in counts.values():
    D += (count / N) ** 2

simpsons_index = 1 - D

# Print summary
print("Biodiversity Summary")
print("-------------------")
print(f"Total organisms: {N}")
print(f"Species richness: {len(counts)}")
print(f"Simpson's Index of Diversity: {simpsons_index:.3f}\n")

# Bar plot
species_names = list(counts.keys())
species_counts = list(counts.values())

plt.bar(species_names, species_counts)
plt.title("Species Abundance")
plt.xlabel("Species")
plt.ylabel("Number of Individuals")
plt.show()

