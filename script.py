import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('sales_data.csv')

print(data.head())
print("missing values:\n", data.isnull().sum())

data["Date"] = pd.to_datetime(data["Date"])

data = data.drop_duplicates()

total_revenue = data["Revenue"].sum()

total_units = data["Units_Sold"].sum()
print(f"total revenue is {total_revenue}")
print(f"total units sold is {total_units}")

best_selling_product = data.groupby("Product")["Revenue"].sum().idxmax()
print(f"Best-Selling Product: {best_selling_product}")

average_revenue = data.groupby("Product")["Revenue"].mean()
print(f"average revenue per product: {average_revenue}")

#plotting revenue over time
plt.figure(figsize=(10, 5))
plt.plot(data["Date"], data["Revenue"], marker="o", linestyle="-", color="b")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.title("Daily Revenue Trend")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# plot sales by product 
plt.figure(figsize=(8,4))
sns.barplot(x="Product", y="Revenue", data=data)
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.title("Revenue per product")
plt.show()


#finnally save new data to cleaned file csv
data.to_csv("cleaned_csv.csv", index=False)
print("cleaned data and saved to cleaned_csv.csv")