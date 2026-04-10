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




# print(' \n--- axis=0 (scan down each column, the default value) --- ')
# print(df_dirty.isnull().any(axis=0))
# print(' \n--- axis=1 (scan across each row) --- ')
# print(df_dirty.isnull().any(axis=1).head(20))

"""
axis is one of those things that keeps appearing everywhere in pandas, so let's get it right once and for all.

The Mental Model

A DataFrame has two directions you can move in:
    axis = 0 — move down the rows (across the row index)
    axis = 1 — move across the columns

Applied to isnull().any()

df.isnull().any(axis=1)

any() is asking: "does at least one True exist?"
The axis=1 tells it which direction to scan. So it scans across columns for each row — and asks "for this row, is any value missing?"

Visually:
         make    model   horsepower   price_inr
row 2   False   False     True        False    → True  (found one)
row 5   False   False     False       True     → True  (found one)
row 7   False   False     False       False    → False (none found)

It collapses each row horizontally into a single True/False answer.


If you used axis=0 instead:

df.isnull().any(axis=0)

Now it scans down each column and asks "for this column, does any row have a missing value?" — which is what isnull().sum() also tells you, just as True/False instead of a count.


The Rule of Thumb
    axis = 0 → operation collapses rows (moves vertically, result is per column)
    axis = 1 → operation collapses columns (moves horizontally, result is per row)

This same axis parameter shows up in drop(), mean(), sum(), concat() and many more. Same logic applies everywhere.
"""



# Drop any row that has at least one NaN
# df_clean = df.dropna()

# Drop only if ALL values in a row are NaN (rarely what gets practically used)
# df_clean = df.dropna(how='all')

# Drop rows only if NaN exists in specific columns you care about
# df_clean = df.dropna(subset=['price_inr', 'horsepower'])

"""
Dropping Missing Values

⚠️ The big pitfall with dropna():
    It's destructive. You lose the entire row because one column had a missing value. If your dataset has 20 columns and only one has a
    missing value, you're throwing away 19 perfectly good data points per row. Always think before dropping — is the missing value in a
    column that matters for your analysis?
"""



# df.dropna(inplace=True)   # modifies df directly
# df = df.dropna()          # same result, but explicit reassignment

"""
⚠️ inplace — something you'll see everywhere:

Both lines of code do the same thing. But inplace=True is actually being discouraged in modern pandas — it can cause subtle bugs in chained
operations. The habit to build is df = df.dropna(). Always reassign explicitly.


What inplace=True does?

Normally when you call df.dropna(), pandas creates a new DataFrame with the rows removed and returns it. Your original df is untouched.
That's why you need to reassign.

With inplace=True, pandas skips creating a new object and modifies the original directly.


Why it's being discouraged?

The problem shows up with chained operations — when you do multiple operations in sequence. We will see this with the example below.
"""

# df_dirty = df.copy()
# df_dirty.loc[2, 'horsepower'] = np.nan

# Filtering creates a VIEW or COPY - pandas decides internally
# filtered = df_dirty[df_dirty['make'] == 'Honda']

# Now trying inplace on this filtered result
# filtered.dropna(inplace=True)
# print('Rows in filtered after inplace dropna:', len(filtered))

# Did the original df_dirty change?
# print('NaN still in df_dirty?', df_dirty['horsepower'].isnull().sum())

"""
Here's the core issue. When you filter a DataFrame, pandas internally decides whether the filtered dataframe is a view (a window into the
original data) or a copy (a brand new independent object). You don't get to control this — pandas decides based on how the operation was
performed.

This matters because:
    If filtered is a view → inplace=True modifies the original df_dirty too. Unintended side effect.
    If filtered is a copy → inplace=True modifies only the copy, and you might think you changed df_dirty but you didn't.

Either way you're not fully in control of what got changed. This is the SettingWithCopyWarning you may have seen in pandas — it's pandas
warning you that it's not sure whether you're modifying a view or a copy.

And that is why explicit reassignment is always safe. Here there is zero ambiguity. You're saying: "take whatever dropna() returns — a
guaranteed new object — and make df point to it." You always know exactly what changed and what didn't.
"""

"""
How does pandas decide whether a filtered dataframe is a view or a copy?

This is actually a really important finding — and it's specific to the pandas version we're running. Let me explain the full picture.


The Old Behaviour (pandas < 2.0):

In older pandas, when you filtered a DataFrame, pandas made an internal decision based on the type of operation:
    1. Simple column selection like df['make'] → usually a view (shared memory with original)
    2. Boolean filtering like df[df['make'] == 'Honda'] → usually a copy
    3. Chained operations like df[df['make'] == 'Honda']['model'] → unpredictable — sometimes view, sometimes copy

The rules were complex, inconsistent, and even pandas itself wasn't always sure. That's why it would throw the SettingWithCopyWarning — it
was genuinely uncertain what you were operating on. This was a long-standing design flaw that confused everyone, including experienced
users.


The New Behaviour (pandas >= 3.0 — your version):

Pandas 3.0 introduced Copy-on-Write (CoW) as a permanent, non-optional behaviour. The rule is now beautifully simple:
    Any DataFrame that came from another DataFrame is treated as a copy — but only actually copied the moment you try to modify it.

So in our version,
    filtered = df[df['make'] == 'Honda']
No copy made yet, memory is shared

The moment you do,
    filtered.loc[0, 'make'] = 'MODIFIED'
Now pandas makes a copy, applies the change to that copy, and the original df is untouched

This is why modifying filtered didn't affect df in the test above. pandas silently made a copy at the moment of modification.


Should you still use df = df.dropna() style?

Yes — and here's why even in pandas 3.0. Even though CoW protects you from accidentally modifying the original, inplace=True still returns
None. So if you ever accidentally write:
    df = df.dropna(inplace=True)   # ← common mistake
df is now None. Your entire DataFrame is gone for the rest of the script. Explicit reassignment df = df.dropna() has no such risk.

The habit of explicit reassignment is still the right one — CoW just means the other failure mode (accidentally changing the original) is
now also fixed.
"""



