import pandas as pd
df = pd.read_csv('data.csv')

"""
Task 1 (Easy): Extract the model column from the DataFrame. What type of object do you get? Verify it using Python.
"""

model_column = df['model']
# print(model_column)
# print(model_column.dtype)

"""
Task 2 (Easy): Extract the make and price_inr columns together as a single object. What type do you get now? How is it different from Task 1?
"""

make_and_price_inr = df[['make', 'price_inr']]
# print(make_and_price_inr)
# print(make_and_price_inr.dtypes)

"""
Task 3 (Medium): Create a Series manually that contains the names of 5 bike types of your choice (e.g., Naked, Sport...). Then check what
its index looks like by default.
"""

bike_types = pd.Series(['Naked', 'Sport', 'Adventure', 'Dirt', 'Touring'])
# print(bike_types)

"""
Task 4 (Slightly tricky): After loading the DataFrame, check what the index of the DataFrame looks like. Now filter the DataFrame to only
keep bikes with price_inr greater than 1,000,000. After filtering, what does the index of the resulting DataFrame look like? Is it reset or
not?
"""

# print(df)
new_df = df[df['price_inr'] > 1000000]
# print(new_df)