import pandas as pd
import matplotlib.pyplot as plt
import os

# ----------------------------
# 1️⃣ Paths
# ----------------------------
data_path = "../data/sales_cleaned.csv"
reports_summary_path = "../reports/summary/"
reports_charts_path = "../reports/charts/"

# Make sure output folders exist
os.makedirs(reports_summary_path, exist_ok=True)
os.makedirs(reports_charts_path, exist_ok=True)

# ----------------------------
# 2️⃣ Load data
# ----------------------------
df = pd.read_csv(data_path, parse_dates=['OrderDate'])

# ----------------------------
# 3️⃣ Calculate KPIs
# ----------------------------
# Total Sales
total_sales = df['TotalPrice'].sum()

# Total Quantity
total_quantity = df['Quantity'].sum()

# Average Sales per Order
average_sales = df['TotalPrice'].mean()

print(f"Total Sales: {total_sales}")
print(f"Total Quantity: {total_quantity}")
print(f"Average Sales per Order: {average_sales:.2f}")

# ----------------------------
# 4️⃣ Sales per Month
# ----------------------------
df['YearMonth'] = df['OrderDate'].dt.to_period('M')
monthly_sales = df.groupby('YearMonth')['TotalPrice'].sum().reset_index()

# Save monthly sales to CSV
monthly_sales.to_csv(os.path.join(reports_summary_path, "monthly_sales.csv"), index=False)

# Plot monthly sales
plt.figure(figsize=(10,5))
plt.plot(monthly_sales['YearMonth'].astype(str), monthly_sales['TotalPrice'], marker='o')
plt.xticks(rotation=45)
plt.ylabel("Total Sales")
plt.title("Monthly Sales")
plt.tight_layout()
plt.savefig(os.path.join(reports_charts_path, "monthly_sales.png"))
plt.close()
# Create KPI Summary Dictionary
kpi_summary = {
    "Total Sales": [total_sales],
    "Total Quantity": [total_quantity],
    "Average Sales": [average_sales],
}

# Convert to DataFrame
kpi_df = pd.DataFrame(kpi_summary)

# Save to CSV
kpi_df.to_csv("../reports/summary/kpi_summary.csv", index=False)

print("KPI Summary saved to reports/summary/kpi_summary.csv")


# ----------------------------
# 5️⃣ Customer Segmentation
# ----------------------------
customer_sales = df.groupby('CustomerID')['TotalPrice'].sum().reset_index()
customer_sales = customer_sales.sort_values(by='TotalPrice', ascending=False)

# Segment customers: Low, Medium, High
bins = [0, 500, 2000, customer_sales['TotalPrice'].max()]
labels = ['Low', 'Medium', 'High']
customer_sales['Segment'] = pd.cut(customer_sales['TotalPrice'], bins=bins, labels=labels)

# Save customer segmentation
customer_sales.to_csv(os.path.join(reports_summary_path, "customer_segment.csv"), index=False)

print("KPIs calculation done. Outputs saved in 'reports/' folder.")
