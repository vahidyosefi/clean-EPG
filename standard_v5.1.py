
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 15:09:46 2021

@author: vahid
"""

import pandas as pd
import numpy as np
import datetime
import os
import time
import datetime as dt
start = time.time() 



df0 = pd.DataFrame()
total = pd.DataFrame()

##### input data

df1_1 = pd.read_excel(r'D:\python\EPG_vahid\input\source\sample\sepeher_1400_12.xlsx')
df1 = pd.read_excel(r'D:\python\EPG_vahid\input\source\sample\Aio-1400_12.xlsx')
df2 = pd.read_excel(r'D:\python\EPG_vahid\input\source\sample\telewebion_1400_12.xlsx')

df3 = pd.read_excel(r'D:\python\EPG_vahid\input\source\sample\lenz_1400_12.1.xlsx')
#df3 = pd.read_csv(r'D:\python\EPG_vahid\input\source\sample\lenz_99_11.csv', header=None)
df4 = pd.read_excel(r'D:\python\EPG_vahid\input\source\sample\tva_1400_12.xlsx')

df5 = pd.read_excel(r'D:\python\EPG_vahid\input\source\sample\iranseda_1400_12.xlsx')


df2.dtypes

# try:
#     # df2['tt']=df2['تاریخ تولید برنامه'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%fZ'))
#     # df2['tt']=df2['تاریخ تولید برنامه'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ'))
    
# except:
#     pass    

df2['تاریخ تولید برنامه'] = df2['تاریخ تولید برنامه'].str[:19]   
df2['tt']=df2['تاریخ تولید برنامه'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')) 

# df2.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\test\telewbion_out1.xlsx', index=False)


df2['ttt']=df2['tt'].astype(str)
df2['t1'] = df2['ttt'].str.replace('-','/')
df2['t2'] = df2['t1'].str[:16]
del df2['tt']
del df2['ttt']
del df2['t1']
df2['تاریخ تولید برنامه'] = df2['t2']

del df2['t2']


# df2['tttt']=df2['ttt'].apply(lambda x: dt.datetime.strptime( x, '%d/%m/%Y')).date()


df3.dtypes

df3['Begin Time']=df3['Begin Time'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

df3['ttt']= df3['Begin Time'].astype(str)
df3['t1'] = df3['ttt'].str.replace('-','/')
df3['Begin Time'] = df3['t1'].str[:16]

del df3['ttt']
del df3['t1']

# df3['Begin Time']=df3['Begin Time'].apply(lambda x: dt.datetime.strptime(x, '%d/%m/%Y %H:%M'))

# dfsp1 = 
#python -W ignore your_script_name.py
# dfsp1 = df1_1
# df22 = pd.read_excel(r'D:\python\EPG_vahid\input\source\sample\telewebion_1400_11_v1.xlsx')

from func_get_and_transfer_v3 import *


d= func_get_and_transfer_v3(df1_1,df1,df2,df3,df4,df5)



path_month= r'D:\python\EPG_vahid\input\source\Estandard\astandard_out.xlsx'


### input date

"""
# for Azar:
start_date = '11-20-2020-23:59:59'
end_date = '12-20-2020-23:59'
bb = 37

for dey: 
start_date = '12-20-2020-23:59:59'
end_date = '01-19-2021-23:59'
bb = 38

###for bahman: 
start_date = '01-19-2021-23:59:59'
end_date = '02-18-2021-23:59'
bb = 39  

##for esfand
start_date = '02-18-2021-23:59:59'
end_date = '03-20-2021-23:59'
bb = 40


# for farvardin_1400: 
start_date = '03-20-2021-23:59:59'
end_date = '04-20-2021-23:59'
bb = 41
 
# ordibehest_1400

start_date = '04-20-2021-23:59:59'
end_date = '05-21-2021-23:59'
bb = 42

#khordad_1400

start_date = '05-21-2021-23:59:59'
end_date = '06-21-2021-23:59'
bb = 43
#tir_1400
start_date = '06-21-2021-23:59:59'
end_date = '07-22-2021-23:59'
bb = 44

# mordad_1400
start_date = '07-22-2021-23:59:59'
end_date = '08-22-2021-23:59'
bb = 45

# shahrivar_1400

start_date = '08-22-2021-23:59:59'
end_date = '09-22-2021-23:59'
bb = 46

# meher_1400

start_date = '09-22-2021-23:59:59'
end_date = '10-22-2021-23:59'
bb = 47

# Aban_1400
start_date = '10-22-2021-23:59:59'
end_date = '11-21-2021-23:59'
bb = 48

# Azar_1400

start_date = '11-22-2021-23:59:59'
end_date = '12-21-2021-23:59'
bb = 49

# dey_1400

start_date = '12-21-2021-23:59:59'
end_date = '01-20-2022-23:59'
bb = 50

