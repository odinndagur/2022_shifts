import docx
import pandas as pd

doc = docx.Document('manlol.docx')

df = pd.read_csv('/Users/odinndagur/Downloads/vaktaplans_test/Vaktaplan 11.07-10.08 lokaútgáfa.csv')

from collections import defaultdict
day = defaultdict(lambda: defaultdict(list))

for person,shift in df.iloc[:,0:2].dropna().values:
    if shift != 'ORLOF':
        time, type = shift.split(' ')
        starttime,endtime = time.split('-')
        starthr = int(starttime.split(':')[0])
        endhr = int(endtime.split(':')[0])
        if 0 < starthr < 12:
            if endhr > 16:
                col = 'dv'
            else:
                col = 'mv'
        if 12 < starthr < 16:
            col = 'dv'
        if 16 <= starthr < 23:
            col = 'kv'
        if 23 <= starthr <= 24:
            col = 'nv'
        print(person,starthr,endhr,type,col)
        day[type][col].append(' '.join([person,time,type,col]))


for col in doc.tables[1].columns:
    for cell in col.cells:
        if not any([cell.text == 'ORLOF', cell.text == '\xa0',len(cell.text.strip()) < 1]):
            print(cell.text.split(' '))