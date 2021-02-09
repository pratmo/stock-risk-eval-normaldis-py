#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd
import numpy as np
import os


# In[38]:


os.chdir("/home/prathikm/Downloads/")


# In[39]:


beml_df = pd.read_csv("BEML.csv")
beml_df[0:5]


# In[40]:


glaxo_df = pd.read_csv("GLAXO.csv")
glaxo_df[0:5]


# In[41]:


#slice dataframe based on the columns we need
beml_df = beml_df[['Date', 'Close']]
glaxo_df = glaxo_df[['Date', 'Close']]


# In[42]:


beml_df


# In[43]:


'''The DataFrames have a date column, so we can
create a DatetimeIndex index from this column Date. It will ensure that the rows are sorted by time in
ascending order.'''
glaxo_df = glaxo_df.set_index(pd.DatetimeIndex(glaxo_df['Date']))
beml_df = beml_df.set_index(pd.DatetimeIndex(beml_df['Date']))


# In[44]:


glaxo_df #quick check at the modified index


# In[45]:


beml_df


# In[46]:


import matplotlib.pyplot as plt
import seaborn as sn
get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(glaxo_df.Close);
plt.xlabel('Time');
plt.ylabel('Close Price'); #plot the close price


# In[47]:


plt.plot(beml_df.Close);
plt.xlabel('Time');
plt.ylabel('Close');


# In[48]:


#compute the gain, with pct() percentage change and period as 1 for one previous day to calculate gain.
glaxo_df['gain'] = glaxo_df.Close.pct_change(periods = 1)
beml_df['gain'] = beml_df.Close.pct_change(periods = 1)


# In[49]:


glaxo_df


# In[50]:


beml_df


# In[51]:


#drop first row since it is NaN
glaxo_df = glaxo_df.dropna()
beml_df = beml_df.dropna()


# In[52]:


glaxo_df


# In[53]:


#Plot the gains
plt.figure(figsize = (8, 6));
plt.plot(glaxo_df.index, glaxo_df.gain);
plt.xlabel('Time');
plt.ylabel('gain');


# In[56]:


#Plot the gains beml
plt.figure(figsize = (8, 6));
plt.plot(beml_df.index, beml_df.gain);
plt.xlabel('Time');
plt.ylabel('gain');


# In[54]:


#density plots
sn.distplot(glaxo_df.gain, label = 'Glaxo');
plt.xlabel('gain');
plt.ylabel('Density');
plt.legend();


# In[57]:


sn.distplot(beml_df.gain, label = 'BEML');
plt.xlabel('gain');
plt.ylabel('Density');
plt.legend();


# In[58]:


print('Mean:', round(glaxo_df.gain.mean(), 4))
print('Standard Deviation: ', round(glaxo_df.gain.std(), 4))


# In[59]:


print('Mean: ', round(beml_df.gain.mean(), 4))
print('Standard Deviation: ', round(beml_df.gain.std(), 4))


# ### Compute 2% loss or gain for Glaxo

# In[60]:


from scipy import stats
#Probability of making 2% loss or higher in Glaxo
stats.norm.cdf( -0.02,
loc=glaxo_df.gain.mean(),
scale=glaxo_df.gain.std())


# In[61]:


#Probability of making 2% gain or higher in Glaxo
1 - stats.norm.cdf(0.02,
loc=glaxo_df.gain.mean(),
scale=glaxo_df.gain.std())


# ### Compute 2% loss or gain for BEML

# In[62]:


#Probability of making 2% loss or higher in BEML
stats.norm.cdf( -0.02,
loc=beml_df.gain.mean(),
scale=beml_df.gain.std())


# In[63]:


#Probability of making 2% gain or higher in BEML
1 - stats.norm.cdf(0.02,
loc=beml_df.gain.mean(),
scale=beml_df.gain.std())


# In[ ]:




