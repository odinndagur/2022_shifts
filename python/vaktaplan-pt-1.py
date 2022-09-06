import camelot
import numpy as np
import pandas as pd
import json
from stuff import *
from stuff import output_directory, tablestocellinfo
import os

file = "../input/11okt10nov.pdf"
file ='/Users/odinndagur/Code/Github/vaktaplan/venv2/input/11okt10nov.pdf'

tables = camelot.read_pdf(file,pages='1-end')
cellinfo = tablestocellinfo(tables)

with open(os.path.join(output_directory,'celldata1.json'), 'w') as f:
    json.dump(cellinfo,f)

docs = []

# tables[0].col = tables[0].df.col + 1
# tables[0].row = tables[0].df.row + 2

# tables[1].col = tables[1].df.col + 1
# tables[1].row = tables[1].df.row + 1


total_tables = cleanuptables(tables)
