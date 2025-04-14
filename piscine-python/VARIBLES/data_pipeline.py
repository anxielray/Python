raw_data = "   This is a sample sentence with extra whitespace and UPPERCASE letters.   "

clean_data = raw_data.strip().lower()

features = clean_data.split()

model = "simple_model"

prediction = f"Prediction based on features: {features}"

print(f"Raw Data: {raw_data}")
print(f"Clean Data: {clean_data}")
print(f"Features: {features}")
print(f"Model: {model}")
print(f"Prediction: {prediction}")