# ==========================================
# STEP 3: Import Libraries and Load Dataset
# ==========================================
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
# Note: If you get encoding errors, resave the 'superstore.csv' file
# in UTF-8 format inside the same folder.
data = pd.read_csv(r"C:\Users\Candi\PythonProjects\Coding Exercise Eight\superstore.csv", encoding="latin1")

# Display the first few rows of the dataset
print("--- First 5 Rows of the Dataset ---")
print(data.head())
print("\n" + "=" * 50 + "\n")

# ==========================================
# STEP 4: Explore the Dataset
# ==========================================
# Show dataset information
print("--- Dataset Information ---")
print(data.info())
print("\n" + "=" * 50 + "\n")

# Summary statistics of numerical columns
print("--- Summary Statistics ---")
print(data.describe())
print("\n" + "=" * 50 + "\n")

# Check for missing values
print("--- Missing Values Per Column ---")
print(data.isnull().sum())
print("\n" + "=" * 50 + "\n")

# ==========================================
# STEP 5: Perform Basic Analysis
# ==========================================
# Calculate total sales and average profit
total_sales = data["Sales"].sum()
average_profit = data["Profit"].mean()

print("--- Financial Metrics ---")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Average Profit: ${average_profit:.2f}")
print("\n" + "=" * 50 + "\n")

# ==========================================
# STEP 6: Create a Visualization
# ==========================================
# Group data by Region and calculate total sales
sales_by_region = data.groupby("Region")["Sales"].sum()

# Plot a bar chart
sales_by_region.plot(kind="bar", color="skyblue", figsize=(8, 6))
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)  # Rotates the region names slightly for better readability
plt.tight_layout()  # Adjusts the layout so nothing gets cut off
plt.show()