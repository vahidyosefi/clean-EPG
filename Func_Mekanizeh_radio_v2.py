# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:24:04 2020

@author: PC
"""
def Func_Mekanizeh_radio_v2 (input0):
    
    import pandas as pd

    df0= input0

    df0.reset_index()
#df1.reset_index()
    print("input success")

    a_input0=len(input0.index)

    print ('تعداد سطرهای کل شبکه های رادیویی',a_input0)

#----------- sort columns 

    df0 = df0[['نام شبکه','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','اپراتور','ساعت','تاریخ','ردیف','جنس','نببت']]


    print("sort row success")

    print ('(add number of radif & check date)success')


    # df0['نام شبکه'] = df0['نام شبکه'].replace({'رادیو نما ': 'رادیونما '})

    df0['نام شبکه'] = df0['نام شبکه'].replace({'رادیو قران': 'رادیو قرآن'})

####        -------  select chanel 
    df0.loc[(df0['جنس'] .isnull()) , 'جنس'] = "سایر"

    df0 = df0.rename(columns = {"نام شبکه":"chan"})
    df0 = df0.drop([], axis=1)
    df0.reset_index()

    df0['chan'] = df0['chan'].str.strip()

    df2=df0.query("chan == 'رادیو اقتصاد'")
    print()
#df21 = df0[df0['chan'].str.contains('رادیو آوا')]
#df211=df0.query("chan == 'رادیو اوا'")
    df21=df0.query("chan == 'رادیو آوا'")
#df21=df21.append(df211)

    df22=df0.query("chan == 'رادیو ایران'")
    df23=df0.query("chan == 'رادیو پیام'")
    #df24=df0.query(" chan == 'شبکه 4'")
    df25=df0.query(" chan == 'رادیو جوان'")
    df26=df0.query(" chan == 'رادیو سلامت'")
    df27=df0.query(" chan == 'رادیو صبا'")
    df28=df0.query(" chan == 'رادیو فرهنگ'")
    df29=df0.query(" chan == 'رادیو گفتگو'")
    df30=df0.query(" chan == 'رادیو معارف'")
    df31=df0.query(" chan == 'رادیو نمایش'")
    df32=df0.query(" chan == 'رادیو ورزش'")
    df33=df0.query(" chan == 'رادیو قرآن'")
    df34=df0.query(" chan == 'رادیو تهران'")

    df35=df0.query(" chan == 'رادیو تلاوت'")
    df36=df0.query(" chan == 'رادیو مرکزی'")
    df37=df0.query(" chan == 'رادیو گیلان'")
    df38=df0.query(" chan == 'رادیو همدان'")
    df39=df0.query(" chan == 'رادیو یزد'")
    df40=df0.query(" chan == 'رادیو اردبیل'")
    df41=df0.query(" chan == 'رادیو قم'")
    df42=df0.query(" chan == 'رادیو آذربایجان غربی'")
    df43=df0.query(" chan == 'رادیو اصفهان'")
    df44=df0.query(" chan == 'رادیو خراسان شمالی'")
    df45=df0.query(" chan == 'رادیو ترتیل'")
    df46=df0.query(" chan == 'رادیو زنجان'")
    df47=df0.query(" chan == 'رادیو سیستان و بلوچستان'")
    df48=df0.query(" chan == 'رادیو فارس'")
    df49=df0.query(" chan == 'رادیو لرستان'")
    df50=df0.query(" chan == 'رادیو مناسبتی'")
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
    a34=len(df34.index)
    a35=len(df35.index)
    a36=len(df36.index)
    a37=len(df37.index)
    a38=len(df38.index)
    a39=len(df39.index)
    a40=len(df40.index)
    a41=len(df41.index)
    a42=len(df42.index)
    a43=len(df43.index)
    a44=len(df44.index)
    a45=len(df45.index)
    a46=len(df46.index)
    a47=len(df47.index)
    a48=len(df48.index)
    a49=len(df49.index)
    a50=len(df50.index)
    
    a_total_1 = a2+a21+a22+a23+a25+a26+a27+a28+a29+a30+a31+a32+a33+a34
    a_total_2 = a35 + a36 + a37+ a38 + a39+ a40+ a41
    a_total_3 = a42+ a43+ a44+ a45+ a45+ a46+ a47+ a48+ a49+ a50
    a_total = a_total_1 + a_total_2+a_total_3

    print ('رادیو اقتصاد',a2)
    print ('رادیو آوا',a21)
    print ('رادیو ایران',a22)
    print ('رادیو پیام',a23)
    print ('رادیو جوان',a25)
    print ('رادیو سلامت',a26)
    print ('رادیو صبا',a27)
    print ('رادیو فرهنگ',a28)
    print ('رادیو گفتگو',a29)
    print ('رادیو معارف',a30)
    print ('رادیو نمایش',a31)
    print ('رادیو ورزش',a32)
    print ('رادیو قرآن',a33)
    print ('رادیو تهران',a34)
    print ('رادیو تلاوت',a35)
    print ('رادیو مرکزی',a36)
    print ('رادیو گیلان',a37)
    print ('رادیو همدان',a38)
    print ('رادیو یزد',a39)
    print ('رادیو اردبیل',a40)
    print ('رادیو قم',a41)
    print ('رادیو آذربایجان غربی',a42)
    print ('رادیو اصفهان',a43)
    print ('رادیو خراسان شمالی',a44)
    print ('رادیو ترتیل',a45)
    print ('رادیو زنجان',a46)
    print ('رادیو سیستان و بلوچستان',a47)
    print ('رادیو فارس',a48)
    print ('رادیو لرستان',a49)
    print ('رادیو مناسبتی',a50)
    
    print('تعداد سطرهای شبکه های رادیویی',a_input)
    print ('جمع تفکیک شبکه های رادیویی',a_total)
    
    list_sarasari1 = ['رادیو اقتصاد','رادیو آوا','رادیو ایران ','رادیو پیام','رادیو جوان','رادیو سلامت','رادیو صبا','رادیو فرهنگ','رادیو گفتگو','رادیو معارف','رادیو نمایش','رادیو ورزش','رادیو قرآن','رادیو تهران','رادیو تلاوت','رادیو مرکزی','رادیو گیلان','رادیو همدان','رادیو یزد','رادیو اردبیل','رادیو قم','رادیو آذربایجان غربی','رادیو اصفهان','رادیو خراسان شمالی','رادیو ترتیل','رادیو زنجان','رادیو سیستان و بلوچستان','رادیو فارس','رادیو لرستان','رادیو مناسبتی','تعداد سطرهای شبکه های رادیویی','جمع تفکیک شبکه های رادیویی']
    list_sarasari2 = [a2,a21,a22,a23,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,a_input,a_total]
      
    dic_radio={'لیست شبکه ها رادیویی' :list_sarasari1,'تعداد سطرهای ثبت شده رادیویی':list_sarasari2}

    check_list_radio = pd.DataFrame(dic_radio)
    check_list_radio.to_excel(r"D:\python\EPG_vahid\Check_list\check_list_radio.xlsx", index=False)
    
    

#df60=df0[df0['chan'].str.contains('رادیو', regex=False)]
#df70=df0.query(" chan == 'iFilm Arabic'")


    frames = [df2, df21, df22, df23 , df25, df26, df27, df28, df29, df30, df31, df32, df33,df34,df35,df36,df37,df38,df39,df40,df41,df42,df43,df44,df45,df46,df47,df48,df49,df50]
    result = pd.concat(frames)

    result = result.rename(columns = {"chan":"نام شبکه"})

    a_merage=len(result.index)
    print ('تعداد سطرهای ادغام شده تفکیک شبکه های رادیویی',a_merage)
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
    dfM14 = df34.rename(columns = {"chan":"نام شبکه"})
    dfM15 = df35.rename(columns = {"chan":"نام شبکه"})
    dfM16 = df36.rename(columns = {"chan":"نام شبکه"})
    dfM17 = df37.rename(columns = {"chan":"نام شبکه"})
    dfM18 = df38.rename(columns = {"chan":"نام شبکه"})
    dfM19 = df39.rename(columns = {"chan":"نام شبکه"})
    dfM20 = df40.rename(columns = {"chan":"نام شبکه"})
    dfM21 = df41.rename(columns = {"chan":"نام شبکه"})
    dfM22 = df42.rename(columns = {"chan":"نام شبکه"})
    dfM23 = df43.rename(columns = {"chan":"نام شبکه"})
    dfM24 = df44.rename(columns = {"chan":"نام شبکه"})
    dfM25 = df45.rename(columns = {"chan":"نام شبکه"})
    dfM26 = df46.rename(columns = {"chan":"نام شبکه"})
    dfM27 = df47.rename(columns = {"chan":"نام شبکه"})
    dfM28 = df48.rename(columns = {"chan":"نام شبکه"})
    dfM29 = df49.rename(columns = {"chan":"نام شبکه"})
    dfM30 = df50.rename(columns = {"chan":"نام شبکه"})
    
    # dfM14 = df34.rename(columns = {"chan":"نام شبکه"})
    # dfM14 = df34.rename(columns = {"chan":"نام شبکه"})
    
    
    
    
    
    
    print ('rename')
    print('ریختن توی فایل رادیویی به تفکیک شبکه ها')

    a= pd.DataFrame()

    my_list = [dfM1, dfM2, dfM3, dfM4, dfM5,dfM6, dfM7, dfM8, dfM9, dfM10, dfM11, dfM12,dfM13,dfM14,dfM15,dfM16,dfM17,dfM18,dfM19,dfM20,dfM21,dfM22,dfM23,dfM24,dfM25,dfM26,dfM27,dfM28,dfM29,dfM30]
    print('write compeletly')

#for my_list1 in range (13):
#    
#    a=my_list[ch1]
#    print(a)
        
    for vahid_radio in range(30):
    
        print("number of data frame", vahid_radio)
    
        ch_radio= vahid_radio + 1
        print("path_out", ch_radio)
        a=my_list[vahid_radio]
#    print(a)
        path_out  =r'D:\python\EPG_vahid\progress\radio\in\{}.xlsx'.format(ch_radio)

        a.to_excel( path_out, index=False)
        
        
    print('write compeletly_radio')
        
    return ch_radio
    
    