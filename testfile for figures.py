import matplotlib as mp

#%matplotlib inline

#figure()
#plot(x, y, 'r')
#xlabel('x')
#ylabel('y')
#title('title')
#show()

_author_ = 'wombat'

hello = 'Hello'
world = 'World'

print(_author_ + ': ' + hello + ' ' + world)


import pandas as pd

excel_datafile_MP2 = "/Users/antoinedeschipper/desktop/paneltest4.xlsx"
dfMP2 = pd.read_excel(excel_datafile_MP2)

print(dfMP2.head())