#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[3]:


request = requests.get("http://pythonhow.com/example.html")
content = request.content
content


# In[5]:


soup = BeautifulSoup(content,'html.parser')


# In[8]:


soup


# Try now to extract the names of cities from https://pythonhow.com/example.html (within h2 tags)

# In[30]:


all = soup.find_all('div',{'class':'cities'})
print(all)
print('length: ' + str(len(all)))
print('type: ' + str(type(all)))


# In[ ]:


all[0]


# ... now fetching the h2 tags ...

# In[32]:


all[0].find_all('h2')


# In[36]:


all[0].find_all('h2')[0].text


# ... get the text from each.

# In[43]:


for item in all:
    print (item.find_all('h2')[0].text)

