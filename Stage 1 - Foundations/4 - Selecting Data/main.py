import pandas as pd

df = pd.read_csv('../../data.csv')



"""
You already know how to select a column — df['make']. But what about selecting specific rows? Or a specific cell? Or a block of rows and
columns together?

That's what loc[] and iloc[] are for. These are the two most important selection tools in pandas, and the confusion between them is
responsible for more bugs than almost anything else in pandas code. Let's kill that confusion permanently.
"""



"""
The Core Distinction

There are two ways to refer to a row:
    1. By its label — the value shown in the index. This is loc[].
    2. By its position — how far from the top it is (0, 1, 2...). This is iloc[].

When your index is the default 0, 1, 2, 3... — label and position are the same number, so the difference feels invisible. It becomes very
visible the moment you filter, sort, or reset your data.


Think of it like seats in a cinema:
    iloc[] is like saying "give me the 3rd seat from the left" — purely positional
    loc[] is like saying "give me the seat labelled B7" — purely by label
"""



# print(df.iloc[0])         # first row (position 0)
# print(df.iloc[-1])        # last row
# print(df.iloc[0:5])       # first 5 rows (like Python list slicing)
# print(df.iloc[0, 2])      # row at position 0, column at position 2
# print(df.iloc[0:5, 0:3])  # first 5 rows, first 3 columns

"""
iloc[] — Position Based

iloc[] behaves exactly like Python list indexing. The rules you already know apply:
    1. Zero-based
    2. End of slice is exclusive —> 0:5 gives you positions 0,1,2,3,4 not 5
    3. Negative indexing works —> -1 is the last row
"""



# print(df.loc[0])                   # row with index LABEL 0
# print(df.loc[0:5])                 # rows with labels 0 through 5
# print(df.loc[0, 'make'])           # row label 0, column named 'make'
# print(df.loc[0:5, 'make':'type'])  # rows 0-5, columns from 'make' to 'type'

"""
loc[] — Label Based

Critical difference from iloc[]: When slicing with loc[], the end is inclusive. loc[0:5] gives you labels 0,1,2,3,4,5 — all six. This is
the opposite of Python's normal slicing behaviour and trips everyone up at least once.
"""



# expensive = df[df['price_inr'] > 2000000]
# print(expensive)
# print("Index labels after filtering:")
# print(expensive.index.to_list())    #Shows a list of only the index values of the new series for expensive bikes

# iloc - Purely positional. Always starts from 0
# print("\nexpensive.iloc[0] - First row by position:")
# print(expensive.iloc[0][['make', 'model', 'price_inr']])

# loc - Looks for the exact label 0
# print("\nexpensive.loc[0] - Row with label 0")
# try:
#     print(expensive.loc[0])
# except KeyError as e:
#     print(f"KeyError: {e} (Label 0 was not found)")

# loc with the actual first label of the expensive dataframe
# first_label = expensive.index[0]
# print(f"\nexpensive.loc[{first_label}] - Actual first row of the expensive dataframe")
# print(expensive.loc[first_label][['make', 'model', 'price_inr']])

"""
⚠️ Where Everything Goes Wrong

Lets recall something we did in topic 1 of this stage - filtering to find the expensive bikes

This is the exact trap. After filtering to expensive bikes, the index labels jump to [3, 7, 24, 28, 33, 40...]. Label 0 no longer exists.
So:
    expensive.iloc[0] — ✅ gives you the first row by position, works fine
    expensive.loc[0] — 💥 KeyError because label 0 doesn't exist in the filtered result
"""



# Single row, single column
# print(df.loc[5, 'make'])           # → 'Honda'

# Multiple rows, multiple columns
# print(df.loc[0:4, ['make', 'model', 'price_inr']])

# All rows, specific columns (note the : for all rows)
# print(df.loc[:, ['make', 'price_inr']])

# Same with iloc
# print(df.iloc[0:5, [0, 1, 11]])    # columns by position

"""
Selecting Rows AND Columns Together

This is where loc[] really shines in real analysis as giving column name is much more simpler than knowing the position of each of them
"""



# Filter rows by condition, and select specific columns
# print(df.loc[df['make'] == 'Honda', ['make', 'model', 'price_inr']])

"""
loc[] with Boolean Conditions — The Most Common Real-World Usage

This pattern — df.loc[condition, columns] — is something you'll write hundreds of times. It filters rows and selects specific columns in
one clean operation.
"""



print(df[df['price_inr'] > 2000000].reset_index(drop=True))

"""
reset_index() — Cleaning Up After Filtering

After filtering, if you want a clean 0, 1, 2... index again:

drop=True means throw away the old index labels, don't keep them as a column. Without drop=True, the old index gets saved as a new column
called index in your DataFrame — almost never what you want.
"""



"""
When to Use Which

"Give me the first/last N rows" --------------> iloc[]
"Give me row number X from the top" ----------> iloc[]
"Give me rows matching a condition" ----------> loc[]
"Give me rows by their actual index label" ---> loc[]
"Filter rows AND select columns together" ----> loc[]

When in doubt:
    a. If you're thinking in terms of position, use iloc[].
    b. If you're thinking in terms of labels or conditions, use loc[].
"""