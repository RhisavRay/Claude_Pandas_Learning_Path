import pandas as pd

# Most basic
df = pd.read_csv('data.csv')

# If your file uses semicolons instead of commas (common in European data)
df = pd.read_csv('data.csv', sep=';')

# If you want a specific column to become the index instead of 0,1,2...
df = pd.read_csv('data.csv', index_col='model')

# Read only specific columns — useful for huge files
df = pd.read_csv('data.csv', usecols=['make', 'model', 'price_inr'])

# Tell pandas which columns contain dates so it parses them properly
df = pd.read_csv('data.csv', parse_dates=['launch_date'])

# Skip the first N rows (useful when files have metadata/notes at the top)
df = pd.read_csv('data.csv', skiprows=2)

# Tell pandas what to treat as NaN
df = pd.read_csv('data.csv', na_values=['N/A', 'missing', '-'])