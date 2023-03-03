### historico de tablas ###

import pandas as pd
from datetime import date
### from datetime import datetime

	### data = [['Alex',10],['Bob',12],['Clarke',13]]
	### df1 = pd.DataFrame(data,columns=['Name','Age'],dtype=int)
df1=pd.read_excel(r"C:\Users\p.pinedo.lopez\Documents\historico.xlsx",sheet_name='historico')
## df1['fecha']=df1['fecha'].dt.strftime('%d/%m/%Y')
print (df1)

## now=datetime.now()	## fecha-hora
today=date.today()	## fecha
df2=pd.read_excel(r"C:\Users\p.pinedo.lopez\Documents\historico.xlsx",sheet_name=1) ## 2ª hoja es tabla a añadir
df2.insert(2,'fecha',today,True)	## añadimos columna fecha (dtypes=objec)
## df2['fecha']=df2['fecha'].dt.strftime('%d/%m/%Y') ## SI T1.dtypes = datetime64 > object
df2['fecha'] = pd.to_datetime(df2['fecha']).dt.strftime('%d/%m/%Y') ## SI T1.dtype=object > object
print (df2)


df3=pd.concat([df1,df2],ignore_index=True)
df3.to_excel(r"C:\Users\p.pinedo.lopez\Documents\historico.xlsx",sheet_name='historico',index=False)
print (df3)
