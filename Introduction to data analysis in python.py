#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("desktop/google.csv")


# In[4]:


print(df.head())


# In[5]:


df=df[["Date","High","Low","Volume"]]


# In[6]:


print(df.head())


# In[22]:


df=df[["Date","High","Low"]]
print(df.head())


# In[23]:


df.plot.scatter(x='High', y='Low')


# In[ ]:





# In[ ]:





# In[ ]:





# In[9]:


df.plot.bar(x='Date', y='Volume')


# In[ ]:





# In[10]:


print(df.head())


# In[11]:


df=df[["Date","High","Low"]]


# In[12]:


print(df.head())


# In[16]:


df.plot.bar(x='Date', y='Low')


# In[28]:


df.plot.bar(x='Date', y='High')


# In[24]:


df.plot.line(x='Date', y='Low')


# In[25]:


df.plot.line(x='Date', y='High')


# In[27]:


df.plot.line(x='Date', y='Low')


# In[ ]:




