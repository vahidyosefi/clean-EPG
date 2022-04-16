# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:24:04 2020

@author: PC
"""

def func_sarsari_v2 (path_month,start_date,end_date,bb):

 
    import pandas as pd
    input0= pd.read_excel (path_month)

#input1= pd.read_excel (path_total)
#input2= pd.read_excel (path_ord)

    df0= input0
#df1= input1
#    sample_input = input0
    df0.reset_index()
#df1.reset_index()
    print("input success")


# --------- add columns & add radif & sort date

    df0['میانگین'] = ''

    df0['ردیف'] = bb

    print ('ورود میانگین و ردیف')
#----------- sort columns 

    df0 = df0[['نام شبکه','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','اپراتور','ساعت','تاریخ','ردیف','جنس','نببت']]
#df1 = df1[['نام شبکه','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','نام اپراتور','ساعت','تاریخ','ردیف','جنس']]

#sample_input=df0

    print("sort row success")

#df0['ردیف'] = ['30']

    print ('(add number of radif & check date)success')


    a_input1=len(df0.index)
    print ('تعداد کل سطرهای ورودی',a_input1)

    df0['تاریخ شروع'] = pd.to_datetime(df0['تاریخ شروع'])

    mask = (df0['تاریخ شروع'] > start_date) & (df0['تاریخ شروع'] <= end_date)

    df0 = df0.loc[mask]

    print ('تاریخ فیلتر به ماه مربوطه شده است')

#df0.to_excel("test1.xlsx", index=False)


    f_input1=len(df0.index)
    print ('تعداد کل سطرهای پس از فیلتر',f_input1)



####        -------  select chanel 

    print ('ستون جنس تکمیل شد')

    df0 = df0.rename(columns = {"نام شبکه":"chan"})
    df0 = df0.drop([], axis=1)
    df0.reset_index()

    df0['chan'] = df0['chan'].str.strip()

#    dfek0_source =df0


    df2=df0.query("chan == 'شبکه 1'")
    print()
    df21=df0.query("chan == 'شبکه 2'")
    df22=df0.query("chan == 'شبکه 3'")
    df23=df0.query("chan == 'شبکه 4'")
    #df24=df0.query(" chan == 'شبکه 4'")
    df25=df0.query(" chan == 'شبکه 5'")
    df26=df0.query(" chan == 'افق'")
    df27=df0.query(" chan == 'قرآن'")
    df28=df0.query(" chan == 'پویا'")
    df29=df0.query(" chan == 'نسیم'")
    df30=df0.query(" chan == 'مستند'")
    df31=df0.query(" chan == 'ورزش'")
    
    df33=df0.query(" chan == 'آموزش'")
    df34=df0.query(" chan == 'امید'")
        
    df36=df0.query(" chan == 'تماشا'")
    df37=df0.query(" chan == 'سلامت'")
    df38=df0.query(" chan == 'شما'")
    df39=df0.query(" chan == 'ایران کالا'")
    df40=df0.query(" chan == 'نمایش'")
    df41=df0.query(" chan == 'خبر'")
    df44=df0.query(" chan == 'سپهر'")
## برون مرزی    
    
    df32=df0.query(" chan == 'العالم'")
    df35=df0.query(" chan == 'آی فیلم'")
    df42=df0.query(" chan == 'پرس تی وی'")
    df43=df0.query(" chan == 'الکوثر'")
    df45=df0.query(" chan == 'جام جم 1'")

    a2=len(df2.index)
    a21=len(df21.index)
    a22=len(df22.index)
    a23=len(df23.index)
    a25=len(df25.index)
#a2=len(df26.index)
    a26=len(df26.index)
    a27=len(df27.index)
    a28=len(df28.index)
    a29=len(df29.index)
    a30=len(df30.index)
    a31=len(df31.index)
    
    a33=len(df33.index)
    a34=len(df34.index)
    
    a36=len(df36.index)
    a37=len(df37.index)
    a38=len(df38.index)
    a39=len(df39.index)
    a40=len(df40.index)
    a41=len(df41.index)

    a44=len(df44.index)
    
    
    a32=len(df32.index)
    a35=len(df35.index)
    a42=len(df42.index)
    a43=len(df43.index)
    a45=len(df45.index)        
    print ('شبکه 1',a2)
    print ('شبکه 2',a21)
    print ('شبکه 3',a22)
    print ('شبکه 4',a23)
    print ('شبکه 5',a25)
    print ('افق',a26)
    print ('قرآن',a27)
    print ('پویا',a28)
    print ('نسیم',a29)
    print ('مستند',a30)
    print ('ورزش',a31)
    print ('آموزش',a33)
    print ('امید',a34)
    print ('تماشا',a36)
    print ('سلامت',a37)
    print ('شما',a38)
    print ('ایران کالا',a39)
    print ('نمایش',a40)
    print ('خبر',a41)
    print ('سپهر',a44)
    
    
    
    print ('العالم',a32)
    print ('آی فیلم',a35)
    print ('پرس تی وی',a42)
    print ('الکوثر',a43)
    print ('جام جم 1',a45)

    a_len_sarasari = a2+a21+a22+a23+a25+a26+a27+a28+a29+a30+a31+a33+a34+a36+a37+a38+a39+a40+a41+a44
    print ('تعداد کل سطرهای شبکه های سراسری ',a_len_sarasari)

    list_sarasari1 = ['شبکه 1','شبکه2','شبکه3 ','شبکه4','شبکه5','افق','قران','پویا','نسیم','مستند','ورزش','آموزش','امید','تماشا','سلامت','شما','ایران کالا','نمایش','خبر','سپهر']
    list_sarasari2 = [a2,a21,a22,a23,a25,a26,a27,a28,a29,a30,a31,a33,a34,a36,a37,a38,a39,a40,a41,a44]
    
    dic_sarasari1={'لیست شبکه ها' :list_sarasari1,'تعداد سطرهای ثبت شده':list_sarasari2}

    check_list_sarasari1 = pd.DataFrame(dic_sarasari1)
    check_list_sarasari1.to_excel(r"D:\python\EPG_vahid\Check_list\check_list_sarasari.xlsx", index=False)
#### جدا کردن استانی
    df50=df0[df0['chan'].str.contains('استانی', regex=False)]




#     list_sarasari1 = ['شبکه 1','شبکه2','شبکه3 ','شبکه4','شبکه5','افق','قران','پویا','نسیم','مستند','ورزش','العالم','آموزش','امید','آی فیلم','تماشا','سلامت','شما','ایران کالا','نمایش','خبر','پرس تی وی','الکوثر','سپهر','جام جم 1']
#     list_sarasari2 = [a2,a21,a22,a23,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45]
    
#     dic_sarasari1={'لیست شبکه ها' :list_sarasari1,'تعداد سطرهای ثبت شده':list_sarasari2}

#     check_list_sarasari1 = pd.DataFrame(dic_sarasari1)
#     check_list_sarasari1.to_excel(r"D:\python\EPG_vahid\Check_list\check_list_sarasari.xlsx", index=False)
# #### جدا کردن استانی
#     df50=df0[df0['chan'].str.contains('استانی', regex=False)]










#### جدا کردن رادیوی

    df60=df0[df0['chan'].str.contains('رادیو', regex=False)]

### جدا کردن شبکه آی فیلم عربی
    df70=df0.query(" chan == 'iFilm Arabic'")
    df71= df0[df0['chan'].str.contains('سحر', regex=False)]
    
    df32 = df32.append(df35)
    df32 = df32.append(df42)
    df32 = df32.append(df43)
    df32 = df32.append(df45)
    df32 = df32.append(df71)
    df70 = df70.append(df32)
    # df70.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\df70.xlsx', index=False)



    frames = [df2, df21, df22, df23, df25, df26, df27, df28, df29, df30, df31, df33, df34, df36, df37, df38, df39, df40, df41, df44]
    result = pd.concat(frames)

    result = result.rename(columns = {"chan":"نام شبکه"})
    # result.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\result.xlsx', index=False)



    print ('distributed seccess')

    print ('مقایسه تعداد سطرها')
    
    print ('تعداد تجمیع کل سطرهای شبکه های سراسری ',len(result.index))
    print ('تعداد کل سطرهای شبکه های استانی ',len(df50.index))
    print ('تعداد کل سطرهای شبکه های رادیویی ',len(df60.index))
    print ('تعداد کل سطرهای شبکه های برون مرزی ',len(df70.index))
    

###########  report for moien  ............

    dfM1 = df2.rename(columns = {"chan":"نام شبکه"})
    dfM2 = df21.rename(columns = {"chan":"نام شبکه"})
    dfM3 = df22.rename(columns = {"chan":"نام شبکه"})
    dfM4 = df23.rename(columns = {"chan":"نام شبکه"})
    dfM5 = df25.rename(columns = {"chan":"نام شبکه"})
    dfM6 = df26.rename(columns = {"chan":"نام شبکه"})
    dfM7 = df27.rename(columns = {"chan":"نام شبکه"})
    dfM8 = df28.rename(columns = {"chan":"نام شبکه"})
    dfM9 = df29.rename(columns = {"chan":"نام شبکه"})
    dfM10 = df30.rename(columns = {"chan":"نام شبکه"})
    dfM11 = df31.rename(columns = {"chan":"نام شبکه"})
    # dfM12 = df32.rename(columns = {"chan":"نام شبکه"})
    dfM13 = df33.rename(columns = {"chan":"نام شبکه"})
    dfM14 = df34.rename(columns = {"chan":"نام شبکه"})
    # dfM15 = df35.rename(columns = {"chan":"نام شبکه"})
    dfM16 = df36.rename(columns = {"chan":"نام شبکه"})
    dfM17 = df37.rename(columns = {"chan":"نام شبکه"})
    dfM18 = df38.rename(columns = {"chan":"نام شبکه"})
    dfM19 = df39.rename(columns = {"chan":"نام شبکه"})
    dfM20 = df40.rename(columns = {"chan":"نام شبکه"})
    dfM21 = df41.rename(columns = {"chan":"نام شبکه"})
    # dfM22 = df42.rename(columns = {"chan":"نام شبکه"})
    # dfM23 = df43.rename(columns = {"chan":"نام شبکه"})
    dfM24 = df44.rename(columns = {"chan":"نام شبکه"})
    # dfM25 = df45.rename(columns = {"chan":"نام شبکه"})


    print ('rename')

    print (' چاپ شبکه های سراسری به تفکیک شبکه')
#dfM1.to_excel('path1', index=False)



    a= pd.DataFrame()

    my_list = [dfM1, dfM2, dfM3, dfM4, dfM5,dfM6, dfM7, dfM8, dfM9, dfM10, dfM11,dfM13,dfM14,dfM16,dfM17,dfM18,dfM19,dfM20,dfM21,dfM24]

    print('write compeletly')

        
    for vahid in range(20):
    
#        print("number of data frame for sarasari", vahid)
    
        ch= vahid + 1
#        print("path_out", ch)
        a=my_list[vahid]

        path_out  =r'D:\python\EPG_vahid\progress\sarasari\in\{}.xlsx'.format(ch)

        a.to_excel( path_out, index=False)
        
    print('خروجی شبکه های سراسری در آدرس داده شده چاپ شده است')



    result0 = df50

    result0 = result0.rename(columns = {"chan":"نام شبکه"})
    
    df60 = df60.rename(columns = {"chan":"نام شبکه"})

    df70 = df70.rename(columns = {"chan":"نام شبکه"})
    


    result = result[['نام شبکه','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','اپراتور','ساعت','تاریخ','ردیف','جنس','نببت']]
    result0 = result0[['نام شبکه','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','اپراتور','ساعت','تاریخ','ردیف','جنس','نببت']]
    df60 = df60[['نام شبکه','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','اپراتور','ساعت','تاریخ','ردیف','جنس','نببت']]
    df70 = df70[['نام شبکه','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','اپراتور','ساعت','تاریخ','ردیف','جنس','نببت']]

#    df_ostani = result0

#    df_radio = df60

    result.to_excel(r"D:\python\EPG_vahid\input\source\Estandard\divide\سراسری.xlsx", index=False)
    print('چاپ کامل سراسری')
    result0.to_excel(r"D:\python\EPG_vahid\input\source\Estandard\divide\استانی.xlsx", index=False)
    print(' چاپ کامل استانی')
    df60.to_excel(r"D:\python\EPG_vahid\input\source\Estandard\divide\رادیوی.xlsx", index=False)
    print(' چاپ کامل رادیوی') 
    df70.to_excel(r"D:\python\EPG_vahid\input\source\Estandard\divide\برون مرزی.xlsx", index=False) 
    print('چاپ کامل برون مرزی ')
    
#    dfnew_sarasari = result 
#
######## for Ekhtesasi
######## for Ekhtesasi


#
    dfe1 = df0.query("chan != 'شبکه 1'")
    dfe2 = dfe1.query("chan != 'شبکه 2'")
    dfe3 = dfe2.query("chan != 'شبکه 3'")
    dfe4 = dfe3.query("chan != 'شبکه 4'")

    dfe5 = dfe4.query(" chan != 'شبکه 5'")
    dfe6 = dfe5.query(" chan != 'افق'")
    dfe7 = dfe6.query(" chan != 'قرآن'")
    dfe8 = dfe7.query(" chan != 'پویا'")
    dfe9 = dfe8.query(" chan != 'نسیم'")
    dfe10= dfe9.query(" chan != 'مستند'")
    dfe11= dfe10.query(" chan != 'ورزش'")
    dfe12= dfe11.query(" chan != 'العالم'")
    dfe13= dfe12.query(" chan != 'آموزش'")
    dfe14= dfe13.query(" chan != 'امید'")
    dfe15= dfe14.query(" chan != 'آی فیلم'")
    dfe16= dfe15.query(" chan != 'تماشا'")
    dfe17= dfe16.query(" chan != 'سلامت'")
    dfe18= dfe17.query(" chan != 'شما'")
    dfe19= dfe18.query(" chan != 'ایران کالا'")
    dfe20= dfe19.query(" chan != 'نمایش'")
    dfe21= dfe20.query(" chan != 'خبر'")
    dfe22= dfe21.query(" chan != 'پرس تی وی'")
    dfe23= dfe22.query(" chan != 'الکوثر'")
    dfe24= dfe23.query(" chan != 'سپهر'")
    dfe25= dfe24.query(" chan != 'جام جم 1'")
    
#df50.loc[(df0['chan'] == 'استانی') , 'chan'] = "1"

    dfe26 = dfe25.query(" chan != 'iFilm Arabic'")
    
    
    dfe27 = dfe26.query(" chan != 'سحر کردی'")
    dfe30 = dfe27.query("chan != 'سحر بالکان'")
    dfe311 = dfe30.query(" chan != 'سحر آذری'")
    dfe31 = dfe311.query(" chan != 'سحر اردو'")
    
    dfe32 = dfe31.query(" chan != 'خراسان رضوی'")
    dfe33 = dfe32.query(" chan != 'خوزستان'")
    dfe34 = dfe33.query(" chan != 'سهند'")
    dfe35 = dfe34.query(" chan != 'فارس'")
    dfe36 = dfe35.query(" chan != 'کردستان'")

# 

    print('without')
#

    dfe37 = dfe36[~dfe36['chan'].str.contains('استانی')]
#df50=df0[df0['chan'].str.contains('استانی', regex=False)]
    dfe38 = dfe37[~dfe37['chan'].str.contains('رادیو')]

#df60=df0[df0['chan'].str.contains('رادیو', regex=False)]


#    dfe38.loc[(dfe38['جنس'] .isnull()) , 'جنس'] = "سایر"

    dfe38 = dfe38.rename(columns = {"chan":"نام شبکه"})
    dfe38 = dfe38[['نام شبکه','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','اپراتور','ساعت','تاریخ','ردیف','جنس','نببت']]
    
    dfe38.to_excel(r"D:\python\EPG_vahid\input\source\Estandard\divide\اختصاصی.xlsx", index=False)

#    dfe38.to_excel('test_dfe.xlsx',index = False)


    print('چاپ کامل اختصاصی ')

    a_sarasari =len(result.index)
    a_ostani = len(df50.index)
    a_radio = len(df60.index)
    a_ifilm = len(df70.index)
    a_ekhtesasi= len(dfe38.index)
    a_tafkik = a_sarasari + a_ostani + a_radio + a_ifilm + a_ekhtesasi
    ekh = f_input1-a_tafkik
    ekh_filter = a_input1 - f_input1

    print ('تعداد کل سطرهای ورودی',a_input1)
    print (' تعداد کل سطرهای ورودی پس از فیلتر ',f_input1)
#print ('تعداد تجمیع سطرهای فیلتر شده کل شبکه ها در 8 ماه',aa_df0)
    print ('تعداد سطرهای فیلتر شده',ekh_filter)
    print ('تعداد تجمیع کل سطرهای شبکه های سراسری ',len(result.index))
    print ('تعداد کل سطرهای شبکه های استانی ',len(df50.index))
    print ('تعداد کل سطرهای شبکه های رادیویی ',len(df60.index))
    print ('تعداد کل سطرهای شبکه های برون مرزی ',len(df70.index)) 
    print ('تعداد کل سطرهای شبکه های اختصاصی ',len(dfe38.index)) 
    print ('تعداد کل سطرهای  تجمیع شده کل استانی + سراسری + رادیوی و اختصاصی ',a_tafkik)
    print ('اختلاف وروردی فیلتر شده با کل تجمیع اختصاصی+ استانی+رادیو + سرارسی ',ekh)
    
    
    list_1=['تعداد کل سطرهای ورودی','تعداد کل سطرهای ورودی پس از فیلتر','تعداد سطرهای فیلتر شده','تعداد تجمیع کل سطرهای شبکه های سراسری ','تعداد کل سطرهای شبکه های استانی ','تعداد کل سطرهای شبکه های رادیویی ','تعداد کل سطرهای شبکه های برون مرزی ','تعداد کل سطرهای شبکه های اختصاصی '
            ,'تعداد کل سطرهای  تجمیع شده کل استانی + سراسری + رادیوی و اختصاصی ','اختلاف وروردی فیلتر شده با کل تجمیع اختصاصی+ استانی+رادیو + سراسری']     
    list_2=[a_input1,f_input1,ekh_filter,len(result.index),len(df50.index),len(df60.index),len(df70.index),len(dfe38.index),a_tafkik,ekh]


    dic11={'مقایسه تعداد ورودی' :list_1,'بررسی اعداد ورودی':list_2}

    check_list_2 = pd.DataFrame(dic11)
    check_list_2.to_excel(r"D:\python\EPG_vahid\Check_list\check_list.xlsx", index=False)

#check_list.to_excel(r"C:\Users\PC\Desktop\new power bi\append\AAA_source\progress\check_list.xlsx", index=False)

    print('check_list') 
 

# 
#
    print ('فراخوانی تابع استانی جهت تفکیک شبکه های استانی')
#
#    from Func_Mekanizeh_ostani import *
##Func_Mekanizeh_ostani (df50)
#    number =Func_Mekanizeh_ostani (df50)
#    print('چاپ شبکه استانی به تفکیک انجام گرفته است',number)
#
    ostani = pd.DataFrame
    radio = pd.DataFrame
    bronmarzi = pd.DataFrame
    ekhtesasi = pd.DataFrame
    
    
    ostani = df50
    radio = df60
    bronmarzi = df70
    ekhtesasi = dfe38
    
#    ekhtesasi.to_excel('test_dfe.xlsx',index = False)
    
    
    return ostani, radio,bronmarzi ,ekhtesasi
    
#
#
#
#
#    print ('فراخوانی تابع رادیویی جهت تفکیک شبکه های رادیویی')
#    from Func_Mekanizeh_radio import *
#    number =Func_Mekanizeh_radio (df60)
#    print('چاپ شبکه رادیویی به تفکیک انجام گرفته است',number)
#
#
#
#    print ('فراخوانی تابع اختصاصی جهت تفکیک شبکه های اختصاصی')
#    from Func_Mekanizeh_ekhtesasi import *
#    number =Func_Mekanizeh_ekhtesasi (dfe38)
#    print('چاپ شبکه رادیویی به تفکیک انجام گرفته است',number)
#
#    print ('شبکه های سراسری ، استانی و رادیوی و اختصاصی به تفکیک شبکه ها ')
#    print('کلین شبکه ها باید انجام شود')