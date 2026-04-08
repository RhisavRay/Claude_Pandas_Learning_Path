"""
Section A — Conceptual Questions


Q1. What is the difference between a Series and a DataFrame? If you do df['make'] vs df[['make']], what type does each return and why?

Ans 1:
A series is like an entry in an Excel sheet. While dataframe is like the entire Excel sheet.
df['make'] will return a series, while df[['make']] returns a dataframe. The reason being, in the second case when we pass it inside [],
pandas takes it as a list of values. It doesn't matter that there is only 1 value in this list.


Q2. You save a DataFrame with df.to_csv('output.csv') and reload it with df = pd.read_csv('output.csv'). What problem will you likely run
into and how do you fix it — at save time and at load time?

Ans 2:
Save time fix: df.to_csv('output.csv', index=False) — prevents the index from being written into the file at all
Load time fix: pd.read_csv('output.csv', index_col=0) — tells pandas the first column is the index, not data


Q3. After filtering a DataFrame, why is it dangerous to use loc[0] on the result? What should you use instead if you want the first row?

Ans 3:
When we are filtering a dataframe, we are basically removing entries based on our condition. Now the entry which had an index 0 (First entry
before filtering), might get removed. The indices don't get recalculated after filtering. So using .loc[], which looks for that exact index
might give you a KeyError, saying the index 0 was not found.
If you want the first index in this situation, you could either use '.reset_index(drop = True)' and continue with the use of '.loc[0]', as
in this case, you have manually reset the index.
Or you could just use '.iloc[0]'. This doesn't look for the exact index. Rather it will return the first entry of the resulting dataframe.


Q4. loc[0:5] and iloc[0:5] — how many rows does each return, and why are they different?

Ans 4:
'loc[0:5]' will return 6 entries - 0, 1, 2, 3, 4, 5
'iloc[0:5]' will return 5 entries - 0, 1, 2, 3, 4
The reason being for 'loc' both extremes of the limit are inclusive, while the right limit in excluded in case of 'iloc'


Q5. You load a CSV and notice that price_inr has dtype str instead of int64. Name two things that could have caused this, and what problem will it create downstream?

Ans 5:
Potential reasons for the issue:
1. Someone wrote the price in words
2. Someone used commas in the number

Problems this can create:
Aggregate functions/operations on the price_inr field will not work, or give unexpected results
"""

