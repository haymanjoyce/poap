import pandas as pd

from utils import get_abs_path


sample = get_abs_path('data/excel/sample.xlsx')
df3 = pd.read_excel(sample)

print(df3)

df3['d'] = df3['a'] + df3['b']

print(df3)
