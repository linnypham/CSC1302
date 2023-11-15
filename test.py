import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_file.csv' with the path to your CSV file
file_path = 'atlanta_weather.csv'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

# Assuming your DataFrame has a 'Date' column, convert it to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract month from the 'Date' column
df['Month'] = df['Date'].dt.month

# Create a line plot for 'High' and 'Low' temperatures by month
plt.figure(figsize=(10, 6))

# Plot 'High' temperature
plt.plot(df['Month'], df['High'], 'b--o', label='High')

# Plot 'Low' temperature
plt.plot(df['Month'], df['Low'], 'g:.^', label='Low')

# Annotate the highest temperature of the year
max_temp_index = df['High'].idxmax()
max_temp = df['High'].max()
plt.annotate(f'Highest Temp: {max_temp}°F', 
             xy=(df['Month'][max_temp_index], max_temp),
             xytext=(df['Month'][max_temp_index] + 1, max_temp + 5),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12,
             )

# Set plot title and labels
plt.title('Atlanta – Monthly Temperature', fontsize=20)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Temperature (Fahrenheit)', fontsize=16)

# Set legend
plt.legend(fontsize=12)

# Show the plot
plt.show()
