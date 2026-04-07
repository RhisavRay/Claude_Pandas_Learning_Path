import pandas as pd

df = pd.read_csv('../../data.csv')

"""
Topic — Inspecting Your Data

Before you do anything with a dataset — cleaning, filtering, analysis — you need to know what you're working with. This is not optional.
Skipping inspection and jumping straight into analysis is like driving in an unknown city without looking at the map first. You might get
somewhere, but you'll probably take a wrong turn and not realize it until much later.

Pandas gives you a small set of tools specifically for this. Let's go through each one properly.
"""



# print(df.shape)

"""
1. df.shape

Returns a tuple — (rows, columns). This is a property, not a method, so no parentheses. It's the first thing you check. Know the dimensions
of your data before anything else.
"""



# print(df.head())
# print(df.head(10))
# print(df.tail())
# print(df.tail(10))

