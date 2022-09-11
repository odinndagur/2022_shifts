# Import pandas library
import pandas as pd
  
# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
data2 = [['ada', 12], ['cac', 40], ['splo', 59]]

  
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])
df2 = pd.DataFrame(data2, columns=['Name', 'Age'])