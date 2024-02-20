from dataclasses import dataclass
import pandas as pd

from utils import get_abs_path


@dataclass
class SvgObject:
    height: int
    width: int


object_1 = SvgObject(width=100, height=100)
object_2 = SvgObject(width=100, height=100)
object_3 = SvgObject(width=100, height=200)

data = {
    'col1': [object_1.width, object_1.height],
    'col2': [object_2.width, object_2.height],
    'col3': [object_3.width, object_3.height]
}

# Create a DataFrame from the dictionary
# df = pd.DataFrame(data)
#
# print(df)

# abs_path = get_abs_path('data/csv/test.csv')
# df.to_csv(abs_path)
#
# df2 = pd.read_csv(abs_path)
#
# print(df2)

df2 = pd.DataFrame(data)

sample = get_abs_path('data/excel/sample.xlsx')
df3 = pd.read_excel(sample)

print(df3)


