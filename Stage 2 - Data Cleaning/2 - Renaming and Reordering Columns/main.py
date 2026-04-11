import pandas as pd

df = pd.read_csv('../../data.csv')


"""
The Big Picture
You'll rarely work with data that has perfectly named columns straight out of the box. Real datasets come with column names that are
inconsistent, too long, have spaces, are in different cases, or simply don't make sense in your context. Renaming and reordering columns is
one of the first things you do when standardising a dataset before analysis.
"""



# df_renamed = df.rename(columns={
#     'price_inr': 'price',
#     'engine_cc': 'displacement',
#     'top_speed_kmh': 'top_speed'
# })
#
# print('\n\n --- Before --- \n')
# print(df.columns.to_list())
# print('\n\n --- After --- \n')
# print(df_renamed.columns.to_list())

"""
Renaming Columns

The most precise way to rename specific columns:
    df.rename(columns={ <old_name> : <new_name> })
You pass a dictionary where keys are current names and values are the new names. You only need to include the columns you want to rename —
the rest stay untouched.
"""


