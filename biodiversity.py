species = [
    "Frog", "Bird", "Snake", "Frog",
    "Lizard", "Bird", "Bird", "Ant"
]

counts = {}

for s in species:
    counts[s] = counts.get(s, 0) + 1

print("Biodiversity Summary")
print("-------------------")
print(f"Total observations: {len(species)}")
print(f"Species richness: {len(counts)}\n")

for species, count in counts.items():
    print(f"{species}: {count}")
