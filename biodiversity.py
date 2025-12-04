# Biodiversity analysis with Simpson's Index of Diversity

species = [
    "Frog", "Bird", "Snake", "Frog",
    "Lizard", "Bird", "Bird", "Ant"
]

# Count each species
counts = {}
for s in species:
    counts[s] = counts.get(s, 0) + 1

# Total number of organisms
N = sum(counts.values())

# Calculate Simpson's Index (D)
D = 0
for count in counts.values():
    D += (count / N) ** 2

# Simpson's Index of Diversity = 1 - D
simpsons_index = 1 - D

# Output results
print("Biodiversity Summary")
print("-------------------")
print(f"Total observations: {N}")
print(f"Species richness: {len(counts)}")
print(f"Simpson's Index of Diversity: {simpsons_index:.3f}\n")

print("Species counts:")
for species, count in counts.items():
    print(f"{species}: {count}")

