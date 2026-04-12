import pandas as pd

df = pd.read_csv('data.csv')

print("Shape:", df.shape)
print("Rows:", len(df))
print("\nColumns:\n", df.columns)
print("\nData Types:\n", df.dtypes)

print("\nHead:\n", df.head())
print("\nTail:\n", df.tail(2))
print("\nSample:\n", df.sample(2))

print("\nDescribe (numeric):\n", df.describe())
print("\nDescribe (object):\n", df.describe(include='str'))

print("\nInfo:")
df.info()

print("\nValue Counts:\n", df['city'].value_counts())
print("Unique cities:", df['city'].nunique())

print("\nMissing per column:\n", df.isnull().sum())
print("Total missing:", df.isnull().sum().sum())
print("\nMissing %:\n", df.isnull().mean() * 100)