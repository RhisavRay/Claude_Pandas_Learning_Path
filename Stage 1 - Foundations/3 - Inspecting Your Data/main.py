import pandas as pd

df = pd.read_csv('../../data.csv')

"""
Topic — Inspecting Your Data

Before you do anything with a dataset — cleaning, filtering, analysis — you need to know what you're working with. This is not optional.
Skipping inspection and jumping straight into analysis is like driving in an unknown city without looking at the map first. You might get
somewhere, but you'll probably take a wrong turn and not realize it until much later.

Pandas gives you a small set of tools specifically for this. Let's go through each one properly.
"""



# print(df.shape)

"""
1. df.shape

Returns a tuple — (rows, columns). This is a property, not a method, so no parentheses. It's the first thing you check. Know the dimensions
of your data before anything else.
"""



# print(df.head())
# print(df.head(10))
# print(df.tail())
# print(df.tail(10))

"""
2. df.head() and df.tail()

Used to visually sanity-check your data. Did it load correctly? Are the column names right? Do the values look reasonable?

Pitfall:
    head() only shows you the beginning. Dirty data — missing values, wrong types, corrupted entries — often hides in the middle or end of
    a file. Don't assume the whole dataset is clean just because the first 5 rows look fine.
"""



# print(df.info())

"""
3. df.info()

This is the single most useful inspection tool. One call tells you:
    a. Total number of rows
    b. Range of the index values
    c. Number of columns
    d. Each column's name
    e. How many non-null values each column has
    f. Each column's dtype
    g. How many columns with each dtype are present
    h. Total RAM memory used by this dataframe

If a column shows 200 non-null but your DataFrame has 215 rows — 15 values are missing in that column. This is how you catch missing data
problems before they silently corrupt your analysis.
"""



# pd.set_option('display.float_format', '{:.2f}'.format)
# print(df.describe().to_string())
# print(df.describe(include='all').to_string())

"""
4. df.describe()

Gives you summary statistics for all numeric columns:
    a. count — how many non-null values
    b. mean — average
    c. std — standard deviation (spread of values)
    d. min, max — range
    e. 25%, 50%, 75% — quartiles

What to look for:
    a. Does min or max look unrealistic? A price_inr of -500 or engine_cc of 99999 would signal bad data
    b. Is count less than your total rows? Missing values
    c. Is std very high relative to mean? High variance — could be legitimate or could be outliers

Pitfall:
    describe() silently skips non-numeric columns by default. You can include them by passing the argument 'include = all', as in line 68.
    For object/str columns it shows count, unique, top (most frequent value), and freq (how often it appears).

Why we used pd.set_option():
    Had some issues with the float value being shown. When this statement is used every float in every DataFrame will display with 2 decimal
    places from that point on.

⚠️ One thing to be aware of:
    This setting changes display only — the actual numbers in memory are untouched. It's purely cosmetic. Also, since price_inr is int64 in
    your dataset, describe() is temporarily treating it as float for the statistics calculation — that's why it shows decimals in the output
    at all. The underlying column is still integers.
"""



