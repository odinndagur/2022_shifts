import pandas as pd
import os
from pathlib import Path
import pdfplumber


output_directory = os.path.join(Path(__file__).parent.resolve().parent.resolve(),'output')
file = '/Users/odinndagur/Code/Github/2022_shifts/input/lokaútgáfa 11.ágúst - 10. sept.pdf'
file = '/Users/odinndagur/Code/Github/2022_shifts/input/11okt10nov.pdf'
filename = os.path.basename(file)

buffer = 0.2

shiftcolors = {
  'LRL': (0.501961,0.0,1.0),
  'PHA': (0.501961,0.501961, 0.501961),
  'GH': (1.0, 1.0, 0.0),
  'Orlof': (0.313726, 0.541176, 0.627451),
  'Símavakt': (0.501961, 0.501961, 0.25098),
  'BÓB': (0.0, 0.501961, 0.752941),
  'GR': (1.0,0.0,0.0),
  'NV': (1.0, 0.501961, 1.0),
  'JS': (0.0, 0.501961, 0.0),
  'Undirbúningur': (1.0,1.0,1.0),
  '': (0.0,0.0,0.0),
  ' ': (0.941176, 0.941176, 0.941176)
}

def getShiftByColor(color):
    return(list(shiftcolors.keys())[list(shiftcolors.values()).index(color)])


def tablestocellinfo(tables):
    cellinfo = []
    for i in range(tables.n):
        table = tables[i]
        for j in range(len(table.cells)):
            row = table.cells[j]
            for ii in range(len(row)):
                cell = row[ii]
                temp = {'text' : cell.text, 'x1' : cell.x1, 'y1' : cell.y1, 'x2' : cell.x2, 'y2' : cell.y2, 'shifttype' : '', 'table' : i,  'row' : j, 'col' : ii}
                # temp = (cell.text,cell.x1-1,cell.y1-1,cell.x2+1,cell.y2+1,'shifttype')
                cellinfo.append(temp)
                # print(temp)
    return cellinfo

def alternate_tablestocellinfo(tables):
    cellinfo = []
    for table_num,table in enumerate(tables):
        for row_num,row in enumerate(table.cells):
            for col_num,cell in enumerate(row):
                cellinfo.append(
                    {
                        'text' : cell.text,
                        'x1' : cell.x1,
                        'y1' : cell.y1,
                        'x2' : cell.x2,
                        'y2' : cell.y2,
                        'shifttype' : '',
                        'table' : table_num,
                        'row' : row_num,
                        'col' : col_num,
                    }
                )
    return cellinfo


def cleanuptables(tables):
    # out = '/Users/odinndagur/Code/Github/vaktaplan/output/'
    docs = []
    for i in range(0,tables.n, 2):
        df = tables[i].df #even
        df2 = tables[i+1].df #odd

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

        total = df.append(df2, ignore_index = True)
        # total.to_csv(out + "vaktaplan" + str(int(i/2)) + ".csv")
        docs.append(total)

    first = docs[0]
    for i in range(len(docs)):
        if(i != 0):
            temp = docs[i].iloc[:,1:]
            first = pd.concat([first, temp], axis=1)

    first.to_csv(os.path.join(output_directory, "ALLT.csv"))
    return first

def is_first_page(df):
    for x in df.iloc[:,0].values:
        if 'Hæf' in x:
            return True
    return False

def get_first_date_cell(df):
    import re
    for row_idx,row in df.iterrows():
        for col_idx, cell in enumerate(row):
            # print(f'row {row_idx}, col {col_idx}, cell: {cell}')
            if re.match('[0-9][0-9]\.[0-9][0-9]', cell):
                return col_idx,row_idx

def get_num_pages(tables):
    counts = []
    last_first_page = 0
    for idx,table in enumerate(tables):
        if is_first_page(table.df):
            if idx > 0:
                counts.append(idx - last_first_page)
                last_first_page = idx
    if len(set(counts)) == 1:
        return counts[0]
    else:
        return counts

def get_pdf_size(filepath):
    with pdfplumber.open(filepath) as pdf:
        page_1 = pdf.pages[0]
    return page_1.height, page_1.width

