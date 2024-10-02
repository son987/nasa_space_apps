import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import seaborn as sns

# Load dataset
try:
    co2_data = pd.read_csv('C:\\Users\\ashwi\\OneDrive\\Desktop\\nasa_datas\\co2.csv')
    print("CO2 Dataset Loaded Successfully")
    print(co2_data.info())
except FileNotFoundError:
    print("Error: CO2 dataset file not found. Please check the file path.")
    exit()

# Check for missing values
print("Missing values in CO2 dataset before preprocessing:")
print(co2_data.isnull().sum())

# Drop the 'date' column since it's not useful for regression
co2_data.drop(columns=['date'], inplace=True)

# Check again for missing values
print("Missing values in CO2 dataset after preprocessing:")
print(co2_data.isnull().sum())

# Prepare features and target variable
X = co2_data.drop('co2', axis=1)
y = co2_data['co2']

# Convert categorical variables into dummy/indicator variables
X = pd.get_dummies(X, drop_first=True)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Random Forest Regressor
rf = RandomForestRegressor()

# Define parameter grid for Randomized Search
param_distributions = {
    'n_estimators': [100, 200, 300],
    'max_features': ['sqrt', None],  # Fixed 'auto' to 'sqrt' and None
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

# Setup RandomizedSearchCV
random_search = RandomizedSearchCV(estimator=rf, 
                                   param_distributions=param_distributions,
                                   n_iter=30,
                                   cv=3,
                                   verbose=2, 
                                   random_state=42, 
                                   n_jobs=-1)

# Fit the model
random_search.fit(X_train, y_train)

# Predict on test set
y_pred = random_search.predict(X_test)

# Calculate R^2 score
r2 = r2_score(y_test, y_pred)
print(f"Model R² score: {r2:.2f}")

# Feature importance
importances = random_search.best_estimator_.feature_importances_
feature_names = X.columns
indices = np.argsort(importances)[::-1]

# Plot feature importance
plt.figure(figsize=(10, 6))
sns.barplot(x=importances[indices], y=feature_names[indices], palette='viridis')
plt.title('Feature Importance')
plt.xlabel('Importance Score')
plt.ylabel('Features')
plt.tight_layout()  # Add this for better layout
plt.show()

# Save the model
joblib.dump(random_search, 'co2_model.pkl')
print("Model saved successfully.")
