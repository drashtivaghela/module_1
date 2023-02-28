#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
cric_data=np.loadtxt("cric.tsv",skiprows=1)


# In[11]:


cric_data


# In[21]:


Sachin=cric_data[:,1]
Dravid=cric_data[:,2]
India=cric_data[:,3]


# In[22]:


def stats(x):
    a=np.mean(x)
    print("Mean:",a)
    b=np.median(x)
    print("Median:",b)


# In[23]:


stats(Sachin)


# In[24]:


stats(Dravid)


# In[25]:


stats(India)


# In[ ]:




