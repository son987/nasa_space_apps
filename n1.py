import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import time

# Start timer for overall execution
overall_start_time = time.time()

# Load CO2 emissions data
start_time = time.time()
co2_data = pd.read_csv("C:/Users/ashwi/OneDrive/Desktop/nasa datas/co2.csv")
print("CO2 Emissions Data Columns:")
print(co2_data.columns)
print(f"Loading data took {time.time() - start_time:.2f} seconds.")

# Data preprocessing
# Convert date column to datetime
co2_data['date'] = pd.to_datetime(co2_data['date'])
co2_data['year'] = co2_data['date'].dt.year

# Filter data for the years 2000 to 2024
filtered_co2_data = co2_data[(co2_data['year'] >= 2000) & (co2_data['year'] <= 2024)]
print("Filtered CO2 Emissions Data (2000 to 2024):")
print(filtered_co2_data.head())

# Prepare features and target variable
X = filtered_co2_data.drop(columns=['co2', 'date', 'year'])  # Adjust this as necessary
y = filtered_co2_data['co2']  # Target variable

# Convert categorical features to numerical
X = pd.get_dummies(X, drop_first=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model_start_time = time.time()
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print(f"Model training took {time.time() - model_start_time:.2f} seconds.")

# Model evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# End timer for overall execution
overall_end_time = time.time()
print(f"Overall execution time: {overall_end_time - overall_start_time:.2f} seconds.")
importances = model.feature_importances_
feature_names = X.columns
feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
print(feature_importance_df.sort_values(by='Importance', ascending=False))
import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)
plt.xlabel("Actual CO2 Emissions")
plt.ylabel("Predicted CO2 Emissions")
plt.title("Actual vs Predicted CO2 Emissions")
plt.show()
