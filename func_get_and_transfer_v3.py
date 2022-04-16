#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 03:22:35 2019

@author: vahid
"""

#from IPython import get_ipython
#get_ipython().magic('reset -sf')


def func_get_and_transfer_v3 (dfsp1,df1,df2,df3,df4,df5):
    
    
    import pandas as pd
    import numpy as np
    import datetime

    df0=pd.DataFrame()
    df222 =pd.DataFrame()

# df3 = pd.read_excel(r'D:\python\EPG_vahid\input\source\sample\lenz_1400_11.xlsx')
##### input data
#df2 = pd.read_excel('telewebion_99_09.xlsx')
#df3 = pd.read_excel('lenz-99-09.xlsx')
#df4 = pd.read_excel('tva_99_09.xlsx')

######## sepeher **************

    dfsp1['dur'] = dfsp1['dur']/60

    dfsp1 = dfsp1.rename(columns={'channel': 'ch', 'Name_Item': 'نام برنامه', 'Time_Play': 'TIME','EP':'تاریخ پایان','visit': 'تعداد بازدید','dur':'مدت بازدید'})
#        df1["تاریخ پایان"] = ""
    # dfsp1["مدت بازدید"] = ""
    dfsp1["اپراتور"] = "سپهر" 
    
    # del dfsp1['@timestamp']
    
    del dfsp1['u_visit']
    del dfsp1['Time_Play_x']
    del dfsp1['ID_Day_Item']
    del dfsp1['Dec_Summary']
    del dfsp1['DTDay']
    del dfsp1['Length']

    dfsp1 = dfsp1[['ch', 'نام برنامه','TIME','تاریخ پایان','مدت بازدید','تعداد بازدید','اپراتور']]
    dfsp1.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\sepeher_Sv1.xlsx',index=False)
    print('سپهر')




######aio*************
#    df1 = pd.read_excel(r'D:\python\EPG_vahid\input\source\sample\Aio-99_10.xlsx')
    # try:
#        df1 = pd.read_excel('aio02.xlsx')
# df1_1 = df1_1.rename
# 
    df1 = df1.rename(columns={'name': 'ch', 'title': 'نام برنامه', 'start_timestamp': 'TIME','end_timestamp':'تاریخ پایان','viewer': 'تعداد بازدید'})
#        df1["تاریخ پایان"] = ""
    df1["مدت بازدید"] = ""
    df1["اپراتور"] = "آیو" 
    del df1['show_id']
    del df1['epg_id']
    
    df1 = df1[['ch', 'نام برنامه','TIME','تاریخ پایان','مدت بازدید','تعداد بازدید','اپراتور']]
    df1.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\aio_Sv1.xlsx',index=False)
    print('آیو')
    # except:
    #         pass    

#*********************

#anten*******************
#df1 = pd.read_excel('anten02.xlsx')
#df1 = df1.rename(columns={'نام کانال': 'ch', 'زمان پایان': 'تاریخ پایان',' تعدا بازدید یر حسب ساعت ': 'مدت بازدید','بازدید': 'تعداد بازدید', 'نام برنامه ': 'نام برنامه', 'زمان شروع': 'TIME'})
#df1["اپراتور"] = "آنتن" 
##df1.to_excel('anten03_0.xlsx')
##

#df1 = df1[['ch', 'نام برنامه','TIME','تاریخ پایان','مدت بازدید','تعداد بازدید','اپراتور']]
#df1.to_excel('anten03.xlsx')
#print('آنتن')
#*************************

#fam***************

    df2["مدت بازدید"] = ""
    df2["تاریخ پایان"] = ""
    df2["مدت بازدید"] = ""
    df2 = df2.rename(columns={'نام شبکه': 'ch', 'زمان پایان': 'تاریخ پایان',' تعدا بازدید یر حسب ساعت ': 'مدت بازدید','تعداد بازدید': 'تعداد بازدید', 'نام برنامه': 'نام برنامه', 'تاریخ تولید برنامه': 'TIME'})
    df2["اپراتور"] = "تلوبیون" 
    df2 = df2[['ch', 'نام برنامه','TIME','تاریخ پایان','مدت بازدید','تعداد بازدید','اپراتور']]
    
    
    df2.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\telewbion_Sv1.xlsx', index=False)
    print('تلوبیون')
    df222 = df2.copy()
    df222_1 = df2.copy()
#***********************

#lenz***************

#    f_input1=len(df3.index)
#
#    print ('تعداد کل سطرهای ورودی لنز',f_input1)
#
#    try:
#        df3 = df3.drop(columns=8)
#    except:
#        pass   
##bb = aa.drop(columns='Unnamed: 8')
#	
#			
#    df3.columns =['Channel ID','Channel Name','Program Name','Begin Time','End Time','Total duration(Hour)','Total Access times','Recorded times']
#
#    df3['Channel ID'] = df3['Channel ID'].astype(str)
#    df3 = df3[~df3['Channel ID'].str.contains('Avg')]
    
#    del remove blank in Channel ID

    df3["اپراتور"] = "لنز" 
    df3.columns=['nm','ch', 'نام برنامه','TIME','تاریخ پایان','مدت بازدید','تعداد بازدید','نامشخص','اپراتور']
    del df3['nm']
    del df3['نامشخص']
    # df3['مدت بازدید'] = df3['مدت بازدید'] *60
    df3.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\lenz_Sv1.xlsx', index=False)
    print('لنز')
#***********************
#tva***************


    df4["اپراتور"] = "تیوا" 
    del df4['Subtitle']
    del df4['Users']
    # df4["مدت بازدید"] = ""
    # df4.loc[(df4['Avg. Duration (sec)'].isnull()),'Avg. Duration (sec)'] = "0"
    df4['Avg. Duration (sec)'] = df4['Avg. Duration (sec)']/3600
    df4 = df4.rename(columns={'Channel': 'ch','Avg. Duration (sec)':'مدت بازدید', 'Name': 'نام برنامه', 'Start At': 'TIME', 'Sessions': 'تعداد بازدید'})
    df4 = df4.rename(columns={'End At': 'تاریخ پایان'})
    df4 = df4[['ch', 'نام برنامه','TIME','تاریخ پایان','مدت بازدید','تعداد بازدید','اپراتور']]
    # df4.loc[(df4['مدت بازدید'].isnull()),'مدت بازدید'] = "0"
    df4.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\tva_Sv1.xlsx', index=False)
    print('تیوا')
    
####******************************
#iranseda**************************
    
    df5["اپراتور"] = "ایران صدا" 
    # del df4['Subtitle']
    # del df4['Users']
    df5["مدت بازدید"] = ""
    # df4.loc[(df4['Avg. Duration (sec)'].isnull()),'Avg. Duration (sec)'] = "0"
    # df4['Avg. Duration (sec)'] = df4['Avg. Duration (sec)']/3600
    df5 = df5.rename(columns={'t_name': 'ch','c_name': 'نام برنامه', 'year_': 'TIME', 'visit': 'تعداد بازدید'})
    df5 = df5.rename(columns={'h_time': 'ساعت'})
    df5 = df5[['ch', 'نام برنامه','TIME','ساعت','مدت بازدید','تعداد بازدید','اپراتور']]
    # df4.loc[(df4['مدت بازدید'].isnull()),'مدت بازدید'] = "0"
    df5.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\iranseda_Sv1.xlsx', index=False)
    print('ایران صدا')
    
    
    
    
    
    
    
#*********************** extract date



  
    dfsp1 ['TIME'] = pd.to_datetime(dfsp1.TIME)
    dfsp1['سال'] = dfsp1['TIME'].dt.year
    dfsp1['ماه'] = dfsp1['TIME'].dt.month
    dfsp1['ماه'] = dfsp1['ماه'].apply(lambda x: '{0:0>2}'.format(x))
    dfsp1['روز'] = dfsp1['TIME'].dt.day
    dfsp1['روز'] = dfsp1['روز'].apply(lambda x: '{0:0>2}'.format(x))
    dfsp1['ساعت'] = dfsp1['TIME'].dt.hour
    dfsp1['ساعت'] = dfsp1['ساعت'].apply(lambda x: '{0:0>2}'.format(x))
    dfsp1['تاریخ'] = dfsp1[dfsp1.columns[7:]].apply(
        lambda x: ''.join(x.dropna().astype(str).astype(str)),
        axis=1)
    # df1.to_excel('aio_date.xlsx')
  


    # try:
    #     dfsp1 ['TIME'] = pd.to_datetime(dfsp1.TIME)
    #     dfsp1['سال'] = dfsp1['TIME'].dt.year
    #     dfsp1['ماه'] = dfsp1['TIME'].dt.month
    #     dfsp1['ماه'] = dfsp1['ماه'].apply(lambda x: '{0:0>2}'.format(x))
    #     dfsp1['روز'] = dfsp1['TIME'].dt.day
    #     dfsp1['روز'] = dfsp1['روز'].apply(lambda x: '{0:0>2}'.format(x))
    #     dfsp1['ساعت'] = dfsp1['TIME'].dt.hour
    #     dfsp1['ساعت'] = dfsp1['ساعت'].apply(lambda x: '{0:0>2}'.format(x))
    #     dfsp1['تاریخ'] = dfsp1[dfsp1.columns[7:]].apply(
    #         lambda x: ''.join(x.dropna().astype(str).astype(str)),
    #         axis=1)
    #     # df1.to_excel('aio_date.xlsx')
    # except:
    #     pass




    try:
        df1['TIME'] = pd.to_datetime(df1.TIME)
        df1['سال'] = df1['TIME'].dt.year
        df1['ماه'] = df1['TIME'].dt.month
        df1['ماه'] = df1['ماه'].apply(lambda x: '{0:0>2}'.format(x))
        df1['روز'] = df1['TIME'].dt.day
        df1['روز'] = df1['روز'].apply(lambda x: '{0:0>2}'.format(x))
        df1['ساعت'] = df1['TIME'].dt.hour
        df1['ساعت'] = df1['ساعت'].apply(lambda x: '{0:0>2}'.format(x))
        df1['تاریخ'] = df1[df1.columns[7:]].apply(
            lambda x: ''.join(x.dropna().astype(str).astype(str)),
            axis=1)
        # df1.to_excel('aio_date.xlsx')
    except:
        pass


    df2['TIME'] = pd.to_datetime(df2.TIME)
    df2['سال'] = df2['TIME'].dt.year
    # df2['سال'] =  df2['سال'].str()
    # df2.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\test\year.xlsx', index=False)
    
    df2['ماه'] = df2['TIME'].dt.month
    df2['ماه'] = df2['ماه'].apply(lambda x: '{0:0>2}'.format(x))
    # df2.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\test\month.xlsx', index=False)
    
    df2['روز'] = df2['TIME'].dt.day
    df2['روز'] = df2['روز'].apply(lambda x: '{0:0>2}'.format(x))
    # df2.to_csv(r'D:\python\EPG_vahid\input\source\Estandard\test\dey.csv', index=False)
    
    df2['ساعت'] = df2['TIME'].dt.hour
    df2['ساعت'] = df2['ساعت'].apply(lambda x: '{0:0>2}'.format(x))
    
    df2['تاریخ'] = df2[df2.columns[7:]].apply(
        lambda x: ''.join(x.dropna().astype(str).astype(str)),
        axis=1)
    # df2.to_excel('telewbion_date.xlsx')
    
    df2.dtypes
    df2['TIME'] = df222['TIME']
    df2.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\test\telewbion_sv1.xlsx', index=False)
    # del df2['TIME']

    df3['TIME'] = pd.to_datetime(df3.TIME)
    df3['سال'] = df3['TIME'].dt.year
    df3['ماه'] = df3['TIME'].dt.month
    df3['ماه'] = df3['ماه'].apply(lambda x: '{0:0>2}'.format(x))
    df3['روز'] = df3['TIME'].dt.day
    df3['روز'] = df3['روز'].apply(lambda x: '{0:0>2}'.format(x))
    df3['ساعت'] = df3['TIME'].dt.hour
    df3['ساعت'] = df3['ساعت'].apply(lambda x: '{0:0>2}'.format(x))
    df3['تاریخ'] = df3[df3.columns[7:]].apply(
        lambda x: ''.join(x.dropna().astype(str).astype(str)),
        axis=1)
    df3.to_excel('lenz03_date.xlsx')
    
    df3.dtypes


    df4['TIME'] = pd.to_datetime(df4.TIME)
    df4['سال'] = df4['TIME'].dt.year
    df4['ماه'] = df4['TIME'].dt.month
    df4['ماه'] = df4['ماه'].apply(lambda x: '{0:0>2}'.format(x))
    df4['روز'] = df4['TIME'].dt.day
    df4['روز'] = df4['روز'].apply(lambda x: '{0:0>2}'.format(x))
    df4['ساعت'] = df4['TIME'].dt.hour
    df4['ساعت'] = df4['ساعت'].apply(lambda x: '{0:0>2}'.format(x))
    df4['تاریخ'] = df4[df4.columns[7:]].apply(
        lambda x: ''.join(x.dropna().astype(str).astype(str)),
        axis=1)
    # df4.to_excel('tiva_date.xlsx')
    
    
    
    df5['TIME'] = pd.to_datetime(df5.TIME)
    df5['سال'] = df5['TIME'].dt.year
    df5['ماه'] = df5['TIME'].dt.month
    df5['ماه'] = df5['ماه'].apply(lambda x: '{0:0>2}'.format(x))
    df5['روز'] = df5['TIME'].dt.day
    df5['روز'] = df5['روز'].apply(lambda x: '{0:0>2}'.format(x))
    # df5['ساعت'] = df5['TIME'].dt.hour
    
    df5 = df5[['ch','نام برنامه','TIME','اپراتور','تعداد بازدید','مدت بازدید','سال','ماه','روز','ساعت']]
    
    df5['ساعت'] = df5['ساعت'].apply(lambda x: '{0:0>2}'.format(x))
    df5['تاریخ'] = df5[df5.columns[6:]].apply(
        lambda x: ''.join(x.dropna().astype(str).astype(str)),
        axis=1)
    
    # del df5['تاریخ']
    df5.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\iranseda_2_Sv1.xlsx', index=False)
    print('ایران صدا')
   
   
    
    
    
    
    
    
    
    
    
    """change channel name sepeher """  
    try:
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'یک': 'شبکه 1'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'دو': 'شبکه 2'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'سه': 'شبکه 3'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'چهار': 'شبکه 4'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'تهران': 'شبکه 5'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'پنج': 'شبکه 5'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'کودک': 'پویا'})
        
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'جام‌جم ۱': 'جام جم 1'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'رادیونما آوا': 'رادیو آوا'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'رادیونما ورزش': 'رادیو ورزش'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'رادیونما ایران': 'رادیو ایران'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'رادیونما پیام': 'رادیو پیام'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'رادیونما تهران': 'رادیو تهران'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'رادیونما جوان': 'رادیو جوان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'رادیونما گفتگو': 'رادیو گفتگو '})
        
        
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'آبادان': 'استانی آبادان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'آذربایجان غربی': 'استانی آذربایجان غربی'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'اصفهان': 'استانی اصفهان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'افلاک': 'استانی افلاک'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'البرز': 'استانی البرز'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'ایلام': 'استانی ایلام'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'گیلان - باران': 'استانی باران'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'بوشهر': 'استانی بوشهر'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'یزد - تابان': 'استانی تابان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'خراسان رضوی': 'استانی خراسان رضوی'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'خوزستان': 'استانی خوزستان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'دنا': 'استانی دنا'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'سبلان': 'استانی سبلان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'سهند': 'استانی سهند'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'فارس': 'استانی فارس'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'قزوین': 'استانی قزوین'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'کردستان': 'استانی کردستان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'مازندران - تبرستان': 'استانی مازندران'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'مازندران': 'استانی مازندران'})
        
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'سیستان و بلوچستان - هامون': 'استانی هامون'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'هامون': 'استانی هامون'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'همدان - سینا': 'استانی همدان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'همدان': 'استانی همدان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'خراسان شمالی - اترک': 'استانی خراسان شمالی -اترک'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'خراسان جنوبی - خاوران': 'استانی خراسان جنوبی -خاوران'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'خراسان جنوبی': 'استانی خراسان جنوبی -خاوران'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'زنجان - اشراق': 'استانی زنجان-اشراق'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'اشراق': 'استانی زنجان-اشراق'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'زاگرس': 'استانی کرمانشاه-زاگرس'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'آفتاب': 'استانی مرکزی-آفتاب'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'مرکزی - آفتاب': 'استانی مرکزی-آفتاب'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'شبکه ایلام': 'استانی ایلام'})
#    df1['ch'] = df1['ch'].replace({'دنا': 'استانی کهگیلویه و بویر احمد - دنا'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'تابان': 'استانی تابان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'چهارمحال‌بختیاری': 'استانی چهار محال بختیاری - جهان بین'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'چهار محال بختیاری - جهان بین': 'استانی چهار محال بختیاری - جهان بین'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'چهارمحال بختیاری': 'استانی چهار محال بختیاری - جهان بین'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'جهان بین': 'استانی چهار محال بختیاری - جهان بین'})
        
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'هرمزگان - خلیج فارس': 'استانی خلیج فارس'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'خلیج فارس': 'استانی خلیج فارس'})
        
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'گلستان - سبز': 'استانی گلستان-سبز'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'گلستان': 'استانی گلستان-سبز'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'سمنان': 'استانی سمنان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'قم - نور': 'استانی قم-نور'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'نور': 'استانی قم-نور'})

        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'کرمان': 'استانی کرمان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'مهاباد': 'استانی مهاباد'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'العالم سوریه': 'العالم'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'آذربایجان شرقی - سهند': 'استانی آذربایجان شرقی - سهند'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'اردبیل - سبلان': 'استانی اردبیل - سبلان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'آی فیلم فارسی':'آی فیلم'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'لرستان - افلاک':'استانی لرستان - افلاک'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'کهگیلویه و بویر احمد - دنا':'استانی کهگیلویه و بویر احمد - دنا'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'کرمانشاه - زاگرس':'استانی کرمانشاه - زاگرس'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'کرمانشاه':'استانی کرمانشاه - زاگرس'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'کیش':'استانی کیش'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({ 'قران':'قرآن'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({ 'سحر - اردو':'سحر اردو'})
        
        
        
        dfsp1.loc[(dfsp1['ch'].isnull()),'ch'] = "سایر"
        
        # df1.to_excel(r'D:\python\Clean_offline\input\source\data_database\out\sepeher.xlsx',index=False)
    except:
        pass
    
    
   
    
    
    """ change chanel name in aio """

    try:
        df1['ch'] = df1['ch'].replace({'یک': 'شبکه 1'})
        df1['ch'] = df1['ch'].replace({'دو': 'شبکه 2'})
        df1['ch'] = df1['ch'].replace({'سه': 'شبکه 3'})
        df1['ch'] = df1['ch'].replace({'چهار': 'شبکه 4'})
        df1['ch'] = df1['ch'].replace({'تهران': 'شبکه 5'})
        df1['ch'] = df1['ch'].replace({'جام‌جم ۱': 'جام جم 1'})
        
        # df1['ch'] = df1['ch'].replace({'رادیو نما ': 'رادیونما '})
        df1['ch'] = df1['ch'].replace({'رادیونما آوا': 'رادیو آوا'})
        df1['ch'] = df1['ch'].replace({'رادیونما ورزش': 'رادیو ورزش'})
        df1['ch'] = df1['ch'].replace({'رادیونما ایران': 'رادیو ایران'})
        df1['ch'] = df1['ch'].replace({'رادیونما پیام': 'رادیو پیام'})
        df1['ch'] = df1['ch'].replace({'رادیونما تهران': 'رادیو تهران'})
        df1['ch'] = df1['ch'].replace({'رادیونما جوان': 'رادیو جوان'})
        df1['ch'] = df1['ch'].replace({'رادیونما گفتگو': 'رادیو گفتگو '})

        df1['ch'] = df1['ch'].replace({'رادیو نما آوا': 'رادیو آوا'})
        df1['ch'] = df1['ch'].replace({'رادیو نما ورزش': 'رادیو ورزش'})
        df1['ch'] = df1['ch'].replace({'رادیو نما ایران': 'رادیو ایران'})
        df1['ch'] = df1['ch'].replace({'رادیو نما پیام': 'رادیو پیام'})
        df1['ch'] = df1['ch'].replace({'رادیو نما تهران': 'رادیو تهران'})
        df1['ch'] = df1['ch'].replace({'رادیو نما جوان': 'رادیو جوان'})
        df1['ch'] = df1['ch'].replace({'رادیو نما گفتگو': 'رادیو گفتگو '})
        df1['ch'] = df1['ch'].replace({'رادیو نما گفت وگو': 'رادیو گفتگو '})
        
        df1['ch'] = df1['ch'].replace({'آبادان': 'استانی آبادان'})
        df1['ch'] = df1['ch'].replace({'آذربایجان غربی': 'استانی آذربایجان غربی'})
        df1['ch'] = df1['ch'].replace({'اصفهان': 'استانی اصفهان'})
        df1['ch'] = df1['ch'].replace({'افلاک': 'استانی افلاک'})
        df1['ch'] = df1['ch'].replace({'البرز': 'استانی البرز'})
        df1['ch'] = df1['ch'].replace({'ایلام': 'استانی ایلام'})
        df1['ch'] = df1['ch'].replace({'باران': 'استانی باران'})
        df1['ch'] = df1['ch'].replace({'بوشهر': 'استانی بوشهر'})
        df1['ch'] = df1['ch'].replace({'تابان': 'استانی تابان'})
        df1['ch'] = df1['ch'].replace({'خراسان رضوی': 'استانی خراسان رضوی'})
        df1['ch'] = df1['ch'].replace({'خوزستان': 'استانی خوزستان'})
        df1['ch'] = df1['ch'].replace({'دنا': 'استانی دنا'})
        df1['ch'] = df1['ch'].replace({'سبلان': 'استانی سبلان'})
        df1['ch'] = df1['ch'].replace({'سهند': 'استانی سهند'})
        df1['ch'] = df1['ch'].replace({'فارس': 'استانی فارس'})
        df1['ch'] = df1['ch'].replace({'قزوین': 'استانی قزوین'})
        df1['ch'] = df1['ch'].replace({'کردستان': 'استانی کردستان'})
        df1['ch'] = df1['ch'].replace({'تبرستان': 'استانی مازندران'})
        df1['ch'] = df1['ch'].replace({'هامون': 'استانی هامون'})
        df1['ch'] = df1['ch'].replace({'همدان': 'استانی همدان'})
        
        df1['ch'] = df1['ch'].replace({'اترک': 'استانی خراسان شمالی -اترک'})
        df1['ch'] = df1['ch'].replace({'خاوران': 'استانی خراسان جنوبی -خاوران'})
        df1['ch'] = df1['ch'].replace({'اشراق': 'استانی زنجان-اشراق'})
        df1['ch'] = df1['ch'].replace({'زاگرس': 'استانی کرمانشاه-زاگرس'})
        df1['ch'] = df1['ch'].replace({'آفتاب': 'استانی مرکزی-آفتاب'})
        df1['ch'] = df1['ch'].replace({'ایلام': 'استانی ایلام'})
#    df1['ch'] = df1['ch'].replace({'دنا': 'استانی کهگیلویه و بویر احمد - دنا'})
#    df1['ch'] = df1['ch'].replace({'تابان': 'استانی یزد-تابان'})
        df1['ch'] = df1['ch'].replace({'چهارمحال‌بختیاری': 'استانی چهار محال بختیاری - جهان بین'})
        df1['ch'] = df1['ch'].replace({'چهارمحال بختیاری': 'استانی چهار محال بختیاری - جهان بین'})
        df1['ch'] = df1['ch'].replace({'خلیج فارس': 'استانی خلیج فارس'})
        df1['ch'] = df1['ch'].replace({'سبز': 'استانی گلستان-سبز'})
        df1['ch'] = df1['ch'].replace({'سمنان': 'استانی سمنان'})
        df1['ch'] = df1['ch'].replace({'نور': 'استانی قم-نور'})
#        df1['ch'] = df1['ch'].replace({'سهند': 'استانی آذربایجان شرقی - سهند'})
        df1['ch'] = df1['ch'].replace({'کرمان': 'استانی کرمان'})
        df1['ch'] = df1['ch'].replace({'مهاباد': 'استانی مهاباد'})
        df1['ch'] = df1['ch'].replace({'ایران‌اکونومی': 'ایران اکونومی'})
        df1['ch'] = df1['ch'].replace({'پرس تی‌وی': 'پرس تی وی'})
        df1['ch'] = df1['ch'].replace({'جام جم ۱': 'جام جم 1'})
        df1['ch'] = df1['ch'].replace({'درفا': 'دُرفا'})
        df1['ch'] = df1['ch'].replace({'سپاهان TV': 'سپاهان‌ تی‌وی'})
        df1['ch'] = df1['ch'].replace({'آیو اسپرت': 'آیواسپرت'})
        df1['ch'] = df1['ch'].replace({'کیپاد': 'آرپا'})
        
        df1['ch'] = df1['ch'].replace({'': ''})
        
        # df1.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\aio_Sv2.xlsx',index=False)
    except:
        pass
    
    
    
    dfsp1['نببت'] = dfsp1['نام برنامه']  

    df1['نببت'] = df1['نام برنامه']
 
    df2['نببت'] = df2['نام برنامه']
    df3['نببت'] = df3['نام برنامه']
    df4['نببت'] = df4['نام برنامه']
    
    
    df2['ch'] = df2['ch'].replace({'ایلام': 'استانی ایلام'})
    df2['ch'] = df2['ch'].replace({'آبادان': 'استانی آبادان'})
    df2['ch'] = df2['ch'].replace({'اترک': 'استانی خراسان شمالی -اترک'})
    df2['ch'] = df2['ch'].replace({'آذربایجان غربی': 'استانی آذربایجان غربی'})
    df2['ch'] = df2['ch'].replace({'اشراق': 'استانی زنجان-اشراق'})
    df2['ch'] = df2['ch'].replace({'آفتاب': 'استانی مرکزی-آفتاب'})
    df2['ch'] = df2['ch'].replace({'البرز': 'استانی البرز'})
    df2['ch'] = df2['ch'].replace({'بوشهر': 'استانی بوشهر'})
    df2['ch'] = df2['ch'].replace({'تبرستان': 'استانی مازندران'})
    df2['ch'] = df2['ch'].replace({'جهانبین': 'استانی چهار محال بختیاری - جهان بین'})
    df2['ch'] = df2['ch'].replace({'خاوران': 'استانی خراسان جنوبی -خاوران'})
    df2['ch'] = df2['ch'].replace({'خلیج فارس': 'استانی خلیج فارس'})
    df2['ch'] = df2['ch'].replace({'دنا': 'استانی دنا'})
    df2['ch'] = df2['ch'].replace({'زاگرس': 'استانی کرمانشاه-زاگرس'})
    df2['ch'] = df2['ch'].replace({'سبز': 'استانی گلستان-سبز'})
    df2['ch'] = df2['ch'].replace({'سبلان': 'استانی سبلان'})
    df2['ch'] = df2['ch'].replace({'سمنان': 'استانی سمنان'})
    df2['ch'] = df2['ch'].replace({'سینا': 'استانی همدان'})
    df2['ch'] = df2['ch'].replace({'قزوین': 'استانی قزوین'})
    df2['ch'] = df2['ch'].replace({'کرمان': 'استانی کرمان'})
    df2['ch'] = df2['ch'].replace({'کیش':'استانی کیش'})
    df2['ch'] = df2['ch'].replace({'لرستان':'استانی لرستان - افلاک'})
    df2['ch'] = df2['ch'].replace({'مهاباد': 'استانی مهاباد'})
    df2['ch'] = df2['ch'].replace({'نور': 'استانی قم-نور'})
    df2['ch'] = df2['ch'].replace({'هامون': 'استانی هامون'})
    df2['ch'] = df2['ch'].replace({'یزد': 'استانی تابان'})
   
    
    
    
    
    
    
    
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ورزشی 12:45': 'اخبار ورزشی'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ورزشی 18:45': 'اخبار ورزشی'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ورزشی 9:30': 'خبر ورزشی'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ورزشی 21:30': 'خبر ورزشی'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ورزشی 14:30': 'خبر ورزشی'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ورزشی 2:30': 'خبر ورزشی'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ورزشی 16:30': 'خبر ورزشی'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ورزشی 6:30': 'خبر ورزشی'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ورزشی 23:30': 'خبر ورزشی'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ورزشی 4:30': 'خبر ورزشی'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ورزشی 7:30': 'خبر ورزشی'})
#df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار': 'خبر ورزشی'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 19': 'اخبار عصرگاهی'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 9:00 شبکه 1': 'اخبار صبحگاهی'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 8:00': 'اخبار صبحگاهی'})
    
    
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار سراسری': 'اخبار شبانگاهی'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار سراسری 22:30': 'اخبار سراسری'})
    


    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 22:00 شبکه 3': 'اخبار شبانگاهی'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 00:00': 'خبر 0'})
    
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 1:00': 'خبر 1'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 2:00': 'خبر 2'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 3:00': 'خبر 3'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 3:00': 'خبر 3'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 4:00': 'خبر 4'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 5:00': 'خبر 5'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 6:00': 'خبر 6'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 7:00': 'خبر 7'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 8:00 - شبکه خبر': 'خبر 8'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 9:00 شبکه خبر': 'خبر 9'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 10:00': 'خبر 10'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 10:00 شبکه خبر': 'خبر 10'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 11:00': 'خبر 11'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 12:00': 'خبر 12'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 13:00': 'خبر 13'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 14:00': 'خبر 14'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 15:00': 'خبر 15'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 16:00': 'خبر 16'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 17:00': 'خبر 17'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 18:00': 'خبر 18'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 19:00': 'خبر 19'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 20:00': 'خبر 20'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'خبر 20:00': 'خبر 20'})    
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 21:00': 'خبر 21'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 22:00 شبکه خبر': 'خبر 22'})
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 23:00': 'خبر 23'})
    
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 10 شبکه قرآن':'اخبار قرآنی'})
    
    df2['نام برنامه'] = df2['نام برنامه'].replace({'اخبار ساعت 20': 'خبر'})
    
    
    
    
    
    
    
     
    """ change chanel name in lenz """
    
    df3['ch'] = df3['ch'].replace({'بارسلونا - گالاتاسارای': 'لنزاسپورت پلاس'})
    df3['ch'] = df3['ch'].replace({'بتیس - اتلتیکو': 'لنزاسپورت پلاس'})
    df3['ch'] = df3['ch'].replace({'آتالانتا - بایرلورکوزن': 'لنزاسپورت پلاس'})
    # df3['ch'] = df3['ch'].replace({'بارسلونا - گالاتاسارای ': 'لنزاسپورت پلاس'})
    
    
    
    """ change chanel name in iranseda """
    
    df5['ch'] = df5['ch'].replace({'آوا ': 'رادیو آوا'})
    df5['ch'] = df5['ch'].replace({'ورزش':'رادیو ورزش'})
    df5['ch'] = df5['ch'].replace({'ايران ': 'رادیو ایران'})
    df5['ch'] = df5['ch'].replace({'پیام': 'رادیو پیام'})
    df5['ch'] = df5['ch'].replace({'تهران': 'رادیو تهران'})
    df5['ch'] = df5['ch'].replace({'جوان': 'رادیو جوان'})
    df5['ch'] = df5['ch'].replace({'جوان': 'رادیو جوان'})
    df5['ch'] = df5['ch'].replace({'پیام': 'رادیو پیام'})
    # df1['ch'] = df1['ch'].replace({'رادیونما گفتگو': 'رادیو گفتگو '})


    


#    del df000

#df0=df0.append(df1)

    dfsp1.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\test\sepeher.xlsx', index=False)
    df1.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\test\Aio.xlsx', index=False)
    df2.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\test\telewebion.xlsx', index=False)
    df3.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\test\lenz.xlsx', index=False)
    df4.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\test\tva.xlsx', index=False)
    df5.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\test\iranseda.xlsx', index=False)
    
    df1.dtypes
    df2.dtypes
    df3.dtypes
    df4.dtypes
    df5.dtypes
    dfsp1.dtypes
    
    df0=df0.append(df5)
    df0=df0.append(dfsp1)
    df0=df0.append(df3)
    df0=df0.append(df4)
    df0=df0.append(df1)

    df0=df0.append(df2)
    
    df0.dtypes
#    df0['نببت']=df0['نام برنامه']

    df0.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\stadard_1.xlsx', index=False)
    print('ادغام')
#    df000 = df0
    

    df0 = df0.rename(columns={'TIME': 'تاریخ شروع'})
    del df0['ماه']
    del df0['روز']
    del df0['سال']




    df0['ch'] = df0['ch'].str.replace('شبکه ','')
    df0['ch'] = df0['ch'].str.replace('ي','ی')
    

    
    df0['نام برنامه'] = df0['نام برنامه'].str.replace('سریال ','مجموعه ')
    df0['نام برنامه'] = df0['نام برنامه'].str.replace(' سریال',' مجموعه')
    df0['نام برنامه'] = df0['نام برنامه'].str.replace('سریال','مجموعه ')
    
    
    
    df0['نام برنامه'] = df0['نام برنامه'].astype(str)
    df0['نام برنامه'] = df0['نام برنامه'].str.replace('ي','ی')

    df0 = df0[~df0['نام برنامه'].str.contains('اذان')]
    df0 = df0[~df0['نام برنامه'].str.contains('میان برنامه')]
    df0 = df0[~df0['نام برنامه'].str.contains('میانبرنامه')]
    df0 = df0[~df0['نام برنامه'].str.contains('آرم تایم')]
    df0 = df0[~df0['نام برنامه'].str.contains('برنامه بعدی')]
    df0 = df0[~df0['نام برنامه'].str.contains('اعلام برنامه')]
    df0 = df0[~df0['نام برنامه'].str.contains('معرفی برنامه')]    
    
    
    
    
    
    
    
    
    df0 = df0.rename(columns={'نام برنامه': 'Name'})

    df0['Name'] = df0['Name'].astype(str)
    df0['Name'] = df0['Name'].str.replace('ي','ی')
    df0['Name'] = df0['Name'].str.replace('قسمت','قسمت ')
    

    df0 = df0[~df0['Name'].str.contains('اذان')]
    df0 = df0[~df0['Name'].str.contains('میان برنامه')]
    df0 = df0[~df0['Name'].str.contains('میانبرنامه')]
    df0 = df0[~df0['Name'].str.contains('میان‌برنامه')]
    df0 = df0[~df0['Name'].str.contains('بازرگانی')]
    df0 = df0[~df0['Name'].str.contains('آگهی')]
    df0 = df0[~df0['Name'].str.contains('اگهی')]
    df0 = df0[~df0['Name'].str.contains('وله')]
    df0 = df0[~df0['Name'].str.contains('ارم استیشن')]
    df0 = df0[~df0['Name'].str.contains('آرم استیشن')]
    df0 = df0[~df0['Name'].str.contains('ارم تایم')]
    df0 = df0[~df0['Name'].str.contains('آرم تایم')]
    df0 = df0[~df0['Name'].str.contains('برنامه بعدی')]
    df0 = df0[~df0['Name'].str.contains('اعلام برنامه')]
    df0 = df0[~df0['Name'].str.contains('معرفی برنامه')]
    df0 = df0[~df0['Name'].str.contains('نماهنگ')]
    df0 = df0[~df0['Name'].str.contains('کپشن')]
    df0 = df0[~df0['Name'].str.contains('مولودی')]
    df0 = df0[~df0['Name'].str.contains('آنونس')]
    df0 = df0[~df0['Name'].str.contains('انونس')]
    df0 = df0[~df0['Name'].str.contains('تیتراژ')]
    df0 = df0[~df0['Name'].str.contains('تیزر')]
    df0 = df0[~df0['Name'].str.contains('هم خوانی')]
    df0 = df0[~df0['Name'].str.contains('همخوانی')]
    df0 = df0[~df0['Name'].str.contains('هم‌خوانی')]
    df0 = df0[~df0['Name'].str.contains('ارتباط مستقیم')]
    df0 = df0[~df0['Name'].str.contains('کلیپ')]
    df0 = df0[~df0['Name'].str.contains('آگهی قبل ')]
    df0 = df0[~df0['Name'].str.contains('ذکر')]
    df0 = df0[~df0['Name'].str.contains('دعا')]
    df0 = df0[~df0['Name'].str.contains('تقدیم برنامه')]
    df0 = df0[~df0['Name'].str.contains('برنامه از')]
    df0 = df0[~df0['Name'].str.contains('حسنی')]
    df0 = df0[~df0['Name'].str.contains('پیش پرده')]
    df0 = df0[~df0['Name'].str.contains('اکنون')]
    df0 = df0[~df0['Name'].str.contains('نشان برنامه')]

    
     

    df0['ch'] = df0['ch'].astype(str)
    df0['ch1']=df0.loc[(df0.ch == 'دو'), 'ch'] = 'شبکه 2' 
    df0['ch1']=df0.loc[(df0.ch == 'سه'), 'ch'] = 'شبکه 3'
    df0['ch1']=df0.loc[(df0.ch == 'چهار'), 'ch'] = 'شبکه 4'
    df0['ch1']=df0.loc[(df0.ch == 'تهران'), 'ch'] = 'شبکه 5'
    df0['ch1']=df0.loc[(df0.ch == 'یک'), 'ch'] = 'شبکه 1'

    df0['ch1']=df0.loc[(df0.ch == '۱'), 'ch'] = 'شبکه 1' 
    df0['ch1']=df0.loc[(df0.ch == '۲'), 'ch'] = 'شبکه 2'
    df0['ch1']=df0.loc[(df0.ch == '۳'), 'ch'] = 'شبکه 3'
    df0['ch1']=df0.loc[(df0.ch == '۴'), 'ch'] = 'شبکه 4'
    df0['ch1']=df0.loc[(df0.ch == '۵'), 'ch'] = 'شبکه 5'
    df0['ch1']=df0.loc[(df0.ch == '3 HD'), 'ch'] = 'شبکه 3'
    df0['ch1']=df0.loc[(df0.ch == 'ورزش HD'), 'ch'] = 'ورزش'
    df0['ch1']=df0.loc[(df0.ch == '1 HD'), 'ch'] = 'شبکه 1'
    df0['ch1']=df0.loc[(df0.ch == 'آی فیلم HD'), 'ch'] = 'آی فیلم'
    df0['ch1']=df0.loc[(df0.ch == 'نسیم HD'), 'ch'] = 'نسیم'
    df0['ch1']=df0.loc[(df0.ch == 'مستند HD'), 'ch'] = 'مستند'  
    df0['ch1']=df0.loc[(df0.ch == 'HDTV3'), 'ch'] = 'شبکه 3'
    
    
    df0['ch1']=df0.loc[(df0.ch == 'بازار'), 'ch'] = 'ایران کالا'
    df0['ch1']=df0.loc[(df0.ch == 'ifilm'), 'ch'] = 'آی فیلم'
    df0['ch1']=df0.loc[(df0.ch == 'Press TV'), 'ch'] = 'پرس تی وی'
    df0['ch1']=df0.loc[(df0.ch == 'اچ دی تماشا'), 'ch'] = 'تماشا'
    
    df0['ch1']=df0.loc[(df0.ch == '1'), 'ch'] = 'شبکه 1' 
    df0['ch1']=df0.loc[(df0.ch == '2'), 'ch'] = 'شبکه 2'
    df0['ch1']=df0.loc[(df0.ch == '3'), 'ch'] = 'شبکه 3'
    df0['ch1']=df0.loc[(df0.ch == '4'), 'ch'] = 'شبکه 4'
    df0['ch1']=df0.loc[(df0.ch == '5'), 'ch'] = 'شبکه 5'

    df0['ch1']=df0.loc[(df0.ch == 'تماشا HD'), 'ch'] = 'تماشا'
    df0['ch1']=df0.loc[(df0.ch == 'سه HD'), 'ch'] = 'شبکه 3'
    df0['ch1']=df0.loc[(df0.ch == 'پنج'), 'ch'] = 'شبکه 5'

#    df0000 = df0
#### part tag
    df0.loc[df0['ch'].str.contains('پویا'), 'tag'] = 'کودک'
    df0.loc[df0['ch'].str.contains('ورزش'), 'tag'] = 'ورزشی'
    df0.loc[df0['ch'].str.contains('دیجتون'), 'tag'] = 'کودک'
    df0.loc[df0['ch'].str.contains('تیوا کودک'), 'tag'] = 'کودک'
    df0.loc[df0['ch'].str.contains('شاپرک'), 'tag'] = 'کودک'
    
    df0.loc[df0['Name'].str.contains('خبر'), 'tag'] = 'اخبار'
    df0.loc[df0['Name'].str.contains('فوتبال'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('والیبال'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('فوتسال'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains(' کشتی فرنگی'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('کشتی آزاد'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('لیگ برتر کشتی'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('خانه کشتی'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('ورزش'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('اسکی'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('هاکی'), 'tag'] = 'ورزشی'
    
    df0.loc[df0['Name'].str.contains('مجموعه'), 'tag'] = 'مجموعه تلویزیونی'
    df0.loc[df0['Name'].str.contains('فیلم'), 'tag'] = 'فیلم سینمایی'
    df0.loc[df0['Name'].str.contains('اخبار'), 'tag'] = 'اخبار'
    df0.loc[df0['Name'].str.contains('سینمایی'), 'tag'] = 'فیلم سینمایی'
    df0.loc[df0['ch'].str.contains('اخبار ورزشی'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('موسیقی فیلم'), 'tag'] = 'سایر'
    df0.loc[df0['Name'].str.contains('کودک'), 'tag'] = 'کودک'
    df0.loc[df0['Name'].str.contains('انیمیشن'), 'tag'] = 'کودک'
    df0.loc[df0['Name'].str.contains('مستند'), 'tag'] = 'مستند'

    
    df0 = df0[~df0['ch'].str.contains('سایر')]
    df0 = df0[~df0['ch'].str.contains('_بدون عنوان')]    
    
    
    
    
    
#df0.loc[df0['Name'].str.contains('خبر'), 'tag'] = 'اخبار'
#df0.loc[df0['tag'].str.contains(''), 'tag'] = 'سایر'

    


    df0['Name'] = df0['Name'].str.replace('0', '۰')
    df0['Name'] = df0['Name'].str.replace('1', '۱')
    df0['Name'] = df0['Name'].str.replace('2', '۲')
    df0['Name'] = df0['Name'].str.replace('3', '۳')
    df0['Name'] = df0['Name'].str.replace('4', '۴')
    df0['Name'] = df0['Name'].str.replace('5', '۵')
    df0['Name'] = df0['Name'].str.replace('6', '۶')
    df0['Name'] = df0['Name'].str.replace('7', '۷')
    df0['Name'] = df0['Name'].str.replace('8', '۸')
    df0['Name'] = df0['Name'].str.replace('9', '۹')

    df0['Name'] = df0['Name'].str.replace('٠', '۰')
    df0['Name'] = df0['Name'].str.replace('١', '۱')
    df0['Name'] = df0['Name'].str.replace('٢', '۲')
    df0['Name'] = df0['Name'].str.replace('٣', '۳')
    df0['Name'] = df0['Name'].str.replace('٤', '۴')
    df0['Name'] = df0['Name'].str.replace('٥', '۵')
    df0['Name'] = df0['Name'].str.replace('٦', '۶')
    df0['Name'] = df0['Name'].str.replace('٧', '۷')
    df0['Name'] = df0['Name'].str.replace('٨', '۸')
    df0['Name'] = df0['Name'].str.replace('٩', '۹')








    df0 = df0.rename(columns={'ch': 'نام شبکه'})
    df0 = df0.rename(columns={'Name': 'نام برنامه'})
    df0 = df0.rename(columns={'tag': 'جنس'})
    
    
    df0['نام شبکه'] = df0['نام شبکه'].replace({'اصفهان': 'استانی اصفهان'})

    df0['نام شبکه'] = df0['نام شبکه'].replace({'باران': 'استانی باران'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'خراسان رضوی': 'استانی خراسان رضوی'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'خوزستان': 'استانی خوزستان'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'سهند': 'استانی سهند'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'فارس': 'استانی فارس'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'کردستان': 'استانی کردستان'})
    

############# for maybe mistake in dictation
    df0['نام شبکه'] = df0['نام شبکه'].replace({'استانی ابادان': 'استانی آبادان'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'استانی آذریایجان غربی': 'استانی آذربایجان غربی'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'افلاک': 'استانی افلاک'})


    df0['نام شبکه'] = df0['نام شبکه'].replace({'قرآن و معارف اسلامی': 'قرآن'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'IFilm': 'آی فیلم'})

    df0['نام شبکه'] = df0['نام شبکه'].replace({'شتاب (اقتصاد و بورس)': 'شتاب'})
    df0.loc[(df0['جنس'] .isnull()) , 'جنس'] = "سایر"    
#df0["avg"] = ""
#df0[['تعداد بازدید']].where(df0[['نام شبکه']].values == 'شبکه 1').stack().mean()
    del df0['ch1']
#df0['avg']=df0[['تعداد بازدید']].where(df0[['نام شبکه']].values == 'تماشا').stack().mean()
#df0['avg1']=df0['تماشا']['avg']

    df0.dtypes

    df0.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\astandard_out.xlsx', index=False)
    
#    df0000.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\astandard_out_test.xlsx', index=False)
    print('استاندارد سازی و یکپارچه سازی داده ها تمام شد ')
    
    print('تفکیک شبکه ها و استانی در مرحله بعدی انجام خواهد گرفت')
#************

# import datetime as dt
# tt = '2019-09-04T06:40:34Z'
# output = dt.datetime.strptime(tt, '%Y-%m-%dT%H:%M:%SZ')

# output2 = dt.datetime.strftime(output, '%d/%m/%Y %H:%M')
# print(output)
# print(output2)

# df222.dtypes

# try:
#     df2['TIME_1']=df2['TIME'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ'))
#     df222['TIME_1']=df222['TIME'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%fZ'))
# except:
#     pass
# df['']=df[''].apply(lambda x: dt.datetime.strptime(x, '%d/%m/%Y %H:%M'))