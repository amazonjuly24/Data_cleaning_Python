
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df=pd.read_csv("/home/manjula/python/cleaning/movie_metadata.csv")


# In[4]:


df.head()


# In[5]:


df.color.describe()


# In[6]:


#to select a coloumn
df['color']


# In[7]:


df['duration'][:10]


# In[8]:


df['duration']>120


# In[11]:


df['country']


# In[17]:


#Add default values
df.country=df.country.fillna('')


# In[18]:


df.country.head(10)


# In[19]:


df.duration=df.duration.fillna(df.duration.mean())


# In[20]:


df.duration.head(10)


# In[21]:


#drop all rows with NAN values
df.dropna()
#df.dropna(how='all')


# In[22]:


#Set threshold to drop rows
df.dropna(thresh=5)


# In[23]:


df.shape


# In[25]:


df.dropna(subset=['title_year'])


# In[33]:


df.drop=df.dropna(axis=1, how='any')


# In[34]:


df.drop.shape


# In[43]:


#normalize data types
df=pd.read_csv("/home/manjula/python/cleaning/movie_metadata.csv",dtype={'duration':float})


# In[44]:


df=pd.read_csv("/home/manjula/python/cleaning/movie_metadata.csv",dtype={'country':str})


# In[45]:


df['director_name'].str.upper()


# In[49]:


df['movie_title'].str.strip()


# In[50]:


#Rename columns
df.rename(columns={'movie_facebook_likes':'fb_likes'})


# In[54]:


#SAVING THE FILE BACK TO CSV
df.to_csv(‘/home/manjula/python/cleaning/cleanmoviefile.csv’ encoding=’utf-8’)

