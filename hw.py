#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
response = requests.get("http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm")
response.encoding = "big5"
book1 = response.text


# In[7]:


print (book1[0:100:2])


# In[ ]:




