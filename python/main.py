import camelot
import numpy as np
import pandas as pd
import json
from stuff import output_directory, tablestocellinfo, file, filename, cleanuptables, is_first_page, get_first_date_cell, get_num_pages, get_pdf_size
import os
import sys

from pdf2image import convert_from_path
pdfs = convert_from_path(file)

h,w = get_pdf_size(file)
new_h,new_w = pdfs[0].height, pdfs[0].width

def get_color(img,cell):
    y = new_h - ((cell.y1 + 3)/h * new_h)
    x = ((cell.x1 + cell.x2)/2)/w * new_w
    return img.getpixel((x,y))

tables = camelot.read_pdf(file,pages='1-end',flavor='lattice',line_scale=20)
colors = set()
for idx, table in enumerate(tables):
    for row in table.cells:
        for cell in row:
            colors.add(get_color(pdfs[idx],cell))
#colors = (255, 255, 0), (198, 198, 198), (240, 240, 240), (255, 128, 255), (0, 128, 0), (255, 0, 0), (129, 129, 129), (122, 122, 122), (128, 0, 255), (255, 255, 255), (80, 138, 160), (128, 128, 64), (128, 128, 128), (128, 0, 64)

parts = []
for offset in range(0,len(tables),get_num_pages(tables)):
    first_page = tables[0+offset].df.iloc[1:,1:].copy()
    first_page.iloc[0,0] = 'Starfsmaður'
    second_page = tables[1+offset].df.copy()
    third_page = tables[2+offset].df.copy()

    first_page.index -= 1
    first_page.columns -= 1
    # second_page.index -= 1
    # third_page.index -= 1


    x,y = get_first_date_cell(second_page)
    first_page.iloc[0,1:] = second_page.iloc[y,x:]

    second_page = second_page.iloc[y+1:,x-1:]
    second_page.index -= 1 
    second_page.columns -= 1

    x,y = get_first_date_cell(third_page)
    third_page = third_page.iloc[y+1:,x-1:]
    third_page.index -= 1
    third_page.columns -= 1

    joined = pd.concat([first_page,second_page,third_page],ignore_index = True)
    joined.iloc[:,:]#.to_csv(os.path.join(output_directory,'out' + str(offset) + '.csv'))
    parts.append(joined)
total = pd.concat(parts,axis=1,ignore_index=True)
total.to_csv(os.path.join(output_directory,'output.csv'))