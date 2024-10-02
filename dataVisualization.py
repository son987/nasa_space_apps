import pandas as pd
import matplotlib.pyplot as plt

# Load the CO2 emissions data
try:
    co2_data = pd.read_csv("C:/Users/ashwi/OneDrive/Desktop/nasa_datas/co2.csv")
    print("CO2 Emissions Data Loaded Successfully.")
except FileNotFoundError:
    print("Error: The file was not found. Please check the file path.")
    exit()

# Display the first few rows of the data
print("CO2 Emissions Data:")
print(co2_data.head())

# Convert 'date' column to datetime and extract the year
co2_data['year'] = pd.to_datetime(co2_data['date'], errors='coerce').dt.year

# Filter data for the year range 2000 to 2024
filtered_co2_data = co2_data[(co2_data['year'] >= 2000) & (co2_data['year'] <= 2024)]

# Group by year and sum the CO2 emissions
annual_co2_data = filtered_co2_data.groupby('year')['co2'].sum().reset_index()

# Check if annual data is empty before plotting
if annual_co2_data.empty:
    print("No data available for the selected year range (2000-2024).")
else:
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(annual_co2_data['year'], annual_co2_data['co2'], marker='o', linestyle='-')
    plt.title('Annual CO2 Emissions (2000-2024)')
    plt.xlabel('Year')
    plt.ylabel('CO2 Emissions (kt)')
    plt.grid()
    plt.xticks(annual_co2_data['year'], rotation=45)
    plt.tight_layout()
    plt.savefig("C:/Users/ashwi/OneDrive/Desktop/nasa_datas/co2_emissions_trend.png")
    plt.show()
