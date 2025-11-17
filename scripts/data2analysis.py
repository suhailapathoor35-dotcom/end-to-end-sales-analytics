import pandas as pd
import matplotlib.pyplot  as plt
import os
import matplotlib.ticker as mtick
os.makedirs("C:/Users/Suhaila/Documents/end-to-end-sales-analytics/reports/charts", exist_ok=True)
os.makedirs("C:/Users/Suhaila/Documents/end-to-end-sales-analytics/reports/results", exist_ok=True)

import os
df = pd.read_csv("C:/Users/Suhaila/Documents/end-to-end-sales-analytics/data/sales_cleaned.csv")
print(df)
df=df.dropna(subset=['OrderDate','TotalPrice'])
df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
df["Year"] = df["OrderDate"].dt.year
df["Month"] = df["OrderDate"].dt.month
df["MonthName"] = df["OrderDate"].dt.strftime("%b")
df["MonthYear"] = df["OrderDate"].dt.to_period("M").astype(str)
print("Sample data after cleaning:")
print(df.head())
print("\n--- SALES TREND OVER MONTHS ---")
sales_trend = df.groupby("MonthYear")["TotalPrice"].sum().reset_index()
print(sales_trend.head())


plt.figure(figsize=(10,5))
plt.plot(sales_trend["MonthYear"], sales_trend["TotalPrice"])
plt.xticks(rotation=45)
plt.title("Sales Trend Over Months")
plt.xlabel("Month-Year")
plt.ylabel("Total Sales")
plt.tight_layout()

plt.savefig("C:/Users/Suhaila/Documents/end-to-end-sales-analytics/reports/charts/sales_trend.png")
plt.show()
sales_trend.to_csv("C:/Users/Suhaila/Documents/end-to-end-sales-analytics/reports/results/sales_by_month.csv", index=False)

###########1############
print("\n--- TOP PRODUCTS ---")



top_products = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_products.plot(kind='bar', edgecolor='black')

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")

# ⭐ Show numbers normally (not scientific notation)
plt.gca().yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("C:/Users/Suhaila/Documents/end-to-end-sales-analytics/reports/charts/top_products.png")
plt.show()
top_products.to_csv("C:/Users/Suhaila/Documents/end-to-end-sales-analytics/reports/results/top_products.csv")
plt.close()


#####################2###############
# --- TOP CUSTOMERS BY SALES ---

# Convert CustomerID to string for better labeling
df['CustomerID'] = df['CustomerID'].astype(str)

# Calculate total sales per customer
top_customers = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_customers.plot(kind='bar', edgecolor='black')

plt.title("Top Customers by Sales")
plt.xlabel("Customer ID")
plt.ylabel("Total Sales")

# Rotate labels clearly
plt.xticks(rotation=45)

# Save chart
plt.tight_layout()
plt.savefig("C:/Users/Suhaila/Documents/end-to-end-sales-analytics/reports/charts/top_customers.png")
plt.show()
top_customers.to_csv("C:/Users/Suhaila/Documents/end-to-end-sales-analytics/reports/results/top_customers.csv")
plt.close()



 ###################3###############
print("\n--- REGION WISE SALES ---")

region_sales = df.groupby("Region")["TotalPrice"].sum().reset_index()
region_sales = region_sales.sort_values("TotalPrice", ascending=False)
print(region_sales)

plt.figure(figsize=(6,6))
plt.pie(region_sales["TotalPrice"], labels=region_sales["Region"], autopct="%1.1f%%")
plt.title("Sales by Region")
plt.savefig("C:/Users/Suhaila/Documents/end-to-end-sales-analytics/reports/charts/region_sales.png")
sales_trend.to_csv("C:/Users/Suhaila/Documents/end-to-end-sales-analytics/reports/results/region_sales.csv", index=False)
plt.show()
################4#######################













