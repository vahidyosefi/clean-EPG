# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:24:04 2020

@author: PC
"""


def Func_Mekanizeh_ekhtesasi (input0):
    import pandas as pd

    df_ghair= pd.DataFrame()

    df0= input0
#df1= input1
#    sample_input = input0
    df0.reset_index()
#df1.reset_index()
    print("input success")

    a_input0=len(input0.index)

    print ('تعداد سطرهای کل شبکه های اختصاصی',a_input0)
    
    df0.to_excel( 'test.xlsx', index=False)

    df0 = df0[['نام شبکه','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','اپراتور','ساعت','تاریخ','ردیف','جنس','نببت']]


    df0['نام شبکه'] = df0['نام شبکه'].replace({'تیوا 1': 'تیوا یک'})

    df0['نام شبکه'] = df0['نام شبکه'].replace({'تیوا محفل': 'محفل'})

    df0['نام شبکه'] = df0['نام شبکه'].replace({'نوا': 'کنسرت'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'نسیم وصل': 'کنسرت'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'شبکه آرا': 'آرا'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'کیپاد': 'آرپا'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'کیپاد': 'شبکه آرپا'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'آرپا': 'کیپاد'})
    
    df0['نام شبکه'] = df0['نام شبکه'].replace({'لنزاسپورت پلاس': 'لنز اسپورت پلاس'})
    
    
    

####        -------  select chanel 

    df0 = df0.rename(columns = {"نام شبکه":"chan"})
    df0 = df0.drop([], axis=1)
    df0.reset_index()

    df0['chan'] = df0['chan'].str.strip()

    df2=df0.query("chan == 'تیوا اسپورت یک'")
    print()
#df21 = df0[df0['chan'].str.contains('رادیو آوا')]
#df211=df0.query("chan == 'رادیو اوا'")
    df21=df0.query("chan == 'تیوا اسپورت دو'")
    #df21=df21.append(df211)

    df22=df0.query("chan == 'لنز فیلم'")
    df23=df0.query("chan == 'تیوا دو'")
    #df24=df0.query(" chan == 'شبکه 4'")
    df25=df0.query(" chan == 'حرم رضوی'")
    df26=df0.query(" chan == 'تیوا کودک'")
    df27=df0.query(" chan == 'محفل'")
    df28=df0.query(" chan == 'رهرو'")
    df29=df0.query(" chan == 'سرباز ماهر'")
    df30=df0.query(" chan == 'شاپرک'")
    df31=df0.query(" chan == 'کودک دیجیتون'")
    df32=df0.query(" chan == 'لنز اسپورت پلاس'")
    # df32=df0.query(" chan == 'لنزاسپورت پلاس'")
    
    
    
    df33=df0.query(" chan == 'لنزاسپورت'")
    df34=df0.query(" chan == 'تیوا یک'")
    df35 = df0[df0['chan'].str.contains('لنز اسپورت 2')]
    df36 = df0[df0['chan'].str.contains('کنسرت')]

    df37=df0.query(" chan == 'تیوا'")
    df38=df0.query(" chan == 'شتاب'")
    df39=df0.query(" chan == 'آیواسپرت'")
    df40=df0.query(" chan == 'استقلال'")
    df41=df0.query(" chan == 'تیوا آوند'")
    df42=df0.query(" chan == 'تیوا فیلم'")
    df43=df0.query(" chan == 'تیوا بورس'")

    df44=df0.query(" chan == 'جشنواره فیلم فجر'")
    df45=df0.query(" chan == 'تیوا نوا'")

    df46=df0.query(" chan == 'آیو جهان‌بین'")
    df47=df0.query(" chan == 'آیوتون'")
    df48=df0.query(" chan == 'بورسان'")
    df49=df0.query(" chan == 'سپاهان‌ تی‌وی'")
    df50=df0.query(" chan == 'دُرفا'")
    df51=df0.query(" chan == 'مس رفسنجان'")
    df52=df0.query(" chan == 'امروز'")
    df53=df0.query(" chan == 'کیپاد'")
    df54=df0.query(" chan == 'اشاره'")
    df55=df0.query(" chan == 'آستان قدس رضوی'")
    df56=df0.query(" chan == 'اکو پارس'")
    df57=df0.query(" chan == 'آرا'")
    df58=df0.query(" chan == 'ایران اکونومی'")
    
    
    df59=df0.query(" chan == 'نما'")
    df60=df0.query(" chan == 'جوانه'")
    df61=df0.query(" chan == 'جام'")
    df62=df0.query(" chan == 'حبیب'")
    df63=df0.query(" chan == 'لبیک'")



    frames0 = [df2, df21, df22, df23 , df25, df26, df27, df28, df29, df30, df31, df32, df33,df34,df35,df36,df37,df38,df39,df40,df41,df42,df43,df44,df45,df46,df47,df48,df49,df50,df51,df52,df53,df54,df55,df56,df57,df58,df59,df60,df61,df62,df63]
    adgham = pd.concat(frames0)

#df_ghair != adgham

    df_ghair_1 = pd.concat([df0, adgham])

    df_ghair = df_ghair_1.drop_duplicates(keep=False)


#    df_ghair.to_excel('رویدادی', index=False)
#print ('تیوا اسپورت',df_ghair)

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
    a46 = len(df46.index)
    a47 = len(df47.index)
    a48 = len(df48.index)
    a49 = len(df49.index)
    a50 = len(df50.index)
    a51 = len(df51.index)
    a52 = len(df52.index)
    a53 = len(df53.index)
    a54 = len(df54.index)
    a55 = len(df55.index)
    a56 = len(df56.index)
    a57 = len(df57.index)
    a58 = len(df58.index)
    a59 = len(df59.index)
    a60 = len(df60.index)
    a61 = len(df61.index)
    a62 = len(df62.index)
    a63 = len(df63.index)
    
    
    a_df_ghair=len(df_ghair.index)

    a_total_1= a2+a21+a22+a23+a25+a26+a27+a28+a29+a30+a31+a32+a33
    a_total_2= a34+a35+a36+a37+a38+a39+a40+a41+a42+a43+a44+a45+a46+a47+a48+a49
    a_total_3 = a50+a51+a52+a53+a54+a55+a56+a57+a58+a59+a60+a61+a62 + a63
    a_total= a_total_1 + a_total_2 + a_total_3
    a_total_a_df_ghair= a_total +a_df_ghair
    a_ekhtelaf =  a_input - a_total

    print ('تیوا اسپورت یک',a2)
    print ('تیوا اسپورت دو',a21)
    print ('لنز فیلم',a22)
    print ('تیوا دو',a23)
    print ('حرم رضوی',a25)
    print ('تیوا کودک',a26)
    print ('محفل',a27)
    print ('رهرو',a28)
    print ('سرباز ماهر',a29)
    print ('شاپرک',a30)
    print ('کودک دیجیتون',a31)
    print ('لنز اسپورت پلاس',a32)
    print ('لنزاسپورت',a33)
    print ('تیوا یک',a34)
    print ('لنز اسپورت 2',a35)
    print ('کنسرت',a36)
    print ('تیوا',a37)
    print ('شتاب',a38)
    print ('آیواسپرت',a39)
    print ('استقلال',a40)
    print ('تیوا آوند',a41)
    print ('تیوا فیلم',a42)
    print ('تیوا بورس',a43)
    print ('جشنواره فیلم فجر',a44)
    print ('تیوا نوا',a45)
    
    print ('آیو جهان بین',a46)
    print ('آیوتون',a47)
    print ('بورسان',a48)
    print ('سپاهان‌ تی‌وی',a49)
    print ('دُرفا',a50)
    print ('مس رفسنجان',a51)
    print ('امروز',a52)
    print ('کیپاد',a53)
    print ('اشاره',a54)
    print ('آستان قدس رضوی',a55)
    print ('اکو پارس',a56)
    print ('آرا',a57)
    print ('ایران اکونومی',a58)
    print ('نما',a59)
    print ('جوانه',a60)
    print ('جام',a61)
    print ('حبیب',a62)
    print ('لبیک',a63)
    
    
    
    
    
    
    print ('مابقی مانده ها',a_df_ghair)
    print ('اختلاف ورودی اختصاصی با  تجمیع ریاضی شبکه ها',a_ekhtelaf)
    
    print(' تعداد سطرهای شبکه های اختصاصی ورودی',a_input)
    print ('جمع ریاضی تفکیک سطرهای شبکه های اختصاصی',a_total)
    print ('جمع ریاضی تفکیک سطرهای شبکه های اختصاصی و مابقی مانده ها',a_total_a_df_ghair)
    
    list_ekhtesasi = ['تیوا اسپورت یک','تیوا اسپورت2','لنز فیلم','تیوا دو','حرم رضوی','تیوا کودک','محفل','رهرو','سرباز ماهر','شاپرک','کودک دیجیتون','لنز اسپورت پلاس','لنز اسپورت','تیوا یک','لنز اسپورت 2','کنسرت','تیوا','شتاب','آیواسپرت','استقلال','تیوا آوند','تیوا فیلم','تیوا بورس','جشنواره فیلم فجر','تیوا نوا','آیو جهان بین','آیوتون','بورسان','سپاهان‌ تی‌وی','دُرفا','مس رفسنجان','امروز','کیپاد','اشاره','آستان قدس رضوی','اکو پارس','آرا','ایران اکونومی','نما','جوانه','جام','حبیب','لبیک','مابقی مانده ها','اختلاف ورودی اختصاصی با  تجمیع ریاضی شبکه ها','تعداد سطرهای شبکه های اختصاصی ورودی','جمع ریاضی تفکیک سطرهای شبکه های اختصاصی','جمع ریاضی تفکیک سطرهای شبکه های اختصاصی و مابقی مانده ها']
    list_ekhtesasi2 = [a2,a21,a22,a23,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,a51,a52,a53,a54,a55,a56,a57,a58,a59,a60,a61,a62,a63,a_df_ghair,a_ekhtelaf,a_input,a_total,a_total_a_df_ghair]
    
    dic_ekhtesasi={'لیست شبکه ها' :list_ekhtesasi,'تعداد سطرهای ثبت شده':list_ekhtesasi2}

    check_list_ekhtesasi = pd.DataFrame(dic_ekhtesasi)
    check_list_ekhtesasi.to_excel(r"D:\python\EPG_vahid\Check_list\check_list_ekhtesasi.xlsx", index=False)


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

#dfM16 = df_remain_5.rename(columns = {"chan":"نام شبکه"})
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
    dfM31 = df51.rename(columns = {"chan":"نام شبکه"})
    dfM32 = df52.rename(columns = {"chan":"نام شبکه"})
    dfM33 = df53.rename(columns = {"chan":"نام شبکه"})
    dfM34 = df54.rename(columns = {"chan":"نام شبکه"})
    dfM35 = df55.rename(columns = {"chan":"نام شبکه"})
    dfM36 = df56.rename(columns = {"chan":"نام شبکه"})
    dfM37 = df57.rename(columns = {"chan":"نام شبکه"})
    dfM38 = df58.rename(columns = {"chan":"نام شبکه"})
    dfM39 = df59.rename(columns = {"chan":"نام شبکه"})
    dfM40 = df60.rename(columns = {"chan":"نام شبکه"})
    dfM41 = df61.rename(columns = {"chan":"نام شبکه"})
    dfM42 = df62.rename(columns = {"chan":"نام شبکه"})
    dfM43 = df63.rename(columns = {"chan":"نام شبکه"})
    # dfM26 = df_remain_13.rename(columns = {"chan":"نام شبکه"})

#### for remain ektesasi
    dfM44 =df_ghair
    dfM44 = dfM44.rename(columns = {"chan":"نام شبکه"})

    dfM44 = dfM44.rename(columns = {"نام برنامه":"نام برنامه اولیه"})
    
    dfM44['نام برنامه'] = ''
    dfM44 = dfM44[['نام شبکه','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','اپراتور','ساعت','تاریخ','ردیف','جنس','نببت']]


    print ('rename')
    print('ریختن توی فایل اختصاصی به تفکیک شبکه ها')

    a= pd.DataFrame()

    my_list = [dfM1, dfM2, dfM3, dfM4, dfM5,dfM6, dfM7, dfM8, dfM9, dfM10, dfM11, dfM12,dfM13,dfM14,dfM15,dfM16,dfM17,dfM18,dfM19,dfM20,dfM21,dfM22,dfM23,dfM24,dfM25,dfM26,dfM27,dfM28,dfM29,dfM30,dfM31,dfM32,dfM33,dfM34,dfM35,dfM36,dfM37,dfM38,dfM39,dfM40,dfM41,dfM42,dfM43,dfM44]
    print('write compeletly')


    for vahid_ekhtesasi in range(44):
    
        print("number of data frame", vahid_ekhtesasi)
    
        ch_ekhtesasi= vahid_ekhtesasi + 1
        print("path_out", ch_ekhtesasi)
        a=my_list[vahid_ekhtesasi]

        path_out  =r'D:\python\EPG_vahid\progress\ekhtesasi\in\{}.xlsx'.format(ch_ekhtesasi)

        a.to_excel( path_out, index=False)
        
       
    print('write compeletly_ekhtesasi')
        
    return ch_ekhtesasi