import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

# New column
df['annual_bonus'] = df['salary'] * 0.10

# Simple condition
df['seniority'] = np.where(df['age'] > 30, 'Senior', 'Junior')

# Multiple conditions
conditions = [
    df['salary'] < 55000,
    df['salary'].between(55000, 65000),
    df['salary'] > 65000
]

choices = ['Low', 'Mid', 'High']

df['salary_band'] = np.select(conditions, choices, default='Unknown')

# Apply function
df['name_length'] = df['name'].apply(len)

# Custom function
def categorize_age(age):
    if age < 26:
        return 'Young'
    elif age < 35:
        return 'Mid'
    else:
        return 'Senior'

df['age_group'] = df['age'].apply(categorize_age)

print(df)