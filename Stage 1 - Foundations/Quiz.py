import pandas as pd

df = pd.read_csv('../data.csv')
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



"""
Section B — Code Questions
"""


"""
Q6. Write code that loads data.csv and in one line prints the number of bikes for each make in descending order.
"""

# print(pd.read_csv('../data.csv')['make'].value_counts())



"""
Q7. Write code to find all bikes where engine_cc is greater than 1000 AND price_inr is less than 2,000,000. Show only make, model, engine_cc
and price_inr.
"""

# filtered_dataframe = df[(df['engine_cc'] > 1000) & (df['price_inr'] < 2000000)]
# print(filtered_dataframe[['make', 'model', 'engine_cc', 'price_inr']])



"""
Q8. Without using sort_values(), write code that retrieves the row containing the bike with the highest horsepower. Use only inspection and
selection tools.
"""

# max_power = df['horsepower'].max()
# print(df[df['horsepower'] == max_power].to_string(index=False))



"""
Q9. Write code that loads data.csv but only reads the make, model, type and price_inr columns, then checks how many unique type values exist,
and prints the actual type names.
"""

# df_1 = pd.read_csv('../data.csv', usecols=['make', 'model', 'type', 'price_inr'])
# print(df_1['type'].nunique())
# print(df_1['type'].unique())



"""
Q10. Look at this code:

df2 = df[df['type'] == 'Adventure']
print(df2.iloc[0])
print(df2.loc[0])

Will both lines work? What will each print, or what error will occur and why?
"""

"""
Solution:
No. the iloc lien works as it isn't looking for the exact index 0. It is just finding the first entry of the new dataframe.
While loc tries to look for the entry with index 0, which has been filtered out in the new dataframe.
"""