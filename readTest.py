import xlrd
from time import time

t1=time()
path=''
wb=xlrd.open_workbook(path)
tab=wb.sheet_by_index(0)
nrows=tab.nrows
ncols=tab.ncols
data=[]
for i in range(1,ncols):
	data.append(tab.col_values(i,1,nrows))
print(data)
t2=time()

print('\nTime: '+str(t2-t1))