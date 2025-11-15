# Simulate IoT sensor readings and AI prediction
import numpy as np


# Example sensor data
soil_moisture = np.random.uniform(10, 40, size=(100, 1)) # percentage
temperature = np.random.uniform(15, 35, size=(100, 1)) # Celsius
sunlight = np.random.uniform(100, 1000, size=(100, 1)) # lux


# Combine sensor data
X = np.hstack((soil_moisture, temperature, sunlight))


# Simulated target crop yield (0=low, 1=medium, 2=high)
y = np.random.randint(0, 3, size=(100,))


# Train simple model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X, y)


# Predict crop yield for new sensor reading
new_reading = np.array([[25, 28, 500]])
predicted_yield = model.predict(new_reading)
print("Predicted crop yield class:", predicted_yield[0])
