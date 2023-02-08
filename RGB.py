#!/usr/bin/env python
# coding: utf-8

# In[2]:


import skimage.io as io


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


import numpy as np


# In[5]:


img=io.imread('1.jpg')


# In[6]:


plt.imshow(img)


# In[7]:


img.shape


# In[8]:


# split
red=img[:,:,0]
green=img[:,:,1]
blue=img[:,:,2]


# In[9]:


plt.imshow(red,cmap="Reds")


# In[10]:


plt.imshow(blue,cmap="Blues")


# In[11]:


plt.imshow(green,cmap="Greens")


# In[ ]:





# In[ ]:




