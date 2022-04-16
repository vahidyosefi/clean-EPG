# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:05:03 2021

@author: vahid
function change the name and cloumn
"""

def func_change_v2 (i_radio,i_bronmarzi,i_ostani,i_ekhtesasi,i_sarasari):
    
    # import pandas as pd
    import numpy as np
    
    """
    part 1 modify radio
    part 2 modify ostani
    part 2 modify ekhtesasi
    part 2 modify sarasari
    change the header 
    change the program name
    change the comeback header
    """
#    i_radio.to_excel('radio.xlsx',index=False)
    del i_radio['نام برنامه اولیه']
    o_radio = i_radio
#    o_radio.to_excel('radio_del.xlsx',index=False)
    o_radio = o_radio.rename(columns={'نببت':'نام برنامه اولیه'})
#    o_radio.to_excel('radio_name.xlsx',index=False)
    
    o_radio = o_radio[['نام شبکه','نام برنامه اولیه','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','اپراتور','ساعت','تاریخ','ردیف','جنس','tag','نوع']]
    o_radio.to_excel(r'D:\python\EPG_vahid\progress\merge\modify_merge\radio.xlsx',index=False)

############# part 2 ostani        
    del i_ostani['نام برنامه اولیه']
    i_ostani = i_ostani.rename(columns={'نببت':'نام برنامه اولیه'})
    i_ostani = i_ostani[['نام شبکه','نام برنامه اولیه','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','اپراتور','ساعت','تاریخ','ردیف','جنس','tag','نوع']]
    i_ostani.to_excel(r'D:\python\EPG_vahid\progress\merge\modify_merge\ostani.xlsx',index=False)
    

############# part 3 ekhtesasi    
    del i_ekhtesasi['نام برنامه اولیه']
    i_ekhtesasi = i_ekhtesasi.rename(columns={'نببت':'نام برنامه اولیه'})
    i_ekhtesasi = i_ekhtesasi[['نام شبکه','نام برنامه اولیه','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','اپراتور','ساعت','تاریخ','ردیف','جنس','tag','نوع']]
    i_ekhtesasi.to_excel(r'D:\python\EPG_vahid\progress\merge\modify_merge\ekhtesasi.xlsx',index=False)


############# part 4 bronmarzi    
    del i_bronmarzi['نام برنامه اولیه']
    i_bronmarzi = i_bronmarzi.rename(columns={'نببت':'نام برنامه اولیه'})
    i_bronmarzi = i_bronmarzi[['نام شبکه','نام برنامه اولیه','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','اپراتور','ساعت','تاریخ','ردیف','جنس','tag','نوع']]
    i_bronmarzi.to_excel(r'D:\python\EPG_vahid\progress\merge\modify_merge\bronmarzi.xlsx',index=False)


############# part 5 sarasari


#####rename hedaer    
    i_sarasari = i_sarasari.rename(columns={'نام برنامه اولیه': 'Name'})
    i_sarasari = i_sarasari.rename(columns={'نام برنامه': 'modify'}) 
#####change the program name

    i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('خبر ۱۰', regex=False), i_sarasari.Name, i_sarasari.modify) 
    i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('خبر ۱۱', regex=False), i_sarasari.Name, i_sarasari.modify)
    i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('خبر ۱۲', regex=False), i_sarasari.Name, i_sarasari.modify)
    i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('خبر ۱۳', regex=False), i_sarasari.Name, i_sarasari.modify)
    i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('خبر ۱۴', regex=False), i_sarasari.Name, i_sarasari.modify) 
    
    # i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('خبر ۲۲', regex=False), i_sarasari.Name, i_sarasari.modify)
    i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('خبر ۱۵', regex=False), i_sarasari.Name, i_sarasari.modify)
    i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('خبر ۱۶', regex=False), i_sarasari.Name, i_sarasari.modify) 
    i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('خبر ۱۷', regex=False), i_sarasari.Name, i_sarasari.modify)                          
    i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('خبر ۱۸', regex=False), i_sarasari.Name, i_sarasari.modify)
    i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('خبر ۱۹', regex=False), i_sarasari.Name, i_sarasari.modify) 
    i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('خبر ۲۰', regex=False), i_sarasari.Name, i_sarasari.modify) 
    i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('خبر ۲۱', regex=False), i_sarasari.Name, i_sarasari.modify) 
    i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('خبر ۲۲', regex=False), i_sarasari.Name, i_sarasari.modify) 
    i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('خبر ۲۳', regex=False), i_sarasari.Name, i_sarasari.modify) 
    i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('اخبار ۲۰:۳۰', regex=False), i_sarasari.Name, i_sarasari.modify) 
    i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('تلاوت برگزیده', regex=False), i_sarasari.Name, i_sarasari.modify) 
    # i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('تلاوت برگزیده', regex=False), i_sarasari.Name, i_sarasari.modify) 
    
    
    # i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('', regex=False), i_sarasari.Name, i_sarasari.modify) 
    # i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('', regex=False), i_sarasari.Name, i_sarasari.modify) 
    
    # i_sarasari['modify'] = np.where(i_sarasari.Name.str.contains('', regex=False), i_sarasari.Name, i_sarasari.modify) 
    



    # i_sarasari['نام برنامه'] = i_sarasari['نام برنامه اولیه'].replace({'خبر ۲۰':'خبر ۲۰:۰۰'})
#input_sarasari['نام برنامه'] = input_sarasari['نام برنامه اولیه'].replace({'خبر ۱۶':'خبر ۱۶'})



####remove the program
    i_sarasari['Name'] = i_sarasari['Name'].astype(str)
    i_sarasari = i_sarasari[~i_sarasari['Name'].str.contains('گل ها و لحظات حساس فوتبال')]
    i_sarasari = i_sarasari[~i_sarasari['Name'].str.contains('گلها و لحظات حساس لیگ اروپا')]


   
####change the comeback header
    i_sarasari = i_sarasari.rename(columns={'نام برنامه اولیه': 'Name'})
    
    i_sarasari = i_sarasari.rename(columns={'modify':'نام برنامه'}) 
    
    # i_sarasari = i_sarasari.rename(columns={'Name': 'نام برنامه اولیه'})
    
    # del i_sarasari['Name']
    i_sarasari = i_sarasari.rename(columns={'نببت':'نام برنامه اولیه'})
    i_sarasari = i_sarasari[['نام شبکه','نام برنامه اولیه','نام برنامه','تاریخ شروع','تاریخ پایان','مدت بازدید','تعداد بازدید','میانگین','اپراتور','ساعت','تاریخ','ردیف','جنس','tag','نوع']]
    i_sarasari.to_excel(r'D:\python\EPG_vahid\progress\merge\modify_merge\sarasari.xlsx',index=False)

    
    
    
    o_bronmarzi = i_bronmarzi
    o_ostani = i_ostani
    o_ekhtesasi = i_ekhtesasi
    o_sarasari =  i_sarasari   
    
    
    
    
    
    
    
    return o_radio, o_bronmarzi, o_ostani, o_ekhtesasi, o_sarasari