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
