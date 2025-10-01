import pandas as pd
import glob

files = glob.glob("data/daily_sales_data_*.csv")
dfs = [pd.read_csv(f) for f in files]
df = pd.concat(dfs, ignore_index=True)

# Filter only Pink Morsels
df = df[df["product"].str.lower() == "pink morsel"]

# Clean price column (remove $ and convert to float)
df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)

# Calculate Sales
df["Sales"] = df["quantity"] * df["price"]

# Keep only needed columns
df = df[["Sales", "date", "region"]]

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# Save cleaned dataset
df.to_csv("processed_sales.csv", index=False)

print("✅ Processed data saved to processed_sales.csv")
print("\nHere are the first 10 rows:")
print(df.head(10))
