import pandas as pd

df = pd.read_csv('data.csv')

print("=== BEFORE ===")
print(df.memory_usage(deep=True))
print(df.dtypes)

# Downcast
df['age'] = pd.to_numeric(df['age'], downcast='integer')
df['salary'] = pd.to_numeric(df['salary'], downcast='float')

print("\n=== AFTER ===")
print(df.memory_usage(deep=True))
print(df.dtypes)