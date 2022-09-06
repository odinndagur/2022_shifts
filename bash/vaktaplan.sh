#!/usr/local/bin/bash

cd /Users/odinndagur/Code/Github/2022_shifts/python
source /Users/odinndagur/Code/Github/2022_shifts/python/camelot-env/bin/activate
echo pt1
python3 /Users/odinndagur/Code/Github/2022_shifts/python/vaktaplan-pt-1.py
deactivate

source /Users/odinndagur/Code/Github/2022_shifts/python/minecart-env/bin/activate
echo pt2
python3 /Users/odinndagur/Code/Github/2022_shifts/python/vaktaplan-pt-2.py
deactivate

source /Users/odinndagur/Code/Github/2022_shifts/python/camelot-env/bin/activate
echo pt3
python3 /Users/odinndagur/Code/Github/2022_shifts/python/vaktaplan-pt-3.py
deactivate

echo 'all done'