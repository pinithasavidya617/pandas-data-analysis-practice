import pandas as pd

df = pd.read_csv('data.csv')

# Rename
df = df.rename(columns={'name': 'full_name', 'age': 'years'})

# Clean column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Sort
df = df.sort_values(['city', 'salary'], ascending=[True, False])

# Drop columns
df = df.drop(columns=['salary'])

# Drop duplicates
df = df.drop_duplicates()

print(df)