feature_value = 85
max_value = 100

normalized_value = feature_value / max_value

print(f"Normalized value: {normalized_value}")

# This is an improved version of the code that normalizes a feature value according to the min-max scaling method.
feature_value = 85
min_value = 0
max_value = 100

normalized_value = (feature_value - min_value) / (max_value - min_value)
print(f"Normalized value: {normalized_value}")