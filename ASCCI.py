#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

# In[16]:


import string
dct = {}
alph = string.ascii_lowercase
for i in alph:
    dct[i] = ord(i)
print(dct)    


# In[15]:


dct = {}
alph = 'abcdefghijklmnopqrstuvwxyz'
j = 97
for i in alph:
    dct[i] = j
    j+=1
print(dct)    


# In[ ]:




