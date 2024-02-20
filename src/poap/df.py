from dataclasses import dataclass
import pandas as pd


@dataclass
class SvgObject:
    height: int
    width: int


object_1 = SvgObject(height=100, width=100)
object_2 = SvgObject(height=100, width=100)
object_3 = SvgObject(height=100, width=100)

data = {
    'col1': [object_1.width, object_1.height],
    'col2': [object_2.width, object_2.height],
    'col3': [object_3.width, object_3.height]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

print(df)
