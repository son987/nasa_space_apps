import pandas as pd

# Load CO2 emissions data
try:
    co2_data = pd.read_csv("C:/Users/ashwi/OneDrive/Desktop/nasa_datas/co2.csv")
    print("CO2 Emissions Data Loaded Successfully:")
    print(co2_data.head())
except FileNotFoundError:
    print("Error: CO2 emissions data file not found. Please check the file path.")

# Filter the CO2 data for years 2000 to 2024
if 'date' in co2_data.columns:
    co2_data['year'] = pd.to_datetime(co2_data['date'], errors='coerce').dt.year
    filtered_co2_data = co2_data[(co2_data['year'] >= 2000) & (co2_data['year'] <= 2024)]
    print("\nFiltered CO2 Emissions Data (2000 to 2024):")
    print(filtered_co2_data)
else:
    print("Error: 'date' column not found in CO2 emissions data.")

# Load methane emissions data
try:
    methane_data = pd.read_csv("C:/Users/ashwi/OneDrive/Desktop/nasa_datas/ch4.csv", sep=r'\s+', header=0)
    print("\nMethane Emissions Data Loaded Successfully:")
    print(methane_data.head())
except FileNotFoundError:
    print("Error: Methane emissions data file not found. Please check the file path.")

# Display the columns of both datasets
if 'co2_data' in locals():
    print("\nCO2 Emissions Data Columns:")
    print(co2_data.columns)

if 'methane_data' in locals():
    print("\nMethane Emissions Data Columns:")
    print(methane_data.columns)
