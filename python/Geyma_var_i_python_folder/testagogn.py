import json
import pandas
import math
from datetime import datetime

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
  'Undirbúningur': (1.0,1.0,1.0)
}

def getpersonfromcell(t,r):
  for p_id, p in staffindexes.items():
    #print(p)
    #print("\nPerson ID:", p_id)
    for key in list(p.keys()):
      if p[key]['table'] == t and p[key]['row'] == r: #and p[key]['col'] == c:
        return p_id

def getshifttype(co):
  r, g, b = co
  #print(r,g,b)
  c = (r,g,b)
  shift = ''
  for key in list(shiftcolors.keys()):
    if c == shiftcolors[key]:
      return key
  #return clr



df = pandas.read_csv('/Users/odinndagur/Code/Github/vaktaplan/output/ALLT.csv')
head = df.head()
#print(df.columns[2])
print("start")
#for col in head.columns:
  #print(col)
#print(df.iloc[6][7])



cells = []

with open('/Users/odinndagur/Code/Github/vaktaplan/venv2/python/celldatawcolors.json') as f:
    cells = [tuple(x) for x in json.load(f)]
colors = set()
for cell in cells:
  colors.add((cell[8], cell[9], cell[10], ''))
#print(colors)
staffnames = []
names = [
  "LRL",
  "orlof",
  "GH",
  "PHA",
  "simavakt",
  "",
  "BÓB",
  "GR",
  "NV",
  "JS",
  "",
  "undirb",
]
ss = []

namecolors = []
for col in colors:
  ss.append(col)

for i in range(len(names)):
  n = names[i]
  c = ss[i]
  namecolors.append((n,(c[0], c[1], c[2])))

#for i in range(len(namecolors)):
    #print(namecolors[i][0] + ' ')
    #print(str(namecolors[i][1]) + '\n')

#print(namecolors)

#def colortoname(col):
#  for name in namecolors:
#    if name[1] == col:
#      return name[0]

#for cell in cells:
  #if colortoname((cell[8], cell[9], cell[10])) == 'JS':
    #print(cell)

staffindexes = {}

ppl = set()
for cell in cells:
  text = cell[0]
  table = cell[5]
  col = cell[7]
  row = cell[6]
  clr = (cell[8],cell[9],cell[10])
  text = text.strip()
  if len(text) > 0:
    if not text[0].isdigit():
      #print(text,table,col,row,clr)
      if not "Starfsmaður" in text and not "Hæfniþáttur" in text and not "ORLOF" in text:
        ppl.add(text)
        if not text in staffindexes:
          staffindexes[text] = {}
        idx = str(table) + str(col) + str(row)
        staffindexes[text][idx] = {'table':table,'col':col,'row':row,'clr':clr}
      #if(len(text.strip()) == 0):
        #print(text, "text long blablaksdl")
for p in ppl:
  staffnames.append(p)
  #print(p)
staffnames.sort()
#print(len(staffnames))


#print(staffnames)
#print(len(staffnames))

shifts = {}

for s in staffnames:
  if s not in shifts:
    shifts[s] = {}
    
odinnvaktir = set()

for cell in cells:
  text = cell[0]
  table = cell[5]
  col = cell[7]
  row = cell[6]
  clr = (cell[8],cell[9],cell[10])
  text = text.strip()
  coloffset = math.floor(table/2)* 14
  #if not clr == (0.0,0.0,0.0):
  tp = 1#getshifttype(clr)
    #print(text,tp)
    #print(clr)
  #print(coloffset)
  if(len(text)>0):
    tp = 2#getshifttype(clr)
    if (text[0].isdigit() and ':' in text):
      tp = 3#getshifttype(clr)
      #print(tp)
      date = df.columns[col]
      date = date.strip()
      date = date.replace('\n', ' ')
      #print(scolor)
      #print(tp)
      person = getpersonfromcell(table,row)
      tp = clr#getshifttype(clr)
      #print(person, text, date, tp)
      if tp:
        shifts[person][tp] = {'date' : date, 'time' : text, 'shifttype' : tp}
      #print(text,tp)

  #if not len(text) == 0 and text[0].isdigit():
    #if text in shifts:

temp = odinnvaktir
odinnvaktir = []
      #shifts[text].append((text,table,col,row,clr))
#print(shifts)
#print(list(odinnvaktir))
for shift in temp:
  odinnvaktir.append(shift)
  #print(shift)
odinnvaktir.sort()
odinnvaktir.sort(key = lambda date: datetime.strptime(date[0:5], '%d.%m')) 
#print(odinnvaktir)
#print(staffindexes)

#for person in staffindexes:
 # for cell in person:
    #print(cell)
    #print(cell[table])

#for p_id, p_info in staffindexes.items():
    #print("\nPerson ID:", p_id)
    
    #for key in p_info:
        #print(key + ':', p_info[key])

for cell in cells:
  text = cell[0]
  table = cell[5]
  col = cell[7]
  row = cell[6]
  clr = (cell[8],cell[9],cell[10])
  #text = text.strip()
  #print(table)
  #if table == 1 and row == 29:
    #print(text)
  #1 1 1
 # 2 1 29
#  4 1 29
  
#print(getpersonfromcell(1, 4))
def printshifts():
  for person, shiftlist in shifts.items():
      print(person + ' vaktir:')
      
      for shift in shiftlist:
          print(shiftlist[shift])
printshifts()
#print(colors)
print("end")