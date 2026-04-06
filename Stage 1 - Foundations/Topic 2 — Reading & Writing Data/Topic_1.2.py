import pandas as pd

# Most basic
df_1 = pd.read_csv('../../data.csv')

# If your file uses semicolons instead of commas (common in European data)
# df_2 = pd.read_csv('data.csv', sep=';')

# If you want a specific column to become the index instead of 0,1,2...
df_3 = pd.read_csv('../../data.csv', index_col='model')

# Read only specific columns — useful for huge files
df_4 = pd.read_csv('../../data.csv', usecols=['make', 'model', 'price_inr'])

# Tell pandas which columns contain dates so it parses them properly
# df_5 = pd.read_csv('data.csv', parse_dates=['launch_date'])

# Skip the first N rows (useful when files have metadata/notes at the top)
df_6 = pd.read_csv('../../data.csv', skiprows=2)

# Tell pandas what to treat as NaN
df_7 = pd.read_csv('../../data.csv', na_values=['N/A', 'missing', '-'])

"""
What pd.read_csv() Actually Does
When you call pd.read_csv('data.csv'), pandas does several things automatically:

1. Reads the first row as column headers — unless you tell it otherwise
2. Infers the data type of each column — it scans the values and guesses: is this integers? floats? strings?
3. Assigns a default RangeIndex — 0, 1, 2... as row labels
4. Handles the file path — relative to wherever your script is running from


⚠️ The Type Inference Trap
This is the most important thing in this topic. When pandas reads your CSV, it guesses types. Most of the time it gets it right. But here
are the cases where it quietly goes wrong:

Case 1 — A numeric column that has one stray text value:
    
    price_inr
    550000
    850000
    N/A        ← pandas sees this as a string
    1200000
    
    Pandas will read the entire price_inr column as object dtype (pandas' word for string/mixed) instead of int, because of that one bad
    value. Every numeric operation you do on it will either fail or give wrong results.


Case 2 — A column of IDs that look like numbers:
    Imagine a bike_id column with values like 00123, 00456. Pandas will read these as integers 123, 456 — stripping the leading zeros. If
    those IDs are meant to be matched against another dataset that preserved the leading zeros, your merge will silently fail to find any
    matches.


Case 3 — Mixed types in a column:
    If a column has both integers and strings, pandas gives it object dtype. You won't get an error — but operations like .mean() will fail
    later when you least expect it.


The habit to build:
    Always run df.dtypes right after loading a file. Check that each column got the type you expected.
"""


# Save to CSV
df_1.to_csv('output.csv')

# The index=False is important — without it, pandas writes the 0,1,2 index
# as an extra column in your CSV, which is almost never what you want
df_1.to_csv('output.csv', index=False)

# Save only specific columns
df_1[['make', 'model', 'price_inr']].to_csv('output.csv', index=False)

"""
Not writing the index=False will give an unnamed first column full of row numbers.

If multiple '.to_csv()' are done to the same file path, the data in that file gets overridden
"""



"""
Task 1 (Easy): Load data.csv and immediately check the dtypes of all columns. Write down which columns are numeric and which are
non-numeric. Do the dtypes match what you'd expect?
"""

# df = pd.read_csv('data.csv')
# print(df.to_string())
# print(df.dtypes)


"""
Task 2 (Easy): Load data.csv but this time only load 3 columns of your choice. Confirm that only those columns were loaded.
"""

# df = pd.read_csv('data.csv', usecols=['make', 'model', 'price_inr'])
# print(df)


"""
Task 3 (Medium): Load data.csv with the model column set as the index. Print the first few rows. How does the DataFrame look different
from the default load?
"""

# df = pd.read_csv('data.csv', index_col='model')
# print(df.head())


"""
Task 4 (Medium): Filter the DataFrame to only keep bikes made by Honda, then save that filtered result to a new CSV file called
honda_bikes.csv — without writing the index into the file. Then reload that saved CSV and confirm it looks correct.
"""

# df = pd.read_csv('data.csv')
# df = df[df['make'] == 'Honda']
# df.to_csv('honda_bikes.csv', index=False)
# honda_bikes = pd.read_csv('honda_bikes.csv')
# print(honda_bikes)


"""
Task 5 (Tricky): Load data.csv, then save it to a new CSV with the index written in (don't use index=False). Now reload that saved file.
What problem do you notice? How would you fix it on the reload?
"""

df = pd.read_csv('../../data.csv', index_col=0)
df.to_csv('new.csv')

"""
Now you might be wondering why we have 2 ways to achieve the same solution - 'index_col = 0' and 'index = False'

They look like they achieve the same end result, but they work at opposite ends of the pipeline and do fundamentally different things.

'index = False' — Prevention (at write time):
    You're telling pandas: "don't write the index into the file at all." The index never touches the CSV. The file stays clean.

'index_col = 0' — Recovery (at read time):
    The index was already written into the CSV as a plain column. Now you're telling pandas: "treat the first column as the index, not as
    data." You're not preventing the problem — you're correcting it after the fact.
"""