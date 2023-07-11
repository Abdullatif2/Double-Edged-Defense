#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 14:28:18 2022

@author: hadeerteryak
"""

import os
import numpy as np
import pandas as pd

directory = './IEC 104 dataset/ics-dataset-for-smart-grids 2/but-iec104-i'


def format(df):

    df['TimeStampOriginal']=df['TimeStamp']

    df['TimeStamp']=df['TimeStamp'].str.replace('.','')

    df['TimeStamp']=df['TimeStamp'].str.split(':',n=1)
    df['TimeStamp']=df['TimeStamp'].str.join('.')

    df['TimeStamp']=df['TimeStamp'].str.replace(':','')
    df['TimeStamp']=df['TimeStamp'].astype(float)
    df['Day']=df['Relative Time']/86400
    df['Day']=df['Day'].astype(int)
    df['label']=0
  

#Benign
f = os.path.join(directory,'normal-traffic.csv' )
df1=pd.read_csv(f,delimiter=';',encoding= 'unicode_escape')

format(df1)


#connection-loss 
f = os.path.join(directory,'connection-loss.csv' )
df2=pd.read_csv(f,delimiter=';',encoding= 'unicode_escape')

format(df2)

df2.loc[(df2['TimeStamp']>=16.2757) & (df2['TimeStamp']<=16.3748) ,'label']=1
df2.loc[(df2['TimeStamp']>=8.0801) & (df2['TimeStamp']<=9.0825),'label']=1


#dos-attack
f = os.path.join(directory,'dos-attack.csv' )
df3=pd.read_csv(f,delimiter=';',encoding= 'unicode_escape')
format(df3)

df3.loc[(df3['TimeStamp']>=23.5002) & (df3['TimeStamp']<=1.1829) ,'label']=2
df3.loc[(df3['TimeStamp']>=2.3005) & (df3['TimeStamp']<=4.0154) ,'label']=2


#switching-attack.csv
f = os.path.join(directory,'switching-attack.csv' )
df4=pd.read_csv(f,delimiter=';',encoding= 'unicode_escape')

format(df4)

df4.loc[(df4['TimeStamp']>=6.2700) & (df4['TimeStamp']<=6.3700) ,'label']=3


#scanning-attack.csv
f = os.path.join(directory,'scanning-attack.csv' )
df5=pd.read_csv(f,delimiter=';',encoding= 'unicode_escape')
format(df5)


df5.loc[(df5['TimeStamp']>=10.3200) & (df5['TimeStamp']<=10.4900) ,'label']=4
df5.loc[(df5['TimeStamp']>=1.0200) & (df5['TimeStamp']<=1.2300) ,'label']=4



#rogue-device
f = os.path.join(directory,'rogue-device.csv' )
df6=pd.read_csv(f,delimiter=';',encoding= 'unicode_escape')
format(df6)


df6.loc[(df6['TimeStamp']>=15.1900) & (df6['TimeStamp']<=15.4603) ,'label']=5


#injection-attack.csv
f = os.path.join(directory,'injection-attack.csv' )
df7=pd.read_csv(f,delimiter=';',encoding= 'unicode_escape')

format(df7)


df7.loc[(df7['TimeStamp']>=19.3519) & (df7['TimeStamp']<=19.4106) ,'label']=6
df7.loc[(df7['TimeStamp']>=21.0532) & (df7['TimeStamp']<=21.2114)  ,'label']=6





####################################################

directory = './IEC 104 dataset/ics-dataset-for-smart-grids 2/rts-iec104'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f) and f!=directory+"/Readme.txt" :
        print(f)
        df8=pd.read_csv(f,
                          delimiter=';',encoding= 'unicode_escape')
format(df8)  


data_With_ioa=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8])
data_With_ioa["TimeStamp"]=data_With_ioa['TimeStampOriginal']
data_With_ioa.drop(columns=data_With_ioa.columns[-2], axis=1, inplace=True)
data_With_ioa.drop(columns=data_With_ioa.columns[-2], axis=1, inplace=True)


data_With_ioa.to_csv('data_with_ioa.csv')





# ####################################################ISSUE: Ioa Column is missing 
 
directory = './IEC 104 dataset/ics-dataset-for-smart-grids 2/but-iec104-ii'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f) and f!=directory+"/Readme.txt" :
        print(f)
        df_0=pd.read_csv(f,
                          delimiter=';',encoding= 'unicode_escape')
        
df_0['label']=0
format(df_0)



# #####################################################

directory = './IEC 104 dataset/ics-dataset-for-smart-grids 2/vrt-iec104'

#Benign
f = os.path.join(directory,'HMI_Standard.csv' )
df_1=pd.read_csv(f,delimiter=';',encoding= 'unicode_escape')

format(df_1)

#HMI_MITM
f = os.path.join(directory,'HMI_MITM.csv' )
df_2=pd.read_csv(f,delimiter=';',encoding= 'unicode_escape')
format(df_2)


df_2.loc[(df_2['TimeStamp']>=20.2304) & (df_2['TimeStamp']<=21.3134)& (df_2['Day']==0) ,'label']=7
df_2.loc[(df_2['TimeStamp']>=5.2945) & (df_2['TimeStamp']<=6.5215) & (df_2['Day']==0) ,'label']=7
df_2.loc[(df_2['TimeStamp']>=22.1519) & (df_2['TimeStamp']<=2.3809)& (df_2['Day']==2)  ,'label']=7



#replay-HMI.csv
f = os.path.join(directory,'replay_HMI.csv')
df_3=pd.read_csv(f,delimiter=';',encoding= 'unicode_escape')
format(df_3)


df_3.loc[(df_3['TimeStamp']>=7.3853) & (df_3['TimeStamp']<=7.5950) & (df_3['Day']==0),'label']=8
df_3.loc[(df_3['TimeStamp']>=7.5951) & (df_3['TimeStamp']<=8.4953) & (df_3['Day']==1),'label']=8


#report-block-HMI.csv

f = os.path.join(directory,'report_block_HMI.csv')
df_4=pd.read_csv(f,delimiter=';',encoding= 'unicode_escape')
format(df_4)


df_4.loc[(df_4['TimeStamp']>=23.3552) & (df_4['TimeStamp']<=1.4732) & (df_4['Day']==0),'label']=9

#value-change-HMI.csv

f = os.path.join(directory,'value_change_HMI.csv')
df_5=pd.read_csv(f,delimiter=';',encoding= 'unicode_escape')
format(df_5)


df_5.loc[(df_5['TimeStamp']>=7.2221) & (df_5['TimeStamp']<=9.0301) & (df_5['Day']==0),'label']=10
df_5.loc[(df_5['TimeStamp']>=20.5623) & (df_5['TimeStamp']<=21.0130) & (df_5['Day']==0),'label']=10
df_5.loc[(df_5['TimeStamp']>=21.0131) & (df_5['TimeStamp']<=22.4433) & (df_5['Day']==1),'label']=10





#Masquerating_HMI
f = os.path.join(directory,'masquerating_HMI.csv')
df_6=pd.read_csv(f,delimiter=';',encoding= 'unicode_escape')
format(df_6)


df_6.loc[(df_6['TimeStamp']>=14.1514) & (df_6['TimeStamp']<=19.1115) & (df_6['Day']==0),'label']=11



data_Without_ioa=pd.concat([df_0,df_1,df_2,df_3,df_4,df_5,df_6])
data_Without_ioa["TimeStamp"]=data_Without_ioa['TimeStampOriginal']
data_Without_ioa.drop(columns=data_Without_ioa.columns[-2], axis=1, inplace=True)
data_Without_ioa.drop(columns=data_Without_ioa.columns[-2], axis=1, inplace=True)



data_Without_ioa.to_csv('data_without_ioa.csv')



# ####################################################
# # directory = './IEC 104 dataset/ics-dataset-for-smart-grids/encs-iec104'

# # f = os.path.join(directory, filename)
# # df9=pd.read_csv(f, delimiter=',',encoding= 'unicode_escape')
        
# # df9['label']=0

# # df9['TimeStamp']=df9['TimeStamp'].astype(float)

# # df9.loc[(df9['TimeStamp']>=1475.19) & (df7['TimeStamp']<=1941.06) ,'label']=8

# # df9.loc[(df9['TimeStamp']>=2105.32) & (df7['TimeStamp']<=2121.14) ,'label']=6











