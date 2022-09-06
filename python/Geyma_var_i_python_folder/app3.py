import camelot
import numpy as np
import pandas as pd
import json
import os
from flask import Flask, render_template, request
from stuff import shiftcolors, getShiftByColor
import requests
# from werkzeug import secure_filename
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'stuff'

@app.route('/')
def pt3():
    # file = "../input/11okt10nov.pdf"
    file ='/Users/odinndagur/Code/Github/vaktaplan/input/11okt10nov.pdf'
    global cellinfo

    tables = camelot.read_pdf(file,pages='1-end')
    # for i in range(tables.n):
    #     table = tables[i]
    #     for j in range(len(table.cells)):
    #         col = table.cells[j]
    #         for ii in range(len(col)):
    #             cell = col[ii]
    #             temp = (cell.text,cell.x1-1,cell.y1-1,cell.x2+1,cell.y2+1,i,j,ii,-1,-1,-1)
    #             cellinfo.append(temp)
    #             # print(temp)
    with open('celldatawcolors.json') as f:
        cellinfo = [dict(x) for x in json.load(f)]
    # print(cellinfo)
    # for table in tables:
    #     for col in table.cells:
    #         for cell in col:
    #             temp = (cell.text,cell.x1,cell.y1,cell.x2,cell.y2,i,j,ii)
    #             print(temp)

    docs = []
    # out = "../output/"

    # tables[0].col = tables[0].df.col + 1
    # tables[0].row = tables[0].df.row + 2

    # tables[1].col = tables[1].df.col + 1
    # tables[1].row = tables[1].df.row + 1



    # for i in range(0, tables.n, 2):
    #     df = tables[i].df #even
    #     df2 = tables[i+1].df #odd

    #     df2 = df2.iloc[:,1:]
    #     df2.iloc[0,0] = "Starfsmaður"
    #     headers = df2.iloc[0]
    #     # headers.to_csv(out + "headers" + str(i+1) + ".csv")

    #     df = df.iloc[2: , 1:]
    #     df2 = df2.iloc[1: , :]

    #     df.index = df.index - 1

    #     df.columns = headers
    #     df2.columns = headers



    for cell in cellinfo:
        print(cell['shifttype'])
        # tables[cell['table']].cells[cell['col']][cell['row']].text = cell['text'] + cell['shifttype']
        tables[cell['table']].df.iloc[cell['row']][cell['col']] = cell['text'] + cell['shifttype']
        # print(tables[cell['table']])
        # if cell['table'] == 0:
        #     text = cell['text']
        #     tablenumber = cell['table']
        #     colnumber = cell['col']
        #     rownumber = cell['row']
        #     if len(cell['shifttype']) > 1:
        #         print(tables[tablenumber].cells[colnumber][rownumber-1].text, "tables i")
        #         print(df.iloc[colnumber-2][rownumber-2], "df i")
        #         # df.iloc[colnumber-2][rownumber-1] += str(int(r*255)) + str(int(g*255)) + str(int(g*255))
        #         # print(tablenumber,colnumber,rownumber)
        #         # print(df.iloc[colnumber-2][rownumber-1])
        # if cell['table'] == 1:
        #     text = cell['text']
        #     tablenumber = cell['table']
        #     colnumber = cell['col']
        #     rownumber = cell['row']
            # if r > 0 or g > 0 or b > 0:
            #     print(tablenumber,colnumber,rownumber)
            #     print(tables[tablenumber].cells[colnumber-2][rownumber].text, "tables i+1")
            #     print(df.iloc[colnumber-2][rownumber], "df i+1")
                # df.iloc[colnumber-2][rownumber-1] += str(int(r*25e5)) + str(int(g*255)) + str(int(g*255))
                # print(tablenumber,colnumber,rownumber)
                # print(df.iloc[colnumber-2][rownumber-1])

    print(tables[0].df)
    out = '/Users/odinndagur/Code/Github/vaktaplan/output/'
    for i in range(tables.n):
        tables[i].df.to_csv(out + 'test' + str(i) + '.csv')


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

    out = '/Users/odinndagur/Code/Github/vaktaplan/output/'
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

    first.to_csv(out + "ALLT.csv")




@app.route('/upload')
def upload_file():
   return render_template('/upload3.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_filel():
    if request.method == 'GET':
        return str(open(os.path.join(app.config['UPLOAD_FOLDER'],'01 Embrace.wav'),'rb'))
    if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8001,debug=True)





