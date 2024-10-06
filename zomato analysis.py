#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


dataframe = pd.read_csv("Zomato data .csv")
print(dataframe.head())


# In[3]:


def handleRate(value):
	value=str(value).split('/')
	value=value[0];
	return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())


# In[4]:


dataframe.info()


# In[92]:


#subplot
fig, axs = plt.subplots(2, 2, figsize=(14, 12))
#plot1
sns.countplot(x=dataframe['listed_in(type)'],ax=axs[0, 0],color="#C62440")
plt.xlabel("Type of restaurant")
axs[0, 0].set_title('Types of restrant and its count',color="#C62440",size=20)
axs[0,0].set_facecolor('#1E1A1A')
#plot3
sns.countplot(x=dataframe['online_order'],ax=axs[1,0],color="#C62440")
axs[1, 0].set_title('online order preference',color="#C62440",size=20)
axs[1,0].set_facecolor('#1E1A1A')
#pl0t4
sns.histplot(dataframe['rate'],bins=5,ax=axs[1,1], color="#C62440")
axs[1, 1].set_title('Ratings Distribution',color="#C62440",size=20)
axs[1,1].set_facecolor('#1E1A1A')
plt.subplots_adjust(wspace=0.2, hspace=0.4)
#plot2
couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data,ax=axs[0,1], color="#C62440")
axs[0,1].set_title('Cost Per Person',color="#C62440",size=20)
axs[0,1].set_facecolor('#1E1A1A')
#plotheading
plt.suptitle('Data Visualization of zomato Dataset', fontsize=25,color="#C62440")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




