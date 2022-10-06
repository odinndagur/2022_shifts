import subprocess
import sys

camelot_env = 'camelot-env/bin/python'
minecart_env = 'minecart-env/bin/python'

file ='/Users/odinndagur/Code/Github/vaktaplan/venv2/input/11okt10nov.pdf'

for arg in sys.argv:
    if arg.endswith('.pdf'):
        file = arg


subprocess.call([camelot_env,'vaktaplan-pt-1.py', file])
subprocess.call([minecart_env,'vaktaplan-pt-2.py', file])
subprocess.call([camelot_env,'vaktaplan-pt-3.py',file])