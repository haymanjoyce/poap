import svgwrite
import pandas as pd


df3 = pd.read_excel('../../data/excel/sample.xlsx')

print(df3)

dwg = svgwrite.Drawing('../../data/svg/test.svg', profile='tiny')

for item in df3['a']:
    print(f"{item}")
    dwg.add(dwg.rect(insert=(50, (item*50)), size=(100, 40), fill='green'))

dwg.save()
