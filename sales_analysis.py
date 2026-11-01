
import pandas as pd
import matplotlib.pyplot as plt

# Creating our sales dataset
data = {
    "Product": [
        "T-shirt", "Jeans", "Hoodie", "Sneakers",
        "T-shirt", "Jacket", "Jeans", "Hoodie",
        "Sneakers", "T-shirt"
    ],

    "Quantity": [5, 3, 4, 2, 8, 2, 5, 3, 4, 6],

    "Price": [800, 1500, 2000, 3500, 800,
              3000, 1500, 2000, 3500, 800],

 # ADD THIS SECTION HERE
    "Date": [
        "2026-01-05", "2026-01-12", "2026-01-20",
        "2026-02-03", "2026-02-10", "2026-02-18",
        "2026-03-02", "2026-03-09", "2026-03-15",
        "2026-03-25"
    ]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Display the dataset
print(df)


# Calculate revenue for each sale
df["Revenue"] = df["Quantity"] * df["Price"]

# Display the updated dataset
print("\nSales Data with Revenue:")
print(df)

# Calculate total revenue
total_revenue = df["Revenue"].sum()

print("\nTotal Business Revenue: KSh", total_revenue)

# MONTHLY SALES ANALYSIS

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.to_period("M")

monthly_revenue = df.groupby("Month")["Revenue"].sum()

print("\nMonthly Revenue:")
print(monthly_revenue)

best_month = monthly_revenue.idxmax()

print("\nBest Performing Month:", best_month)

# VISUALISE MONTHLY REVENUE

monthly_revenue.plot(kind="bar", figsize=(8, 5))

plt.title("Monthly Business Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (KSh)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()

# BUSINESS PERFORMANCE SUMMARY

# Calculate total units sold
total_units = df["Quantity"].sum()

# Calculate average revenue per transaction
average_revenue = df["Revenue"].mean()

# Calculate quantity sold per product
product_sales = df.groupby("Product")["Quantity"].sum()

# Calculate revenue per product
product_revenue = df.groupby("Product")["Revenue"].sum()

# Identify the best-selling product
best_selling_product = product_sales.idxmax()

# Identify highest revenue product
highest_revenue_product = product_revenue.idxmax()


# Display business summary
print("\n========== BUSINESS PERFORMANCE SUMMARY ==========")

print("Total Revenue: KSh", total_revenue)

print("Total Units Sold:", total_units)

print("Average Revenue Per Sale: KSh", average_revenue)

print("Best-Selling Product:", best_selling_product)

print("Highest Revenue Product:", highest_revenue_product)

print("==================================================")


