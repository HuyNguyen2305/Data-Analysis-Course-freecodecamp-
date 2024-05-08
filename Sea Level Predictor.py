import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

# Get line of best fit for all data
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Predict sea level rise in 2050 using all data
x_future = range(1880, 2051)
y_future = slope * x_future + intercept
plt.plot(x_future, y_future, 'r', label='Best Fit Line (1880-2050)')

# Get line of best fit for data since 2000
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

# Predict sea level rise in 2050 using data since 2000
x_future_recent = range(2000, 2051)
y_future_recent = slope_recent * x_future_recent + intercept_recent
plt.plot(x_future_recent, y_future_recent, 'g', label='Best Fit Line (2000-2050)')

# Plot settings
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()
plt.grid(True)

# Save and return the image
plt.savefig('sea_level_plot.png')
plt.show()
