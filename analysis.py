import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales.csv")

print("First 5 rows:")
print(df.head())

# Data Cleaning
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Convert Date column
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst =True)

# Create Month column
df['Month'] = df['Order Date'].dt.month

# Total Sales
total_sales = df['Sales'].sum()
print("\nTotal Sales:", total_sales)

# Top Products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False)
print("\nTop Products:")
print(top_products)

# Monthly Sales
monthly_sales = df.groupby('Month')['Sales'].sum()
print("\nMonthly Sales:")
print(monthly_sales)

# Plot Graph
monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()