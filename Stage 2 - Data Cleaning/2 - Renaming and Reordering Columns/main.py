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



# A common real-world pattern - standardize all column names
# Strip whitespace, lowercase, replace spaces with underscores
# df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
# print(df.columns.to_list())

"""
Renaming All Columns at Once

If you want to rename every column in one go, assign a list directly. This is useful when you're standardising an entire dataset — for
example, making all names lowercase with underscores. But be careful — the list must have exactly the same length as the number of columns,
and the order matters. If you get either wrong, you'll either get an error or silently mislabel columns.


⚠️ Pitfalls with Renaming

Pitfall 1 — Renaming a column that doesn't exist

    df.rename(columns={'pricc_inr': 'price'})   # typo in key
Pandas silently does nothing. No error, no warning. The column stays named price_inr. This is one of those quiet failures — always verify
after renaming.

Pitfall 2 — Duplicate column names

Nothing stops you from renaming two columns to the same name.
    df.rename(columns={'engine_cc': 'value', 'horsepower': 'value'})
Now you have two columns called value. df['value'] will return both as a DataFrame instead of a Series. This causes confusing bugs
downstream.
"""



# Define your desired order
# new_order = ['make', 'model', 'type', 'year', 'price_inr', 'engine_cc', 'horsepower', 'torque_nm', 'top_speed_kmh', 'weight_kg', 'fuel_tank_liters', 'seat_height_mm']

# df = df[new_order]
# print(df.columns.tolist())

