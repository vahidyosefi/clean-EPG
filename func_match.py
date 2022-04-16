# -*- coding: utf-8 -*-
"""
Created on Sun May 30 16:50:38 2021

@author: vahid 
    
 program :function match with total 

"""



def func_match(o_sarasari):
    
    import pandas as pd
    
    
    
    #append
    
    # translate number to persion
    
    df0 = o_sarasari
    
    
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('0', '۰')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('1', '۱')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('2', '۲')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('3', '۳')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('4', '۴')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('5', '۵')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('6', '۶')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('7', '۷')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('8', '۸')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('9', '۹')

    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('٠', '۰')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('١', '۱')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('٢', '۲')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('٣', '۳')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('٤', '۴')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('٥', '۵')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('٦', '۶')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('٧', '۷')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('٨', '۸')
    df0['نام تغییر یافته'] = df0['نام برنامه اولیه'].str.replace('٩', '۹')
    
    
    result = df0
    
    result = result.rename(columns={'tag':'ثبت تغییرات'})
    
    result = result[['نام شبکه','نام برنامه اولیه','نام تغییر یافته','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','اپراتور','ساعت','تاریخ','ردیف','جنس','ثبت تغییرات','نوع']]

    
    
    result = result.rename(columns = {"نوع":"type"})
    result = result.drop([], axis=1)
    result.reset_index()
    
    
    result['type'] = result['type'].str.strip()
    
    
    df_sarasari =result.query("type == 'سراسری'")
    df_ostani =result.query("type == 'استانی'")
    df_radio =result.query("type == 'رادیویی'")
    df_ekhtesasi =result.query("type == 'اختصاصی'")
    df_bronmarzi =result.query("type == 'برون مرزی'")
    
    
    #    dfek0_source =df0
    
    df_sarasari = df_sarasari.rename(columns = {"type":"نوع"})
    df_ostani = df_ostani.rename(columns = {"type":"نوع"})
    df_radio = df_radio.rename(columns = {"type":"نوع"})
    df_ekhtesasi = df_ekhtesasi.rename(columns = {"type":"نوع"})
    df_bronmarzi = df_bronmarzi.rename(columns = {"type":"نوع"})
    
    
    
    
    
    
    
    
   # radio
    
    df_radio.to_excel(r'D:\python\EPG_vahid\progress\merge\match merge\radio.xlsx', index=False)


    # ostani
    df_ostani.to_excel(r'D:\python\EPG_vahid\progress\merge\match merge\ostani.xlsx', index=False)


    #ekhtesasi
    df_ekhtesasi.to_excel(r'D:\python\EPG_vahid\progress\merge\match merge\ekhtesasi.xlsx', index=False)


    #sarsari

    df_sarasari.to_excel(r'D:\python\EPG_vahid\progress\merge\match merge\sarasari.xlsx', index=False)

    df_bronmarzi.to_excel(r'D:\python\EPG_vahid\progress\merge\match merge\bronmarzi.xlsx', index=False)


    
    df_ostani = df_ostani.append(df_radio)
    df_ekhtesasi = df_ekhtesasi.append(df_ostani)
    df_sarasari = df_sarasari.append(df_ekhtesasi)
    df_bronmarzi = df_bronmarzi.append(df_sarasari)



    df_bronmarzi.to_excel(r'D:\python\EPG_vahid\progress\merge\match merge\total_EPG_match.xlsx', index=False)
