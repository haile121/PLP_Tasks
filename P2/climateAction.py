import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# simulate dataset
np.random.seed(42)
years = np.arange(2000, 2024)
population = np.random.randint(1_000_000, 10_000_000, size=len(years))
industrial_index = np.random.randint(50, 150, size=len(years))
renewable_energy = np.random.uniform(5, 35, size=len(years))
carbon_emissions = population * 0.0005 + industrial_index * 2 - renewable_energy * 1.5 + np.random.normal(0, 10, len(years))
data = pd.DataFrame({'Year': years, 'Population': population, 'IndustrialIndex': industrial_index,
                     'RenewableEnergyPercent': renewable_energy, 'CarbonEmissions': carbon_emissions})

# explore dataset
print(data.head())
sns.pairplot(data)
plt.show()
plt.figure(figsize=(6,4))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.show()

# preprocess data
X = data[['Year', 'Population', 'IndustrialIndex', 'RenewableEnergyPercent']]
y = data['CarbonEmissions']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# train model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train_scaled, y_train)
y_pred = rf_model.predict(X_test_scaled)

# evaluate model
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print(f"MAE: {mae:.2f}, RMSE: {rmse:.2f}, R2: {r2:.2f}")

# visualize predictions
plt.figure(figsize=(8,5))
plt.plot(y_test.values, label='Actual', marker='o')
plt.plot(y_pred, label='Predicted', marker='x')
plt.legend()
plt.show()

# forecast future emissions
future_years = np.arange(2024, 2029)
future_population = np.random.randint(1_000_000, 10_000_000, size=len(future_years))
future_industrial_index = np.random.randint(50, 150, size=len(future_years))
future_renewable = np.random.uniform(5, 35, size=len(future_years))
future_data = pd.DataFrame({'Year': future_years, 'Population': future_population,
                            'IndustrialIndex': future_industrial_index, 'RenewableEnergyPercent': future_renewable})
future_scaled = scaler.transform(future_data)
future_pred = rf_model.predict(future_scaled)
plt.figure(figsize=(8,5))
plt.plot(data['Year'], data['CarbonEmissions'], label='Historical', marker='o')
plt.plot(future_years, future_pred, label='Forecast', marker='x', linestyle='--')
plt.legend()
plt.show()

# ethical reflection
print("Ethical: Data bias possible, fairness important, promotes sustainability")
