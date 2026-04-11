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

"""
Reordering Columns

Pandas doesn't have a dedicated "reorder" function. You simply select columns in the order you want. This works because df[list_of_columns]
selects columns in exactly the order you specify.
"""



# print('Before:', df.columns.tolist())
# print()

# Move price_inr to the front
# col = df.pop('price_inr')   # removes column and returns it as Series
# print(col)
# df.insert(0, 'price_inr', col)  # inserts it back at position 0

# print('After moving price_inr to front:', df.columns.tolist())

"""
Moving a Specific Column

A common need:
    Move one column to the front ,end or at any specified position without manually listing all others.

In th code above pop() removes the column from the DataFrame and returns it as a Series. insert(position, name, data) puts it back wherever
you want. This avoids having to type out all column names just to move one.
"""



# Drop a single column
# df = df.drop(columns=['seat_height_mm'])

# Drop multiple columns
# df = df.drop(columns=['seat_height_mm', 'fuel_tank_liters'])

"""
Dropping Columns

Sometimes you don't need a column at all. That is when we use df.drop()

Always use columns= explicitly. df.drop() can also drop rows by index label — so without specifying columns=, pandas needs to guess what
you mean and can drop the wrong thing.
"""




"""
Task 1 (Easy): Rename price_inr to price, engine_cc to displacement, and top_speed_kmh to top_speed. Verify by printing the column names.
"""

# print('\n\n --- Column names before --- ')
# print(df.columns.to_list())

# df_renamed = df.rename(columns={
#     'price_inr': 'price',
#     'engine_cc': 'displacement',
#     'top_speed_kmh': 'top_speed'
# })

# print('\n\n --- Column names after --- ')
# print(df_renamed.columns.to_list())




"""
Task 2 (Easy): Drop the seat_height_mm and fuel_tank_liters columns from the DataFrame. Confirm they're gone.
"""

# print('\n\n --- Column names before --- ')
# print(df.columns.to_list())

# df = df.drop(columns=['seat_height_mm', 'fuel_tank_liters'])

# print('\n\n --- Column names after --- ')
# print(df.columns.to_list())




"""
Task 3 (Medium): Reorder the columns so that make, model, type come first, followed by price_inr, followed by all remaining columns in their
original order. Do this without hardcoding every column name — think about how to get the remaining columns programmatically.
"""

# print('\n\n --- Column names before --- ')
# print(df.columns.to_list())

# One way to do it. But this is fragile, because after every pop and insert, the index/position of columns changes
# col = df.pop('price_inr')
# df.insert(2, 'price_inr', col)
# col = df.pop('type')
# df.insert(2, 'type', col)

# Below code is a better solution, when we know a set of columns need to be at the beginning/end
# priority = ['make', 'model', 'type', 'price_inr']
# remaining = [col for col in df.columns if col not in priority]
# df = df[priority + remaining]

# print('\n\n --- Column names after --- ')
# print(df.columns.to_list())




"""
Task 4 (Medium): Standardise all column names by making them uppercase. Do this in one line without hardcoding any column names.
"""

# print('\n\n --- Column names before --- ')
# print(df.columns.to_list())

# df.columns = df.columns.map(lambda x: x.upper())

# print('\n\n --- Column names after --- ')
# print(df.columns.to_list())




"""
Task 5 (Tricky): The column torque_nm has an inconsistency — the unit nm is part of the name, but horsepower has no unit in its name. Rename
all columns that contain units in their name to remove the unit suffix, keeping only the base measurement name. Do this programmatically —
not by hardcoding the new names directly, but by writing code that strips the suffix. Think about what string operation achieves this.
"""

# print('\n\n --- Column names before --- ')
# all_cols = df.columns.to_list()
# print(all_cols)

# print('\n\n --- Fetching columns with _ in them --- ')
# alter_cols = list(filter(lambda col: '_' in col, all_cols))
# print(alter_cols)

# print('\n\n --- Removing the units from the new list --- ')
# all_cols = [col.rsplit('_', 1)[0] if '_' in col else col for col in all_cols]
# print(all_cols)

# print('\n\n --- Adding this to the original dataframe --- ')
# df.columns = pd.Series(all_cols)
# print(df.columns)


# In the above code, we cannot nitpick for which values to alter and which to not. If we are working on something with a specific pattern
# then this works fine. But if we wanna choose which ones to change, the below code will be better

# print('\n\n --- Altering column names --- ')
# df = df.rename(columns={
#     'torque_nm': 'torque',
#     'top_speed_kmh': 'top_speed',
#     'seat_height_mm': 'seat_height'
# })
# print(df.columns.to_list())