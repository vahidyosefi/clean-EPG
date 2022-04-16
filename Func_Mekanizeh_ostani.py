# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:24:04 2020

@author: PC
"""


def Func_Mekanizeh_ostani (input0):
    import pandas as pd

    df0= input0
#df1= input1
#    sample_input = input0
    df0.reset_index()
#df1.reset_index()
    print("input success")

    a_input0=len(input0.index)

    print ('تعداد سطرهای کل شبکه های استانی',a_input0)
 
    df0 = df0.rename(columns = {"نام شبکه":"chan"})
    df0 = df0.drop([], axis=1)
    df0.reset_index()

    df0['chan'] = df0['chan'].str.strip()

    df2=df0.query("chan == 'استانی آبادان'")
    print()
#df21 = df0[df0['chan'].str.contains('رادیو آوا')]
#df211=df0.query("chan == 'رادیو اوا'")
    df21=df0.query("chan == 'استانی آذربایجان غربی'")
#df21=df21.append(df211)

    df22=df0.query("chan == 'استانی اصفهان'")
    df23=df0.query("chan == 'استانی افلاک'")
#df24=df0.query(" chan == 'شبکه 4'")
    df25=df0.query(" chan == 'استانی البرز'")
    df26=df0.query(" chan == 'استانی ایلام'")
    df27=df0.query(" chan == 'استانی باران'")
    df28=df0.query(" chan == 'استانی بوشهر'")
    df29=df0.query(" chan == 'استانی تابان'")
    df30=df0.query(" chan == 'استانی خراسان رضوی'")
    df31=df0.query(" chan == 'استانی خوزستان'")
    df32=df0.query(" chan == 'استانی دنا'")
    df33=df0.query(" chan == 'استانی سبلان'")
    df34=df0.query(" chan == 'استانی سهند'")
    df35=df0.query(" chan == 'استانی فارس'")
    df36=df0.query(" chan == 'استانی قزوین'")
    df37=df0.query(" chan == 'استانی کردستان'")
    df38=df0.query(" chan == 'استانی لرستان - افلاک'")
    df39=df0.query(" chan == 'استانی کیش'")
    df40=df0.query(" chan == 'استانی مازندران'")
    df41=df0.query(" chan == 'استانی هامون'")
    df42=df0.query(" chan == 'استانی همدان'")
    
    df43=df0.query(" chan == 'استانی خراسان شمالی -اترک'")
    df44=df0.query(" chan == 'استانی خراسان جنوبی -خاوران'")
    df45=df0.query(" chan == 'استانی زنجان-اشراق'")
    df46=df0.query(" chan == 'ااستانی کرمانشاه-زاگرس'")
    df47=df0.query(" chan == 'استانی مرکزی-آفتاب'")
    # df48=df0.query(" chan == 'استانی ایلام'")
    df49=df0.query(" chan == 'استانی کهگیلویه و بویر احمد - دنا'")
    df50=df0.query(" chan == 'استانی یزد-تابان'")
    df51=df0.query(" chan == 'استانی چهار محال بختیاری - جهان بین'")
    df52=df0.query(" chan == 'استانی خلیج فارس'")
    df53=df0.query(" chan == 'استانی گلستان-سبز'")
    df54=df0.query(" chan == 'استانی سمنان'")
    df55=df0.query(" chan == 'استانی قم-نور'")
    df56=df0.query(" chan == 'استانی آذربایجان شرقی - سهند'")
    df57=df0.query(" chan == 'استانی کرمان'")
    df58=df0.query(" chan == 'استانی مهاباد'")
#    df59=df0.query(" chan == 'استانی همدان'")
#    df60=df0.query(" chan == ''")
    # df60=df0.query(" chan == ''")
    # df60=df0.query(" chan == ''")
    

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
    # a48=len(df48.index)
    a49=len(df49.index)
    a50=len(df50.index)
    a51=len(df51.index)
    a52=len(df52.index)
    a53=len(df53.index)
    a54=len(df54.index)
    a55=len(df55.index)
    a56=len(df56.index)
    a57=len(df57.index)
    a58=len(df58.index)
    

    a_total_1 = a2+a21+a22+a23+a25+a26+a27+a28+a29+a30+a31+a32+a33
    a_total_2 = a34+a35+a36+a37+a38+a39+a40+a41+a42+a43+a44+a45+a46+a47  +a49
    a_total_3 = a50+a51+a52+a53+a54+a55+a56+a57+a58 
    a_total= a_total_1 + a_total_2 + a_total_3


    print ('استانی آبادان',a2)
    print ('استانی آذربایجان غربی',a21)
    print ('استانی اصفهان',a22)
    print ('استانی افلاک',a23)
    print ('استانی البرز',a25)
    print ('استانی ایلام',a26)
    print ('استانی باران',a27)
    print ('استانی بوشهر',a28)
    print ('استانی تابان',a29)
    print ('استانی خراسان رضوی',a30)
    print ('استانی خوزستان',a31)
    print ('استانی دنا',a32)
    print ('استانی سبلان',a33)
    print ('استانی سهند',a34)
    print ('استانی فارس',a35)
    print ('استانی قزوین',a36)
    print ('استانی کردستان',a37)
    print ('استانی کرمانشاه',a38)
    print ('استانی کیش',a39)
    print ('استانی مازندران',a40)
    print ('استانی هامون',a41)
    print ('استانی همدان',a42)
    
    print ('استانی خراسان شمالی -اترک',a43)
    print ('استانی خراسان جنوبی -خاوران',a44)
    print ('استانی زنجان-اشراق',a45)
    print ('استانی کرمانشاه-زاگرس',a46)
    print ('استانی مرکزی-آفتاب',a47)
    # print ('استانی ایلام',a48)
    print ('استانی کهگیلویه و بویر احمد - دنا',a49)
  
    print ('استانی یزد-تابان',a50)
    print ('استانی چهار محال بختیاری - جهان بین',a51)
    print ('استانی خلیج فارس',a52)
    print ('استانی گلستان-سبز',a53)
    print ('استانی سمنان',a54)
    print ('استانی قم-نور',a55)
    print ('استانی آذربایجان شرقی - سهند',a56)
    print ('استانی کرمان',a57)
    print ('استانی مهاباد',a58)
    
    
    
    
    
    
    
    
    
    print('تعداد سطرهای شبکه های استانی',a_input)
    print ('جمع تفکیک شبکه های استانی',a_total)

    list_ostani1 = ['استانی آبادان','استانی آذربایجان غربی','استانی اصفهان','استانی افلاک','استانی البرز','استانی ایلام','استانی باران','استانی بوشهر','استانی تابان','استانی خراسان رضوی','استانی خوزستان','استانی دنا','استانی سبلان','استانی سهند','استانی فارس','استانی قزوین','استانی کردستان','استانی کرمانشاه','استانی کیش','استانی مازندران','استانی هامون','استانی همدان','استانی خراسان شمالی -اترک','استانی خراسان جنوبی -خاوران','استانی زنجان-اشراق','استانی کرمانشاه-زاگرس','استانی مرکزی-آفتاب','استانی کهگیلویه و بویر احمد - دنا','استانی یزد-تابان','استانی چهار محال بختیاری - جهان بین','استانی خلیج فارس','استانی گلستان-سبز','استانی سمنان','استانی قم-نور','استانی آذربایجان شرقی - سهند','استانی کرمان','استانی مهاباد','تعداد سطرهای شبکه های استانی','جمع تفکیک شبکه های استانی']
    list_ostani2 = [a2,a21,a22,a23,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47  ,a49,a50,a51,a52,a53,a54,a55,a56,a57,a58,a_input,a_total]
    
    dic_ostani1={'لیست شبکه ها استانی' :list_ostani1,'تعداد سطرهای ثبت شده استانی':list_ostani2}

    check_list_ostani1 = pd.DataFrame(dic_ostani1)
    check_list_ostani1.to_excel(r"D:\python\EPG_vahid\Check_list\check_list_ostani.xlsx", index=False)


    df_ostani = [df2, df21, df22, df23 , df25, df26, df27, df28, df29, df30, df31, df32, df33,df34,df35,df36,df37,df38,df39,df40,df41,df42,df43,df44,df45,df46,df47   ,df49,df50,df51,df52,df53,df54,df55,df56,df57,df58]
    result_ostani = pd.concat(df_ostani)

    result_ostani = result_ostani.rename(columns = {"chan":"نام شبکه"})
    result_ostani.to_excel( 'result_merge_ostani.xlsx', index=False)

    a_merage=len(result_ostani.index)
    print ('تعداد سطرهای ادغام شده تفکیک شبکه های استانی',a_merage)
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
    # dfM28 = df48.rename(columns = {"chan":"نام شبکه"})
    dfM29 = df49.rename(columns = {"chan":"نام شبکه"})
    dfM30 = df50.rename(columns = {"chan":"نام شبکه"})
    dfM31 = df51.rename(columns = {"chan":"نام شبکه"})
    dfM32 = df52.rename(columns = {"chan":"نام شبکه"})
    dfM33 = df53.rename(columns = {"chan":"نام شبکه"})
    dfM34 = df54.rename(columns = {"chan":"نام شبکه"})
    dfM35 = df55.rename(columns = {"chan":"نام شبکه"})
    dfM36 = df56.rename(columns = {"chan":"نام شبکه"})
    dfM37 = df57.rename(columns = {"chan":"نام شبکه"})
    dfM38 = df58.rename(columns = {"chan":"نام شبکه"})
#    dfM39 = df59.rename(columns = {"chan":"نام شبکه"})
    
    
    
    #dfM23 = df33.rename(columns = {"chan":"نام شبکه"})



    print ('rename')
    print('ریختن توی فایل استانی به تفکیک شبکه ها')

    a= pd.DataFrame()

    my_list = [dfM1, dfM2, dfM3, dfM4, dfM5,dfM6, dfM7, dfM8, dfM9, dfM10, dfM11, dfM12,dfM13,dfM14,dfM15,dfM16,dfM17,dfM18,dfM19,dfM20,dfM21,dfM22, dfM23, dfM24, dfM25, dfM26, dfM27  ,dfM29, dfM30, dfM31,dfM32, dfM33, dfM34, dfM35, dfM36, dfM37, dfM38]

    print('write compeletly')

        
    for vahid_ostani in range(37):
    
        print("number of data frame", vahid_ostani)
    
        ch1= vahid_ostani + 1
        print("path_out", ch1)
        a=my_list[vahid_ostani]
#    print(a)
        path_out  =r'D:\python\EPG_vahid\progress\ostani\in\{}.xlsx'.format(ch1)
#    dfM1.to_excel( path_out, index=False)
#    b= 'ali'+'vahid'
#    a= dfM[ch]
#    print (b)
        a.to_excel( path_out, index=False)
        
    print('write compeletly')
        
    return ch1