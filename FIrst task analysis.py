import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv(r"C:\Users\acer\Downloads\ElectricCarData_Clean.csv)
df

# Display basic dataset information
print(df.info())
print(df.describe())  # Provides summary statistics
print(df.head())

# Calculate average values of key numerical columns
average_values = df[['AccelSec', 'TopSpeed_KmH', 'Range_Km', 'Efficiency_WhKm', 'PriceEuro']].mean()
print("\nAverage Values:")
print(average_values)

# Bar chart for average values
plt.figure(figsize=(10, 5))
average_values.plot(kind='bar', color=['blue', 'green', 'red', 'purple', 'orange'])
plt.title('Average Values of Key Metrics')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Scatter plot: Price vs. Range
plt.figure(figsize=(10, 5))
sns.scatterplot(x=df['Range_Km'], y=df['PriceEuro'], hue=df['Brand'], alpha=0.7, edgecolor='k')
plt.title('Price vs. Range of Electric Cars')
plt.xlabel('Range (Km)')
plt.ylabel('Price (Euro)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# Pairplot for numerical data visualization
sns.pairplot(df[['AccelSec', 'TopSpeed_KmH', 'Range_Km', 'Efficiency_WhKm', 'PriceEuro']])
plt.show()

# Heatmap of correlations
plt.figure(figsize=(10, 6))
sns.heatmap(df[['AccelSec', 'TopSpeed_KmH', 'Range_Km', 'Efficiency_WhKm', 'PriceEuro']].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Key Metrics')
plt.show()

# Boxplot to analyze price distribution by brand
plt.figure(figsize=(12, 6))
sns.boxplot(x='Brand', y='PriceEuro', data=df)
plt.xticks(rotation=90)
plt.title('Price Distribution by Brand')
plt.ylabel('Price (Euro)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
