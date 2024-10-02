import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CO2 dataset
co2_data = pd.read_csv('C:\\Users\\ashwi\\OneDrive\\Desktop\\nasa datas\\co2.csv')
print("CO2 Dataset Loaded Successfully")

# Display initial CO2 dataset info
print("Initial CO2 Dataset Info:")
print(co2_data.info())

# Display initial records of the CO2 dataset
print(co2_data.head())

# Check for duplicates in the CO2 dataset
duplicates_co2 = co2_data.duplicated().sum()
print(f"Duplicates in CO2 dataset: {duplicates_co2}")

# Check for missing values in the CO2 dataset
print("Missing values in CO2 dataset before date conversion:")
print(co2_data.isna().sum())

# Convert 'date' column to datetime
co2_data['date'] = pd.to_datetime(co2_data['date'], errors='coerce')

# Check for missing values after date conversion
print("Missing values in CO2 dataset after date conversion:")
print(co2_data.isna().sum())

# Descriptive statistics for the CO2 dataset
print("CO2 Descriptive Statistics:")
print(co2_data['co2'].describe())

# Calculate correlation matrix for numeric columns only
correlation_matrix = co2_data[['co2']].corr()
print("Correlation Matrix:")
print(correlation_matrix)

# Visualization for CO2 data
plt.figure(figsize=(12, 6))
sns.lineplot(data=co2_data, x='date', y='co2', hue='sector', marker='o')
plt.title('CO2 Emissions Over Time by Sector')
plt.xlabel('Year')
plt.ylabel('CO2 Emissions (kt)')
plt.xticks(rotation=45)
plt.legend(title='Sector')
plt.tight_layout()
plt.show()

# Load the CH4 dataset
ch4_data = pd.read_csv('C:\\Users\\ashwi\\OneDrive\\Desktop\\nasa datas\\ch4.csv', delimiter=',', header=0)
print("CH4 Dataset Loaded Successfully")

# Display initial CH4 dataset info
print("Initial CH4 Dataset Info:")
print(ch4_data.info())

# Display initial records of the CH4 dataset
print(ch4_data.head())

# Check for duplicates in the CH4 dataset
duplicates_ch4 = ch4_data.duplicated().sum()
print(f"Duplicates in CH4 dataset: {duplicates_ch4}")

# Check for missing values in the CH4 dataset
print("Missing values in CH4 dataset:")
print(ch4_data.isna().sum())

# Descriptive statistics for the CH4 dataset
print("CH4 Descriptive Statistics:")
print(ch4_data.describe())

# Visualization for CH4 data
plt.figure(figsize=(12, 6))
sns.lineplot(data=ch4_data, x='year', y='average')
plt.title('Average CH4 Concentration Over Time')
plt.xlabel('Year')
plt.ylabel('Average CH4 Concentration (ppb)')
plt.tight_layout()
plt.show()

# Correlation heatmap for CO2 dataset
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix for CO2 Dataset')
plt.tight_layout()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Enable interactive mode
plt.ion()

# Load the CO2 dataset
co2_data = pd.read_csv('C:\\Users\\ashwi\\OneDrive\\Desktop\\nasa datas\\co2.csv')
print("CO2 Dataset Loaded Successfully")

# Display initial CO2 dataset info
print("Initial CO2 Dataset Info:")
print(co2_data.info())

# Display initial records of the CO2 dataset
print(co2_data.head())

# Check for duplicates in the CO2 dataset
duplicates_co2 = co2_data.duplicated().sum()
print(f"Duplicates in CO2 dataset: {duplicates_co2}")

# Check for missing values in the CO2 dataset
print("Missing values in CO2 dataset before date conversion:")
print(co2_data.isna().sum())

# Convert 'date' column to datetime
co2_data['date'] = pd.to_datetime(co2_data['date'], errors='coerce')

# Check for missing values after date conversion
print("Missing values in CO2 dataset after date conversion:")
print(co2_data.isna().sum())

# Descriptive statistics for the CO2 dataset
print("CO2 Descriptive Statistics:")
print(co2_data['co2'].describe())

# Calculate correlation matrix for numeric columns only
correlation_matrix = co2_data[['co2']].corr()
print("Correlation Matrix:")
print(correlation_matrix)

# Visualization for CO2 data
plt.figure(figsize=(12, 6))
sns.lineplot(data=co2_data, x='date', y='co2', hue='sector', marker='o')
plt.title('CO2 Emissions Over Time by Sector')
plt.xlabel('Year')
plt.ylabel('CO2 Emissions (kt)')
plt.xticks(rotation=45)
plt.legend(title='Sector')
plt.tight_layout()
plt.grid(True)
plt.show()

# Correlation heatmap for CO2 dataset
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix for CO2 Dataset')
plt.tight_layout()
plt.show()
