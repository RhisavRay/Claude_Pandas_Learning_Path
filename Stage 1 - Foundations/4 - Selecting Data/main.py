import pandas as pd

df = pd.read_csv('../../data.csv')


"""
You already know how to select a column — df['make']. But what about selecting specific rows? Or a specific cell? Or a block of rows and
columns together?

That's what loc[] and iloc[] are for. These are the two most important selection tools in pandas, and the confusion between them is
responsible for more bugs than almost anything else in pandas code. Let's kill that confusion permanently.


"""