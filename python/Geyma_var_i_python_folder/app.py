from flask import Flask, render_template, request
import camelot
import numpy as np
import pandas as pd
import json
from stuff import *
import os
import requests
# from werkzeug import secure_filename
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './stuff'

@app.route('/')
def pt1():
    # file = "../input/11okt10nov.pdf"
    file ='/Users/odinndagur/Code/Github/vaktaplan/input/11okt10nov.pdf'
    cellinfo = []

    tables = camelot.read_pdf(file,pages='1-end')
    cellinfo = tablestocellinfo(tables)

    with open('celldata1.json', 'w') as f:
        json.dump(cellinfo,f)

    docs = []

    # tables[0].col = tables[0].df.col + 1
    # tables[0].row = tables[0].df.row + 2

    # tables[1].col = tables[1].df.col + 1
    # tables[1].row = tables[1].df.row + 1


    cleanuptables(tables,docs)
    return str(docs)



@app.route('/upload')
def upload_file():
   return render_template('/upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_filel():
   if request.method == 'POST':
        f = request.files['file']
        print(f)
        filename = f.filename
        # f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],'input.pdf'))
        file = os.path.join(app.config['UPLOAD_FOLDER'],'input.pdf')
        files = {'file':file}
        resp = requests.get('http://127.0.0.1:8001/uploader')
        return resp.content
        # cellinfo = []
        # tables = camelot.read_pdf(file,pages='1-end')
        # cellinfo = tablestocellinfo(tables)
        # with open('celldata1.json', 'w') as f:
        #     json.dump(cellinfo,f)
        # docs = []
        # cleanuptables(tables,docs)
        # return str(docs)
        # return r

# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_filel():
#    if request.method == 'POST':
#       f = request.files['file']
#       filename = secure_filename(f.filename)
#       f.save(f.filename)
#       return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)





