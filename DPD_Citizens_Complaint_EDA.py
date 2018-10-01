
# coding: utf-8

# # DPD Citizens Complaint 

# # Data Description

# •	BPC or Board of Police Commissioners number – a unique identifier issued by the BPC to each case in numerical order after the case has been assigned to an Investigator, used for internal tracking purposes
# •	CCR or Citizen Complaint Report number – the unique identifier automatically assigned to the case via the data management system 
# •	Report Date – date the complaint was filed
# •	Entry – mode of entry for the complaint by the citizen
# •	Age – age of the citizen filing the complaint 
# •	ctznRace – race of the citizen filing the complaint 
# •	ctznSex – sex of the citizen filing the complaint 
# •	Closed – date the investigation was completed by OCI 
# •	Unit – commanding unit of the officer against which the complaint was filed
# •	Administrative Closure – administrative finding 
# •	Allegation – a claim as set forth by the citizen complaint
# •	Finding – the disposition of a citizen complaint after investigation
# •	ofcrRace – race of the officer against which the complaint was filed
# •	ofcrSex – sex of the officer against which the complaint was filed

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[4]:


df = pd.read_csv("DPD__Citizen_Complaints.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.describe()


# In[5]:


df.info()


# In[7]:


df.shape


# In[9]:


df.columns


# In[8]:


df.ndim


# In[6]:


vals = df['Allegation'].value_counts()


# In[7]:


vals


# In[8]:


plt.figure(figsize=(10, 6),)
ax = vals.plot.bar(width = 1.0)
for i, v in vals.reset_index().iterrows():
    ax.text(i, v.Allegation + 0.2, v.Allegation, color = 'blue')


# In[9]:


df['ctznRace'].unique()


# In[10]:


df['ctznSex'].unique()


# In[11]:


df['ofcrRace'].unique()


# In[12]:


df['ofcrSex'].unique()


# In[13]:


plt.figure(figsize=(12, 6),)
sns.countplot(x = 'ctznRace', hue = 'ctznSex', data = df)
plt.tight_layout()
plt.show()


# In[14]:


plt.figure(figsize=(12, 6),)
sns.countplot(x = 'ofcrRace', hue = 'ofcrSex', data = df)
plt.tight_layout()
plt.show()


# In[15]:


entry_vals = df['Entry'].value_counts()


# In[16]:


entry_vals


# In[17]:


plt.figure(figsize=(10, 6),)
ax = entry_vals.plot.bar(width = 1.0)
for i, v in entry_vals.reset_index().iterrows():
    ax.text(i, v.Entry + 0.2, v.Entry, color = 'red')


# In[18]:


Finding_vals = df['Finding'].value_counts()


# In[21]:


plt.figure(figsize=(10, 6),)
ax = Finding_vals.plot.bar(width = 1.0)
for i, v in Finding_vals.reset_index().iterrows():
    ax.text(i, v.Finding + 0.2, v.Finding, color = 'red')


# In[21]:


# Time difference between Closing Date and Reporting Date for each case
df['Report Date'] = pd.to_datetime(df['Report Date'], dayfirst=True)
df['Closed'] = pd.to_datetime(df['Closed'], dayfirst=True)


# In[22]:


num_days = df['Closed'] - df['Report Date']


# In[23]:


plt.figure(figsize=(15, 6),)
num_days.plot(kind = 'line')


# In[24]:


num_corr = df.corr()
sns.heatmap(num_corr)


# In[25]:


sns.set_style("whitegrid")
ax = sns.violinplot(x = df['Age'], color = 'green', )


# # Summary

# The name of the dataset is “DPD: Citizen Complaints” which has been fetched from the following URL: https://data.detroitmi.gov/Public-Safety/DPD-Citizen-Complaints/kahe-efs3
# 
# This particular dataset shows all citizen complaints that were received by the Detroit Police Department and the Board of Police Commissioners since January 1, 2016. This dataset has information about the nature of individual complaints, demographics for citizens filing the complaints and the officer against which the complaint was filed. This data gets updated every month.
# 
# The dataset contains 9,378 rows and 14 columns. Each row is a citizen complaint. The head and tail commands displayed the initial and last 5 rows of the data. The data had NaN values, which mean not a number. Using the describe function, the statistical data was shown. With this, it was understood that the CCR and Age had numerical data. The count of each allegation has been provided.
# 
# The first visualization shows that Procedure type allegation has been repeated for the highest number of times and Arrest type allegation has repeated for the least number of times. 
# 
# The second visualization shows the count and gender of citizen race. In this it was found that Black Male and Female had the highest count. Asian and Chaldean had the least count.
# 
# Similarly, the third visualization showed the count of officer’s race and gender, Black being the highest and Other being the least. 
# 
# The fourth visualization shows how the complaint was filed. In this, Telephone had the highest count and Unknown had the least count.
# 
# The fifth visualization showed the count of Findings. No Charge had the highest count and Pending had the least count.
# 
# The sixth visualization shows the duration between reporting date and closing date of the complaints. 
# 
# The seventh visualization shows the correlation between Age and CCR. From the visualization it was observed that there was a strong negative correlation.
# 
# The eighth visualization shows the violin plot for age. It was observed that the age was widespread between the range 20 and 60.
# 
