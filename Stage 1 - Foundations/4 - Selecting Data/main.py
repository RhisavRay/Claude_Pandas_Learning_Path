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
iloc[] behaves exactly like Python list indexing. The rules you already know apply:
    1. Zero-based
    2. End of slice is exclusive —> 0:5 gives you positions 0,1,2,3,4 not 5
    3. Negative indexing works —> -1 is the last row
"""


