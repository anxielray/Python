def train_model():
    model_status = 'Training'
    print(f"Inside the function: {model_status}")

model_status = 'Not started'

print(f"Outside the function: {model_status}")

train_model()

print(f"Outside the function after calling the function: {model_status}")