start_date = '01-20-2021-23:59:59'
end_date = '02-19-2022-23:59'
bb = 51

"""

# esfand_1400

start_date = '02-19-2021-23:59:59'
end_date = '03-20-2022-23:59'
bb = 52

print('Get Date and Radif')

## input  ردیف 

""" for divide file , sarsari , ostani , radio , ekhtesasi """
from func_sarsari_v2 import *

[ostani , radio,bronmarzi ,ekhtesasi]= func_sarsari_v2(path_month,start_date,end_date,bb)

#ostani.to_excel( 'test.xlsx', index=False)

from Func_Mekanizeh_ostani import *
#Func_Mekanizeh_ostani (df50)
number =Func_Mekanizeh_ostani (ostani)
print('چاپ شبکه استانی به تفکیک انجام گرفته است',number)


print ('فراخوانی تابع رادیویی جهت تفکیک شبکه های رادیویی')
from Func_Mekanizeh_radio_v2 import *
number =Func_Mekanizeh_radio_v2 (radio)
print('چاپ شبکه رادیویی به تفکیک انجام گرفته است',number)

print ('فراخوانی تابع رادیویی جهت تفکیک شبکه های برون مرزی')
from Func_Mekanizeh_bronmarzi import *
number =Func_Mekanizeh_bronmarzi (bronmarzi)
print('چاپ شبکه برون مرزی به تفکیک انجام گرفته است',number)

print ('فراخوانی تابع اختصاصی جهت تفکیک شبکه های اختصاصی')
from Func_Mekanizeh_ekhtesasi import *
number =Func_Mekanizeh_ekhtesasi (ekhtesasi)
print('چاپ شبکه اختصاصی به تفکیک انجام گرفته است',number)


# ostani.tfunctoolsexcel
# excel(r'D:\python\EPG_vahid\input\source\sample\tva_1400_08.xlsx')


""" for delete files in outin the folder """

vahid = 1    
for vahid in range(50):
#     vahid = 13
    print("number of chanel sarasari", vahid)
    
    ch= vahid+1
    
    clean1 = r'D:\python\EPG_vahid\progress\sarasari\out\{}.xlsx'.format(ch)
    try:
        os.remove(clean1)
    except:
        pass
    clean2 = r'D:\python\EPG_vahid\progress\\radio\out\{}.xlsx'.format(ch)
    try:
        os.remove(clean2)
    except:
        pass
    clean3 = r'D:\python\EPG_vahid\progress\ostani\out\{}.xlsx'.format(ch)
    try:
        os.remove(clean3)
    except:
        pass
    clean4 = r'D:\python\EPG_vahid\progress\ekhtesasi\out\{}.xlsx'.format(ch)
    try:
        os.remove(clean4)
    except:
        pass
    
    clean5 = r'D:\python\EPG_vahid\progress\bronmarzi\out\{}.xlsx'.format(ch)
        
                   
    try:
        os.remove(clean5)
    except:
        pass

print('فولدرها پاک شده ')

""" clean system """



from func_epg_clean_v20 import *

vahid = 1    
for vahid in range(25):
#     vahid = 13
    print("number of chanel sarasari", vahid)
    
    ch= vahid+1
    
    vorodi  = r'D:\python\EPG_vahid\progress\sarasari\in\{}.xlsx'.format(ch)
    khoroji = r'D:\python\EPG_vahid\progress\sarasari\out\{}.xlsx'.format(ch)
    try:
        d= func_epg_clean_v20(vorodi,khoroji,ch)
    except:
        pass
print('out tabehe',d)


vahid = 1    
for vahid in range(20):
#     vahid = 13
    print("number of chanel radio", vahid)
    
    ch= vahid+1
    
    vorodi  = r'D:\python\EPG_vahid\progress\radio\in\{}.xlsx'.format(ch)
    khoroji = r'D:\python\EPG_vahid\progress\radio\out\{}.xlsx'.format(ch)
    try:
        d= func_epg_clean_v20(vorodi,khoroji,ch)
    except:
        pass
print('out tabehe',d)

vahid = 1    
for vahid in range(50):
#     vahid = 13
    print("number of chanel ostani", vahid)
    
    ch= vahid+1
    
    vorodi  = r'D:\python\EPG_vahid\progress\ostani\in\{}.xlsx'.format(ch)
    khoroji = r'D:\python\EPG_vahid\progress\ostani\out\{}.xlsx'.format(ch)
    try:
        d= func_epg_clean_v20(vorodi,khoroji,ch)
    except:
        pass
print('out tabehe',d)


vahid = 1    
for vahid in range(50):
#     vahid = 13
    print("number of chanel bronmarzi", vahid)
    
    ch= vahid+1
    
    vorodi  = r'D:\python\EPG_vahid\progress\bronmarzi\in\{}.xlsx'.format(ch)
    khoroji = r'D:\python\EPG_vahid\progress\bronmarzi\out\{}.xlsx'.format(ch)
    try:
        d= func_epg_clean_v20(vorodi,khoroji,ch)
    except:
        pass
print('out tabehe',d)

vahid = 1    
for vahid in range(50):
#     vahid = 13
    print("number of chanel ekhtesasi", vahid)
    
    ch= vahid+1
    ch= 43
    
    vorodi  = r'D:\python\EPG_vahid\progress\ekhtesasi\in\{}.xlsx'.format(ch)
    khoroji = r'D:\python\EPG_vahid\progress\ekhtesasi\out\{}.xlsx'.format(ch)
    try:
        d= func_epg_clean_v20(vorodi,khoroji,ch)
    except:
        pass
print('out tabehe',d)





""" merge , sarsari , ostani , radio , ekhtesasi """ 



from func_merge  import *

vorodi =r'D:\python\EPG_vahid\progress\sarasari\out\*.xlsx'
khoji   = r'D:\python\EPG_vahid\progress\merge\marge\sarasari.xlsx'


func_merge(vorodi,khoji)

print('سراسری')

vorodi =r'D:\python\EPG_vahid\progress\radio\out\*.xlsx'
khoji   = r'D:\python\EPG_vahid\progress\merge\marge\radio.xlsx'

func_merge(vorodi,khoji)
print('رادیویی')

vorodi =r'D:\python\EPG_vahid\progress\ostani\out\*.xlsx'
khoji   = r'D:\python\EPG_vahid\progress\merge\marge\ostani.xlsx'


func_merge(vorodi,khoji)
print('استانی')

vorodi =r'D:\python\EPG_vahid\progress\bronmarzi\out\*.xlsx'
khoji   = r'D:\python\EPG_vahid\progress\merge\marge\bronmarzi.xlsx'


func_merge(vorodi,khoji)
print('استانی')

""" delete file mabaghi ekhtesasti """

os.remove(r'D:\python\EPG_vahid\progress\ekhtesasi\out\43.xlsx')


vorodi =r'D:\python\EPG_vahid\progress\ekhtesasi\out\*.xlsx'
khoji   = r'D:\python\EPG_vahid\progress\merge\marge\ekhtesasi.xlsx'

func_merge(vorodi,khoji)

print('اختصاصی')


#vorodi =r'D:\python\EPG_vahid\progress\merge\marge\*.xlsx'
#khoji   = r'D:\python\EPG_vahid\progress\merge\total.xlsx'

#func_merage(vorodi,khoji)

#print('ادغام کل')

##  for moien

i_radio= pd.read_excel (r'D:\python\EPG_vahid\progress\merge\marge\radio.xlsx')
i_radio['نوع'] = 'رادیویی'
i_bronmarzi= pd.read_excel (r'D:\python\EPG_vahid\progress\merge\marge\bronmarzi.xlsx')
i_bronmarzi['نوع'] = 'برون مرزی'
i_ostani= pd.read_excel (r'D:\python\EPG_vahid\progress\merge\marge\ostani.xlsx')
i_ostani['نوع'] = 'استانی'
i_ekhtesasi= pd.read_excel (r'D:\python\EPG_vahid\progress\merge\marge\ekhtesasi.xlsx')
i_ekhtesasi['نوع'] = 'اختصاصی'
i_sarasari= pd.read_excel (r'D:\python\EPG_vahid\progress\merge\marge\sarasari.xlsx')
i_sarasari['نوع'] = 'سراسری'

total=total.append(i_radio)
total=total.append(i_bronmarzi)
total=total.append(i_ostani)
total=total.append(i_ekhtesasi)
total=total.append(i_sarasari)


total.to_excel(r'D:\python\EPG_vahid\progress\merge\total__.xlsx', index=False)


from func_change_v2  import *

[o_radio,o_bronmarzi,o_ostani,o_ekhtesasi,o_sarasari]=func_change_v2(i_radio,i_bronmarzi,i_ostani,i_ekhtesasi,i_sarasari)



#input_sarasari.to_excel(r'D:\python\EPG_vahid\progress\merage\total_moien_1.xlsx', index=False)

o_radio = o_radio.append(o_bronmarzi)
o_ostani = o_ostani.append(o_radio)
o_ekhtesasi = o_ekhtesasi.append(o_ostani)
o_sarasari = o_sarasari.append(o_ekhtesasi)



o_sarasari.to_excel(r'D:\python\EPG_vahid\progress\merge\total_EPG.xlsx', index=False)

print('ادغام کل با ذکر حوزه')

from func_match  import *

func_match(o_sarasari)

print('match item with total data')

end = time.time()
# total time taken
mo = (end - start)/60
print ('مدت زمان اجرا برنامه به دقیقه',mo)
print(f"Runtime of the program is {end - start}")

