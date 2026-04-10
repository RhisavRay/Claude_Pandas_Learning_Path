import numpy as np
import pandas as pd

df = pd.read_csv('../../data.csv')

"""
Why Data Cleaning Exists?

In the real world, data is collected by humans, exported from different systems, merged from multiple sources, and passed through pipelines
that nobody fully understands anymore. By the time it reaches you, it's almost never clean. Missing values, wrong types, duplicate rows,
inconsistent formatting — these are not edge cases. They are the norm.

The danger is not that dirty data throws errors. Errors are actually the good outcome — you know something is wrong. The real danger is
dirty data that silently produces wrong results. A missing value that gets treated as zero. A duplicate row that inflates your average. A
column that looks numeric but is secretly a string. Your analysis runs fine, produces a number, and that number is wrong. Nobody notices.

Data cleaning is how you prevent that.
"""


"""
What is a Missing Value in Pandas?

Pandas represents missing data as NaN — which stands for "Not a Number". It comes from the numpy library underneath pandas. You'll also
sometimes encounter None (Python's null object) — pandas treats these as interchangeable in most situations, converting None to NaN
automatically in numeric columns.
"""


# NaN is a float value from numpy
# print(type(np.nan))   # → float

"""
This has an important consequence: a column of integers that gains even one missing value gets silently converted to float. Because NaN is a
float, and an integer column can't hold a float, pandas upgrades the whole column to float64. You'll see your clean int64 column become
float64 the moment one NaN sneaks in.
"""



# Introduce some missing values for demonstration
# df_dirty = df.copy()
# df_dirty.loc[2, 'horsepower'] = np.nan
# df_dirty.loc[5, 'price_inr'] = np.nan
# df_dirty.loc[10, 'horsepower'] = np.nan
# df_dirty.loc[15, 'make'] = np.nan
# df_dirty.loc[20, 'price_inr'] = np.nan

# print(' --- isnull() on a single column --- ')
# print(df_dirty['horsepower'].isnull().head(15))
#
# print('\n --- sum of missing values per column --- ')
# print(df_dirty.isnull().sum())
#
# print('\n --- which rows have ANY missing value --- ')
# print(df_dirty[df_dirty.isnull().any(axis=1)])

"""
Detecting Missing Values


Here's what these tools give you:

    1. df.isnull() — returns a DataFrame of the same shape, with True where values are missing and False where they aren't. By itself it's
    hard to read on large data.
    2. df.isnull().sum() — the useful one. Collapses each column to a count of missing values. This is your go-to check after loading any
     real dataset.
    3. df.isnull().any(axis=1) — returns True for any row that has at least one missing value. axis=1 means "check across columns for each
    row." Use it to isolate exactly which rows are problematic.
"""



