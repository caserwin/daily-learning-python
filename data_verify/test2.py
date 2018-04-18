# coding: utf-8
import pandas as pd

df = pd.read_table('data2/prod.csv', sep=',', header=None, dtype=str, na_filter=False)

df.head()
