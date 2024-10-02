import pandas as pd
import matplotlib.pyplot as plt

# Load the CO2 emissions data
co2_data = pd.read_csv("C:/Users/ashwi/OneDrive/Desktop/nasa datas/co2.csv")

# Display the first few rows of the data
print("CO2 Emissions Data:")
print(co2_data.head())

# Filter data for the year range 2000 to 2024
co2_data['year'] = pd.to_datetime(co2_data['date']).dt.year
filtered_co2_data = co2_data[(co2_data['year'] >= 2000) & (co2_data['year'] <= 2024)]

# Group by year and sum the CO2 emissions
annual_co2_data = filtered_co2_data.groupby('year')['co2'].sum().reset_index()

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(annual_co2_data['year'], annual_co2_data['co2'], marker='o', linestyle='-')
plt.title('Annual CO2 Emissions (2000-2024)')
plt.xlabel('Year')
plt.ylabel('CO2 Emissions (kt)')
plt.grid()
plt.xticks(annual_co2_data['year'], rotation=45)
plt.tight_layout()
plt.savefig("C:/Users/ashwi/OneDrive/Desktop/nasa datas/co2_emissions_trend.png")
plt.show()
