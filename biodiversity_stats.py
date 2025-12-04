# Simple Biodiversity Analysis Program
# Counts species and calculates species richness

species_observations = [
    "Lion", "Elephant", "Zebra", "Lion", "Zebra",
    "Giraffe", "Elephant", "Lion", "Hyena", "Zebra"
]

# Count frequency of each species
species_count = {}

for species in species_observations:
    if species in species_count:
        species_count[species] += 1
    else:
        species_count[species] = 1

# Calculate species richness (number of unique species)
species_richness = len(species_count)

# Print results
print("Biodiversity Report")
print("-------------------")
print("Total observations:", len(species_observations))
print("Species richness:", species_richness)
print("\nSpecies counts:")

for species, count in species_count.items():
    print(f"{species}: {count}")
