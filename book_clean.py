
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


df=pd.read_csv('/home/manjula/python/cleaning/Datasets/Book.csv')
print( df.shape)
print(df.head())


# In[4]:


to_drop= ['Edition Statement',
           'Corporate Author',
            'Corporate Contributors',
            'Former owner',
            'Engraver',
            'Contributors',
            'Issuance type',
            'Shelfmarks']


# In[5]:


df.drop(to_drop,inplace=True,axis=1)


# In[7]:


print (df.shape)

print (df.head())


# In[8]:


df.set_index('Identifier')


# In[10]:


df.loc[206]


# In[11]:


df.loc[472]


# In[12]:


df.iloc[0]


# In[13]:


df.get_dtype_counts()


# In[20]:


df.loc[206:, 'Date of Publication'].head(10)


# In[21]:


regex = r'^(\d{4})'


# In[22]:


extr=df['Date of Publication'].str.extract(r'^(\d{4})',expand=False)


# In[25]:


extr.head(10)


# In[26]:


df['Date of publication']=pd.to_numeric(extr)


# In[27]:


df['Date of publication'].dtype


# In[28]:


len(df)


# In[29]:


df['Date of publication'].isnull().sum


# In[31]:


df['Date of publication'].isnull().sum()/len(df)


# In[32]:


df.head()


# In[33]:


df.loc[216
      ]


# In[34]:


df.loc[472]


# In[ ]:


df.head(20)


# In[37]:


df.iloc[8
       ]


# In[39]:


df.iloc[9]


# In[41]:


pub=df['Place of Publication']


# In[42]:


london=pub.str.contains('London')


# In[45]:


london[:10]


# In[46]:


oxford=pub.str.contains('Oxford')
oxford[:10]


# In[61]:


df['Place of Publication'] = np.where(london, 'London',
                                      np.where(oxford, 'Oxford',
                                               pub.str.replace('-', ' ')))                                     
#this problem arises with python 3.5 and belower version


# In[62]:


df['Place of Publication'].head()

