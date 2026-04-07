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



# print(df.columns)

"""
5. df.columns

df.columns gives you all column names — useful when you want to programmatically loop over columns or check if a column exists.

The dtype='object' at the end of df.columns output is not describing your data columns. It's describing the Index object itself —
specifically, what type the column names are stored as.

pythonIndex(['make', 'model', 'year', ...], dtype='object')

Your column names are strings like 'make', 'model', 'year'. Pandas stores those strings internally as object dtype — the same dtype it uses
for any string data.


Why does this matter?

It would matter if your column names were not strings. For example, if you had a DataFrame where columns were integers:

pythondf = pd.DataFrame([[1,2,3], [4,5,6]])
print(df.columns)
# → RangeIndex(start=0, stop=3, step=1)

Or if you explicitly set integer column names:

df.columns = [1, 2, 3]
print(df.columns)
# → Index([1, 2, 3], dtype='int64')

Now the dtype would be int64 because the column names themselves are integers. This actually has practical consequences — you'd need to
use df[1] instead of df['make'] to access a column.


What if mixed column names?

1. Mixed column names → dtype stays object
    
    Index(['make', 2, 'type', 4], dtype='object')
    
    When column names are mixed types, pandas still shows dtype='object' — because object is essentially pandas' way of saying "mixed or
    string data, I'm not going to be more specific." It's the fallback dtype for anything that isn't cleanly numeric.

2. The practical danger of mixed column names

    df[2]    # ✅ works — integer key for integer column name
    df['2']  # ❌ KeyError — string '2' ≠ integer 2

    Pandas is strict about this. The type of the key you use to access a column must match the type of the column name exactly. 2 and '2'
    are completely different things to pandas.
    
    This is a real-world bug that shows up when you load messy Excel files where some headers got saved as numbers instead of strings.
    Your code will work fine on some columns and silently fail on others.


The takeaway
    Mixed column names are a sign of a dirty dataset. The first thing you'd do when you encounter them is standardise — either make all
    column names strings, or rename them entirely. We'll cover df.rename() and df.columns = [...] in Stage 2.
"""



# print(df.dtypes)

