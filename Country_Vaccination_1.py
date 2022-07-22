#!/usr/bin/env python
# coding: utf-8

# ## Country_Vaccination Project

# Below is a dataset for daily vaccination numbers per country.

# In[125]:


#importing library
import pandas as pd
import numpy as np


# In[126]:


df=pd.read_csv('country_vaccination_stats.csv')


# In[127]:


df_copy=df.copy()


# In[128]:


df


# In[129]:


def display_percent_missing(data):
    '''
    data: Data is the dataset we want to see the percentage of missing data.
    Function Action: This function show us of persent missing value for each column.
    '''   
    percent_missing = data.isnull().sum() *100 / len(data)
    missing_value_df = pd.DataFrame({'column_name': data.columns, 
                                     'percent_missing': percent_missing})
    
    display(missing_value_df.sort_values(by='percent_missing', ascending=False).head(25))
    return(missing_value_df)

missing_value_df= display_percent_missing(df)


# In[130]:


df.isnull().sum()


# In[131]:


df['country'].unique()


# ### Answer 4) 

# Code Implementation Task: Implement code to fill the missing data (impute) in daily_vaccinations column per country with the minimum daily vaccination number of relevant countries.  
# Note: If a country does not have any valid vaccination number yet, fill it with “0” (zero). 

# In[132]:


df.groupby('country')['daily_vaccinations'].min()


# In[133]:


#Filling missing value  per country with the minimum daily vaccination number of relevant countries.
df["daily_vaccinations"]=df.groupby('country')['daily_vaccinations'].apply(lambda x: x.fillna(x.min())).fillna(0)


# In[134]:


missing_value_df= display_percent_missing(df)


# ###  Answer 5)

# Code Implementation Task: Implement code to list the top-3 countries with highest median daily vaccination numbers by considering missing values imputed version of dataset.

# In[122]:


df.groupby('country')['daily_vaccinations'].median().sort_values(ascending=False).head(3)


# ##### Top 3 Countries
# 1-United States <br>
# 2-China <br>
# 3-India <br>

# ### Answer 6) 

# What is the number of total vaccinations done on 1/6/2021 (MM/DD/YYYY) by considering missing values imputed version of dataset? Please  just provide the number as answer.

# In[102]:


df['date'] = pd.to_datetime(df['date'])


# In[103]:


df.groupby('date')['daily_vaccinations'].sum()


# In[113]:


df[df['date'] == '01-06-2021']['daily_vaccinations'].sum()


# #### Total vaccinations done on 1/6/2021 (MM/DD/YYYY)
# 1485255.0
