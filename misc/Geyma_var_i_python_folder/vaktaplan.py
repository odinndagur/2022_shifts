import camelot
import numpy as np
import pandas as pd

file = "../input/11okt10nov.pdf"
file ='/Users/odinndagur/Code/Github/vaktaplan/input/11okt10nov.pdf'


tables = camelot.read_pdf(file,pages='1-end')

docs = []
out = "../output/"
out = '/Users/odinndagur/Code/Github/vaktaplan/output/'
for i in range(0,tables.n, 2):
    df = tables[i].df #even
    df2 = tables[i+1].df #odd

    df.to_csv(out + 'original_df' + str(i) + '.csv')
    df2.to_csv(out + 'original_df' + str(i+1) + '.csv')

    df2 = df2.iloc[:,1:]
    df2.iloc[0,0] = "Starfsmaður"
    headers = df2.iloc[0]
    # headers.to_csv(out + "headers" + str(i+1) + ".csv")

    df = df.iloc[2: , 1:]
    df2 = df2.iloc[1: , :]

    df.index = df.index - 1

    df.columns = headers
    df2.columns = headers

    # df.dropna(how='all',axis=1)
    # df2.dropna(how='all',axis=1)

    df.to_csv(out + 'df' + str(i) + '.csv')
    df2.to_csv(out + 'df' + str(i+1) + '.csv')

    total = df.append(df2, ignore_index = True)
    total.to_csv(out + "vaktaplan" + str(int(i/2)) + ".csv")
    docs.append(total)

first = docs[0]
for i in range(len(docs)):
    if(i != 0):
        temp = docs[i].iloc[:,1:]
        first = pd.concat([first, temp], axis=1)

first.to_csv(out + "ALLT.csv")