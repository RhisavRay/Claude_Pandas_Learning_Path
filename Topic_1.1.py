import pandas as pd
df = pd.read_csv('data.csv')

"""
Task 1 (Easy): Extract the model column from the DataFrame. What type of object do you get? Verify it using Python.
"""

model_column = df['model']
# print(model_column)
# print(model_column.dtype)