# df_dirty = df.copy()
# df_dirty.loc[2, 'horsepower'] = np.nan
# df_dirty.loc[10, 'horsepower'] = np.nan
# df_dirty.loc[5, 'price_inr'] = np.nan

# Fill with a fixed value
# print(' --- Fill horsepower with 0 --- ')
# print(df_dirty['horsepower'].fillna(0).iloc[0:15:2])

# Fill with the mean of the column
# mean_hp = df_dirty['horsepower' ].mean ()
# print(f'Mean horsepower: {mean_hp :. 2f}')
# print(' --- Fill horsepower with column mean --- ')
# print(df_dirty['horsepower'].fillna(mean_hp) . iloc[0:15:2])

# Forward fill - fill with the previous valid value
# print(' --- Forward fill horsepower --- ')
# print(df_dirty['horsepower'].ffill() . iloc[0:15:2])

"""
Filling Missing Values — fillna():

Sometimes dropping rows is too aggressive. You want to fill in a reasonable value instead.

Three common strategies — and each one is appropriate in different situations:
    
    1. Fill with a fixed value - Use when you know what the missing value should be. Example: if a bike has no listed fuel tank, treating it as 0 might make sense
    contextually, or might be completely wrong depending on why it's missing.
    
    2. Fill with the column mean — The most common strategy for numeric data. It doesn't distort the average of the column because you're
    filling with the average itself. But it does reduce variance — you're making the data look less spread out than it really is.
    
    3. Forward fill (ffill()) — fills each missing value with the previous valid value. Makes most sense for time series data where values
    evolve gradually. On our bikes dataset it would be meaningless — why would a missing horsepower value equal the previous bike's
    horsepower?

The key question to ask before filling: Why is this value missing? The answer determines the right strategy. Missing at random → mean fill
is usually fine. Missing because the data was never collected → filling might introduce false information.
"""



# print('Original horsepower dtype:', df['horsepower'].dtype)
#
# df.loc[2, 'horsepower'] = np.nan
# print('After adding NaN:', df['horsepower'].dtype)
#
# df['horsepower' ] = df['horsepower' ]. fillna(df['horsepower'].mean())
# print('After fillna:', df['horsepower'].dtype)
#
# df['horsepower' ] = df['horsepower'].astype(int)
# print('After converting back to int:', df['horsepower'].dtype)

"""
⚠️ The Integer → Float Conversion Trap:

Notice — even after filling the NaN, the column stays float64. Filling doesn't automatically restore the original type. You have to
explicitly convert back with astype(int) — which we'll cover properly in Topic 2.3. I'm flagging it now so it doesn't surprise you.
"""


# Setup for tasks
df_dirty = df.copy()

# Introduce missing values
df_dirty.loc[2, 'horsepower'] = np.nan
df_dirty.loc[10, 'horsepower'] = np.nan
df_dirty.loc[50, 'horsepower'] = np.nan
df_dirty.loc[5, 'price_inr'] = np.nan
df_dirty.loc[20, 'price_inr'] = np.nan
df_dirty.loc[15, 'make'] = np.nan
df_dirty.loc[100, 'engine_cc'] = np.nan



"""
Task 1 (Easy): Find how many missing values exist in each column of df_dirty. Then find the total number of missing values across the
entire DataFrame.
"""

# print('\n\n --- No of missing values of each column --- ')
# print(df_dirty.isnull().sum())

# print('\n\n --- Total no of missing values across all columns --- ')
# print(df_dirty.isnull().sum().sum())




"""
Task 2 (Easy): Display only the rows from df_dirty that have at least one missing value.
"""

# print('\n\n --- Rows that have at least one null value --- ')
# print(df_dirty[df_dirty.isnull().any(axis=1) == True].to_string())




"""
Task 3 (Medium): Create a cleaned version of df_dirty by dropping all rows that have a missing value in either price_inr or horsepower. How
many rows does the cleaned DataFrame have?
"""

# print('\n\n --- Removing rows with null value in price_inr or horsepower --- ')
# df_clean = df_dirty.dropna(subset=['price_inr', 'horsepower'])

# print('\n\n --- No of rows in the cleaned dataframe --- ')
# print(len(df_clean))




"""
Task 4 (Medium): Instead of dropping, fill the missing horsepower values with the mean horsepower of the dataset. Fill the missing price_inr
values with the median price. Verify your fills worked.
"""

# print('\n\n --- Filling missing horsepower values with the mean HP --- ')
# mean_hp = df_dirty['horsepower'].mean()
# df_dirty['horsepower'] = df_dirty['horsepower'].fillna(mean_hp)

# print('\n\n --- Filling missing price_inr values with the median price_inr --- ')
# median_price = df_dirty['price_inr'].median()
# df_dirty['price_inr'] = df_dirty['price_inr'].fillna(median_price)




"""
Task 5 (Tricky): After filling missing values in Task 4, you'll notice horsepower is now float64 even though it should logically be integers.
Fix this — but only if there are no more missing values in the column. Write code that checks first, then converts.
"""

# print(df_dirty['horsepower'])

# if df_dirty['horsepower'].isnull().sum() == 0:
#     df_dirty['horsepower'] = df_dirty['horsepower'].astype(int)

# print(df_dirty['horsepower'])



