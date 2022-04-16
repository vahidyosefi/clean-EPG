# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:24:04 2020

@author: PC
"""
def Func_Mekanizeh_bronmarzi (input0):
    
    import pandas as pd

    df0= input0

    df0.reset_index()
#df1.reset_index()
    print("input success")

    a_input0=len(input0.index)

    print ('تعداد سطرهای کل شبکه های برون مرزی',a_input0)

#----------- sort columns 

    df0 = df0[['نام شبکه','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','اپراتور','ساعت','تاریخ','ردیف','جنس','نببت']]


    print("sort row success")

    df0 = df0.rename(columns = {"نام شبکه":"chan"})
    df0 = df0.drop([], axis=1)
    df0.reset_index()
    

    df0['chan'] = df0['chan'].str.strip()

    df2=df0.query("chan == 'العالم'")
    print()

    df21=df0.query("chan == 'آی فیلم'")
#df21=df21.append(df211)

    df22=df0.query("chan == 'پرس تی وی'")
    df23=df0.query("chan == 'الکوثر'")
    #df24=df0.query(" chan == 'شبکه 4'")
    df25=df0.query(" chan == 'جام جم 1'")
    df26=df0.query(" chan == 'iFilm Arabic'")
    df27=df0.query(" chan == 'سحر کردی'")
    df28=df0.query(" chan == 'سحر بالکان'")
    df29=df0.query(" chan == 'سحر آذری'")
    df30=df0.query(" chan == 'سحر اردو'")
    df31=df0.query(" chan == 'هیسیپان تی‌وی'")
    df32=df0.query(" chan == 'جام جم 2'")
    df33=df0.query(" chan == 'جام جم 3'")
    # df34=df0.query(" chan == 'رادیو تهران'")
#df330=df0.query(" chan == 'رادیو قران'")
#df33=df33.append(df330)

    a_input=len(df0.index)
    
    a2=len(df2.index)
    a21=len(df21.index)
    a22=len(df22.index)
    a23=len(df23.index)
    a25=len(df25.index)
    a26=len(df26.index)
    a27=len(df27.index)
    a28=len(df28.index)
    a29=len(df29.index)
    a30=len(df30.index)
    a31=len(df31.index)
    a32=len(df32.index)
    a33=len(df33.index)
    # a34=len(df34.index)
    
    a_total= a2+a21+a22+a23+a25+a26+a27+a28+a29+a30 +a31+a32+a33

    
    print ('العالم',a2)
    print ('آی فیلم',a21)
    print ('پرس تی وی',a22)
    print ('الکوثر',a23)
    print ('جام جم 1',a25)
    print ('iFilm Arabic',a26)
    print ('سحر کردی',a27)
    print ('سحر بالکان',a28)
    print ('سحر آذری',a29)
    print ('سحر اردو',a30)
    print ('هیسیپان تی‌وی',a31)
    print ('جام جم 2',a32)
    print ('جام جم 3',a33)
    # print ('رادیو تهران',a34)
    print('تعداد سطرهای شبکه های برون مرزی',a_input)
    print ('جمع تفکیک شبکه های برون مرزی',a_total)
    
    list_sarasari1 = ['العالم','آی فیلم','پرس تی وی','الکوثر','جام جم 1','iFilm Arabic','سحر کردی','سحر بالکان','سحر آذری','سحر اردو','هیسیپان تی‌وی','جام جم 2','جام جم 3','تعداد سطرهای شبکه های برون مرزی','جمع تفکیک شبکه های برون مرزی']
    list_sarasari2 = [a2,a21,a22,a23,a25,a26,a27,a28,a29,a30,a31,a32,a33,a_input,a_total]
    
    dic_radio={'لیست شبکه ها برون مرزی' :list_sarasari1,'تعداد سطرهای ثبت شده برون مرزی':list_sarasari2}

    check_list_radio = pd.DataFrame(dic_radio)
    check_list_radio.to_excel(r"D:\python\EPG_vahid\Check_list\check_list_bronmarzi.xlsx", index=False)
    
    

#df60=df0[df0['chan'].str.contains('رادیو', regex=False)]
#df70=df0.query(" chan == 'iFilm Arabic'")


    frames = [df2, df21, df22, df23 , df25, df26, df27, df28, df29, df30,df31,df32,df33]
    result = pd.concat(frames)

    result = result.rename(columns = {"chan":"نام شبکه"})

    a_merage=len(result.index)
    print ('تعداد سطرهای ادغام شده تفکیک شبکه های برون مرزی',a_merage)
    print ('distributed seccess')
    

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
    dfM12 = df32.rename(columns = {"chan":"نام شبکه"})
    dfM13 = df33.rename(columns = {"chan":"نام شبکه"})
    # dfM14 = df34.rename(columns = {"chan":"نام شبکه"})
    
    print ('rename')
    print('ریختن توی پوشه برون مرس به تفکیک شبکه ها')

    a= pd.DataFrame()

    my_list = [dfM1, dfM2, dfM3, dfM4, dfM5,dfM6, dfM7, dfM8, dfM9, dfM10,dfM11,dfM12,dfM13]
    print('write compeletly')

#for my_list1 in range (13):
#    
#    a=my_list[ch1]
#    print(a)
        
    for vahid_bronmarzi in range(13):
    
        print("number of data frame", vahid_bronmarzi)
    
        ch_bronmarzi= vahid_bronmarzi + 1
        print("path_out", ch_bronmarzi)
        a=my_list[vahid_bronmarzi]
#    print(a)
        path_out  =r'D:\python\EPG_vahid\progress\bronmarzi\in\{}.xlsx'.format(ch_bronmarzi)

        a.to_excel( path_out, index=False)
        
        
    print('write compeletly_bronmarzi')
        
    return ch_bronmarzi
    
    