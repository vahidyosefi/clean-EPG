# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:05:08 2020

@author: mohseni
"""




#g = map(pd.read_excel, glob.glob(r"C:\Users\PC\Desktop\new power bi\append\input tir\progrss\tir_progress\sarasari\out\*.xlsx"))
def func_merge(vorodi,khoji):
    
    import pandas as pd
#    import os
    import glob
    g = map(pd.read_excel, glob.glob(vorodi))

    print('input seccess')

    dfnn = pd.concat(list(g), ignore_index=True) 
    print(pd)


#del dfnn['Unnamed: 0']

    print('del')

    dfnn=dfnn.sort_values(['ردیف'])

    l = len(dfnn)
    print('lenth(dfnn)='+str(l))



    dfnn = dfnn[['نام شبکه','نام برنامه اولیه','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','اپراتور','ساعت','تاریخ','ردیف','جنس','نببت','tag']]
     
    dfnn.to_excel(khoji,index=False)

#
