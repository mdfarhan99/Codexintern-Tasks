import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load csv file
df = pd.read_csv(r"C:\Users\acer\Downloads\airline_passengers.csv")
print(df)

#Analysis
print(df.info())
print(df.describe())
print(df.head())

sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
plt.plot(df.index, df["Thousands of Passengers"], color="blue", linewidth=2)
plt.title("Airline Passenger Trend (1949-1960)")
plt.xlabel("Year")
plt.ylabel("Thousands of Passengers")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

df["Moving Average"] = df["Thousands of Passengers"].rolling(window=12).mean()
print(df)

plt.figure(figsize=(12, 6))
plt.plot(df.index, df["Thousands of Passengers"], label="Original Data", color="blue", alpha=0.5)
plt.plot(df.index, df["Moving Average"], label="12-Month Moving Average", color="red", linewidth=2)
plt.title("Moving Average of Airline Passengers")
plt.xlabel("Year")
plt.ylabel("Thousands of Passengers")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

#Histogram
plt.figure(figsize=(12, 6))
df["Thousands of Passengers"].hist(bins=20, color="blue", alpha=0.7, edgecolor="black")
plt.title("Histogram of Passenger Counts")
plt.xlabel("Thousands of Passengers")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

#Heatmap corr
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Heatmap of Correlations")
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x=df.index, y=df["Thousands of Passengers"], color="blue", alpha=0.7, edgecolor="black")
plt.title("Scatter Plot of Passenger Counts Over Time")
plt.xlabel("Year")
plt.ylabel("Thousands of Passengers")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
