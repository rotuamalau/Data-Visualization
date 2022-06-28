#!/usr/bin/env python
# coding: utf-8

# In[174]:


import numpy as np
import pandas as pd

get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib as plt


# In[175]:


# Read data

df = pd.read_csv('D:\Hacktiv8\london_crime_by_lsoa.csv') 


# In[176]:


#Show data atas

df.head()


# In[177]:


#Show data bawah

df.tail()


# In[178]:


#Show info dataframe

df.info


# In[179]:


#Show baris dan kolom dataframe

df.shape


# In[180]:


#show columns dataframe
df.columns.values


# In[181]:


#Show major_category

df['major_category']


# In[182]:


#rename columns value menjadi columns total

df.rename(columns={'value':'total'}, inplace=True)
df.columns


# In[183]:


#Filter dari tahun 2011 - 2016

df_filter = df[df.year > 2010]
df_filter


# In[184]:


#Membuat pivot table untuk major_category & year

summary = df_filter.pivot_table('total',index=['major_category'], columns='year', aggfunc = {'total' : 'sum'})
summary.head()


# In[185]:


#Membuat columns Total untuk melihat trend dari index major_category setiap tahunnya

summary['Total'] = summary.sum(axis=1)
summary.head()


# In[186]:


#Mengurutkan kejahatan yang jumlahnya tertinggi hingga terendah dari tahun 2011-2016

summary.sort_values(by='Total', ascending=False, axis=0, inplace = True)
summary


# In[187]:


#Mengambil 5 kejahatan yang tertinggi dari tahun 2011-2016

crime_top5 = summary.head(5)
crime_top5


# In[188]:


import matplotlib as mpl
import matplotlib.pyplot as plt


# In[189]:


#Membuat grafik line dari 5 kejahatan tertinggi dari tahun 2011-2016

crime_top5.drop('Total', axis=1, inplace=True)
crime_top5.plot(kind='line', figsize=(20, 10))

plt.title('Top 5 Criminal in London')
plt.ylabel('Number of crime')
plt.xlabel('Category')

plt.show()


# In[190]:


df_crime = crime_top5.transpose()


# In[191]:


#Membuat grafik line dari 5 kejahatan tertinggi dari tahun 2011-2016 dimana x = major_category, y = jumlah kejahatan

df_crime.plot(kind='line', figsize=(20, 10))

plt.title('Top 5 Crimes in London')
plt.ylabel('Number of crimes')
plt.xlabel('Category')

plt.show()


# In[192]:


#Membuat grafik area dari 5 kejahatan tertinggi dari tahun 2011-2016

df_crime.index = df_crime.index.map(int)

df_crime.plot(kind='area', 
             stacked=False,
              alpha=0.25,
             figsize=(20, 10),
             )

plt.title('Top 5 Crimes in London')
plt.ylabel('Number of crimes')
plt.xlabel('Category')

plt.show()


# In[193]:


crime_least5 = summary.tail(5)
crime_least5


# In[194]:


#df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
crime_least5.drop('Total', axis=1, inplace=True)
crime_least5.plot(kind='line', figsize=(20, 10))

plt.title('Least 5 Criminal in London')
plt.ylabel('Number of crime')
plt.xlabel('Category')

plt.show()


# In[195]:


df_least5 = crime_least5.transpose()
df_least5


# In[196]:


df_least5.index = df_crime.index.map(int) # let's change the index values of df_top5 to type integer for plotting

df_least5.plot(kind='area', 
             stacked=False,
              alpha=0.25,
             figsize=(20, 10), # pass a tuple (x, y) size
             )

plt.title('Least 5 Crimes in London')
plt.ylabel('Number of crimes')
plt.xlabel('Category')

plt.show()


# In[197]:


#df_can.loc[['Denmark', 'Norway', 'Sweden'], years]
summary.columns.values


# In[198]:


summary


# In[199]:


new_summary = summary.transpose()
new_summary


# In[ ]:


top_crime = 


# In[ ]:


theft_and_handling = df[df['major_category'].isin(['Theft and Handling'])]
theft_and_handling


# In[ ]:


theft_and_handling_borough = df.groupby('borough')
theft_and_handling_borough


# In[ ]:


theft_and_handling_crime = df.groupby(['borough','year'])['total'].sum().reset_index()
theft_handling = theft_and_handling_crime[theft_and_handling_crime.year > 2015]

theft_handling


# In[ ]:


theft_and_handling_summary = theft_handling.reset_index().pivot(columns='year', index='borough', values='total')
theft_and_handling_summary


# In[201]:


theft_and_handling_summary.sort_values(by=2016, ascending=False, axis=0, inplace=True)


# In[202]:


theft_and_handling_summary


# In[203]:


top_borough_theft_handling = theft_and_handling_summary.head(5)
top_borough_theft_handling


# In[124]:


top_borough_theft_handling.plot(kind='bar')


# In[149]:


df[df.year > 2015]
crime_borough = df.groupby(['borough','major_category'])['total'].sum().reset_index()
crime_borough


# In[150]:


crime_borough.sort_values(by='total', ascending=False, axis=0, inplace=True)
crime_borough


# In[128]:


top5crime_borough = crime_borough.head(5)
top5crime_borough


# In[145]:


top5crime_borough.index.values


# In[158]:


top5crime_borough['total'].plot(kind='pie',
                            figsize=(10, 6),
                            autopct='%1.1f%%', # add in percentages
                            startangle=90,     # start angle 90° (Africa)
                            shadow=True,       # add shadow      
                            )

plt.title('5 Top Borough by Theft and Handling Crime in 2016')
plt.axis('equal') # Sets the pie chart to look like a circle.
plt.legend(labels=top5crime_borough['borough'], loc='upper right')
plt.show()


# In[152]:


colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']

top5crime_borough['total'].plot(kind='pie',
                            figsize=(15, 6),
                            autopct='%1.1f%%', 
                            startangle=90,    
                            shadow=True,       
                            labels=None,         
                            pctdistance=1.12,    
                            colors=colors_list, 
                            )

plt.title('5 Top Borough by Theft and Handling Crime in 2016', y=1.12) 

plt.axis('equal') 

plt.legend(labels=top5crime_borough['borough'], loc='upper left') 

plt.show()


# In[161]:


get_ipython().system('pip install folium')
import folium


# In[204]:


world_map = folium.Map()
world_map


# In[205]:


london = folium.Map(location=[51.509865,-0.118092], zoom_start=8)

# display world map
london


# In[ ]:




