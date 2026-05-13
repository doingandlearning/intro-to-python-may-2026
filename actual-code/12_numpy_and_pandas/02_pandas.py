import pandas as pd

# DataFrame -> the spreadsheet -> a 2D
# Series -> np arrays

df = pd.read_csv("12_numpy_and_pandas/vehicles.csv")

# Exploration
print(df.head())
print(df.tail()) 
print(df.sample(5))
print(df.describe())  # Something in year is not numeric!
print(df.info())

# no_of_years_old

df["no_of_years_old"] = 2026 - df["year"]
print(df)

print(df[df['registration'].isna()])
print(df[df["no_of_years_old"] < 5])

print(df[df["status"] == "Available"][["registration", "max_payload_kg"]])

df = df.drop_duplicates()
df = df.dropna(subset=['registration'])
df = df[df["max_payload_kg"] > 0]

print(df.describe())

hgv = df[df["max_payload_kg"] > 3500]
print(hgv)

scanias = df[df["make"] == "Scania"]

## Aggregation and GRouping

print(df.groupby('make')['max_payload_kg'].min().sort_values(ascending=False))
print(df["make"].value_counts())
print(df.groupby('make')['year'].agg(['min', 'max', 'mean']))

df[["registration", "make", "model", "max_payload_kg"]].to_csv("cleaned_data.csv")