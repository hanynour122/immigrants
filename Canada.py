#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_excel(r"C:\Users\Hany\Downloads\Canada.xlsx", sheet_name= "Canada by Citizenship (2)")


# In[4]:


df=df.drop(["Type","Coverage","AREA","REG","DEV"],axis=1)


# In[5]:


df.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True)


# In[6]:


df.columns = list(map(str, df.columns))


# In[7]:


df.head()


# In[8]:


df["total"]=df.sum(axis=1)
df.head()


# In[9]:


years=list(map(str,range(1980,2014)))


# In[10]:


df=df.set_index("Country")


# In[11]:


df_5=df.head()
df_5=df_5[years].transpose()


# In[12]:


df_5.plot(kind='area',
             stacked=False,
             figsize=(20, 10))  # pass a tuple (x, y) size

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()


# In[13]:


df_5.plot(kind='area', 
             alpha=0.25,  # 0 - 1, default value alpha = 0.5
             stacked=False,
             figsize=(20, 10))

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()


# In[14]:


haiti = df.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
haiti.head()


# In[27]:


haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show()


# In[16]:


df_t = df.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
df_t.head()


# In[17]:


# generate histogram
df_t.plot(kind='hist', figsize=(10, 6))

plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

plt.show()


# In[18]:


df_iceland = df.loc['Iceland', years].transpose()
df_iceland.head()


# In[19]:


df_iceland.plot(kind='bar', figsize=(10, 6))

plt.xlabel('Year') # add to x-label to the plot
plt.ylabel('Number of immigrants') # add y-label to the plot
plt.title('Icelandic immigrants to Canada from 1980 to 2013') # add title to the plot

plt.show()


# In[20]:


df_Continent=df.groupby("Continent").sum()
df_Continent


# In[21]:


df_Continent["total"].plot(kind="pie")
plt.title("total of imma from 1980 to 2013")
plt.show()


# In[ ]:





# In[22]:


df_japan=df.loc["Japan",years].transpose()


# In[23]:


df_japan.plot(kind="box")
plt.title("number of immig from japan to canda form 1980 to 2013")
plt.ylabel("number of immig")
plt.show()
df_japan.plot(kind='box', figsize=(10, 7), color='blue', vert=False)

plt.title('Box plots of Immigrants from China and India (1980 - 2013)')
plt.xlabel('Number of Immigrants')

plt.show()


# In[24]:


df_tot = pd.DataFrame(df[years].sum(axis=0))
df_tot.index = map(int, df_tot.index)
df_tot.reset_index(inplace = True)
df_tot.columns = ['year', 'total']
df_tot.head()


# In[25]:


df_tot.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')

plt.title('Total Immigration to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')

plt.show()


# In[26]:


sns.regplot(x="year",y="total",data=df_tot)


# In[ ]:





# In[ ]:





# In[ ]:




