import pandas as pd

# Load CO2 emissions data
co2_data = pd.read_csv("C:/Users/ashwi/OneDrive/Desktop/nasa datas/co2.csv")
print("CO2 Emissions Data:")
print(co2_data.head())

# Filter the CO2 data for years 2000 to 2024
co2_data['year'] = pd.to_datetime(co2_data['date']).dt.year
filtered_co2_data = co2_data[(co2_data['year'] >= 2000) & (co2_data['year'] <= 2024)]
print("\nFiltered CO2 Emissions Data (2000 to 2024):")
print(filtered_co2_data)

# Load methane emissions data
methane_data = pd.read_csv("C:/Users/ashwi/OneDrive/Desktop/nasa datas/ch4.csv", sep=r'\s+', header=0)
print("\nMethane Emissions Data:")
print(methane_data.head())

# Display the columns of both datasets
print("\nCO2 Emissions Data Columns:")
print(co2_data.columns)

print("\nMethane Emissions Data Columns:")
print(methane_data.columns)
