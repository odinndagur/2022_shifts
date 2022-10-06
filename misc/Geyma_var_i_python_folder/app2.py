from flask import Flask, render_template, request
import minecart
import json
from stuff import *
import os
# from werkzeug import secure_filename
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'stuff'

@app.route('/')
def pt2():
    file ='/Users/odinndagur/Code/Github/vaktaplan/input/11okt10nov.pdf'
    file = os.path.join(app.config['UPLOAD_FOLDER'],'input.pdf')
    colors = set()
    # temp = (cell.text,cell.x1,cell.y1,cell.x2,cell.y2,i,j,ii,r,g,b)
    global cellinfo
    with open('celldata1.json') as f:
        cellinfo = [dict(x) for x in json.load(f)]
    # print(cellinfo)
    print(len(cellinfo))

    cellcolors = []

    x1=186
    y1=419
    x2=233
    y2=436

    BOX = (x1,y1,x2,y2)
    global s

    pagenumber = 0

    buffer = 1

    with open(file,"rb") as doc:
        document = minecart.Document(doc)
        # print(document)
        for page in document.iter_pages():
            print("pagenumber: " + str(pagenumber))
            for shape in page.shapes:
                for cell in cellinfo:
                    left = cell['x1'] - buffer
                    bottom = cell['y1'] - buffer
                    right = cell['x2'] + buffer
                    top = cell['y2'] + buffer
                    box = (left,bottom,right,top)
                    # box = (0,0,600,600)
                    # box = (696.9200331584948, 486.8216768762596, 745.4800353705815, 506.09819469971785)
                    if shape.check_inside_bbox(box):
                        # print("check")
                        r, g, b = shape.fill.color.as_rgb()
                        shift = getShiftByColor((r,g,b))
                        if(len(shift) > 1):
                            # print(cell['shifttype'] + 'pre')
                            if(cell['table'] == pagenumber):
                                cell['shifttype'] = shift
                                # if pagenumber == 0: print(cell['text'],shift,cell['table'],cell['row'],cell['col'])
                            # print(cell['shifttype'] + 'post')
                        # ls[8] = r
                        # ls[9] = g
                        # ls[10] = b
                        # cell[8] = r
                        # cell[9] = g
                        # cell[10] = b
                        # cell = tuple(ls)
                        # print(cell)
                        cellcolors.append(cell)
                        # i5 j6 ii7 r8 g9 b10
                    # if shape.fill:
                    #     color = shape.fill.color.as_rgb()
                    #     colors.add(color)
                    #     def allZero(c):
                    #         if c[0] == 0:
                    #             if c[1] == 0:
                    #                 if c[2] == 0:
                    #                     return True
                    #         else:
                    #             return False
                    #     if not allZero(color):
                    #         print(color)
                    #         print(shape.get_bbox())
                            # s = shape
                        # print(shape.fill.color.as_rgb())
                        # print(shape.get_bbox())
            pagenumber +=1
        # page = document.get_page(0)
        # for shape in page.shapes:
        #     if shape.fill:
        #         colors.add(shape.fill.color.as_rgb())
    # for cell in cellcolors:
    #     print(cell['shifttype'])
    with open('celldatawcolors.json', 'w') as f:
            json.dump(cellcolors,f)
    # output = '['
    # for color in colors: 
    #     # print(color)
    #     output +=('color' + '(' + str(color[0]) + ',' + str(color[1]) + ',' + str(color[2]) + '),')
    # output = output[:-1]
    # output += '];'
    # box=(233,108,279,126)
    # box = list(box)
    # box[0] -=1
    # box[1] -=1
    # box[2] +=1
    # box[3] +=1
    # box = tuple(box)
    # sb = s.check_inside_bbox(box)
    # print(sb)
    # print(output)
    return str(cellcolors)


@app.route('/upload')
def upload_file():
   return render_template('/upload2.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_filel():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)





