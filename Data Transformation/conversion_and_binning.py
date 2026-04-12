import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

# Type conversion
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['salary'] = df['salary'].astype(float)
df['city'] = df['city'].astype('category')

# Binning
df['age_bin'] = pd.cut(df['age'], bins=3, labels=['Young', 'Mid', 'Senior'])

df['salary_bin'] = pd.cut(
    df['salary'],
    bins=[0, 40000, 60000, 80000, float('inf')],
    labels=['Low', 'Mid', 'High', 'Top']
)

df['salary_quartile'] = pd.qcut(df['salary'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

print(df)